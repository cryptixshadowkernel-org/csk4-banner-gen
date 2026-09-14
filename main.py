#!/usr/bin/env python3
"""
CSK4 Banner Generator - Professional Terminal Customizer for Kali Linux, Termux & Linux
Author: cryptixshadowkernel-org
License: MIT
Version: 1.1.0 (Bug-fixed & Improved)
"""

import os
import sys
import json
import platform
import socket
import shutil
from pathlib import Path
from datetime import datetime

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    import pyfiglet
    import psutil
    import requests
except ImportError:
    print("❌ Missing dependencies! Run: pip install -r requirements.txt")
    sys.exit(1)

# ============================================================================
# CONFIGURATION & COLOR PRESETS
# ============================================================================

CONSOLE = Console()

COLOR_PRESETS = {
    "cyber_neon": {
        "name": "Cyber Neon",
        "primary": "bright_cyan",
        "secondary": "bright_magenta",
        "accent": "bright_yellow",
        "border": "bright_white",
    },
    "matrix_green": {
        "name": "Matrix Green",
        "primary": "bright_green",
        "secondary": "green",
        "accent": "bright_white",
        "border": "green",
    },
    "dracula_dark": {
        "name": "Dracula Dark",
        "primary": "color(141)",
        "secondary": "color(212)",
        "accent": "color(228)",
        "border": "color(61)",
    },
}

# Config file to persist user banner settings
CONFIG_DIR = Path.home() / ".config" / "csk4-banner"
CONFIG_FILE = CONFIG_DIR / "settings.json"

