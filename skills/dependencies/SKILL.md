---
name: dependencies
description: Add, remove, upgrade, or pin a dependency with the ecosystem's package manager instead of hand-editing the manifest. Use when installing a library, bumping a version, enabling a package feature, or about to edit package.json, Cargo.toml, pyproject.toml, go.mod, pubspec.yaml, Gemfile, or any other dependency manifest.
---

# Dependencies

Always use the appropriate package manager to manage dependencies. Never simply edit the manifest. This ensures we get the latest release version. It facilitates dependency configuration, e.g. enabling features, and ensures correct manifest syntax.