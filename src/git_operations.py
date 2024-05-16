import subprocess

def get_modified_files(repo_path):
    """Get a list of modified files in the git repository."""
    result = subprocess.run(['git', '-C', repo_path, 'status', '--porcelain'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    modified_files = [line.split()[1] for line in lines if len(line.split()) > 1]
    return modified_files

def get_file_content(repo_path, file_path, commit='HEAD'):
    """Get the content of a file at a specific commit."""
    result = subprocess.run(['git', '-C', repo_path, 'show', f'{commit}:{file_path}'], capture_output=True, text=True)
    return result.stdout

def get_file_diff(repo_path, file_path):
    """Get the diff of a file."""
    result = subprocess.run(['git', '-C', repo_path, 'diff', file_path], capture_output=True, text=True)
    return result.stdout

def git_add(repo_path, file_path):
    subprocess.run(['git', '-C', repo_path, 'add', file_path])

def git_commit(repo_path, title, message):
    full_commit_message = f"{title}\n\n{message}"
    subprocess.run(['git', '-C', repo_path, 'commit', '-m', full_commit_message])

def git_push(repo_path, branch):
    subprocess.run(['git', '-C', repo_path, 'push', 'origin', branch])