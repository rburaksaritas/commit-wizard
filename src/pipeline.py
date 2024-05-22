import os
import difflib
from .ai_integration import generate_commit_message, parse_commit_message
from .git_operations import get_modified_files, get_file_content, get_file_diff, git_add, git_commit, git_rm, file_exists_in_commit

GREEN = "\033[92m"
RESET = "\033[0m"

def generate_commits(repo_path, specific_files=None, ignored_files=None):
    ignored_files = ignored_files or []
    ignored_files.append('src/config.py')
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

    print(f"{GREEN}Generating commits for files: %s{RESET}" % modified_files)

    for file_path in modified_files:
        print(f"{GREEN}Generating commit for file: {file_path}{RESET}")
        file_existed_in_previous_commit = file_exists_in_commit(repo_path, file_path, 'HEAD')
        old_content = get_file_content(repo_path, file_path, commit='HEAD') if file_existed_in_previous_commit else ''
        new_content = get_file_content(repo_path, file_path, commit='WORKING')
        diff_summary = '\n'.join(difflib.unified_diff(
            old_content.splitlines(),
            new_content.splitlines(),
            fromfile='old_content',
            tofile='new_content',
            lineterm=''
        ))
        diff_content = get_file_diff(repo_path, file_path)
        summary = (
                    f"diff summary: {diff_summary}\n"
                    f"diff content: {get_file_diff(repo_path, file_path)}"
        )
        
        is_new_file = not file_existed_in_previous_commit and os.path.exists(os.path.join(repo_path, file_path)) and not diff_content.split()
        is_deleted_file = file_existed_in_previous_commit and not os.path.exists(os.path.join(repo_path, file_path))

        if is_new_file:
            summary += f"The file {file_path} is newly created."
        elif is_deleted_file:
            summary += f"The file {file_path} was deleted."

        commit_message_response = generate_commit_message(
            summary,
            is_new_file=is_new_file,
            is_deleted_file=is_deleted_file
        )
        title, message = parse_commit_message(commit_message_response)

        if title and message:
            print(title, "\n\n", message, "\n", f"{GREEN}Commit message generated successfully.{RESET}")
            if is_deleted_file:
                git_rm(repo_path, file_path)
            else:
                git_add(repo_path, file_path)
            git_commit(repo_path, title, message)
            print(f"{GREEN}Modified file {file_path} is commited successfully.{RESET}")
        else:
            print("No commit message generated. Please try again.")
            exit(1)
