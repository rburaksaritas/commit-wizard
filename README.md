# Commit Wizard

Commit Wizard is a python tool designed to automate the process of generating meaningful and descriptive commit messages for your Git repository. Leveraging OpenAI's GPT-3.5 API, this tool analyzes the changes in your codebase and generates commit messages that accurately reflect the modifications made, ensuring your project history is clear and informative.

## Features

- **Automatic Commit Message Generation**: Uses OpenAI's GPT-3.5 to generate descriptive commit messages based on the diffs of modified files.
- **Git Integration**: Seamlessly integrates with your Git workflow to add, commit, and push changes with generated messages.
- **Configurable API Key and Model**: Specify your OpenAI API key and desired model in `config.py` file.
