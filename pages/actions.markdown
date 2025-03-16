---
layout: software
title: Actions
permalink: /actions
---

[🔙 Go back home](/OwlArchRepo/)

# Introduction to the Three Pipelines

This repository utilizes three distinct GitHub Actions pipelines to automate key processes: **Build Packages**, **Build Pages**, and **Prepare and Deploy Artifact**. Each pipeline serves a specific purpose, ensuring efficient workflows for package management, documentation generation, and artifact deployment. Below is an overview of each pipeline and its role in the overall workflow.

---

## 1. Build Packages Pipeline

The **Build Packages** pipeline is responsible for building Arch Linux packages from `PKGBUILD` files and managing a repository database. This pipeline ensures that your package repository remains up-to-date with minimal manual intervention.

### Key Features:
- **Selective Building**: Detects changes in the repository and rebuilds only the affected packages, improving efficiency.
- **Artifact Management**: Downloads the latest artifact from previous runs to reuse existing packages and avoid redundant builds.
- **Repository Management**: Automatically updates the repository database (`OwlArchRepo.db.tar.gz`) with valid packages.
- **Error Handling**: Includes fallback mechanisms for scenarios where no artifact exists or invalid packages are encountered.

### Use Case:
This pipeline is ideal for maintaining an Arch Linux package repository. It automates the detection of changes, builds packages, and updates the repository database, ensuring consistency and reliability.

[View the full GitHub Actions pipeline →](buildpackages)
---

## 2. Build Pages Pipeline

The **Build Pages** pipeline focuses on generating static HTML pages using Jekyll. It processes Markdown files from various directories and organizes them into a cohesive structure for hosting on GitHub Pages.

### Key Features:
- **Markdown File Processing**: Copies `.markdown` files from `extra` and `ownSoftware` directories into the `pages` directory while preserving their folder structure.
- **Jekyll Integration**: Uses Jekyll to generate static HTML pages from Markdown content, making it suitable for documentation or blog sites.
- **Artifact Management**: Uploads the generated site as an artifact for reuse in downstream workflows, such as deployment to GitHub Pages.
- **Efficient Dependency Management**: Leverages Bundler caching to speed up dependency installation during subsequent runs.

### Use Case:
This pipeline is designed for automating the generation of a Jekyll-based static site hosted on GitHub Pages. It ensures that your documentation or content remains organized and up-to-date, even when managing content across multiple directories.

[View the full GitHub Actions pipeline →](buildpages)
---

## 3. Prepare and Deploy Artifact Pipeline

The **Prepare and Deploy Artifact** pipeline combines artifacts from the **Build Pages** and **Build Packages** pipelines and deploys them to GitHub Pages. This pipeline ensures that both documentation and downloadable assets are hosted together on a unified site.

### Key Features:
- **Manual Triggering**: Allows flexibility in specifying the artifacts and pipeline IDs for deployment.
- **Artifact Management**: Combines artifacts from two separate workflows (page generation and package build) into a single directory (`pages`) for deployment.
- **Environment Configuration**: Configures the `github-pages` environment with appropriate permissions and outputs the deployed site's URL.
- **Verification**: Includes a step to list the contents of the `pages` directory, ensuring that the artifacts are correctly downloaded before proceeding.

### Use Case:
This pipeline is ideal for deploying a GitHub Pages site that hosts both documentation and downloadable assets (e.g., ISOs or binaries). By combining artifacts from multiple upstream workflows, it creates a unified site that provides users with easy access to all resources.

[View the full GitHub Actions pipeline →](deploy)
---

## Workflow Overview

1. **Build Packages**:
   - Detects changes in the repository and builds Arch Linux packages.
   - Updates the repository database with valid packages.

2. **Build Pages**:
   - Processes Markdown files and generates a static site using Jekyll.
   - Uploads the generated site as an artifact.

3. **Prepare and Deploy Artifact**:
   - Combines artifacts from the **Build Pages** and **Build Packages** pipelines.
   - Deploys the combined artifacts to GitHub Pages.

---

By leveraging these three pipelines, this repository achieves a fully automated workflow for managing packages, generating documentation, and deploying resources. Each pipeline plays a critical role in ensuring that the project remains maintainable, efficient, and user-friendly.
