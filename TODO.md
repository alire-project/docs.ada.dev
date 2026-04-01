# docs.ada.dev - TODO & Feature Roadmap

This document tracks planned features and improvements for the Ada/SPARK documentation website.

## Legend
- [ ] Not started
- [x] Completed
- [~] In progress
- [!] Blocked/needs discussion

---

## 🟢 High Priority - Can Implement Now

### Enhanced Search
- [x] Full-text search across descriptions and documentation
- [x] Fuzzy matching for typo tolerance
- [x] Intelligent ranking by relevance (name > tags > description)
- [x] Debounced search for performance
- [ ] Type/function search - search for specific API elements
- [ ] Keyboard shortcut (`/` or `Ctrl+K`) to focus search
- [ ] Search filters: by tag, license, author

### Platform/Target Badges
- [ ] Show which targets crates support (embedded, native, cross-platform)
- [ ] Filter crates by platform compatibility
- [ ] Badge for "no dependencies" crates

### Documentation Quality Indicators
- [ ] Coverage percentage - how many units have documentation
- [ ] Completeness score - percentage of public APIs documented
- [ ] Missing docs warnings in red/yellow
- [ ] Badge: "Well documented" vs "Needs docs"

### Version Comparison
- [ ] Changelog view between versions
- [ ] API diff - what was added/removed/changed
- [ ] Visual indicator for breaking changes
- [ ] Link to repository tags/releases

### Source Links Enhancement
- [ ] Per-declaration source links (partially implemented)
- [ ] "View on GitHub/GitLab" buttons
- [ ] Link to specific commit/tag for version
- [ ] Blame view integration

### Build Status Integration
- [x] Error page listing failed builds
- [ ] Visual indicators for build success/failure on crate pages
- [ ] Link to build logs for failed builds
- [ ] Time since last successful build
- [ ] Historical build success rate

### Dark Mode
- [ ] Toggle between light/dark themes
- [ ] System preference detection
- [ ] Persisted user preference in localStorage

### Dependency Features
- [ ] Dependency graph visualization (D3.js/Mermaid)
- [ ] Reverse dependencies - "who uses this crate?"
- [ ] Dependency tree viewer - full transitive deps
- [ ] Security advisories for dependencies
- [x] Basic dependency list on crate pages

---

## 🟡 Medium Priority - Requires Some Backend Work

### Download/Usage Statistics
- [ ] Pull stats from Alire index
- [ ] "Downloads this month" counter
- [ ] Popularity score/trending crates
- [ ] Most-starred/forked repositories

### Code Examples Extraction
- [ ] Parse README for examples
- [ ] Extract test cases as examples
- [ ] Syntax highlighting improvements
- [ ] "Run in playground" button (if Ada playground exists)

### API Reference Enhancements
- [ ] Permalink to declarations (#declaration-id)
- [ ] Copy link button for each declaration
- [ ] Copy code snippet button
- [ ] Breadcrumb navigation within units
- [x] Basic breadcrumb navigation

### Smart Cross-Referencing
- [ ] "Similar crates" recommendations
- [ ] "Alternatives to consider"
- [ ] "Commonly used together with..."
- [ ] Related documentation links

### RSS/Atom Feeds
- [ ] Feed for new crates
- [ ] Feed for crate updates
- [ ] Per-crate update feeds
- [ ] Filter feeds by tags

### Keyboard Navigation
- [ ] Shortcuts for common actions
- [ ] Quick switcher (Cmd+K) for crates
- [ ] Navigate between declarations
- [ ] Help overlay with shortcuts

### Improved Mobile Experience
- [ ] Responsive navigation
- [ ] Touch-friendly controls
- [ ] Collapsible sections
- [ ] Mobile-optimized search

---

## 🔴 Lower Priority - Significant Infrastructure Needed

### Interactive Features
- [ ] Voting/rating system
- [ ] Comments on crates
- [ ] "Report documentation issue" button
- [ ] Community contributions

### CI/CD Integration
- [ ] Webhook for automatic updates
- [ ] Real-time build status
- [ ] Auto-rebuild on index changes
- [ ] Preview deployments for PRs

### Advanced Analytics
- [ ] Page view tracking
- [ ] Popular search terms
- [ ] Most viewed crates/units
- [ ] User journey analysis

### API Compatibility Checker
- [ ] Semver compliance verification
- [ ] Breaking change detection
- [ ] Migration guides between versions
- [ ] Deprecation warnings

### Multi-Language Support
- [ ] i18n for UI text
- [ ] Community translations
- [ ] Language selector

---

## 📋 Quick Wins (Highest Impact, Lowest Effort)

Priority order for implementation:

1. **Dark mode** - Pure CSS, minimal JS
2. **Improved search** - Add fuzzy matching, search in descriptions
3. **Platform badges** - Parse from crate metadata
4. **Copy buttons** - For code snippets and links
5. **Keyboard shortcut** - `/` to focus search
6. **Build status badges** - Use error.json data we already have
7. **Reverse dependencies** - Calculate from existing index
8. **Permalinks** - Add IDs to all declarations

---

## 🎯 Recommended Roadmap

### Phase 1 (This Month)
- [ ] Dark mode
- [ ] Enhanced search with fuzzy matching
- [ ] Platform/target badges
- [ ] Copy-to-clipboard buttons

### Phase 2 (Next Month)
- [ ] Dependency graph visualization
- [ ] Reverse dependencies
- [ ] Build status dashboard
- [ ] Documentation quality scores

### Phase 3 (Future)
- [ ] Version comparison
- [ ] API compatibility checker
- [ ] RSS feeds
- [ ] Usage statistics integration

---

## ✅ Recently Completed

### Infrastructure
- [x] Namespace collision fixes (moved crates to `/c/`, data to `/crate-data/`)
- [x] Proper semver version sorting using `packaging` library
- [x] Markdown rendering for `long_description` fields
- [x] Markdown rendering for unit documentation
- [x] Separate errors page for failed builds
- [x] Basic search functionality (name/tag/description)
- [x] GitHub Pages deployment via gh-pages branch

### Bug Fixes
- [x] Fixed search functionality (handle crates without descriptions)
- [x] Fixed base URL handling for GitHub Pages subdirectory deployment
- [x] Fixed all URL path resolution for `/c/` prefix

---

## 💡 Ideas for Discussion

- Should we integrate with an Ada playground for live code examples?
- What metrics from Alire should we prioritize displaying?
- Should we show security advisories or vulnerability scanning?
- Is there demand for a "trending" or "most popular" section?
- Should we support user accounts for favorites/bookmarks?

---

## 🐛 Known Issues

- None currently tracked

---

*Last updated: 2026-04-01*
