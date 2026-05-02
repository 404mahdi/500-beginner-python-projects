# Contributing Guidelines

Thank you for considering contributing to this project! If you face any issues or have suggestions for improvements, feel free to contact us!

# Keep in mind

- Try to use prettier for formatting your code.
- Make the code as much readable as possible.
- Try to use comments to explain your code.

## How to contribute

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a new branch.
4. Create a new project directory.
5. Implement your project using Python. Make sure to follow the [project structure](./README.md/#project-structure).
6. Commit and push your changes to your forked repository.
7. Create a pull request to submit your project for review.

## Automated PR Validation 🤖

We've enabled GitHub Actions to automatically validate your pull requests! Here's what happens:

### What gets checked:

- 🔒 **Security Scan**: Automated detection of potentially malicious code patterns
  - Dangerous functions like `eval()`, `exec()`, `compile()`
  - Shell command execution (`os.system()`, `shell=True`)
  - Suspicious imports (pickle, base64 decoding)
  - Direct IP addresses (potential data exfiltration)
  - System directory writes
  - Bandit security scanner for additional vulnerabilities
- ✅ **Project Structure**: Your project must be in its own directory
- ✅ **README.md**: Must be present and include the key sections. The validator accepts common alternative headings (case-insensitive), for example:
  - Description
  - Frameworks and Modules Used (also accepted: `Tech Stack`, `Technologies Used`)
  - How to run
  - Author
    Note: Missing non-security sections will now generate warnings (the PR can still pass validation unless a critical error exists).
- ✅ **Python Files**: At least one `.py` file with valid Python syntax
- ✅ **Code Quality**: Python syntax validation for all files

### Automated Workflow:

1. **Submit PR**: When you create a pull request, automated checks will run
2. **Security Scan**: Your Python code is scanned for malicious patterns
3. **Validation**: The workflow validates your project structure and code
4. **Feedback**: You'll receive a comment with the validation results
5. **Auto-merge**: If all checks pass, your PR will be labeled `auto-merge-ready` and automatically approved
6. **Merge**: PRs that pass validation can be automatically merged (if repository settings allow)
7. **README Update**: After merge, your project is automatically added to the main README.md table! 🎉

### No Manual README Updates Needed!

When your PR is merged, a bot will automatically:

- Extract your project name, description, and author info from your project's README.md
- If an explicit `Author` link is present, that will be used. If the `Author` section is missing or doesn't include a link, the bot will use the PR author's GitHub username as the author and populate a profile URL (e.g. `https://github.com/<username>`).
- Add your project to the main README.md table with the next available serial number
- Attempt to commit and push the update to the `main` branch. If the repository's branch protection prevents a direct push, the bot will create a branch with the README change and open a PR for maintainers to review and merge.
- You'll get a confirmation comment on your PR linking to the README update (or the README-update PR when applicable).

**Important**: Make sure your project's README.md follows the template and includes the key sections (see above). If a non-critical section is missing, you'll receive a warning in the validation comment but the PR can still proceed if no other errors are present.

### If validation fails:

- Check the PR comments for specific errors
- Fix the issues in your branch
- Push the changes - validation will run again automatically

### If security scan flags your code:

- 🚨 Review the security warnings carefully
- Remove any potentially malicious code patterns
- If the flagged code is necessary for your project's functionality, explain why in your PR description
- A maintainer will manually review PRs with security concerns before merging

### Safe coding practices:

- ❌ Avoid using `eval()`, `exec()`, or `compile()` - they can execute arbitrary code
- ❌ Don't use `os.system()` or `subprocess` with `shell=True` - use safer alternatives
- ❌ Avoid pickle for data serialization - use JSON instead
- ✅ Use parameterized queries/commands to prevent injection attacks
- ✅ Validate and sanitize all user inputs
- ✅ Use built-in libraries and functions when possible

### Documentation Changes:

- PRs that only modify documentation files (README.md, CONTRIBUTING.md) skip project validation
- These still need manual review before merging

### README auto-update details

- The README updater extracts project info from the project's `README.md`. To ensure accurate entries:
  - Include an `Author` section with a link `[Name](https://github.com/username)` if you want a specific author display.
  - If no author link is present, the PR author's GitHub username will be used and a profile URL will be generated automatically.
  - Use one of the accepted headings for the tech list: `Frameworks and Modules Used`, `Tech Stack`, or `Technologies Used`.
  - The updater will try to push directly to `main`. If a push is blocked by branch protection, it creates a branch and opens a PR with the README update. The README-update PR will be linked in the original PR's comments for maintainers to review.

## What to contribute

- You can contribute any project you like, as long as it is written in Python.
- You can update documentation, fix typos, and other small improvements.

## Conclusion

Thank contributors for their interest in the project and their willingness to contribute. Provide contact information or links to further resources if needed.

We appreciate your contributions and look forward to your involvement in the project!
