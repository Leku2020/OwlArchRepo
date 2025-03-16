---
layout: page
title: Build Packages
permalink: /buildpackages/
---

[🔙 Go back home](/OwlArchRepo/)

# GitHub Actions Workflow: Build Packages

This document explains the structure and functionality of a GitHub Actions workflow designed to build Arch Linux packages from `PKGBUILD` files and manage a repository database. The workflow is triggered by specific events and includes steps to detect changes, build packages, and upload artifacts.

---

## Workflow Triggers

The workflow is triggered under the following conditions:

1. **Push Events**:
   - Activates when changes are pushed to the `main` branch.
   - Only triggers if changes are made to specific file types or paths, such as:
     - `PKGBUILD`
     - `.SRCINFO`
     - Python scripts (`*.py`)
     - Desktop files (`*.desktop`)
     - Shell scripts (`*.sh`)
     - Icons (`*.png`)
     - License files (`COPYING`)
     - Systemd service files (`*.service`, `*.timer`)
     - Policy files (`*.policy`)
     - And more (see the full list in the workflow definition).

2. **Manual Trigger (`workflow_dispatch`)**:
   - Allows manual execution of the workflow via the GitHub UI.

---

## Jobs in the Workflow

### 1. Build Packages Job (`build_packages`)

#### Environment:
- Runs on: `ubuntu-latest`.
- Container: Uses the `archlinux:latest` Docker image with `--privileged` mode for elevated permissions.

#### Steps:

1. **Install Dependencies and Prepare Directories**:
   - Installs necessary packages (`base-devel`, `git`) using `pacman`.
   - Creates directories for storing built packages (`output_dir/pkgs/x86_64`).

2. **Checkout Repository**:
   - Clones the repository into the workspace using `actions/checkout@v4`.

3. **Mark Repository as Safe**:
   - Configures Git to treat the repository as safe to avoid permission issues.

4. **Download Latest Artifact**:
   - Uses a script to fetch the latest artifact named `packages_artifact-*` from previous workflow runs.
   - Outputs the artifact ID, name, and associated workflow run ID.

5. **Download Artifact if Exists**:
   - Downloads the latest artifact if it exists, placing it in the `output_dir`.

6. **Fallback if No Artifact Exists**:
   - Logs a message if no matching artifact is found.

7. **Detect Modified Paths**:
   - Compares the last two commits to identify modified files and directories.
   - Filters out irrelevant paths (e.g., `.github`, `pages`) and extracts unique parent directories.

8. **Create Non-Root User**:
   - Adds a non-root user (`builder`) with `sudo` privileges for building packages.

9. **Build Packages**:
   - Builds all packages if no artifact exists.
   - If an artifact exists, builds only the packages corresponding to modified directories.

10. **Clean Up Old Packages**:
    - Removes old package files in `output_dir` that match the names of modified directories.

11. **Build Modified Packages**:
    - Rebuilds packages for modified directories, ensuring that only valid `PKGBUILD` files are processed.

12. **Clean Up Repository Database**:
    - Removes existing repository database files (`OwlArchRepo.db.tar.gz`, `OwlArchRepo.db`) to prepare for regeneration.

13. **Create Repository Database**:
    - Uses `repo-add` to create a new repository database (`OwlArchRepo.db.tar.gz`).
    - Adds valid package files to the database, removing invalid ones.

14. **Upload Packages to GitHub**:
    - Uploads the `output_dir` containing the built packages and repository database as an artifact named `packages_artifact-${{ github.sha }}`.

15. **Job ID and Package Hash**:
    - Logs the workflow run ID and package hash for reference.

---

## Key Features

1. **Selective Building**:
   - Detects changes in the repository and rebuilds only the affected packages, improving efficiency.

2. **Artifact Management**:
   - Downloads the latest artifact from previous runs to reuse existing packages and avoid redundant builds.

3. **Repository Management**:
   - Automatically updates the repository database (`OwlArchRepo.db.tar.gz`) with valid packages.

4. **Error Handling**:
   - Includes fallback mechanisms for scenarios where no artifact exists or invalid packages are encountered.

5. **Privileged Mode**:
   - Uses `--privileged` mode in the container to ensure sufficient permissions for tasks like building packages.

---

## Example Use Case

This workflow is ideal for maintaining an Arch Linux package repository. By automating the detection of changes, building packages, and updating the repository database, it ensures that your repository remains up-to-date with minimal manual intervention. This setup is particularly useful for projects that frequently update their packages or manage multiple packages across different directories.

---
