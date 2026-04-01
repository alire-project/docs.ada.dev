# Changelog

All notable changes to the docs.ada.dev website will be documented in this file.

## [Unreleased]

### Added
- **Enhanced Search with Fuzzy Matching** (2026-04-01)
  - Fuzzy matching algorithm that tolerates typos and character transpositions
  - Full-text search across crate names, tags, and descriptions
  - Intelligent ranking system:
    - Name matches weighted 3x (highest priority)
    - Tag matches weighted 2x (medium priority)
    - Description matches weighted 1x (base priority)
  - Consecutive character bonus for better substring matching
  - Results automatically reordered by relevance score
  - 150ms debounce for improved performance
  - Enhanced search input with better placeholder text
  - Visual feedback when search is focused (highlighted count)

### Changed
- Search now ranks and sorts results by relevance instead of alphabetical order
- Crate list changed from CSS Grid to Flexbox to support dynamic reordering

### Technical Details
- Fuzzy scoring algorithm gives exact matches score of 1000
- Substring matches score 500+ based on position
- Character-by-character fuzzy matching with consecutive match bonuses
- No external dependencies - pure vanilla JavaScript implementation

---

## Previous Changes

### Infrastructure (2026-04-01)
- Moved all crate pages to `/c/` prefix to avoid namespace conflicts
- Moved data files to `/crate-data/` directory
- Implemented proper semantic versioning with `packaging` library
- Added Markdown rendering for long descriptions and documentation
- Created dedicated `/errors.html` page for failed builds
- Fixed GitHub Pages deployment with gh-pages branch

### Bug Fixes (2026-04-01)
- Fixed search breaking on crates without descriptions
- Fixed base URL handling for GitHub Pages subdirectory deployment
- Fixed all URL path resolution for `/c/` prefix structure

