# GitHub Actions Workflows

This directory contains automated workflows for the 500 Beginner Python Projects repository.

## Workflows

### 1. PR Validation (`pr-validation.yml`)

**Trigger**: When a pull request is opened, updated, or reopened

**Purpose**: Automatically validates that pull requests meet the contribution guidelines and checks for malicious code

**Checks Performed**:

**Security Checks** 🔒:
- 🚨 Scans for dangerous Python functions (`eval()`, `exec()`, `compile()`, `__import__()`)
- 🚨 Detects shell command execution (`os.system()`, `shell=True` in subprocess)
- 🚨 Identifies pickle usage (can execute arbitrary code)
- 🚨 Flags suspicious IP addresses (potential data exfiltration)
- 🚨 Detects base64 decoding (potential code obfuscation)
- 🚨 Checks for writes to system directories
- 🚨 Runs Bandit security scanner for additional vulnerability detection

**Structure Checks**:
- ✅ Validates project directory structure
- ✅ Ensures README.md exists and contains required sections:
  - Description
  - Frameworks and Modules Used
  - How to run
  - Author
- ✅ Verifies at least one Python file exists
- ✅ Validates Python syntax for all `.py` files
- ✅ Adds `auto-merge-ready` label if all checks pass

**Outputs**:
- Comments on PR with validation results
- Adds labels for automated processing
- Provides specific error messages if validation fails
- **Blocks auto-merge if security concerns are detected**

### 2. Auto Merge (`auto-merge.yml`)

**Trigger**: When a PR is labeled or when PR Validation workflow completes successfully

**Purpose**: Automatically approves and merges PRs that pass all validation checks

**Process**:
1. Checks if PR has `auto-merge-ready` label
2. Approves the PR automatically
3. Enables auto-merge (or directly merges if possible)
4. Comments on PR with merge status

**Requirements**:
- PR must have `auto-merge-ready` label (added by PR Validation workflow)
- All validation checks must pass
- No merge conflicts

### 3. Update README on Merge (`update-readme.yml`)

**Trigger**: When a pull request is merged to main branch

**Purpose**: Automatically adds new projects to the main README.md table

**Process**:
1. Detects new project directories from merged PR
2. Extracts project information from project README.md:
   - Project title (from first # heading)
   - Description (from ## Description section)
   - Author name and link (from ## Author section)
3. Checks if project already exists in main README
4. If not present, adds new entry to the projects table with:
   - Next available serial number
   - Project title with link to project directory
   - Project description
   - Author name with link to GitHub profile
5. Commits and pushes changes to main branch
6. Comments on the merged PR confirming the update

**Benefits**:
- 🤖 Eliminates manual README updates
- ✅ Ensures consistent formatting
- 🎯 Automatically assigns serial numbers
- 📝 Extracts info directly from project documentation
- 🚫 Prevents duplicate entries
4. Comments on PR with merge status

**Requirements**:
- PR must have `auto-merge-ready` label (added by PR Validation workflow)
- All validation checks must pass
- No merge conflicts

## How It Works

```
┌─────────────────┐
│   PR Created    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ PR Validation   │
│   Workflow      │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌────────┐
│ Pass  │ │  Fail  │
└───┬───┘ └───┬────┘
    │         │
    │         └──► Comments with errors
    │
    ▼
┌─────────────────┐
│ Add auto-merge  │
│  -ready label   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Auto Merge     │
│   Workflow      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PR Approved &  │
│     Merged      │
└─────────────────┘
```

## Configuration

### Repository Settings Required

For auto-merge to work properly, ensure these settings are configured in your repository:

1. **Allow auto-merge**: Go to Settings → General → Pull Requests → Check "Allow auto-merge"
2. **Branch protection** (optional but recommended):
   - Go to Settings → Branches → Add rule for `main`
   - Enable "Require status checks to pass before merging"
   - Select the PR Validation workflow as a required check

### Permissions

The workflows require the following permissions:
- `contents: write` - To merge PRs
- `pull-requests: write` - To comment and label PRs

## Customization

### Adding More Validation Rules

To add more validation rules, edit `.github/workflows/pr-validation.yml`:

1. Add new checks in the "Validate project structure" step
2. Update error messages accordingly
3. Ensure validation failures set `VALIDATION_PASSED=false`

### Changing Merge Method

By default, PRs are merged using the **squash** method. To change this:

1. Edit `.github/workflows/auto-merge.yml`
2. Find `mergeMethod: SQUASH` and change to:
   - `MERGE` for regular merge
   - `REBASE` for rebase merge

## Troubleshooting

### Auto-merge doesn't work

**Possible causes**:
- Auto-merge is not enabled in repository settings
- PR has merge conflicts
- Required status checks are not passing
- Branch protection rules prevent auto-merge

**Solution**: Check repository settings and branch protection rules

### Validation fails unexpectedly

**Possible causes**:
- Missing required sections in README.md
- Python syntax errors
- Project files in wrong location

**Solution**: Check the PR comments for specific error messages and fix accordingly

### Workflow doesn't trigger

**Possible causes**:
- Workflows are disabled in repository settings
- Branch name doesn't match (should target `main`)

**Solution**: Enable workflows in Settings → Actions → General

## Testing

To test the workflows without affecting the main repository:

1. Create a test branch
2. Make changes to workflow files
3. Create a test PR with sample project
4. Observe workflow execution in the Actions tab
5. Check PR comments and labels

## Support

For issues or questions about the workflows:
- Open an issue in the repository
- Check workflow logs in the Actions tab
- Review the [Contributing Guidelines](../CONTRIBUTING.md)
