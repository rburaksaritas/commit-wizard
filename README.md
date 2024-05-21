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

- **`--file`**: (Optional) Specify one or more files to generate commits for. If absent, the program checks for all modified files.

- **`--ignore`**: (Optional) Specify one or more files or directories to ignore during commit message generation. `src/config.py` is ignored to prevent API key exposure.

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

3. **Specify files to generate commits for**:
    ```sh
    python3 main.py /path/to/repo --file src/pipeline.py main.py
    ```

4. **Ignore specific files or directories**:
    ```sh
    python3 main.py /path/to/repo --ignore src/config.py src/__pycache__
    ```

3. **Example Process used for adding sections to this README**:
    ```sh
    $ python3 main.py ./commit-wizard --push main
    ----Commit Generated---- 
    Added Contributing Guidelines and Acknowledgements 

    - Added a "Contributing" section to the README file encouraging contributions through forking and creating pull requests.
    - Added an "Acknowledgements" section with links to OpenAI and Git websites to acknowledge their contributions. 
    -----------------------
    [main def1e2c] Added Contributing Guidelines and Acknowledgements
    1 file changed, 9 insertions(+)
    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 681 bytes | 681.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    To github.com:rburaksaritas/commit-wizard.git
    72275f9..def1e2c  main -> main
   ```

4. **Example of multiple file modifications**:
    ```sh
    $ python3 main.py burak/tcdd-bilet-bulucu-web --push main
    ----Commit Generated---- 
    Update hour dropdown selection and adjust loop iterations 

    - Added a function updateHourDropdown() to format and update selections in the hour dropdown.
    - Updated the loop iteration in runFinder() from iterating 5 times to 4 times for better performance. 
    -----------------------
    [main e566a41] Update hour dropdown selection and adjust loop iterations
    1 file changed, 2 insertions(+), 1 deletion(-)
    ----Commit Generated---- 
    Update background colors in style.css 

    - Updated background color in the body selector from f4f4f5 to f4f4f4.
    - Updated background color in the button selector from 3498db to 3498dd. 
    -----------------------
    [main e1fdf7d] Update background colors in style.css
    1 file changed, 2 insertions(+), 2 deletions(-)
    Enumerating objects: 12, done.
    Counting objects: 100% (12/12), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (9/9), done.
    Writing objects: 100% (9/9), 1.17 KiB | 1.17 MiB/s, done.
    Total 9 (delta 5), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (5/5), completed with 3 local objects.
    To github.com:rburaksaritas/tcdd-bilet-bulucu-web.git
    884f102..e1fdf7d  main -> main
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