/**
 * Ada/SPARK Documentation Website — client-side unit renderer.
 *
 * This script handles two responsibilities:
 *
 *  1. Unit page rendering (when the page is the 404 fallback handler):
 *     Parses the current URL to find /{crate}/{version}/{unit}/, fetches
 *     data/{crate}/{version}/{unit}.json, and renders the API documentation.
 *
 *  2. Static page enhancements already present in index.html are handled
 *     inline in those pages (search filter); this script does not touch them.
 *
 * The script depends on marked.js (loaded from CDN) for Markdown rendering.
 * It degrades gracefully: if marked is absent, documentation text is shown
 * as plain text.
 */

(function () {
  'use strict';

  // -------------------------------------------------------------------------
  // Base URL (injected at build time via window.BASE_URL)
  // -------------------------------------------------------------------------

  var BASE_URL = window.BASE_URL || '';

  /**
   * Resolve a path relative to the base URL.
   */
  function resolvePath(path) {
    if (!path) return BASE_URL || '/';
    if (path.startsWith('http://') || path.startsWith('https://')) return path;
    if (!path.startsWith('/')) path = '/' + path;
    return (BASE_URL + path).replace(/\/+/g, '/');
  }

  // -------------------------------------------------------------------------
  // Utility: Markdown → HTML
  // -------------------------------------------------------------------------

  function renderMd(text) {
    if (!text) return '';
    if (typeof marked !== 'undefined') {
      return marked.parse(String(text));
    }
    // Plain-text fallback: escape HTML and preserve newlines.
    return '<p>' + String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\n\n+/g, '</p><p>')
      .replace(/\n/g, '<br>') + '</p>';
  }

  function esc(text) {
    return String(text || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // Module-level repository info populated once the version manifest is loaded.
  var repo = null;

  // -------------------------------------------------------------------------
  // URL parsing
  // -------------------------------------------------------------------------

  /**
   * Parse the current URL path into { crate, version, unit }.
   * Expects paths like /crate/version/unit/ or /crate/version/unit.
   * Returns null if the path does not match a unit page pattern.
   */
  function parsePath(pathname) {
    // Strip base URL first
    if (BASE_URL && pathname.startsWith(BASE_URL)) {
      pathname = pathname.substring(BASE_URL.length);
    }
    // Strip leading slash and split
    var parts = pathname.replace(/^\//, '').replace(/\/$/, '').split('/');
    if (parts.length >= 3) {
      return { crate: parts[0], version: parts[1], unit: parts[2] };
    }
    return null;
  }

  // -------------------------------------------------------------------------
  // Data fetching
  // -------------------------------------------------------------------------

  async function fetchUnit(crate, version, unit) {
    var url = resolvePath('/data/' + crate + '/' + version + '/' + unit + '.json');
    var resp = await fetch(url);
    if (!resp.ok) {
      throw new Error('HTTP ' + resp.status + ' fetching ' + url);
    }
    return resp.json();
  }

  async function fetchVersionManifest(crate, version) {
    var url = resolvePath('/data/' + crate + '/' + version + '/index.json');
    try {
      var resp = await fetch(url);
      if (!resp.ok) return null;
      return resp.json();
    } catch (e) {
      return null;
    }
  }

  /**
   * Build a source file URL for a given location and repository descriptor.
   * Returns null when the information is insufficient to build a URL.
   *
   * @param {object} location  - {file, line} from unit JSON
   * @param {object} repoInfo  - {url, host, commit?, subdir?} from index.json
   */
  function sourceLink(location, repoInfo) {
    if (!location || !repoInfo || !repoInfo.url) return null;
    var file = location.file;
    if (!file) return null;
    var filePath = (repoInfo.subdir || '') + file;
    var ref  = repoInfo.commit || 'HEAD';
    var base = repoInfo.url;
    var line = location.line;
    switch (repoInfo.host) {
      case 'github':
        return base + '/blob/' + ref + '/' + filePath + (line ? '#L' + line : '');
      case 'gitlab':
        return base + '/-/blob/' + ref + '/' + filePath + (line ? '#L' + line : '');
      case 'codeberg':
        return base + '/src/commit/' + ref + '/' + filePath + (line ? '#L' + line : '');
      case 'bitbucket':
        return base + '/src/' + ref + '/' + filePath + (line ? '#n' + line : '');
      default:
        // Unknown forge: link to repo root only
        return base;
    }
  }

  // -------------------------------------------------------------------------
  // Human-readable section labels
  // -------------------------------------------------------------------------

  var SECTION_LABELS = {
    simple_types:           'Simple Types',
    array_types:            'Array Types',
    record_types:           'Record Types',
    tagged_types:           'Tagged Types',
    interface_types:        'Interface Types',
    protected_types:        'Protected Types',
    task_types:             'Task Types',
    access_types:           'Access Types',
    subtypes:               'Subtypes',
    constants:              'Constants',
    variables:              'Variables',
    exceptions:             'Exceptions',
    subprograms:            'Subprograms',
    entries:                'Entries',
    generic_instantiations: 'Generic Instantiations',
    packages:               'Nested Packages',
  };

  var SECTION_ORDER = Object.keys(SECTION_LABELS);

  // Short kind labels shown as badges on entity cards
  var KIND_LABELS = {
    ada_package:               'package',
    ada_function:              'function',
    ada_procedure:             'procedure',
    ada_entry:                 'entry',
    ada_tagged_type:           'tagged type',
    ada_interface_type:        'interface',
    ada_record_type:           'record',
    ada_simple_type:           'type',
    ada_array_type:            'array',
    ada_access_type:           'access',
    ada_task_type:             'task type',
    ada_protected_type:        'protected',
    ada_subtype:               'subtype',
    ada_constant:              'constant',
    ada_variable:              'variable',
    ada_exception:             'exception',
    ada_generic_package:       'generic pkg',
    ada_generic_function:      'generic fn',
    ada_generic_procedure:     'generic proc',
    ada_package_instantiation: 'pkg instance',
    ada_subprogram_instantiation: 'subp instance',
    ada_package_renaming:      'pkg renaming',
    ada_formal:                'formal',
  };

  // -------------------------------------------------------------------------
  // HTML rendering helpers
  // -------------------------------------------------------------------------

  /** Build a URL for an entity reference cross-link. */
  function xrefUrl(ref) {
    if (!ref || !ref.crate || !ref.version || !ref.unit) return null;
    var url = resolvePath('/' + ref.crate + '/' + ref.version + '/' + ref.unit + '/');
    if (ref.id) url += '#' + ref.id;
    return url;
  }

  /** Render an entity reference as an <a> or plain text. */
  function renderRef(ref) {
    if (!ref) return '';
    var url = xrefUrl(ref);
    var label = esc(ref.qualified_name || ref.name || '?');
    if (url) return '<a href="' + esc(url) + '">' + label + '</a>';
    return label;
  }

  /** Render a list of entity references as <li> items inside a <ul>. */
  function renderRefList(refs) {
    if (!refs || refs.length === 0) return '';
    var items = refs.map(function (r) {
      return '<li>' + renderRef(r) + '</li>';
    }).join('');
    return '<ul class="xref-list">' + items + '</ul>';
  }

  /** Render a named-section array (parameters, exceptions, fields, etc.) */
  function renderNamedArray(items, label) {
    if (!items || items.length === 0) return '';
    var rows = items.map(function (item) {
      return '<li>'
        + '<span class="param-name">' + esc(item.name) + '</span>'
        + '<span class="param-desc">' + renderMd(item.description) + '</span>'
        + '</li>';
    }).join('');
    return '<div class="param-block">'
      + '<p class="param-block-label"><strong>' + esc(label) + '</strong></p>'
      + '<ul class="param-list">' + rows + '</ul>'
      + '</div>';
  }

  /** Render the documentation object for an entity. */
  function renderDocumentation(doc) {
    if (!doc) return '';
    var html = '';

    if (doc.description) {
      html += '<div class="entity-doc">' + renderMd(doc.description) + '</div>';
    }

    if (doc.parameters && doc.parameters.length) {
      html += renderNamedArray(doc.parameters, 'Parameters');
    }
    if (doc.returns) {
      html += '<div class="param-block"><p class="param-block-label"><strong>Returns</strong></p>'
        + '<div class="entity-doc">' + renderMd(doc.returns) + '</div></div>';
    }
    if (doc.exceptions && doc.exceptions.length) {
      html += renderNamedArray(doc.exceptions, 'Exceptions');
    }
    if (doc.fields && doc.fields.length) {
      html += renderNamedArray(doc.fields, 'Fields');
    }
    if (doc.formals && doc.formals.length) {
      html += renderNamedArray(doc.formals, 'Generic Formals');
    }
    if (doc.enumeration_literals && doc.enumeration_literals.length) {
      html += renderNamedArray(doc.enumeration_literals, 'Enumeration Literals');
    }

    return html;
  }

  /** Render type-hierarchy cross-references for tagged/interface types. */
  function renderTypeHierarchy(entity) {
    var html = '';
    var fields = [
      ['parent_type',               'Parent type',              false],
      ['progenitor_types',          'Progenitor interfaces',    true],
      ['derived_types',             'Known derived types',      true],
      ['dispatching_declared',      'Dispatching (declared)',   true],
      ['dispatching_overridden',    'Dispatching (overridden)', true],
      ['dispatching_inherited',     'Dispatching (inherited)',  true],
      ['prefix_callable_declared',  'Prefix-call (declared)',   true],
      ['prefix_callable_inherited', 'Prefix-call (inherited)',  true],
    ];

    var anyPresent = fields.some(function (f) { return entity[f[0]]; });
    if (!anyPresent) return '';

    html += '<div class="type-hierarchy"><strong>Type hierarchy</strong>';
    fields.forEach(function (f) {
      var key = f[0], label = f[1], isList = f[2];
      if (!entity[key]) return;
      html += '<div class="xref-row"><span class="xref-label">' + esc(label) + '</span>';
      if (isList) {
        html += renderRefList(entity[key]);
      } else {
        html += '<ul class="xref-list"><li>' + renderRef(entity[key]) + '</li></ul>';
      }
      html += '</div>';
    });
    html += '</div>';
    return html;
  }

  /** Render one entity as a card. */
  function renderEntityCard(entity) {
    var id = entity.id ? ' id="' + esc(entity.id) + '"' : '';
    var kind = entity.kind || '';
    var kindLabel = KIND_LABELS[kind] || kind.replace(/^ada_/, '').replace(/_/g, ' ');
    var locText = entity.location
      ? entity.location.file + ':' + entity.location.line
      : '';

    var locHtml = '';
    if (locText) {
      var srcUrl = repo ? sourceLink(entity.location, repo) : null;
      if (srcUrl) {
        locHtml = '<a class="entity-location" href="' + esc(srcUrl) + '"'
          + ' target="_blank" rel="noopener">' + esc(locText) + '</a>';
      } else {
        locHtml = '<span class="entity-location">' + esc(locText) + '</span>';
      }
    }

    var html = '<div class="entity-card"' + id + '>';

    // Header
    html += '<div class="entity-header">'
      + '<span class="entity-name">' + esc(entity.name || entity.qualified_name || '?') + '</span>'
      + '<span class="entity-kind">' + esc(kindLabel) + '</span>'
      + locHtml
      + '</div>';

    // Body
    html += '<div class="entity-body">';

    // Code snippet
    if (entity.code) {
      html += '<div class="entity-code"><pre><code>' + esc(entity.code) + '</code></pre></div>';
    }

    // Documentation
    html += renderDocumentation(entity.documentation);

    // Type hierarchy (for tagged/interface types)
    html += renderTypeHierarchy(entity);

    html += '</div>'; // entity-body
    html += '</div>'; // entity-card
    return html;
  }

  /** Render one section (e.g. "subprograms") of the unit. */
  function renderSection(key, entities) {
    if (!entities || entities.length === 0) return '';
    var label = SECTION_LABELS[key] || key;
    var html = '<section class="entity-section" id="section-' + esc(key) + '">';
    html += '<h2>' + esc(label) + ' <span class="section-count">(' + entities.length + ')</span></h2>';
    entities.forEach(function (e) {
      html += renderEntityCard(e);
    });
    html += '</section>';
    return html;
  }

  /** Build the sticky nav bar listing populated sections. */
  function renderNav(unitData) {
    var links = SECTION_ORDER
      .filter(function (k) { return unitData[k] && unitData[k].length > 0; })
      .map(function (k) {
        return '<a href="#section-' + esc(k) + '">'
          + esc(SECTION_LABELS[k] || k) + '</a>';
      });
    if (links.length === 0) return '';
    return '<nav class="unit-nav" aria-label="Unit sections">' + links.join('') + '</nav>';
  }

  /** Render the full unit page from JSON data. */
  function renderUnitPage(container, unitData, crate, version) {
    var qname  = esc(unitData.qualified_name || unitData.name || 'Unknown');
    var locText = unitData.location
      ? unitData.location.file + ':' + unitData.location.line
      : '';

    var html = '<div class="page-unit">';
    html += '<h1>' + qname + '</h1>';

    // Meta line
    html += '<div class="unit-meta">';
    html += '<span>' + esc(crate) + ' ' + esc(version) + '</span>';
    if (locText) {
      var unitSrcUrl = repo ? sourceLink(unitData.location, repo) : null;
      if (unitSrcUrl) {
        html += '<span><a href="' + esc(unitSrcUrl) + '" target="_blank" rel="noopener">'
          + esc(locText) + '</a></span>';
      } else {
        html += '<span>' + esc(locText) + '</span>';
      }
    }
    html += '</div>';

    // Package-level documentation
    html += renderDocumentation(unitData.documentation);

    // Section navigation
    html += renderNav(unitData);

    // Entity sections
    SECTION_ORDER.forEach(function (key) {
      html += renderSection(key, unitData[key]);
    });

    html += '</div>';
    container.innerHTML = html;
  }

  // -------------------------------------------------------------------------
  // Breadcrumb injection (for dynamically rendered pages)
  // -------------------------------------------------------------------------

  function injectBreadcrumb(crate, version, unitName) {
    var nav = document.querySelector('.site-nav');
    if (!nav) return;
    // Remove any existing breadcrumb
    var existing = nav.querySelector('.breadcrumb');
    if (existing) existing.remove();

    var ol = document.createElement('ol');
    ol.className = 'breadcrumb';
    ol.setAttribute('aria-label', 'Breadcrumb');
    ol.innerHTML =
      '<li><a href="' + esc(resolvePath('/')) + '">Registry</a></li>'
      + '<li><a href="' + esc(resolvePath('/' + crate + '/')) + '">' + esc(crate) + '</a></li>'
      + '<li aria-current="page">' + esc(unitName) + '</li>';
    nav.appendChild(ol);
  }

  // -------------------------------------------------------------------------
  // Main: detect unit page and render
  // -------------------------------------------------------------------------

  async function main() {
    var params = parsePath(window.location.pathname);
    if (!params) {
      // Redirect /crate/version/ (two path segments) to /crate/
      var pathname = window.location.pathname;
      // Strip BASE_URL first
      if (BASE_URL && pathname.startsWith(BASE_URL)) {
        pathname = pathname.substring(BASE_URL.length);
      }
      var parts = pathname.replace(/^\//, '').replace(/\/$/, '').split('/');
      if (parts.length === 2 && parts[0] && parts[1]) {
        window.location.replace(resolvePath('/' + parts[0] + '/'));
      }
      return;
    }

    var main = document.querySelector('main.site-main') || document.querySelector('main') || document.body;

    // Show loading state
    main.innerHTML = '<p class="loading">Loading ' + esc(params.unit) + '…</p>';

    try {
      var results = await Promise.all([
        fetchUnit(params.crate, params.version, params.unit),
        fetchVersionManifest(params.crate, params.version),
      ]);
      var unitData        = results[0];
      var versionManifest = results[1];

      // Set module-level repo info for source link generation
      repo = versionManifest ? (versionManifest.repository || null) : null;

      // Update page title and meta description
      var title = (unitData.qualified_name || params.unit)
        + ' — ' + params.crate + ' ' + params.version + ' — Ada/SPARK Docs';
      document.title = title;

      var metaDesc = document.querySelector('meta[name="description"]');
      if (metaDesc && unitData.documentation && unitData.documentation.description) {
        metaDesc.setAttribute('content',
          unitData.documentation.description.replace(/\n/g, ' ').slice(0, 200));
      }

      renderUnitPage(main, unitData, params.crate, params.version);
      injectBreadcrumb(
        params.crate, params.version,
        unitData.qualified_name || params.unit
      );

      // Scroll to anchor if present
      if (window.location.hash) {
        var target = document.querySelector(window.location.hash);
        if (target) target.scrollIntoView({ behavior: 'smooth' });
      }
    } catch (err) {
      main.innerHTML =
        '<div class="error-message">'
        + '<p>Could not load documentation for <code>' + esc(params.unit) + '</code>.</p>'
        + '<p><small>' + esc(err.message) + '</small></p>'
        + '<p><a href="' + esc(resolvePath('/' + params.crate + '/' + params.version + '/')) + '">'
        + '← Back to ' + esc(params.crate) + ' ' + esc(params.version) + '</a></p>'
        + '</div>';
    }
  }

  // Run once the DOM is ready.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', main);
  } else {
    main();
  }

}());
