---
layout: software
title: Contribute
permalink: /contribute
---

[🔙 Go back home](/owlArchRepo/)

# Contributing to OwlArch Package Repository

Thank you for contributing! Follow these guidelines to maintain package quality and consistency.

## Repository Structure

```
.
├── extra/                      # Package directories
│   ├── package-name/
│   │   ├── PKGBUILD            # Build recipe
│   │   └── .SRCINFO            # Auto-generated metadata
│   │   └── README.markdown     # Auto-generated metadata
├── pages/                      # Documentation site
└── ...
```

## Creating/Updating Packages

1. **Package Requirements**  
   - Follow [Arch Packaging Standards](https://wiki.archlinux.org/title/Arch_package_guidelines)
   - Use `makepkg --printsrcinfo > .SRCINFO` to generate metadata
   - Test builds locally with:  
     ```bash
     docker run --rm -v $(pwd):/pkg -w /pkg archlinux:latest makepkg -si --noconfirm
     ```

2. **New Packages**  
   - Create directory: `extra/<package-name>`
   - Add `PKGBUILD` and generate `.SRCINFO`
   - Verify dependencies exist in official repos or this repository
   - Create the `README.markdown` with the structure specified below

    ````markdown
    ---
    layout: software
    title: Title
    permalink: /title
    ---

    [🔙 Go back home](/owlArchRepo/)

    # Title

    ## Introduction
    Description
    ## Features

    - ...
    - ...
    - ...

    ## Installation

    1. Open a terminal.
    2. Install ... using the following command:

      ```sh
      sudo pacman -S ...
      ```

    ### Install verification

    ### Uninstall
    ## Usage


    ## Official documentation & More Info

    ## Contributing

    ## Support

    ## License

    <div style="display: flex; justify-content: space-between;">
      <a href="prevtitle">🔙 PrevTitle</a>
      <a href="nexttitle">🔜 NextTitle</a>
    </div>
    ````

3. **Updates**  
   - Bump `pkgver` and `pkgrel` appropriately
   - Update checksums with `updpkgsums`
   - Document significant changes in PKGBUILD comments and in the `README.markdown`

## Branching & Pull Requests

1. **Branch Strategy**  
   - `main`: Stable packages with automated deployment
   - `feature/*`: Work-in-progress changes (automatically tested)

2. **PR Checklist**  
   - [ ] Valid `PKGBUILD` and `.SRCINFO`  
   - [ ] Local build test passed  
   - [ ] Dependencies properly declared  
   - [ ] Package name follows `lowercase-hyphenated` format  
   - [ ] Version update reflected in `pkgver`/`pkgrel`

## Testing Locally

Simulate CI workflow:
```bash
# Build packages
docker run --rm -v $(pwd):/workspace -w /workspace archlinux:latest bash -c "
  pacman -Syu --noconfirm && 
  pacman -S --noconfirm base-devel &&
  makepkg --noextract --noprepare --nocheck --nosign
"

# Verify repository structure
repo-add pkgs/x86_64/owlArchRepo.db.tar.gz *.pkg.tar.zst
```

## Common Issues

- **Build Failures**  
  Check CI logs for:  
  `error: failed to prepare transaction (package failed to build)`  
  Common fixes: Update dependencies, fix checksums, or adjust build steps

- **Database Conflicts**  
  Ensure only one package provides the same binary/files

## Deployment Process

On `main` branch push:
1. Builds all PKGBUILDs in `extra/`
2. Generates repository database (`owlArchRepo.db`)
3. Deploys documentation to GitHub Pages
4. Packages become immediately available via:  
   ```ini
   [owlArchRepo]
   Server = https://leku2020.github.io/owlArchRepo/pkgs/x86_64
   ```

## Need Help?

- Check [GitHub Actions logs](https://github.com/Leku2020/owlArchRepo/actions)
- Ask in [Discussions](https://github.com/Leku2020/owlArchRepo/discussions)
- Review existing [PKGBUILD examples](https://github.com/Leku2020/owlArchRepo/tree/main/extra)

Let's keep the OSINT/malware analysis community tools sharp! 🦉🔍