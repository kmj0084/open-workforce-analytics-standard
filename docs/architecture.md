# Information architecture

| Public section | Route | Role |
|---|---|---|
| Home | `/index.html` | Orientation and primary entry points |
| Standards | `/standards/` | Automatic searchable, sortable metric table with category browsing |
| Domain pages | `/standards/<domain>/` | Domain context and references |
| Metric | `/standards/<domain>/<slug>/` | Durable definition with ID, version, and status |
| Research | `/research/` | Automatic reverse-chronological research listing |
| Research note | `/research/<slug>/` | Sources, method, results, limitations |
| Essays | `/essays/` | Automatic reverse-chronological essay listing |
| Essay | `/essays/<slug>/` | Conceptual argument with supporting material |
| Dashboard | `/dashboard/` | Access, refresh context, and separate report hosting |
| Dashboard methodology | `/dashboard/methodology.html` | Report-specific documentation |
| About | `/about.html` | Purpose and project stage |
| Methodology | `/methodology.html` | Shared measurement principles |
| Get involved | `/get-involved.html` | Contribution entry point |

Routes are relative to the deployment base: a GitHub project site adds `/repository/` before them. Quarto handles source-page link conversion. The primary navigation stays short; About, Methodology, and Get involved are under Project, with footer access to About and Get involved.

```text
owas/
├── _quarto.yml
├── index.qmd
├── about.qmd
├── methodology.qmd
├── get-involved.qmd
├── styles.css
├── references.bib
├── standards/
│   ├── index.qmd
│   ├── _metadata.yml
│   ├── headcount/
│   │   ├── index.qmd
│   │   └── point-in-time-headcount/index.qmd
│   ├── movement/index.qmd
│   ├── talent-acquisition/index.qmd
│   ├── organization/index.qmd
│   └── engagement/index.qmd
├── research/
│   ├── index.qmd
│   ├── _metadata.yml
│   ├── recording-time/index.qmd
│   └── unpublished-example/index.qmd
├── essays/
│   ├── index.qmd
│   ├── _metadata.yml
│   └── what-a-number-counts/index.qmd
├── dashboard/
│   ├── index.qmd
│   └── methodology.qmd
├── templates/{metric,essay,research-note}.qmd
├── scripts/{check_source,check_site}.py
├── docs/{architecture,metadata}.md
├── .github/workflows/publish.yml
├── .gitignore
├── README.md
└── CHANGELOG.md
```

## Expansion rules

Use one folder per article so figures and scripts can travel with it. Use categories for research themes; avoid unnecessary directory levels. Metric IDs remain stable even if a title changes. The standards table exposes structured domain/type/status fields with text filtering; category browsing is single-category navigation, not simultaneous faceted filtering. Independent facet controls can be added later without changing metadata or routes.

Quarto's local full-text search covers rendered headings and body text with snippets. It needs no external search account. There is no custom search service, CMS, or client application to maintain. If the corpus eventually exceeds practical static-search size, evaluate a hosted index then.

The CSS uses system fonts, a restrained teal accent, visible keyboard focus, a two-column homepage that collapses on small screens, and horizontally scrollable tables. Navigation, search, and listing controls come from Quarto.
