# Portfolio Proof Hub — content guide

The website uses static HTML, CSS and JavaScript. It can be hosted on GitHub Pages without a build system.

## Publishing

Keep the existing repository's `favicon.svg` and `og.png` when replacing the old site files. The HTML references those assets.

1. Create a branch from the existing portfolio repository (`main`).
2. Replace `index.html`, `styles.css` and `script.js` with the files from this package.
3. Add `content/catalog.js` to the repository (the `content` directory is new).
4. Inspect the preview/PR and test the site on mobile and desktop.
5. Merge after approval. GitHub Pages must be configured to publish the expected branch and root directory.

## Adding new material

Update **only** `content/catalog.js` for normal content changes:

- `projects`: documented system case studies with GitHub repo, evidence and optional video link.
- `videos`: YouTube walkthrough links and matching `i.ytimg.com` thumbnails.
- `slices`: focused components inside existing builds. Do not describe them as standalone projects unless they genuinely are.
- `posts`: selected public LinkedIn posts. Use the direct post URL and a short original summary.

New work should link to concrete evidence, scope, and ownership. Avoid client metrics, production claims or customer logos without permission and supporting evidence.

## Quality checks before publishing

- Link checker for GitHub, YouTube and LinkedIn URLs (some platforms restrict automated checks).
- Review all technical claims against actual repositories.
- Test `index.html` in a browser; the scripts do not need a web server for basic rendering.
- Verify responsive layout at mobile and desktop widths.
- Check the open-graph sharing image (`og.png`) and canonical URL after the production URL is selected.
- Update the canonical and OG URLs together if migrating to a new single-link domain.

## Verified initial evidence sources

P1: https://github.com/mahdi-eqbal/p1-product-led-revenue-system
P2: https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system
P3: https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system

Default technical walkthrough: https://youtu.be/Q-sc8ETdLwk
Short overview: https://youtu.be/WypfoN5QbWY

Initial public LinkedIn posts are listed in `content/catalog.js`.

## Notes

This package is an additive redesign proposal, not an overwrite of the live GitHub repository. Only `content/catalog.js`, `index.html`, `styles.css`, `script.js` and this guide are new/replaced; the existing projects and any other repository files stay unchanged.