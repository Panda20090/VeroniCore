# metadata_handler.py
# This script handles metadata for files within the VeroniCore project.
# It provides functionality to read, write, and update metadata associated with files, such as tags, descriptions, and timestamps.

import os
import json
from datetime import datetime

class MetadataHandler:
    def __init__(self, metadata_file="metadata.json"):
        self.metadata_file = metadata_file
        self.metadata = self._load_metadata()

    def _load_metadata(self):
        if os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'r') as file:
                return json.load(file)
        else:
            return {}

    def _save_metadata(self):
        with open(self.metadata_file, 'w') as file:
            json.dump(self.metadata, file, indent=4)

    def add_metadata(self, file_path, tags=None, description=None):
        file_key = os.path.abspath(file_path)
        self.metadata[file_key] = {
            "tags": tags if tags else [],
            "description": description if description else "",
            "last_modified": self._get_file_modification_time(file_path)
        }
        self._save_metadata()
        print(f"Metadata added for {file_path}")

    def update_metadata(self, file_path, tags=None, description=None):
        file_key = os.path.abspath(file_path)
        if file_key in self.metadata:
            if tags is not None:
                self.metadata[file_key]["tags"] = tags
            if description is not None:
                self.metadata[file_key]["description"] = description
            self.metadata[file_key]["last_modified"] = self._get_file_modification_time(file_path)
            self._save_metadata()
            print(f"Metadata updated for {file_path}")
        else:
            print(f"No metadata found for {file_path}. Use add_metadata to add new metadata.")

    def get_metadata(self, file_path):
        file_key = os.path.abspath(file_path)
        return self.metadata.get(file_key, None)

    def _get_file_modification_time(self, file_path):
        return datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()

if __name__ == "__main__":
    # Example usage of the MetadataHandler
    metadata_handler = MetadataHandler()

    # Example file path (replace with actual file path)
    file_path = "example_file.txt"

    # Adding metadata
    metadata_handler.add_metadata(file_path, tags=["example", "test"], description="This is a test file.")

    # Updating metadata
    metadata_handler.update_metadata(file_path, tags=["updated", "example"], description="Updated description.")

    # Retrieving metadata
    metadata = metadata_handler.get_metadata(file_path)
    print(f"Metadata for {file_path}: {metadata}")
