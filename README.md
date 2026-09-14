# CSK4 Banner Generator v1.1

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen?style=flat-square&logo=python)
![Linux](https://img.shields.io/badge/Linux-Kali%2FTermux-red?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

> **Professional Terminal Customizer & Banner Generator for Kali Linux, Termux, and general Linux systems** with cyberpunk aesthetics and real-time system monitoring.

**v1.1 Bug-fixed & Improved** – Fixed double color prompt, Rich input styling, fragile injection paths, missing settings persistence, Termux detection, and more.

---

## 🎯 Features

- ✅ **Custom ASCII Banner Generator** – Personalized ASCII art with 3 font styles (Slant, Shadow, Standard)
- ✅ **Real-time System Dashboard** – OS, Kernel, CPU, RAM, Local/Public IP, Python version, Timestamp
- ✅ **Permanent Terminal Integration** – Auto-inject into `~/.bashrc` or `~/.zshrc`
- ✅ **Settings Persistence** – Your custom username/role/bio/font/color are saved and used on every terminal open
- ✅ **Safe Backup & Restore** – Automatic `.csk4.backup` before any change
- ✅ **Color Presets** – Cyber Neon, Matrix Green, Dracula Dark
- ✅ **Termux Detection** – Special handling and tips for Termux
- ✅ **Cross-Platform** – Kali Linux, Termux, Ubuntu, Debian, and other Linux distros
- ✅ **Zero hard crashes** – Better error handling on file ops, network, and fonts

---

## 📦 Installation

### Kali Linux / General Linux

```bash
git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git
cd csk4-banner-gen
pip install -r requirements.txt
python3 main.py
```

### Termux

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git
cd csk4-banner-gen
pip install -r requirements.txt
python3 main.py
```

### One-liner (Kali)

```bash
git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git && cd csk4-banner-gen && pip install -r requirements.txt && python3 main.py
```

### One-liner (Termux)

```bash
pkg install python git && git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git && cd csk4-banner-gen && pip install -r requirements.txt && python3 main.py
```

---

## 🚀 Usage

### Interactive Menu
```bash
python3 main.py
```

```
═══════════════════════════
Main Menu:
1️⃣  Generate & Save Custom Banner
2️⃣  View System Dashboard
3️⃣  Enable Auto-Injection (Bash)
4️⃣  Enable Auto-Injection (Zsh)
5️⃣  Disable Auto-Injection
6️⃣  Show Current Saved Settings
7️⃣  Exit
═══════════════════════════
```

### Quick Banner (for shell startup)
```bash
python3 main.py --banner-only
```
Uses your **saved settings**. If none saved, falls back to hostname + defaults.

### Help
```bash
python3 main.py --help
```

---

## 📋 Menu Options

### 1️⃣ Generate & Save Custom Banner
- Enter username, role, bio
- Choose font (Slant / Shadow / Standard)
- Choose color preset
- **Settings are saved** to `~/.config/csk4-banner/settings.json`
- Banner + Dashboard shown immediately
- Next time you open terminal (after injection) it will use these values

### 2️⃣ View System Dashboard
Shows live system info with selected color theme.

### 3️⃣ / 4️⃣ Enable Auto-Injection
- Creates backup (`~/.bashrc.csk4.backup` or `~/.zshrc.csk4.backup`)
- Appends safe injection block
- Banner runs automatically on every new terminal

### 5️⃣ Disable Auto-Injection
Removes the CSK4 block cleanly. Backup remains available.

### 6️⃣ Show Current Saved Settings
Displays what will be used by `--banner-only`.

---

## 🎨 Color Presets

| Preset         | Primary       | Secondary     | Accent        |
|----------------|---------------|---------------|---------------|
| Cyber Neon     | Bright Cyan   | Bright Magenta| Bright Yellow |
| Matrix Green   | Bright Green  | Green         | Bright White  |
| Dracula Dark   | Purple        | Pink          | Yellow        |

---

## 💾 Backup & Restore

Automatic backup is created on injection:
```
~/.bashrc.csk4.backup
~/.zshrc.csk4.backup
```

Manual restore:
```bash
cp ~/.bashrc.csk4.backup ~/.bashrc
# or
cp ~/.zshrc.csk4.backup ~/.zshrc
```

Settings location:
```
~/.config/csk4-banner/settings.json
```

---

## 📋 Requirements

- Python 3.8+
- OS: Kali Linux, Termux, Ubuntu, Debian, or any Linux
- Internet optional (Public IP gracefully falls back to N/A)

### Dependencies
```
rich
pyfiglet
psutil
requests
```

```bash
pip install -r requirements.txt
```

---

## 🐛 Changelog v1.1 (Fixes)

- Fixed double color-preset prompt in custom banner flow
- Replaced plain `input()` with `CONSOLE.input()` (Rich styling now works)
- Injection now uses quoted absolute path + auto-detects `python3`/`python`
- Custom banner settings are **persisted** and used by `--banner-only`
- Better Termux detection + tips
- Safer file backup/restore with proper error handling
- Network call cached + shorter timeout
- Font fallback if selected font is missing
- Added “Show Current Saved Settings” menu option
- Cleaner remove logic for injection markers

---

## 🛠 Troubleshooting

**ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Public IP shows N/A**  
Offline or firewall – tool continues normally.

**Banner not appearing after injection**
```bash
source ~/.bashrc   # or ~/.zshrc
# or simply close & reopen the terminal / Termux
```

**Permission issues**
```bash
chmod +x main.py
```

**Zsh not found (Termux)**
```bash
pkg install zsh
```

---

## 📄 License

MIT License – see [LICENSE](LICENSE) file.

---

## 👨‍💻 Author

**cryptixshadowkernel-org**

This tool is for educational and personal terminal customization. Use responsibly.

---

**Made with ❤️ – v1.1 Bug-fixed for Termux & Kali**
