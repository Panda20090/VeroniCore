import os


def create_directories_and_files(structure, root="VeroniCore"):
    for directory, files in structure.items():
        # Create the directory if it doesn't exist
        dir_path = os.path.join(root, directory)
        os.makedirs(dir_path, exist_ok=True)

        for file in files:
            # Create the file within the directory
            file_path = os.path.join(dir_path, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    pass  # Create an empty file
            # Open the file in Notepad
            os.system(f'notepad {file_path}')


if __name__ == "__main__":
    # File structure for VeroniCore
    file_structure = {
        "src/ai/personalization": ["ai_engine.py", "learning_module.py", "recommendation_system.py"],
        "src/data_management": ["repository_manager.py", "data_sync.py", "metadata_handler.py"],
        "src/github_integration": ["repo_manager.py", "ci_cd_pipeline.py", "actions_handler.py"],
        "src/unity_integration": ["visualization_manager.py", "ui_components.py", "simulation_engine.py"],
        "src/api/endpoints": ["user_api.py", "data_api.py", "auth_api.py"],
        "src/api/middlewares": ["authentication.py", "logging.py", "error_handler.py"],
        "docs": ["user_guide.md", "developer_guide.md", "api_reference.md", "integration_guide.md"],
        "tests/unit_tests": ["test_core.py", "test_ai.py", "test_data_management.py"],
        "tests/integration_tests": ["test_github_integration.py", "test_unity_integration.py"],
        "tests/performance_tests": ["test_scalability.py", "test_load_handling.py"],
        "config": ["settings.ini", "logging.conf", "database.yml"],
        "scripts": ["deploy.sh", "backup.sh", "automate_ci_cd.sh"],
        "data/raw": [],
        "data/processed": [],
        "data/models": [],
        "data/backups": [],
        "integrations/microsoft_office": ["excel_integration.py", "outlook_integration.py", "teams_integration.py"],
        "integrations/azure": ["storage_integration.py", "compute_integration.py", "ai_integration.py"],
        "integrations/third_party": ["slack_integration.py", "salesforce_integration.py", "google_workspace_integration.py"],
        "assets/images": [],
        "assets/styles": [],
        "assets/icons": []
    }

    # Create directories and files
    create_directories_and_files(file_structure)
