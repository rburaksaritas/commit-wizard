import argparse
from src.pipeline import generate_commits
from src.git_operations import git_push

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate commit messages for modified files in a git repository.")
    parser.add_argument("repo_path", help="Path to the git repository")
    parser.add_argument("--file", nargs='+', help="Specific files to generate commits for")
    parser.add_argument("--ignore", nargs='+', help="Specific files to ignore")
    parser.add_argument("--push", help="Branch name to push the changes")

    args = parser.parse_args()
    
    generate_commits(args.repo_path, args.file, args.ignore)

    if args.push:
        git_push(args.repo_path, args.push)