# Cursor 设备 ID 管理器

Cursor 设备 ID 管理器是一个功能强大且跨平台的工具集，专门用于解决 Cursor 编辑器中的设备标识问题。它提供了一个简洁的解决方案，帮助您在设备 ID 锁定问题出现时，快速重置或修改编辑器的设备标识，确保您的编辑器始终保持流畅的运行状态。

[English](README.md) | [中文说明](README_CN.md)

## 功能特性

- 🔄 解决设备 ID 锁定问题
- 💾 修改前自动备份配置
- 🔙 支持随时还原备份
- 🌍 跨平台支持（Windows、macOS、Linux）
- 🛠️ 支持自定义机器 ID
- 🔒 安全可靠的操作机制
- 📝 清晰的日志和错误提示

## 系统要求

- Python 3.6 或更高版本
- 无需其他依赖项

## 快速开始

### Windows 用户
1. 从 [Python官网](https://www.python.org/downloads/) 下载并安装 Python
   - 安装时请勾选"Add Python to PATH"选项
2. 下载并解压本工具
3. 双击运行 `run_windows.bat`

### macOS/Linux 用户
1. 打开终端
2. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/cursor-id-manager.git
   cd cursor-id-manager
   ```
3. 添加执行权限：
   ```bash
   chmod +x cursor_id_manager.py
   ```
4. 运行脚本：
   ```bash
   ./cursor_id_manager.py
   ```

## 进阶使用

### 命令行选项

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

## 配置文件位置

- Windows: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Linux: `~/.config/Cursor/User/globalStorage/storage.json`

## 重要说明

1. 运行前请确保：
   - 已完全关闭 Cursor 编辑器
   - 具有足够的文件系统权限
   - 已备份重要数据（虽然工具��自动创建备份）

2. 自动备份机制：
   - 在进行任何修改前自动创建
   - 备份文件保存在原配置文件同目录下
   - 文件名格式：`storage.json.backup_YYYYMMDD_HHMMSS`

3. 故障排除：
   - 验证 Python 是否正确安装
   - 检查文件访问权限
   - 查看错误信息获取详细提示

## 安全性

- 所有生成的 ID 使用加密安全的随机数生成
- 自动备份保护防止数据丢失
- 无需外部依赖
- 不会向任何外部服务器发送数据

## 参与贡献

欢迎提交 Pull Request 来改进这个项目！

## 许可证

MIT 许可证

Copyright (c) 2024 [作者名称]

特此免费授予任何获得本软件和相关文档文件（"软件"）副本的人不受限制地处理本软件的权利，
包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，
并允许向其提供本软件的人这样做，但须符合以下条件：

上述版权声明和本许可声明应包含在本软件的所有副本或重要部分中。

本软件按"原样"提供，不提供任何形式的明示或暗示的保证，包括但不限于对适销性、
特定用途的适用性和非侵权性的保证。在任何情况下，作者或版权持有人均不对任何索赔、
损害或其他责任负责，无���是在合同诉讼、侵权行为或其他方面，由软件或软件的使用或
其他交易产生、引起或与之相关。 