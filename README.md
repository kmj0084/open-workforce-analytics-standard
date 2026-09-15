# OWAS website · v0.1

A Quarto technical reference website designed for routine publishing over several years. No JavaScript framework, package manager, database, or Power BI build dependency is required.

## Start locally

Install [Quarto 1.8.27](https://github.com/quarto-dev/quarto-cli/releases/tag/v1.8.27), the version pinned in CI. Python 3 is used only for repository checks; the initial content requires no R installation.

From this repository root:

```sh
quarto preview
```

Preview deliberately displays drafts. To inspect exactly what will publish, stop preview and run:

```sh
python scripts/check_source.py
quarto render
python scripts/check_site.py
python -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. Do not publish output created by preview. Production CI always renders in a clean checkout.

## First GitHub Pages publication

1. Create a GitHub repository, with `main` as its default branch. Add **the contents of this folder**, including `.github`, at its root. This starter has no configured remote.
2. In repository **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. The included workflow deploys a Pages artifact; no `gh-pages` branch is needed.
3. Add `website.site-url` to `_quarto.yml`, using your actual published address, e.g. `https://YOUR-ACCOUNT.github.io/YOUR-REPO/`. Add `website.repo-url` with the real GitHub repository URL and optionally `website.repo-actions: [source, issue]`. Values are intentionally omitted until an actual repository is known.
4. Replace the repository-address notice in `get-involved.qmd` with links to that repository's Issues, Pull requests, and Discussions (enable Discussions first if desired). Confirm stewardship and licensing before inviting reuse; this starter does not choose a license on your behalf.
5. Push to `main`, or run **Build and publish OWAS** under Actions. Check both build and deploy jobs. Pull requests run validation and render but do not deploy.
6. Open the deployed URL. Check search, navigation, standards filters, and a narrow mobile viewport. Confirm unpublished content is absent.

Use source links such as `../../standards/index.qmd`; Quarto rewrites these during rendering. Do not hand-code a GitHub repository prefix into links or CSS assets. This supports both project Pages URLs and a future custom domain.

## Publish a metric

1. Copy `templates/metric.qmd` to `standards/<domain>/<stable-slug>/index.qmd`.
2. Fill all metadata and sections. Assign a unique, durable `metric-id`. Update dates manually to reflect editorial changes, not build time.
3. Keep `draft: true` while unfinished. Use `status: Draft` for a proposed definition even if it is ready for public discussion.
4. Set `categories` to the domain, type, and status, e.g. `[Headcount, Stock, Draft]`. These power Quarto's category browsing. Keep them consistent with the separate structured fields.
5. Set `draft: false` when ready to publish. Preview, render, check, then commit and push. The standards directory updates automatically.

Every domain page has an automatic listing, including domains with no published definitions yet. New metrics appear there and in the main standards directory without editing navigation.

## Publish an essay or research note

Copy the appropriate template to `essays/<slug>/index.qmd` or `research/<slug>/index.qmd`. Put figures, analysis code, and permitted supporting data beside it. Set title, description, author, dates, categories, and `draft`. Landing pages pick up one article folder per entry automatically. Use categories such as `PA Pulse`, `Labor market`, `Methodology`, or `Public data` instead of introducing a new navigation section for every topic.

## Drafts and review status

- `draft: true` controls publication. Production `draft-mode: gone` removes draft content and excludes it from search and listings. Quarto may leave an empty HTML placeholder at the URL.
- `status` controls metric maturity: Draft, Review, Recommended, Deprecated. Public Draft metrics are allowed; Recommended requires a documented decision.
- `templates/` is excluded from rendering. `research/unpublished-example/` is an intentional draft fixture with a sentinel checked by CI.
- Drafts in a public GitHub repository are still visible in its source history. Keep private material outside the repository.

## R and reproducible research

The initial site renders without R. For executable R notes, install R and `knitr`/`rmarkdown` locally, add project dependencies through `renv`, and render the note locally to produce `_freeze/`. Commit `_freeze/` and required assets (it is intentionally not ignored). Full project builds reuse frozen results. A new or changed executable note without frozen results will require R in CI; add `r-lib/actions/setup-r` and `r-lib/actions/setup-renv` before rendering if you prefer execution there. Do not rely on the default workflow to provision R. Record source versions and extraction dates in each note.

## Power BI

Update `dashboard/index.qmd` with a real report link once available. Record the report's data refresh date separately from the page's update date. Keep a direct link even if embedding; use an approved embed URL and an iframe with `class="powerbi"`, `title="Descriptive report title"`, and `loading="lazy"`. Authenticated reports still require Power BI access. A public embed exposes the report publicly; use only reports intended for public access. No report URL or invented refresh date is shipped in this starter.

## Maintenance rhythm

- Each edit: update metadata, preview, render, run checks, review the diff, and push or open a pull request.
- Each release: check mobile navigation, keyboard search, links, and draft exclusion on the deployed site. Add important changes to `CHANGELOG.md`.
- Quarterly: review external links and Actions/Quarto releases. Upgrade the local and CI Quarto version together in a pull request; render and check before merging.
- Keep slugs stable. If moving a page, add `aliases` to the new page for the old published HTML path and verify the redirect under your actual Pages base URL.
- Custom domain: configure DNS and the domain under GitHub Pages Settings, enable HTTPS when available, and update `website.site-url`. Recheck links and search after deployment.

## Structure and conventions

See [information architecture](docs/architecture.md) and [metadata conventions](docs/metadata.md). Add citations to `references.bib` and cite them with `@key`; no sample bibliography entries are invented.

Documentation used: [Quarto listings](https://quarto.org/docs/websites/website-listings.html), [search](https://quarto.org/docs/websites/website-search.html), [draft behavior](https://quarto.org/docs/websites/website-drafts.html), and [GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
