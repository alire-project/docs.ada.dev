# JSON Data Schema

This document specifies the JSON files produced by the gnatdoc JSON backend
and consumed by the website (both the static page generator and the JS
frontend).

All free-text documentation fields contain **raw Markdown** as extracted
from Ada source comments. The JS frontend is responsible for rendering it.

---

## Schema versioning

Every file carries `"schema_version": "1"` at the top level. Increment this
when making a breaking change. The JS frontend and static page generator
must reject files whose schema version they do not support.

---

## `data/index.json` — global crate index

One file for the whole site. Updated whenever a crate is added or its
latest version changes.

```json
{
  "schema_version": "1",
  "updated": "2025-01-15T10:00:00Z",
  "crates": [
    {
      "name": "libfoo",
      "description": "Short description from Alire manifest.",
      "tags": ["containers", "spark"],
      "latest": "1.2.3",
      "versions": ["1.0.0", "1.1.0", "1.2.3"]
    }
  ]
}
```

| Field       | Type             | Description |
|-------------|------------------|-------------|
| `updated`   | ISO 8601 string  | Timestamp of last modification |
| `crates`    | array of objects | One entry per indexed crate |
| `name`      | string           | Alire crate name (lowercase, hyphenated) |
| `description` | string         | Short description from `alire.toml` |
| `tags`      | array of strings | Tags from `alire.toml` |
| `latest`    | string           | Latest indexed version |
| `versions`  | array of strings | All indexed versions, oldest first |

---

## `data/{crate}/{version}/index.json` — crate version manifest

One file per crate version. Updated when a new version is indexed or when
Alire manifest metadata changes. Never updated just because unit content
changes.

```json
{
  "schema_version": "1",
  "crate": "libfoo",
  "version": "1.2.3",
  "description": "Short description.",
  "long_description": "Markdown long description from alire.toml.",
  "authors": ["AdaCore"],
  "licenses": ["Apache-2.0"],
  "tags": ["containers"],
  "website": "https://example.com",
  "dependencies": [
    { "crate": "gnatcoll", "version": "^24.0.0" }
  ],
  "units": [
    { "name": "Foo",     "id": "abc123", "file": "foo.json" },
    { "name": "Foo.Bar", "id": "def456", "file": "foo-bar.json" }
  ]
}
```

| Field              | Type             | Description |
|--------------------|------------------|-------------|
| `crate`            | string           | Alire crate name |
| `version`          | string           | Semantic version string |
| `description`      | string           | Short description |
| `long_description` | string           | Markdown long description (may be empty) |
| `authors`          | array of strings | Author names |
| `licenses`         | array of strings | SPDX license identifiers |
| `tags`             | array of strings | Alire tags |
| `website`          | string           | Project website URL (may be empty) |
| `repository`       | object           | Detected source repository (may be absent) |
| `dependencies`     | array of objects | Direct Alire dependencies |
| `units`            | array of objects | All Ada compilation units in this version |

### `repository` object

Present when the source repository can be identified from the Alire manifest.
Detected heuristically from `origin.url` (preferred) and `website` (fallback,
accepted only for recognised forges).

```json
{
  "url":    "https://github.com/mosteo/aaa",
  "host":   "github",
  "commit": "7bfebd18eb1c9a7eb283ec1a8a05009449239c88",
  "subdir": "aaa_base/"
}
```

| Field    | Type   | Description |
|----------|--------|-------------|
| `url`    | string | Canonical repository root URL |
| `host`   | string | Forge identifier: `github`, `gitlab`, `codeberg`, `bitbucket`, `sourceforge`, or `git` |
| `commit` | string | Exact commit SHA from `origin.commit` (present for git origins) |
| `subdir` | string | Path prefix within the repo to the crate root, with trailing `/` (present for monorepo layouts) |

The JS frontend uses `host`, `commit`, and `subdir` to construct per-line
source links: `{url}/blob/{commit}/{subdir}{file}#L{line}` (GitHub pattern).

---

### Unit entry

| Field  | Type   | Description |
|--------|--------|-------------|
| `name` | string | Ada qualified name (e.g. `Foo.Bar`) |
| `id`   | string | SHA-256 digest of the entity signature (first 16 hex chars) |
| `file` | string | Filename relative to this directory (e.g. `foo-bar.json`) |

---

## `data/{crate}/{version}/{unit}.json` — compilation unit

One file per Ada compilation unit (package spec). The top-level object is
the package entity itself.

**Filename convention:** Ada qualified name, lowercased, dots replaced by
hyphens. Example: `Foo.Bar.Baz` → `foo-bar-baz.json`.

```json
{
  "schema_version": "1",
  "crate": "libfoo",
  "version": "1.2.3",
  "id": "abc123",
  "name": "Bar",
  "qualified_name": "Foo.Bar",
  "kind": "ada_package",
  "location": { "file": "foo-bar.ads", "line": 24, "column": 1 },
  "documentation": { ... },

  "simple_types":           [ ...entity objects... ],
  "array_types":            [ ...entity objects... ],
  "record_types":           [ ...entity objects... ],
  "tagged_types":           [ ...entity objects... ],
  "interface_types":        [ ...entity objects... ],
  "protected_types":        [ ...entity objects... ],
  "task_types":             [ ...entity objects... ],
  "access_types":           [ ...entity objects... ],
  "subtypes":               [ ...entity objects... ],
  "constants":              [ ...entity objects... ],
  "variables":              [ ...entity objects... ],
  "exceptions":             [ ...entity objects... ],
  "subprograms":            [ ...entity objects... ],
  "entries":                [ ...entity objects... ],
  "generic_instantiations": [ ...entity objects... ],
  "packages":               [ ...entity objects... ]
}
```

