import os
from .ai_integration import generate_commit_message, parse_commit_message
from .git_operations import get_modified_files, get_file_content, get_file_diff, git_add, git_commit
GREEN = "\033[92m"
RESET = "\033[0m"

def generate_commits(repo_path, specific_files=None, ignored_files=None):
    ignored_files = ignored_files or []
    modified_files = get_modified_files(repo_path)

    if specific_files:
        modified_files = [file for file in specific_files if file in modified_files]
    
    def is_ignored(file):
        for ignore in ignored_files:
            if file == ignore or file.startswith(ignore + os.sep):
                return True
        return False
    
    if ignored_files:
        modified_files = [file for file in modified_files if not is_ignored(file)]

    if not modified_files:
        print("No modified files to process.")
        return

    print(f"Generating commits for files: %s" % modified_files)

    for file_path in modified_files:
        old_content = get_file_content(repo_path, file_path, commit='HEAD^')
        new_content = get_file_content(repo_path, file_path, commit='HEAD')
        diff_content = get_file_diff(repo_path, file_path)

        is_new_file = not old_content.strip() and new_content.strip()

        commit_message_response = generate_commit_message(diff_content, is_new_file=is_new_file)
        print(commit_message_response)
        title, message = parse_commit_message(commit_message_response)

        if title and message:
            print(f"{GREEN}----Commit Generated----{RESET}", "\n", title, "\n\n", message, "\n", f"{GREEN}-----------------------{RESET}")
            git_add(repo_path, file_path)
            git_commit(repo_path, title, message)
        else:
            print("No commit message generated. Please try again.")
            exit(1)
