# Cursor Device ID Manager

Cursor Device ID Manager is a powerful cross-platform toolkit specifically designed to address device identification issues in Cursor Editor. It provides a streamlined solution for quickly resetting or modifying editor device identifiers when encountering ID lock issues, ensuring your editor maintains smooth operation at all times.

[English](README.md) | [中文说明](README_CN.md)

## Features

- 🔄 Reset device and machine IDs when encountering lock issues
- 💾 Automatic backup before any modifications
- 🔙 Restore from previous backups if needed
- 🌍 Cross-platform support (Windows, macOS, Linux)
- 🛠️ Custom machine ID support
- 🔒 Safe operations with automatic backup
- 📝 Clear logging and error reporting

## Requirements

- Python 3.6 or higher
- No additional dependencies required

## Quick Start

### Windows Users
1. Install Python from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation
2. Download and extract this tool
3. Double-click `run_windows.bat`

### macOS/Linux Users
1. Open Terminal
2. Clone the repository:
   ```bash
   git clone https://github.com/alexlifexyz/cursor_machine_id_manager.git
   cd cursor_machine_id_manager
   ```
3. Make the script executable:
   ```bash
   chmod +x cursor_id_manager.py
   ```
4. Run the script:
   ```bash
   ./cursor_id_manager.py
   ```

## Advanced Usage

### Command Line Options

1. Generate new IDs (default behavior):
```bash
python cursor_id_manager.py
```

2. Use custom machine ID:
```bash
python cursor_id_manager.py --machine-id YOUR_CUSTOM_ID
```

3. Restore from backup:
```bash
python cursor_id_manager.py --restore path/to/backup/file
```

## Storage File Locations

- Windows: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Linux: `~/.config/Cursor/User/globalStorage/storage.json`

## Important Notes

1. Before running:
   - Close Cursor Editor completely
   - Ensure you have proper file system permissions
   - Backup important data (though the tool creates automatic backups)

2. Automatic Backups:
   - Created before any modifications
   - Stored in the same directory as the original file
   - Format: `storage.json.backup_YYYYMMDD_HHMMSS`

3. Troubleshooting:
   - Verify Python installation
   - Check file permissions
   - Review error messages for detailed information

## Security

- All generated IDs use cryptographically secure random number generation
- Automatic backups protect against data loss
- No external dependencies required
- No data is sent to any external servers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
