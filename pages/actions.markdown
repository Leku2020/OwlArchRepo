---
layout: software
title: Actions
permalink: /actions
---

[🔙 Go back home](/)

# GitHub Actions Pipeline for Building PKGBUILDs and Deploying Pages

## Overview
This GitHub Actions pipeline automates the process of building Arch Linux packages from `PKGBUILD` files, generating documentation pages with Jekyll, and deploying the output to GitHub Pages. It supports feature branch builds and main branch deployments.

## Workflow Triggers
The pipeline runs under the following conditions:
- On every push to the `main` branch
- On every push to branches following the pattern `feature/**`
- Manually triggered via `workflow_dispatch`

## Jobs Breakdown
### 1. `build_packages`
Builds the Arch Linux packages from `PKGBUILD` files.

**Steps:**
- Checkout the repository
- Run an Arch Linux container to:
  - Create a `builder` user
  - Install required dependencies (`sudo`, `base-devel`, `git`)
  - Locate all `PKGBUILD` files and run `makepkg -si`
  - Move built `.pkg.tar.zst` files to `output_dir`
- Upload the generated package artifacts to GitHub

### 2. `build_pages`
Builds Jekyll-based documentation pages.

**Steps:**
- Checkout the repository
- Set up GitHub Pages
- Install Ruby and Jekyll dependencies
- Copy markdown files from `extra/` to `pages/`
- Run `jekyll build` to generate static pages
- Upload the generated pages as an artifact

### 3. `prepare_deploy_artifact`
Combines package artifacts and Jekyll-generated pages into a final deployment package.

**Steps:**
- Download artifacts from `build_packages` and `build_pages`
- Copy `.pkg.tar.zst` files into `/pkgs/x86_64/`
- Run `repo-add` inside an Arch Linux container to update the package database
- Merge Jekyll build output into the deployment directory
- Upload the combined artifact for deployment

### 4. `deploy`
Deploys the prepared artifact to GitHub Pages.

**Steps:**
- Deploy `deploy_artifact` using `actions/deploy-pages`

### 5. `detect_modified_paths`
Detects modified files in feature branches and selectively builds affected packages.

**Steps:**
- Checkout the repository
- Compare changes against `main`
- Identify modified directories within `extra/`
- Build only the affected packages
- Upload the modified package artifacts

## Conditional Execution
- The `build_pages`, `prepare_deploy_artifact`, and `deploy` jobs run only when pushing to `main`
- The `detect_modified_paths` job runs only for feature branches

## Artifact Management
- `build_packages_artifact`: Contains compiled Arch Linux packages
- `build_pages_artifact`: Contains Jekyll-generated HTML files
- `deploy_artifact`: Combines package repository and documentation pages

## Deployment URL
The final deployed website is available at the GitHub Pages environment URL defined in the pipeline.

---

This workflow ensures efficient package management and documentation deployment for an Arch Linux repository while maintaining CI/CD best practices.

