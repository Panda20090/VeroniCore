# data_sync.py
# This script handles the synchronization of data across different devices and directories.
# It uses file comparison to ensure that the latest versions of files are present in all locations.

import os
import shutil
from filecmp import dircmp

class DataSyncManager:
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir

    def sync_directories(self):
        print(f"Synchronizing {self.source_dir} with {self.target_dir}...")
        self._sync(self.source_dir, self.target_dir)
        print("Synchronization complete.")

    def _sync(self, source, target):
        # Compare the source and target directories
        comparison = dircmp(source, target)
        
        # Copy files from source to target
        self._copy_new_files(comparison)
        
        # Recursively sync subdirectories
        for subdir in comparison.common_dirs:
            self._sync(os.path.join(source, subdir), os.path.join(target, subdir))
        
        # Handle any files that are only in the target (e.g., deletion or archiving)
        self._handle_extra_files(comparison)

    def _copy_new_files(self, comparison):
        # Copy files that are only in the source directory
        for file in comparison.left_only:
            src_path = os.path.join(self.source_dir, file)
            tgt_path = os.path.join(self.target_dir, file)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, tgt_path)
                print(f"Directory copied: {src_path} to {tgt_path}")
            else:
                shutil.copy2(src_path, tgt_path)
                print(f"File copied: {src_path} to {tgt_path}")

        # Replace files that differ between source and target
        for file in comparison.diff_files:
            src_path = os.path.join(self.source_dir, file)
            tgt_path = os.path.join(self.target_dir, file)
            shutil.copy2(src_path, tgt_path)
            print(f"File updated: {src_path} to {tgt_path}")

    def _handle_extra_files(self, comparison):
        # List files that are only in the target directory
        for file in comparison.right_only:
            tgt_path = os.path.join(self.target_dir, file)
            print(f"Extra file in target directory: {tgt_path}")
            # Here you can decide to delete or archive these files
            # Example: shutil.move(tgt_path, archive_dir)

if __name__ == "__main__":
    # Example usage of the DataSyncManager
    data_sync_manager = DataSyncManager(
        source_dir="path_to_source_directory",
        target_dir="path_to_target_directory"
    )

    # Perform the synchronization
    data_sync_manager.sync_directories()
