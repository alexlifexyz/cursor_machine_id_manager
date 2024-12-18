# Cursor Machine ID Manager

[English](#english) | [中文说明](#简体中文)

<a id="english"></a>
## English

A powerful cross-platform toolkit specifically designed to address device identification issues in Cursor Editor. It provides a streamlined solution for quickly resetting or modifying editor device identifiers when encountering ID lock issues, ensuring your editor maintains smooth operation at all times.

This tool helps resolve the device limitation issue when Cursor Editor shows the following message:
> "Too many free trial accounts used on this machine."

### Features

- 🔄 Reset device and machine IDs when encountering lock issues
- 💾 Automatic backup before any modifications
- 🔙 Restore from previous backups if needed
- 🌍 Cross-platform support (Windows, macOS, Linux)
- 🛠️ Custom machine ID support
- 🔒 Safe operations with automatic backup
- 📝 Clear logging and error reporting

### Requirements

- Python 3.6 or higher
- No additional dependencies required

### Quick Start

#### Windows Users
1. Install Python from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation
2. Download and extract this tool
3. Double-click `run_windows.bat`

#### macOS/Linux Users
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

### Advanced Usage

#### Command Line Options

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

### Storage File Locations

- Windows: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Linux: `~/.config/Cursor/User/globalStorage/storage.json`

### Important Notes

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

### Security

- All generated IDs use cryptographically secure random number generation
- Automatic backups protect against data loss
- No external dependencies required
- No data is sent to any external servers

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alexlifexyz/cursor_machine_id_manager&type=Date)](https://star-history.com/#alexlifexyz/cursor_machine_id_manager&Date)

---

<a id="简体中文"></a>
## 简体中文

这是一个功能强大且跨平台的工具集，专门用于解决 Cursor 编辑器中的设备标识问题。它提供了一个简洁的解决方案，帮助您在设备 ID 锁定问题出现时，快速重置或修改编辑器的设备标识，确保您的编辑器始终保持流畅的运行状态。

本工具可以解决 Cursor 编辑器显示以下提示时的设备限制问题：
> "Too many free trial accounts used on this machine."

### 功能特性

- 🔄 解决设备 ID 锁定问题
- 💾 修改前自动备份配置
- 🔙 支持随时还原备份
- 🌍 跨平台支持（Windows、macOS、Linux）
- 🛠️ 支持自定义机器 ID
- 🔒 安全可靠的操作机制
- 📝 清晰的日志和错误提示

### 系统要求

- Python 3.6 或更高版本
- 无需其他依赖项

### 快速开始

#### Windows 用户
1. 从 [Python官网](https://www.python.org/downloads/) 下载并安装 Python
   - 安装时请勾选"Add Python to PATH"选项
2. 下载并解压本工具
3. 双击运行 `run_windows.bat`

#### macOS/Linux 用户
1. 打开终端
2. 克隆仓库：
   ```bash
   git clone https://github.com/alexlifexyz/cursor_machine_id_manager.git
   cd cursor_machine_id_manager
   ```
3. 添加执行权限：
   ```bash
   chmod +x cursor_id_manager.py
   ```
4. 运行脚本：
   ```bash
   ./cursor_id_manager.py
   ```

### 进阶使用

#### 命令行选项

1. 生成新的 ID（默认行为）：
```bash
python cursor_id_manager.py
```

2. 使用自定义机器 ID：
```bash
python cursor_id_manager.py --machine-id 你的自定义ID
```

3. 从备份还原：
```bash
python cursor_id_manager.py --restore 备份文件路径
```

### 配置文件位置

- Windows: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Linux: `~/.config/Cursor/User/globalStorage/storage.json`

### 重要说明

1. 运行前请确保：
   - 已完全关闭 Cursor 编辑器
   - 具有足够的文件系统权限
   - 已备份重要数据（虽然工具自动创建备份）

2. 自动备份机制：
   - 在进行任何修改前自动创建
   - 备份文件保存在原配置文件同目录下
   - 文件名格式：`storage.json.backup_YYYYMMDD_HHMMSS`

3. 故障排除：
   - 验证 Python 是否正确安装
   - 检查文件访问权限
   - 查看错误信息获取详细提示

### 安全性

- 所有生成的 ID 使用加密安全的随机数生成
- 自动备份保护防止数据丢失
- 无需外部依赖
- 不会向任何外部服务器发送数据

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alexlifexyz/cursor_machine_id_manager&type=Date)](https://star-history.com/#alexlifexyz/cursor_machine_id_manager&Date)

---

## License / 许可证

MIT License

Copyright (c) 2024 Alex Li

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
