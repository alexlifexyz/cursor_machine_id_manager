#!/usr/bin/env python3
import json
import os
import sys
import uuid
import shutil
import platform
from datetime import datetime
from pathlib import Path
import secrets
import argparse

class CursorIDManager:
    def __init__(self):
        self.os_type = platform.system().lower()
        self.storage_file = self._get_storage_path()
        
    def _get_storage_path(self) -> Path:
        """Get the storage.json path based on the operating system."""
        if self.os_type == "darwin":  # macOS
            return Path.home() / "Library/Application Support/Cursor/User/globalStorage/storage.json"
        elif self.os_type == "windows":
            return Path(os.getenv("APPDATA")) / "Cursor/User/globalStorage/storage.json"
        elif self.os_type == "linux":
            return Path.home() / ".config/Cursor/User/globalStorage/storage.json"
        else:
            raise OSError(f"Unsupported operating system: {self.os_type}")

    @staticmethod
    def generate_machine_id() -> str:
        """Generate a random 32-byte hex string."""
        return secrets.token_hex(32)

    @staticmethod
    def generate_device_id() -> str:
        """Generate a random UUID."""
        return str(uuid.uuid4())

    def create_backup(self) -> Path:
        """Create a backup of the storage file."""
        if not self.storage_file.exists():
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.storage_file.with_name(f"storage.json.backup_{timestamp}")
        shutil.copy2(self.storage_file, backup_path)
        return backup_path

    def update_ids(self, machine_id=None, restore_backup=None):
        """Update the telemetry IDs in the storage file."""
        if restore_backup:
            if not Path(restore_backup).exists():
                raise FileNotFoundError(f"Backup file not found: {restore_backup}")
            shutil.copy2(restore_backup, self.storage_file)
            print(f"Successfully restored from backup: {restore_backup}")
            return

        # Create directory if it doesn't exist
        self.storage_file.parent.mkdir(parents=True, exist_ok=True)

        # Generate new IDs
        new_ids = {
            "telemetry.machineId": machine_id or self.generate_machine_id(),
            "telemetry.macMachineId": self.generate_machine_id(),
            "telemetry.devDeviceId": self.generate_device_id()
        }

        # Create backup
        backup_path = self.create_backup()
        if backup_path:
            print(f"Backup created at: {backup_path}")

        # Read existing config or create new one
        if self.storage_file.exists():
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = {}

        # Update IDs
        config.update(new_ids)

        # Save updated config
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

        print("\nSuccessfully updated IDs:")
        for key, value in new_ids.items():
            print(f"{key}: {value}")

def main():
    parser = argparse.ArgumentParser(description="Cursor Editor Telemetry ID Manager")
    parser.add_argument("--machine-id", help="Specify custom machine ID")
    parser.add_argument("--restore", help="Restore from backup file")
    args = parser.parse_args()

    try:
        manager = CursorIDManager()
        manager.update_ids(machine_id=args.machine_id, restore_backup=args.restore)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 