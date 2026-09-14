# CSK4 Banner Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen?style=flat-square&logo=python)
![Linux](https://img.shields.io/badge/Linux-Kali%2FTermux-red?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Stars](https://img.shields.io/github/stars/cryptixshadowkernel-org/csk4-banner-gen?style=flat-square)
![Contributors](https://img.shields.io/github/contributors/cryptixshadowkernel-org/csk4-banner-gen?style=flat-square)

> **A professional Terminal Customizer & Banner Generator for Kali Linux, Termux, and general Linux systems with cyberpunk aesthetics and real-time system monitoring.**

---

## 🎯 Features

- ✅ **Custom ASCII Banner Generator** - Create personalized ASCII art banners with 3 font styles (Slant, Shadow, Standard)
- ✅ **Real-time System Dashboard** - Monitor OS, Kernel, CPU, RAM, IP addresses, and more in a cyberpunk-styled table
- ✅ **Permanent Terminal Integration** - Auto-inject banner & dashboard into `~/.bashrc` or `~/.zshrc` for automatic startup
- ✅ **Safe Backup & Restore** - One-click backup and restore functionality for shell configurations
- ✅ **Color Presets** - 3 stunning themes: Cyber Neon, Matrix Green, and Dracula Dark
- ✅ **Cross-Platform** - Works seamlessly on Kali Linux, Termux, Ubuntu, Debian, and all Linux distributions
- ✅ **Zero Dependencies Conflicts** - Lightweight and modular architecture
- ✅ **Interactive Menu System** - User-friendly CLI interface with intuitive navigation

---

## 📦 Installation

### **Quick Install - Kali Linux / Linux**

```bash
git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git
cd csk4-banner-gen
pip install -r requirements.txt
python3 main.py
```

### **Quick Install - Termux**

```bash
pkg update && pkg upgrade
pkg install python3 python3-pip git
git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git
cd csk4-banner-gen
pip install -r requirements.txt
python3 main.py
```

### **One-Liner Installation (Kali Linux)**

```bash
git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git && cd csk4-banner-gen && pip install -r requirements.txt && python3 main.py
```

### **One-Liner Installation (Termux)**

```bash
pkg install python3 python3-pip git && git clone https://github.com/cryptixshadowkernel-org/csk4-banner-gen.git && cd csk4-banner-gen && pip install -r requirements.txt && python3 main.py
```

---

## 🚀 Usage Guide

### **Run Interactive Menu**
```bash
python3 main.py
```

This opens the main menu with the following options:

```
═══════════════════════════
Main Menu:
1️⃣  Generate Custom Banner
2️⃣  View System Dashboard
3️⃣  Enable Auto-Injection (Bash)
4️⃣  Enable Auto-Injection (Zsh)
5️⃣  Disable Auto-Injection
6️⃣  Exit
═══════════════════════════
```

### **Quick Banner Display (for Terminal Startup)**
```bash
python3 main.py --banner-only
```
This displays the banner and system dashboard without the interactive menu (perfect for auto-injection into shell configs).

### **Show Help**
```bash
python3 main.py --help
```

---

## 📋 Menu Options Explained

### **1️⃣ Generate Custom Banner**
- Enter your username/name
- Specify your role/title (e.g., "Penetration Tester", "Security Researcher")
- Add your bio/motto
- Choose ASCII font style: Slant, Shadow, or Standard
- Select a color preset: Cyber Neon, Matrix Green, or Dracula Dark
- Your custom banner is displayed with the system dashboard

**Example Output:**
```
   _____ _____ _____ _____ 
  |     |  |  |  __ \  _  |
  |  |  |  |  |  |__) |_| |
  |__|__|____ |____/| ___ |
             |   | |_| |_|
             
╔═══ Penetration Tester ═══╗
└─> Securing the Digital World
```

### **2️⃣ View System Dashboard**
Displays a real-time cyberpunk-styled system information table:
- Operating System & Architecture
- Kernel Version
- Hostname
- CPU Usage (%)
- RAM Usage (GB & %)
- Local IP Address
- Public IP Address
- Python Version
- Current Timestamp

Choose from 3 color themes to customize the dashboard appearance.

### **3️⃣ Enable Auto-Injection (Bash)**
Automatically adds the banner generator to `~/.bashrc` so it runs every time you open a new terminal session.

**What happens:**
- Creates a backup of `~/.bashrc` as `~/.bashrc.csk4.backup`
- Injects the banner display command
- Banner + Dashboard appear automatically on terminal startup

### **4️⃣ Enable Auto-Injection (Zsh)**
Same as Bash, but for Zsh shell (`~/.zshrc`).

### **5️⃣ Disable Auto-Injection**
- Removes the banner injection from your shell config
- Cleans up the CSK4 marker lines
- Your shell config is restored to normal
- Option to fully restore from backup

### **6️⃣ Exit**
Close the application.

---

## 🎨 Color Presets

### **Cyber Neon** (Default)
- Primary: Bright Cyan
- Secondary: Bright Magenta
- Accent: Bright Yellow
- Perfect for cyberpunk aesthetic enthusiasts

### **Matrix Green**
- Primary: Bright Green
- Secondary: Green
- Accent: Bright White
- Classic hacker aesthetic inspired by The Matrix

### **Dracula Dark**
- Primary: Purple (Color 141)
- Secondary: Pink (Color 212)
- Accent: Yellow (Color 228)
- Modern dark theme with vibrant accents

---

## 🔧 Configuration

All configuration is interactive through the menu. However, you can modify the following in `main.py`:

```python
COLOR_PRESETS = {
    "cyber_neon": {...},
    "matrix_green": {...},
    "dracula_dark": {...},
}
```

Add your own color preset by extending the `COLOR_PRESETS` dictionary with custom color values.

---

## 💾 Backup & Restore

### **Automatic Backups**
When you enable auto-injection, a backup is automatically created:
```
~/.bashrc.csk4.backup          # Bash backup
~/.zshrc.csk4.backup           # Zsh backup
```

### **Manual Restore**
To restore from backup:
```bash
# For Bash
cp ~/.bashrc.csk4.backup ~/.bashrc

# For Zsh
cp ~/.zshrc.csk4.backup ~/.zshrc
```

---

## 📋 Requirements

- **Python:** 3.8 or higher
- **OS:** Kali Linux, Termux, Ubuntu, Debian, or any Linux distribution
- **Internet:** Required for Public IP lookup (gracefully handles offline mode)

### **Dependencies:**
- `rich` - Beautiful terminal output with panels and tables
- `pyfiglet` - ASCII art text generation
- `psutil` - System and process utilities
- `requests` - HTTP library for IP lookup

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🐛 Troubleshooting

### **Issue: "ModuleNotFoundError: No module named 'rich'**
**Solution:** Install requirements
```bash
pip install -r requirements.txt
```

### **Issue: Public IP shows "N/A"**
**Solution:** You're likely offline or blocked by firewall. The tool gracefully handles this.

### **Issue: Banner not appearing on terminal startup**
**Solution:** Check if injection was successful
```bash
cat ~/.bashrc | grep "CSK4 BANNER"
```
If not found, run the tool and select option 3 (Enable Auto-Injection).

### **Issue: Permission denied when running**
**Solution:** Make the script executable
```bash
chmod +x main.py
python3 main.py
```

### **Issue: Zsh not recognized**
**Solution:** Verify Zsh is installed
```bash
which zsh
```
If not installed:
```bash
# Kali Linux / Ubuntu / Debian
sudo apt install zsh

# Termux
pkg install zsh
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🎨 Add new color presets
- 📝 Improve documentation

### **How to Contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**cryptixshadowkernel-org**  
🔗 GitHub: [@cryptixshadowkernel-org](https://github.com/cryptixshadowkernel-org)  
💼 Portfolio & Projects: [GitHub Profile](https://github.com/cryptixshadowkernel-org)

### **Disclaimer**
This tool is designed for **educational and authorized security testing purposes only**. Users are responsible for compliance with local laws and regulations.

---

## ⭐ Show Your Support

If you find this tool useful, please consider:
- ⭐ **Starring** the repository
- 🔄 **Sharing** with your network
- 🐛 **Reporting** issues you encounter
- 💬 **Providing** feedback and suggestions

---

## 📞 Support & Feedback

- 📧 Open an Issue on GitHub
- 🔗 Follow on GitHub for updates
- 💬 Discuss ideas in the Discussions section

---

**Made with ❤️ by [cryptixshadowkernel-org](https://github.com/cryptixshadowkernel-org)**

*Last Updated: 2026*
