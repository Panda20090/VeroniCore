# repo_manager.py
# This script manages Git repositories for the VeroniCore project, providing functionality to clone, pull, and push changes to remote repositories.
# It is designed to integrate with GitHub and other Git-based systems, automating version control tasks.

import os
import git  # GitPython library

class RepositoryManager:
    def __init__(self, repo_url, local_dir):
        self.repo_url = repo_url
        self.local_dir = local_dir
        self.repo = None
        self.clone_repository()

    def clone_repository(self):
        if not os.path.exists(self.local_dir):
            try:
                print(f"Cloning repository from {self.repo_url} to {self.local_dir}...")
                self.repo = git.Repo.clone_from(self.repo_url, self.local_dir)
                print("Repository cloned successfully.")
            except Exception as e:
                print(f"Error cloning repository: {e}")
        else:
            print(f"Repository already exists at {self.local_dir}.")
            self.repo = git.Repo(self.local_dir)

    def pull_changes(self):
        if self.repo:
            try:
                print("Pulling latest changes from the remote repository...")
                self.repo.remotes.origin.pull()
                print("Changes pulled successfully.")
            except Exception as e:
                print(f"Error pulling changes: {e}")
        else:
            print("Repository not initialized.")

    def push_changes(self, commit_message):
        if self.repo:
            try:
                print("Adding and committing changes...")
                self.repo.git.add(A=True)
                self.repo.index.commit(commit_message)
                print("Pushing changes to the remote repository...")
                self.repo.remotes.origin.push()
                print("Changes pushed successfully.")
            except Exception as e:
                print(f"Error pushing changes: {e}")
        else:
            print("Repository not initialized.")

if __name__ == "__main__":
    # Example usage of the Repository Manager
    repo_manager = RepositoryManager(
        repo_url="https://github.com/your_username/your_repository.git",
        local_dir="path_to_local_directory"
    )

    # Pull the latest changes
    repo_manager.pull_changes()

    # Push new changes with a commit message
    repo_manager.push_changes("Updated project files")
