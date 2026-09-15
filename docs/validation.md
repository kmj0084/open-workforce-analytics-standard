# v0.1 validation

Validated locally with Quarto 1.8.27 and Python 3.13.

- Full production render completed: 18 HTML outputs, including Quarto's empty draft placeholder.
- Source metadata checks passed.
- Rendered local link and asset targets resolved.
- Search index contained the published metric, research note, and essay.
- The draft sentinel was absent from rendered HTML, JSON, and XML; draft and template paths were absent from search.
- Browser search for `headcount` returned matching documents and section snippets.
- Typing `Recommended` in the standards filter showed no matching items; the starter metric is Draft.
- Homepage and standards layout inspected at 390px width; mobile navigation opened successfully.
- Four empty domain listings emit expected unmatched-content warnings until their first metric is added. The render still succeeds.

GitHub Pages deployment has not been run: no destination repository was supplied. Follow README setup instructions and verify the actual project URL after first deployment. No Power BI report is connected. Browser checks are focused smoke checks, not a full accessibility audit.