Empty collections are omitted from the file.

---

## Entity object

Used as members of all collections above. Every entity carries a `kind`
field so it is self-describing when appearing outside its natural collection
(e.g. in search results or cross-reference lists).

```json
{
  "id": "d4e5f6",
  "name": "Push",
  "qualified_name": "Foo.Bar.Push",
  "kind": "ada_procedure",
  "location": { "file": "foo-bar.ads", "line": 42, "column": 4 },
  "code": "procedure Push (Container : in out Stack; Item : Element_Type);",
  "documentation": { ... }
}
```

| Field           | Type   | Description |
|-----------------|--------|-------------|
| `id`            | string | First 16 hex chars of SHA-256 of entity signature |
| `name`          | string | Short (unqualified) name |
| `qualified_name`| string | Full Ada qualified name |
| `kind`          | string | Entity kind (see below) |
| `location`      | object | Source location |
| `code`          | string | Ada source declaration (may be multi-line) |
| `documentation` | object | Structured documentation (see below) |

### `kind` values

| Value                        | Ada construct |
|------------------------------|---------------|
| `ada_package`                | Package |
| `ada_function`               | Function |
| `ada_procedure`              | Procedure |
| `ada_entry`                  | Task or protected entry |
| `ada_tagged_type`            | Tagged record type |
| `ada_interface_type`         | Interface type |
| `ada_record_type`            | Non-tagged record type |
| `ada_simple_type`            | Scalar / enumeration / numeric type |
| `ada_array_type`             | Array type |
| `ada_access_type`            | Access (pointer) type |
| `ada_task_type`              | Task type |
| `ada_protected_type`         | Protected type |
| `ada_subtype`                | Subtype declaration |
| `ada_constant`               | Constant declaration |
| `ada_variable`               | Variable declaration |
| `ada_exception`              | Exception declaration |
| `ada_generic_package`        | Generic package |
| `ada_generic_function`       | Generic function |
| `ada_generic_procedure`      | Generic procedure |
| `ada_package_instantiation`  | Package instantiation |
| `ada_subprogram_instantiation` | Subprogram instantiation |
| `ada_package_renaming`       | Package renaming |
| `ada_formal`                 | Generic formal parameter |

### `location` object

```json
{ "file": "foo-bar.ads", "line": 42, "column": 4 }
```

`file` is relative to the crate source root.

---

## Tagged / interface type — additional fields

Tagged types and interface types carry type-hierarchy and dispatch
information in addition to the base entity fields.

```json
{
  "id": "...",
  "name": "Stack",
  "kind": "ada_tagged_type",
  ...
  "parent_type":               { ...entity ref... },
  "progenitor_types":          [ ...entity refs... ],
  "derived_types":             [ ...entity refs... ],
  "dispatching_declared":      [ ...entity refs... ],
  "dispatching_overridden":    [ ...entity refs... ],
  "dispatching_inherited":     [ ...entity refs... ],
  "prefix_callable_declared":  [ ...entity refs... ],
  "prefix_callable_inherited": [ ...entity refs... ]
}
```

Fields not applicable (e.g. `parent_type` for a root type) are omitted.

---

## Entity reference object

Used in all cross-reference fields (`parent_type`, `derived_types`,
`dispatching_declared`, etc.). Carries enough information to build a
hyperlink without fetching the target unit.

```json
{
  "qualified_name": "Foo.Base.Stack",
  "kind": "ada_tagged_type",
  "id": "abc123",
  "unit": "foo-base",
  "crate": "libfoo",
  "version": "1.2.3"
}
```

| Field           | Type   | Description |
|-----------------|--------|-------------|
| `qualified_name`| string | Full Ada qualified name of the target |
| `kind`          | string | Entity kind of the target |
| `id`            | string | Entity id of the target (for `#{id}` anchor) |
| `unit`          | string | Unit filename stem (for URL path segment) |
| `crate`         | string | Target crate name (may differ from current unit) |
| `version`       | string | Target version (may differ from current unit) |

The full URL for a cross-reference is:
`/{crate}/{version}/{unit}/#{id}`

---

## `documentation` object

All free-text fields are **Markdown strings**. The JS frontend renders them.
Fields with no content are omitted.

```json
{
  "description": "Push an element onto the stack.\n\nRaises `Constraint_Error` if full.",
  "parameters": [
    { "name": "Container", "description": "The stack to modify." },
    { "name": "Item",      "description": "The element to push." }
  ],
  "returns": "The number of remaining slots.",
  "exceptions": [
    { "name": "Constraint_Error", "description": "Raised when the stack is full." }
  ],
  "fields": [
    { "name": "Count", "description": "Current number of elements." }
  ],
  "formals": [
    { "name": "Element_Type", "description": "Type of elements stored." }
  ],
  "enumeration_literals": [
    { "name": "Red", "description": "The colour red." }
  ]
}
```

| Field                   | Type             | Description |
|-------------------------|------------------|-------------|
| `description`           | string           | Markdown: main entity description |
| `parameters`            | array of named   | Subprogram parameters |
| `returns`               | string           | Markdown: return value description |
| `exceptions`            | array of named   | Raised exceptions |
| `fields`                | array of named   | Record component / discriminant docs |
| `formals`               | array of named   | Generic formal parameter docs |
| `enumeration_literals`  | array of named   | Enumeration literal docs |

Each **named entry** (`parameters`, `exceptions`, `fields`, `formals`,
`enumeration_literals`) has the form:

```json
{ "name": "X", "description": "Markdown string." }
```
