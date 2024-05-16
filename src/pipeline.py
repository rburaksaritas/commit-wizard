def generate_commits(repo_path, api_key):
    modified_files = get_modified_files(repo_path)

    for file_path in modified_files:
        old_content = get_file_content(repo_path, file_path, commit='HEAD^')
        new_content = get_file_content(repo_path, file_path, commit='HEAD')
        diff_content = get_file_diff(repo_path, file_path)
        
        commit_message_response = generate_commit_message(api_key, diff_content)
        title, message = parse_commit_message(commit_message_response)
        print("Commit Generated", "\n\n", title, "\n\n", message)
        git_add(repo_path, file_path)
        git_commit(repo_path, title, message)