DEFAULT_SETTINGS = {
    "username": None,          # None = use hostname
    "role": "Cyber Warrior",
    "bio": "Securing the Digital World",
    "font_style": "slant",
    "color_preset": "cyber_neon",
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def is_termux() -> bool:
    """Detect Termux environment"""
    return "com.termux" in os.environ.get("PREFIX", "") or "TERMUX_VERSION" in os.environ


def get_python_cmd() -> str:
    """Return best available python command"""
    for cmd in ("python3", "python"):
        if shutil.which(cmd):
            return cmd
    return "python3"


def load_settings() -> dict:
    """Load saved banner settings or return defaults"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            # merge with defaults so new keys appear
            merged = DEFAULT_SETTINGS.copy()
            merged.update(data)
            return merged
        except Exception:
            pass
    return DEFAULT_SETTINGS.copy()


def save_settings(settings: dict) -> bool:
    """Save banner settings to config file"""
    try:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        CONSOLE.print(f"[red]❌ Failed to save settings: {e}[/red]")
        return False


def get_public_ip() -> str:
    """Fetch public IP address with fallback (cached for session)"""
    if hasattr(get_public_ip, "_cache"):
        return get_public_ip._cache
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=2)
        ip = response.json().get("ip", "N/A")
    except Exception:
        ip = "N/A"
    get_public_ip._cache = ip
    return ip


def get_local_ip() -> str:
    """Get local IP address safely"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1.0)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def get_system_info() -> dict:
    """Gather real-time system information"""
    try:
        cpu = psutil.cpu_percent(interval=0.5)
    except Exception:
        cpu = 0.0
    try:
        mem = psutil.virtual_memory()
        ram_percent = mem.percent
        ram_used = mem.used / (1024 ** 3)
        ram_total = mem.total / (1024 ** 3)
    except Exception:
        ram_percent = ram_used = ram_total = 0.0

    return {
        "os": platform.system(),
        "kernel": platform.release(),
        "hostname": socket.gethostname(),
        "cpu_percent": cpu,
        "ram_percent": ram_percent,
        "ram_used": ram_used,
        "ram_total": ram_total,
        "local_ip": get_local_ip(),
        "public_ip": get_public_ip(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "is_termux": is_termux(),
    }


def backup_shell_config(shell_type: str = "bash") -> bool:
    """Create backup of shell configuration file"""
    home = Path.home()
    config_file = home / f".{shell_type}rc"
    backup_file = home / f".{shell_type}rc.csk4.backup"

    if not config_file.exists():
        # Create empty file so injection can still work
        try:
            config_file.touch()
        except Exception:
            return False

    try:
        shutil.copy2(config_file, backup_file)
        return True
    except Exception as e:
        CONSOLE.print(f"[red]❌ Backup failed: {e}[/red]")
        return False


def get_banner_injection_code() -> str:
    """Generate the command to inject into shell config"""
    script_path = Path(__file__).resolve()
    py = get_python_cmd()
    # Use quotes so spaces in path don't break
    return f'{py} "{script_path}" --banner-only\n'


def is_already_injected(config_file: Path) -> bool:
    """Check if CSK4 banner is already injected"""
    if not config_file.exists():
        return False
    try:
        content = config_file.read_text(encoding="utf-8", errors="ignore")
        return "===== CSK4 BANNER GENERATOR" in content
    except Exception:
        return False


def inject_into_shell_config(shell_type: str = "bash") -> None:
    """Permanently inject banner script into shell configuration"""
    home = Path.home()
    config_file = home / f".{shell_type}rc"
    injection_code = get_banner_injection_code()

    if is_already_injected(config_file):
        CONSOLE.print(
            f"[yellow]⚠️  Banner already injected into {config_file}[/yellow]"
        )
        return

    # Create backup first
    if not backup_shell_config(shell_type):
        CONSOLE.print("[red]❌ Could not create backup. Aborting injection.[/red]")
        return

    try:
        with open(config_file, "a", encoding="utf-8") as f:
            f.write("\n# ===== CSK4 BANNER GENERATOR - DO NOT EDIT =====\n")
            f.write(injection_code)
            f.write("# ===== END CSK4 BANNER GENERATOR =====\n")

        CONSOLE.print(
            f"[bright_green]✅ Banner injected into {config_file}[/bright_green]"
        )
        CONSOLE.print(
            f"[cyan]Backup saved to {config_file}.csk4.backup[/cyan]"
        )
        CONSOLE.print(
            "[yellow]💡 The banner will now run automatically on terminal startup![/yellow]"
        )
        if is_termux():
            CONSOLE.print(
                "[cyan]Termux tip: Close & reopen Termux or run 'source ~/.bashrc'[/cyan]"
            )
    except Exception as e:
        CONSOLE.print(f"[red]❌ Injection failed: {e}[/red]")


def remove_from_shell_config(shell_type: str = "bash") -> None:
    """Remove banner injection from shell configuration"""
    home = Path.home()
    config_file = home / f".{shell_type}rc"
    backup_file = home / f".{shell_type}rc.csk4.backup"

    if not config_file.exists():
        CONSOLE.print(f"[red]❌ {config_file} not found[/red]")
        return

    try:
        lines = config_file.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)

        filtered_lines = []
        skip = False
        for line in lines:
            if "===== CSK4 BANNER GENERATOR" in line:
                skip = True
                continue
            if "===== END CSK4 BANNER GENERATOR" in line:
                skip = False
                continue
            if not skip:
                filtered_lines.append(line)

        config_file.write_text("".join(filtered_lines), encoding="utf-8")
        CONSOLE.print(
            f"[bright_green]✅ Banner removed from {config_file}[/bright_green]"
        )

        if backup_file.exists():
            CONSOLE.print(
                f"[cyan]💾 Backup available at {backup_file}[/cyan]\n"
                f"[cyan]Run 'cp {backup_file} {config_file}' to fully restore[/cyan]"
            )
    except Exception as e:
        CONSOLE.print(f"[red]❌ Remove failed: {e}[/red]")


def display_ascii_banner(username: str, role: str, bio: str, font_style: str, color_preset: str) -> None:
    """Display ASCII art banner with custom text"""
    colors = COLOR_PRESETS.get(color_preset, COLOR_PRESETS["cyber_neon"])

    try:
        ascii_art = pyfiglet.figlet_format(username, font=font_style, justify="center")
    except Exception:
        # Fallback if font missing
        ascii_art = pyfiglet.figlet_format(username, font="standard", justify="center")

    banner_text = Text(ascii_art, style=f"bold {colors['primary']}")
    role_text = Text(f"╔═══ {role} ═══╗", style=f"bold {colors['secondary']}")
    bio_text = Text(f"└─> {bio}", style=colors["accent"])

    CONSOLE.print("\n")
    CONSOLE.print(banner_text)
    CONSOLE.print(role_text, justify="center")
    CONSOLE.print(bio_text, justify="center")
    CONSOLE.print("\n")


def display_system_dashboard(color_preset: str) -> None:
    """Display cyberpunk-styled system dashboard"""
    colors = COLOR_PRESETS.get(color_preset, COLOR_PRESETS["cyber_neon"])
    info = get_system_info()

    table = Table(
        title="[bold]⚙️  SYSTEM DASHBOARD[/bold]",
        border_style=colors["border"],
        show_header=True,
        header_style=f"bold {colors['primary']}",
    )

    table.add_column("Parameter", style=colors["secondary"])
    table.add_column("Value", style=colors["accent"])

    os_label = f"{info['os']} ({info['architecture']})"
    if info["is_termux"]:
        os_label += " [Termux]"

    table.add_row("🖥️  Operating System", os_label)
    table.add_row("🔧 Kernel Version", info["kernel"])
    table.add_row("📟 Hostname", info["hostname"])
    table.add_row(
        "⚡ CPU Usage",
        f"[bold {colors['accent']}]{info['cpu_percent']:.1f}%[/bold]",
    )
    table.add_row(
        "💾 RAM Usage",
        f"[bold {colors['accent']}]{info['ram_used']:.2f}GB / {info['ram_total']:.2f}GB ({info['ram_percent']:.1f}%)[/bold]",
    )
    table.add_row("🌐 Local IP", info["local_ip"])
    table.add_row("🔗 Public IP", info["public_ip"])
    table.add_row("🐍 Python Version", info["python_version"])
    table.add_row("⏰ Timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    CONSOLE.print("\n")
    CONSOLE.print(table)
    CONSOLE.print("\n")


# ============================================================================
# MENU & INTERACTIVE
# ============================================================================


def interactive_menu() -> None:
    """Interactive setup menu"""
    CONSOLE.print(
        Panel(
            "[bold bright_cyan]CSK4 BANNER GENERATOR[/bold bright_cyan]\n"
            "[bright_magenta]Professional Terminal Customizer v1.1[/bright_magenta]\n"
            f"[dim]{'Termux' if is_termux() else platform.system()} detected[/dim]",
            border_style="bright_white",
        )
    )

    while True:
        CONSOLE.print("\n[bold bright_yellow]═══════════════════════════[/bold bright_yellow]")
        CONSOLE.print("[bold]Main Menu:[/bold]")
        CONSOLE.print("1️⃣  Generate & Save Custom Banner")
        CONSOLE.print("2️⃣  View System Dashboard")
        CONSOLE.print("3️⃣  Enable Auto-Injection (Bash)")
        CONSOLE.print("4️⃣  Enable Auto-Injection (Zsh)")
        CONSOLE.print("5️⃣  Disable Auto-Injection")
        CONSOLE.print("6️⃣  Show Current Saved Settings")
        CONSOLE.print("7️⃣  Exit")
        CONSOLE.print("[bold bright_yellow]═══════════════════════════[/bold bright_yellow]\n")

        choice = CONSOLE.input("[bright_cyan]Select option (1-7): [/bright_cyan]").strip()

        if choice == "1":
            generate_custom_banner()
        elif choice == "2":
            select_color_preset()
        elif choice == "3":
            inject_into_shell_config("bash")
        elif choice == "4":
            inject_into_shell_config("zsh")
        elif choice == "5":
            remove_choice = CONSOLE.input(
                "[yellow]Remove from which shell? (bash/zsh/both): [/yellow]"
            ).strip().lower()
            if remove_choice in ("bash", "zsh"):
                remove_from_shell_config(remove_choice)
            elif remove_choice == "both":
                remove_from_shell_config("bash")
                remove_from_shell_config("zsh")
            else:
                CONSOLE.print("[red]❌ Invalid choice. Use bash / zsh / both[/red]")
        elif choice == "6":
            show_saved_settings()
        elif choice == "7":
            CONSOLE.print("[bright_green]👋 Goodbye![/bright_green]")
            break
        else:
            CONSOLE.print("[red]❌ Invalid option![/red]")


def generate_custom_banner() -> None:
    """Interactive custom banner generator + save settings"""
    CONSOLE.print("\n[bold bright_cyan]╔═══ CUSTOM BANNER GENERATOR ═══╗[/bold bright_cyan]")

    current = load_settings()

    username = CONSOLE.input(
        f"[bright_magenta]Enter your username/name [{current.get('username') or socket.gethostname()}]: [/bright_magenta]"
    ).strip()
    if not username:
        username = current.get("username") or socket.gethostname()

    role = CONSOLE.input(
        f"[bright_magenta]Enter your role/title [{current.get('role', 'Cyber Ninja')}]: [/bright_magenta]"
    ).strip() or current.get("role", "Cyber Ninja")

    bio = CONSOLE.input(
        f"[bright_magenta]Enter your bio/motto [{current.get('bio', 'Securing the Digital World')}]: [/bright_magenta]"
    ).strip() or current.get("bio", "Securing the Digital World")

    CONSOLE.print("\n[bold]Select ASCII Font Style:[/bold]")
    CONSOLE.print("1️⃣  Slant (Modern)")
    CONSOLE.print("2️⃣  Shadow (Bold)")
    CONSOLE.print("3️⃣  Standard (Classic)")
    font_choice = CONSOLE.input("[cyan]Select (1-3): [/cyan]").strip()
    fonts = {"1": "slant", "2": "shadow", "3": "standard"}
    font_style = fonts.get(font_choice, current.get("font_style", "slant"))

    color_preset = select_color_preset(return_choice=True)

    # Save for future --banner-only runs
    settings = {
        "username": username,
        "role": role,
        "bio": bio,
        "font_style": font_style,
        "color_preset": color_preset,
    }
    if save_settings(settings):
        CONSOLE.print("[bright_green]✅ Settings saved! Auto-banner will use these values.[/bright_green]")

    display_ascii_banner(username, role, bio, font_style, color_preset)
    display_system_dashboard(color_preset)


def select_color_preset(return_choice: bool = False):
    """Color preset selector"""
    CONSOLE.print("\n[bold]Select Color Preset:[/bold]")
    CONSOLE.print("1️⃣  Cyber Neon (Cyan & Magenta)")
    CONSOLE.print("2️⃣  Matrix Green (Hacker Aesthetic)")
    CONSOLE.print("3️⃣  Dracula Dark (Purple & Pink)")

    choice = CONSOLE.input("[cyan]Select (1-3): [/cyan]").strip()
    presets = {"1": "cyber_neon", "2": "matrix_green", "3": "dracula_dark"}
    preset = presets.get(choice, "cyber_neon")

    if return_choice:
        return preset

    display_system_dashboard(preset)


def show_saved_settings() -> None:
    """Show currently saved banner settings"""
    s = load_settings()
    table = Table(title="Saved Banner Settings", border_style="bright_cyan")
    table.add_column("Key", style="bright_magenta")
    table.add_column("Value", style="bright_yellow")
    table.add_row("Username", s.get("username") or "(hostname)")
    table.add_row("Role", s.get("role", ""))
    table.add_row("Bio", s.get("bio", ""))
    table.add_row("Font", s.get("font_style", ""))
    table.add_row("Color Preset", s.get("color_preset", ""))
    table.add_row("Config File", str(CONFIG_FILE))
    CONSOLE.print(table)


def banner_only_mode() -> None:
    """Quick banner display mode (for .bashrc/.zshrc injection)"""
    settings = load_settings()
    username = settings.get("username") or socket.gethostname()
    role = settings.get("role", "Cyber Warrior")
    bio = settings.get("bio", "Securing the Digital World")
    font_style = settings.get("font_style", "slant")
    color_preset = settings.get("color_preset", "cyber_neon")

    display_ascii_banner(username, role, bio, font_style, color_preset)
    display_system_dashboard(color_preset)


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================


def main() -> None:
    """Main application entry point"""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--banner-only":
            banner_only_mode()
        elif arg in ("--help", "-h"):
            CONSOLE.print(
                Panel(
                    "[bold]CSK4 BANNER GENERATOR v1.1 - Help[/bold]\n\n"
                    "[cyan]Usage:[/cyan]\n"
                    "  main.py                 - Interactive menu\n"
                    "  main.py --banner-only   - Quick banner (for .bashrc/.zshrc)\n"
                    "  main.py --help          - Show this help\n\n"
                    "[yellow]Features:[/yellow]\n"
                    "  ✓ Custom ASCII banners with multiple fonts\n"
                    "  ✓ Real-time system dashboard\n"
                    "  ✓ Color presets (Cyber Neon, Matrix Green, Dracula Dark)\n"
                    "  ✓ Auto-inject into terminal startup\n"
                    "  ✓ Settings saved → auto-banner uses your custom values\n"
                    "  ✓ Safe backup & restore + Termux detection\n"
                    "  ✓ Fixed: double prompt, input styling, path issues",
                    border_style="bright_cyan",
                )
            )
        else:
            CONSOLE.print(f"[red]Unknown argument: {arg}[/red]")
            CONSOLE.print("Run with --help for usage information")
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
