---
layout: page
title: Build Pages
permalink: /buildpages/
---

[🔙 Go back home](/OwlArchRepo/)

# GitHub Actions Workflow: Build Pages

This document explains the structure and functionality of a GitHub Actions workflow designed to build static pages using Jekyll. The workflow is triggered by specific events and includes steps to install dependencies, process Markdown files, build the site, and upload artifacts.

---

## Workflow Triggers

The workflow is triggered under the following conditions:

1. **Push Events**:
   - Activates when changes are pushed to the `main` branch.
   - Only triggers if changes are made to `.markdown` files or within the `pages/**` directory.

2. **Manual Trigger (`workflow_dispatch`)**:
   - Allows manual execution of the workflow via the GitHub UI.

---

## Jobs in the Workflow

### 1. Build Pages Job (`build_pages`)

#### Conditions:
- Runs only if the trigger is from the `main` branch (`github.ref == 'refs/heads/main'`).

#### Environment:
- Runs on: `ubuntu-latest`.

#### Steps:

1. **Checkout Repository**:
   - Clones the repository into the workspace using `actions/checkout@v4`.

2. **Setup Pages**:
   - Configures the environment for GitHub Pages using `actions/configure-pages@v5`.

3. **Install Ruby and Bundler**:
   - Sets up Ruby version `3.0` and installs Bundler with caching enabled using `ruby/setup-ruby@v1`.

4. **Install Dependencies**:
   - Navigates to the `pages` directory and installs dependencies using `bundle install`.

5. **Copy Markdown Files**:
   - Copies `.markdown` files from the `extra` and `ownSoftware` directories to the `pages` directory while preserving their folder structure.
   - Creates necessary subdirectories in `pages` to maintain the relative paths of the copied files.

6. **Build with Jekyll**:
   - Builds the Jekyll site using `actions/jekyll-build-pages@v1`.
   - Specifies the source directory (`./pages`) and the destination directory (`./output_dir`).

7. **Upload Artifact**:
   - Uploads the built site (located in `./output_dir`) as a GitHub artifact named `pages_artifact-${{ github.sha }}` using `actions/upload-artifact@v4`.

8. **Job ID and Package Hash**:
   - Logs the workflow run ID and artifact hash (`pages_artifact-${{ github.sha }}`) for reference.

---

## Key Features

1. **Selective Building**:
   - Detects changes in `.markdown` files and the `pages` directory to ensure only relevant updates trigger the workflow.

2. **Markdown File Processing**:
   - Automatically copies `.markdown` files from `extra` and `ownSoftware` directories into the `pages` directory, preserving their folder structure for organization.

3. **Jekyll Integration**:
   - Uses Jekyll to generate static HTML pages from Markdown content, making it suitable for documentation or blog sites.

4. **Artifact Management**:
   - Uploads the generated site as an artifact for reuse in downstream workflows, such as deployment to GitHub Pages.

5. **Efficient Dependency Management**:
   - Leverages Bundler caching to speed up dependency installation during subsequent runs.

---

## Example Use Case

This workflow is ideal for automating the generation of a Jekyll-based static site hosted on GitHub Pages. By copying Markdown files from multiple directories and building them into a unified site, it ensures that your documentation or content remains organized and up-to-date. This setup is particularly useful for projects that manage content across different sections (e.g., `extra` and `ownSoftware`) but want to present it as a cohesive site.

---