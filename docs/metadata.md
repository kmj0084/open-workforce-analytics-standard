# Metadata convention

Keep top-level fields on single lines in YAML front matter. The small source checker verifies required fields using this intentionally narrow convention; it is not a general YAML schema validator.

| Field | Applies to | Convention |
|---|---|---|
| title | All pages | Specific, readable title |
| description | All pages | One-sentence summary for listing/search context |
| content-type | Articles | `metric`, `essay`, `research-note` |
| author | Essays/research | Actual author or responsible organization |
| date | Articles | First publication date, ISO `YYYY-MM-DD` |
| date-modified | Articles | Last substantive editorial update |
| draft | Articles | Explicit boolean `true` or `false` |
| categories | Articles | YAML list; controlled labels, consistent capitalization |
| metric-id | Metrics | Unique stable ID, e.g. `OWAS-HC-001` |
| domain | Metrics | Headcount, Movement, Talent acquisition, Organization, Engagement |
| metric-type | Metrics | Stock, Flow, Rate, Ratio, Index, or Duration; expand deliberately |
| status | Metrics | Draft, Review, Recommended, Deprecated |
| version | Metrics | Quoted semantic version string |

For metrics, categories repeat domain, type, and status for native category browsing. The separate fields support the directory table and future exports. The metric template displays ID/status/version using metadata shortcodes so visible values stay synchronized.

Change the major version for incompatible population or calculation rules, minor for compatible additions, and patch for corrections that do not alter the result. Explain every change in the page history. This is a starter editorial convention, not evidence of an established governance body.
