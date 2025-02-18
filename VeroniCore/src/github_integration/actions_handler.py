# actions_handler.py
# This script manages custom GitHub Actions for the VeroniCore project.
# It allows you to define, trigger, and manage GitHub Actions directly from within the application.

import requests
import os

class GitHubActionsHandler:
    def __init__(self, repo_owner, repo_name, github_token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = github_token
        self.base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/actions"

    def list_workflows(self):
        url = f"{self.base_url}/workflows"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            workflows = response.json().get("workflows", [])
            print(f"Found {len(workflows)} workflows:")
            for workflow in workflows:
                print(f"- {workflow['name']} (ID: {workflow['id']})")
            return workflows
        else:
            print(f"Failed to retrieve workflows: {response.status_code}")
            return None

    def trigger_workflow(self, workflow_id, ref="main"):
        url = f"{self.base_url}/workflows/{workflow_id}/dispatches"
        headers = self._get_headers()
        payload = {"ref": ref}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 204:
            print(f"Workflow {workflow_id} triggered successfully on ref {ref}.")
        else:
            print(f"Failed to trigger workflow {workflow_id}: {response.status_code} - {response.text}")

    def get_workflow_run_status(self, run_id):
        url = f"{self.base_url}/runs/{run_id}"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            run_status = response.json()
            print(f"Run ID: {run_id}, Status: {run_status['status']}, Conclusion: {run_status['conclusion']}")
            return run_status
        else:
            print(f"Failed to retrieve run status for {run_id}: {response.status_code}")
            return None

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

if __name__ == "__main__":
    # Example usage of the GitHubActionsHandler
    handler = GitHubActionsHandler(
        repo_owner="your_github_username",
        repo_name="your_repository_name",
        github_token="your_github_personal_access_token"
    )

    # List available workflows
    workflows = handler.list_workflows()

    # Trigger a specific workflow by ID (replace with actual workflow ID)
    if workflows:
        workflow_id = workflows[0]['id']  # Example: Triggering the first workflow
        handler.trigger_workflow(workflow_id)

    # Get the status of a specific workflow run (replace with actual run ID)
    run_id = "your_workflow_run_id"
    handler.get_workflow_run_status(run_id)
