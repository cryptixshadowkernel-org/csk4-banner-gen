#!/usr/bin/env python3
"""
CSK4 Banner Generator - Professional Terminal Customizer for Kali Linux, Termux & Linux
Author: cryptixshadowkernel-org
License: MIT
"""

import os
import sys
import platform
import socket
import subprocess
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

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def get_public_ip():
    """Fetch public IP address with fallback"""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=3)
        return response.json().get("ip", "N/A")
    except:
        return "N/A"


def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def get_system_info():
    """Gather real-time system information"""
    return {
        "os": platform.system(),
        "kernel": platform.release(),
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "ram_used": psutil.virtual_memory().used / (1024**3),
        "ram_total": psutil.virtual_memory().total / (1024**3),
        "local_ip": get_local_ip(),
        "public_ip": get_public_ip(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
    }


def backup_shell_config(shell_type="bash"):
    """Create backup of shell configuration file"""
    home = str(Path.home())
    config_file = f"{home}/.{shell_type}rc"
    backup_file = f"{config_file}.csk4.backup"

    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config_content = f.read()
        with open(backup_file, "w") as f:
            f.write(config_content)
        return True
    return False


def get_banner_injection_code():
    """Generate the Python one-liner to inject into shell config"""
    script_path = os.path.abspath(__file__)
    return f"python3 {script_path} --banner-only\n"


def inject_into_shell_config(shell_type="bash"):
    """Permanently inject banner script into shell configuration"""
    home = str(Path.home())
    config_file = f"{home}/.{shell_type}rc"
    injection_code = get_banner_injection_code()

    # Check if already injected
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            if "csk4-banner-gen" in f.read():
                CONSOLE.print(
                    "[yellow]⚠️  Banner already injected into",
                    config_file,
                    "[/yellow]",
                )
                return

    # Create backup
    backup_shell_config(shell_type)

    # Append injection code with marker
    with open(config_file, "a") as f:
        f.write(f"\n# ===== CSK4 BANNER GENERATOR - DO NOT EDIT =====\n")
        f.write(injection_code)
        f.write(f"# ===== END CSK4 BANNER GENERATOR =====\n")

    CONSOLE.print(
        f"[bright_green]✅ Banner injected into {config_file}[/bright_green]"
    )
    CONSOLE.print(f"[cyan]Backup saved to {config_file}.csk4.backup[/cyan]")
    CONSOLE.print(
        f"[yellow]💡 The banner will now run automatically on terminal startup![/yellow]"
    )


def remove_from_shell_config(shell_type="bash"):
    """Remove banner injection from shell configuration"""
    home = str(Path.home())
    config_file = f"{home}/.{shell_type}rc"
    backup_file = f"{config_file}.csk4.backup"

    if not os.path.exists(config_file):
        CONSOLE.print(f"[red]❌ {config_file} not found[/red]")
        return

    # Read current config
    with open(config_file, "r") as f:
        lines = f.readlines()

    # Remove CSK4 section
    filtered_lines = []
    skip = False
    for line in lines:
        if "===== CSK4 BANNER GENERATOR" in line:
            skip = True
        elif "===== END CSK4 BANNER GENERATOR" in line:
            skip = False
            continue
        elif not skip:
            filtered_lines.append(line)

    # Write back
    with open(config_file, "w") as f:
        f.writelines(filtered_lines)

    CONSOLE.print(f"[bright_green]✅ Banner removed from {config_file}[/bright_green]")

    # Offer restore option
    if os.path.exists(backup_file):
        CONSOLE.print(
            f"[cyan]💾 Backup available at {backup_file}[/cyan]\n"
            f"[cyan]Run 'cp {backup_file} {config_file}' to fully restore[/cyan]"
        )


def display_ascii_banner(username, role, bio, font_style, color_preset):
    """Display ASCII art banner with custom text"""
    colors = COLOR_PRESETS.get(color_preset, COLOR_PRESETS["cyber_neon"])

    # Generate ASCII art
    ascii_art = pyfiglet.figlet_format(username, font=font_style, justify="center")

    # Create styled banner
    banner_text = Text(ascii_art, style=f"bold {colors['primary']}")
    role_text = Text(f"╔═══ {role} ═══╗", style=f"bold {colors['secondary']}")
    bio_text = Text(f"└─> {bio}", style=colors['accent'])

    CONSOLE.print("\n")
    CONSOLE.print(banner_text)
    CONSOLE.print(role_text, justify="center")
    CONSOLE.print(bio_text, justify="center")
    CONSOLE.print("\n")


def display_system_dashboard(color_preset):
    """Display cyberpunk-styled system dashboard"""
    colors = COLOR_PRESETS.get(color_preset, COLOR_PRESETS["cyber_neon"])
    info = get_system_info()

    # Create dashboard table
    table = Table(
        title="[bold]⚙️  SYSTEM DASHBOARD[/bold]",
        border_style=colors["border"],
        show_header=True,
        header_style=f"bold {colors['primary']}",
    )

    table.add_column("Parameter", style=colors["secondary"])
    table.add_column("Value", style=colors["accent"])

    # Add rows
    table.add_row("🖥️  Operating System", f"{info['os']} ({info['architecture']})")
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


def interactive_menu():
    """Interactive setup menu"""
    CONSOLE.print(
        Panel(
            "[bold bright_cyan]CSK4 BANNER GENERATOR[/bold bright_cyan]\n"
            "[bright_magenta]Professional Terminal Customizer[/bright_magenta]",
            border_style="bright_white",
        )
    )

    while True:
        CONSOLE.print("\n[bold bright_yellow]═══════════════════════════[/bold bright_yellow]")
        CONSOLE.print("[bold]Main Menu:[/bold]")
        CONSOLE.print("1️⃣  Generate Custom Banner")
        CONSOLE.print("2️⃣  View System Dashboard")
        CONSOLE.print("3️⃣  Enable Auto-Injection (Bash)")
        CONSOLE.print("4️⃣  Enable Auto-Injection (Zsh)")
        CONSOLE.print("5️⃣  Disable Auto-Injection")
        CONSOLE.print("6️⃣  Exit")
        CONSOLE.print("[bold bright_yellow]═══════════════════════════[/bold bright_yellow]\n")

        choice = input("[bright_cyan]Select option (1-6): [/bright_cyan]").strip()

        if choice == "1":
            generate_custom_banner()
        elif choice == "2":
            select_color_preset()
        elif choice == "3":
            inject_into_shell_config("bash")
        elif choice == "4":
            inject_into_shell_config("zsh")
        elif choice == "5":
            remove_choice = input(
                "[yellow]Remove from which shell? (bash/zsh/both): [/yellow]"
            ).strip()
            if remove_choice in ["bash", "zsh"]:
                remove_from_shell_config(remove_choice)
            elif remove_choice == "both":
                remove_from_shell_config("bash")
                remove_from_shell_config("zsh")
        elif choice == "6":
            CONSOLE.print("[bright_green]👋 Goodbye![/bright_green]")
            break
        else:
            CONSOLE.print("[red]❌ Invalid option![/red]")


def generate_custom_banner():
    """Interactive custom banner generator"""
    CONSOLE.print("\n[bold bright_cyan]╔═══ CUSTOM BANNER GENERATOR ═══╗[/bold bright_cyan]")

    username = input("[bright_magenta]Enter your username/name: [/bright_magenta]").strip()
    role = (
        input(
            "[bright_magenta]Enter your role/title (e.g., Penetration Tester): [/bright_magenta]"
        ).strip()
        or "Cyber Ninja"
    )
    bio = (
        input("[bright_magenta]Enter your bio/motto: [/bright_magenta]").strip()
        or "Securing the Digital World"
    )

    CONSOLE.print("\n[bold]Select ASCII Font Style:[/bold]")
    CONSOLE.print("1️⃣  Slant (Modern)")
    CONSOLE.print("2️⃣  Shadow (Bold)")
    CONSOLE.print("3️⃣  Standard (Classic)")
    font_choice = input("[cyan]Select (1-3): [/cyan]").strip()
    fonts = {"1": "slant", "2": "shadow", "3": "standard"}
    font_style = fonts.get(font_choice, "slant")

    select_color_preset()
    color_preset = select_color_preset(return_choice=True)

    display_ascii_banner(username, role, bio, font_style, color_preset)


def select_color_preset(return_choice=False):
    """Color preset selector"""
    CONSOLE.print("\n[bold]Select Color Preset:[/bold]")
    CONSOLE.print("1️⃣  Cyber Neon (Cyan & Magenta)")
    CONSOLE.print("2️⃣  Matrix Green (Hacker Aesthetic)")
    CONSOLE.print("3️⃣  Dracula Dark (Purple & Pink)")

    choice = input("[cyan]Select (1-3): [/cyan]").strip()
    presets = {"1": "cyber_neon", "2": "matrix_green", "3": "dracula_dark"}
    preset = presets.get(choice, "cyber_neon")

    if return_choice:
        return preset

    display_system_dashboard(preset)


def banner_only_mode():
    """Quick banner display mode (for .bashrc/.zshrc injection)"""
    # Use default settings for quick banner
    display_ascii_banner(
        socket.gethostname(), "Cyber Warrior", "Securing the Digital World", "slant", "cyber_neon"
    )
    display_system_dashboard("cyber_neon")


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================


def main():
    """Main application entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--banner-only":
            banner_only_mode()
        elif sys.argv[1] == "--help":
            CONSOLE.print(
                Panel(
                    "[bold]CSK4 BANNER GENERATOR - Help[/bold]\n\n"
                    "[cyan]Usage:[/cyan]\n"
                    "  main.py              - Interactive menu\n"
                    "  main.py --banner-only - Quick banner (for .bashrc/.zshrc)\n"
                    "  main.py --help       - Show this help\n\n"
                    "[yellow]Features:[/yellow]\n"
                    "  ✓ Custom ASCII banners with multiple fonts\n"
                    "  ✓ Real-time system dashboard\n"
                    "  ✓ Color presets (Cyber Neon, Matrix Green, Dracula Dark)\n"
                    "  ✓ Auto-inject into terminal startup\n"
                    "  ✓ Safe backup & restore functionality",
                    border_style="bright_cyan",
                )
            )
        else:
            CONSOLE.print(f"[red]Unknown argument: {sys.argv[1]}[/red]")
            CONSOLE.print("Run with --help for usage information")
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
