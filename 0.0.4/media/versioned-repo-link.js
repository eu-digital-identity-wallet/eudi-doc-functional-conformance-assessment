(function () {
  // Canonical repo URL (keep in sync with mkdocs.yml repo_url)
  const REPO =
    "https://github.com/eu-digital-identity-wallet/eudi-doc-functional-conformance-assessment";

  // mike version is the first path segment: /0.0.2/... or /latest/...
  const seg = window.location.pathname.split("/").filter(Boolean)[0];

  // Tags are assumed to be vX.Y.Z (e.g., v0.0.2). If your tags are X.Y.Z, remove the 'v' prefix here.
  const tag = seg && seg !== "latest" ? `v${seg}` : null;

  // 1) Rewrite the Material "repo" header link to version-specific tree
  const repoLink =
    document.querySelector("a.md-header__source") ||
    document.querySelector(
      'a[href^="https://github.com/"][class*="md-header__source"]'
    );

  if (repoLink) {
    if (tag) {
      repoLink.href = `${REPO}/tree/${tag}`;
      repoLink.title = `View source (${tag})`;
    } else {
      repoLink.href = REPO;
      repoLink.title = "View source";
    }
  }

  // Helper: resolve a root file URL for either a tag or default branch without hardcoding branch name
  function rootFileUrl(filename) {
    if (tag) return `${REPO}/blob/${tag}/${filename}`;
    return `${REPO}/blob/HEAD/${filename}`;
  }

  // 2) Rewrite placeholder links in docs to point to correct version of root files
  // Use these placeholders in docs markdown:
  //   - [View CONTRIBUTING](#contributing-source)
  //   - [View LICENSE](#license-source)
  //   - [View CHANGELOG](#changelog-source) (optional)
  const rewrites = [
    { selector: 'a[href="#contributing-source"]', file: "CONTRIBUTING.md", label: "CONTRIBUTING.md" },
    { selector: 'a[href="#license-source"]', file: "LICENSE.md", label: "LICENSE" },
    { selector: 'a[href="#changelog-source"]', file: "CHANGELOG.md", label: "CHANGELOG.md" },
  ];

  rewrites.forEach(({ selector, file, label }) => {
    document.querySelectorAll(selector).forEach((a) => {
      a.href = rootFileUrl(file);
      a.title = tag ? `View ${label} (${tag})` : `View ${label}`;
    });
  });
})();
