# Commit Wizard

Commit Wizard is a python tool designed to automate the process of generating meaningful and descriptive commit messages for your Git repository. Leveraging OpenAI's GPT-3.5 API, this tool analyzes the changes in your codebase and generates commit messages that accurately reflect the modifications made, ensuring your project history is clear and informative.

## Features

- **Automatic Commit Message Generation**: Uses OpenAI's GPT-3.5 to generate descriptive commit messages based on the diffs of modified files.
- **Git Integration**: Seamlessly integrates with your Git workflow to add, commit, and push changes with generated messages.
- **Configurable API Key and Model**: Specify your OpenAI API key and desired model in `config.py` file.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/rburaksaritas/commit-wizard.git
    cd commit-wizard
    ```

2. **Install dependencies**:
    Ensure you have `openai` and other required libraries installed. You can install them using pip:
    ```sh
    pip install openai
    ```

3. **Configure API Key and Model**:
    Modify the `config.py` file under the `src` directory to add your OpenAI API key:
    ```python
    OPENAI_API_KEY = 'your_api_key'
    MODEL = 'gpt-3.5-turbo'
    ```
    You can also specify the model as desired.

## Usage

### Command Line Interface

The tool can be used directly from the command line. Here are the available options:

- **`repo_path`**: Path to the local Git repository.
- **`--push`**: (Optional) Branch name to push the changes. If not specified, the program will stage the changes and generate seperate commits for each file with generated commit messages, but it will not push them to the remote repository.

### Examples

1. **Generate commit messages and commit changes**:
    ```sh
    python3 main.py /path/to/repo
    ```

2. **Generate commit messages, commit changes, and push to a branch**:
    ```sh
    python3 main.py /path/to/repo --push main
    ```

## Project Structure

- **`main.py`**: Entry point of the application. Handles command-line arguments and orchestrates the commit process.
- **`src/git_operations.py`**: Contains functions for interacting with Git, such as getting modified files, adding files, and committing changes.
- **`src/ai_integration.py`**: Contains functions for interacting with OpenAI's GPT-3.5 API to generate and parse commit messages.
- **`src/config.py`**: Configuration file for specifying the OpenAI API key and model.
- **`src/pipeline.py`**: Contains the pipeline functionality that detects changes, generates commit messages and commit the changes for each file.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT-3.5 API.
- [Git](https://git-scm.com/) for the powerful version control system.