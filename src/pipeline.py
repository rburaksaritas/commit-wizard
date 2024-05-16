from .ai_integration import generate_commit_message, parse_commit_message
from .git_operations import get_modified_files, get_file_content, get_file_diff, git_add, git_commit
GREEN = "\033[92m"
RESET = "\033[0m"

def generate_commits(repo_path):
    modified_files = get_modified_files(repo_path)

    for file_path in modified_files:
        old_content = get_file_content(repo_path, file_path, commit='HEAD^')
        new_content = get_file_content(repo_path, file_path, commit='HEAD')
        diff_content = get_file_diff(repo_path, file_path)
        
        commit_message_response = generate_commit_message(diff_content)
        title, message = parse_commit_message(commit_message_response)

        if title and message:
            print(f"{GREEN}----Commit Generated----{RESET}", "\n", title, "\n\n", message, "\n", f"{GREEN}-----------------------{RESET}")
            git_add(repo_path, file_path)
            git_commit(repo_path, title, message)
        else:
            print("No commit message generated. Please try again.")
            exit(1)