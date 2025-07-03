#!/bin/bash

# WiFi Penetration Testing Tools Installation Script
# Installs all necessary dependencies for WiFi penetration testing
# Author: Security Researcher
# Version: 1.0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[*]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[+]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[-]${NC} $1"
}

print_info() {
    echo -e "${CYAN}[i]${NC} $1"
}

# Function to check if running as root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        print_error "This script must be run as root (use sudo)"
        exit 1
    fi
}

# Function to check if running on Kali Linux
check_kali() {
    if ! grep -q "Kali" /etc/os-release 2>/dev/null; then
        print_warning "This script is designed for Kali Linux"
        print_info "Some features may not work on other distributions"
        echo -e "${YELLOW}Continue anyway? (y/N):${NC}"
        read -r response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            exit 1
        fi
    else
        print_success "Kali Linux detected"
    fi
}

# Function to update system
update_system() {
    print_status "Updating system packages..."
    
    apt update -y
    if [ $? -eq 0 ]; then
        print_success "System updated successfully"
    else
        print_error "Failed to update system"
        exit 1
    fi
}

# Function to install basic dependencies
install_basic_deps() {
    print_status "Installing basic dependencies..."
    
    local packages=(
        "build-essential"
        "git"
        "curl"
        "wget"
        "python3"
        "python3-pip"
        "wireless-tools"
        "wpasupplicant"
        "pkg-config"
        "libssl-dev"
        "libnl-3-dev"
        "libnl-genl-3-dev"
        "libpcap-dev"
        "zlib1g-dev"
    )
    
    for package in "${packages[@]}"; do
        print_info "Installing $package..."
        apt install -y "$package"
        if [ $? -ne 0 ]; then
            print_warning "Failed to install $package"
        fi
    done
    
    print_success "Basic dependencies installed"
}

# Function to install aircrack-ng suite
install_aircrack() {
    print_status "Installing aircrack-ng suite..."
    
    # Install aircrack-ng from package manager
    apt install -y aircrack-ng
    
    if [ $? -eq 0 ]; then
        print_success "Aircrack-ng suite installed successfully"
    else
        print_error "Failed to install aircrack-ng suite"
        exit 1
    fi
    
    # Verify installation
    if command -v aircrack-ng &> /dev/null; then
        print_success "Aircrack-ng verification successful"
    else
        print_error "Aircrack-ng installation verification failed"
        exit 1
    fi
}

# Function to install hashcat
install_hashcat() {
    print_status "Installing hashcat..."
    
    # Install hashcat from package manager
    apt install -y hashcat
    
    if [ $? -eq 0 ]; then
        print_success "Hashcat installed successfully"
    else
        print_warning "Failed to install hashcat from package manager"
        print_info "Attempting to install from source..."
        install_hashcat_from_source
    fi
    
    # Verify installation
    if command -v hashcat &> /dev/null; then
        print_success "Hashcat verification successful"
        # Check GPU support
        if hashcat -I &> /dev/null; then
            print_success "GPU acceleration available"
        else
            print_warning "GPU acceleration not available"
        fi
    else
        print_error "Hashcat installation verification failed"
    fi
}

# Function to install hashcat from source
install_hashcat_from_source() {
    print_info "Installing hashcat from source..."
    
    cd /tmp
    
    # Clone hashcat repository
    if git clone https://github.com/hashcat/hashcat.git; then
        cd hashcat
        
        # Build and install
        make
        make install
        
        if [ $? -eq 0 ]; then
            print_success "Hashcat built and installed from source"
        else
            print_error "Failed to build hashcat from source"
        fi
        
        cd ..
        rm -rf hashcat
    else
        print_error "Failed to clone hashcat repository"
    fi
}

# Function to install additional tools
install_additional_tools() {
    print_status "Installing additional WiFi testing tools..."
    
    local tools=(
        "hcxdumptool"
        "hcxtools"
        "reaver"
        "pixiewps"
        "bully"
        "wifite"
        "fern-wifi-cracker"
    )
    
    for tool in "${tools[@]}"; do
        print_info "Installing $tool..."
        apt install -y "$tool" 2>/dev/null
        
        if [ $? -eq 0 ]; then
            print_success "$tool installed"
        else
            print_warning "$tool not available in package manager"
        fi
    done
}

# Function to install wordlists
install_wordlists() {
    print_status "Installing wordlists..."
    
    # Create wordlists directory
    mkdir -p /usr/share/wordlists
    
    # Install common wordlists
    local wordlists=(
        "rockyou"
        "seclists"
        "metasploit"
    )
    
    for wordlist in "${wordlists[@]}"; do
        print_info "Installing $wordlist wordlist..."
        apt install -y "wordlists-$wordlist" 2>/dev/null
        
        if [ $? -eq 0 ]; then
            print_success "$wordlist wordlist installed"
        else
            print_warning "$wordlist wordlist not available in package manager"
        fi
    done
    
    # Download rockyou.txt if not available
    if [ ! -f "/usr/share/wordlists/rockyou.txt" ]; then
        print_info "Downloading rockyou.txt..."
        cd /usr/share/wordlists
        
        # Try to download from multiple sources
        if wget -q "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"; then
            print_success "rockyou.txt downloaded successfully"
        elif wget -q "https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt.gz" && gunzip rockyou.txt.gz; then
            print_success "rockyou.txt downloaded and extracted"
        else
            print_warning "Failed to download rockyou.txt"
            print_info "You can download it manually from:"
            print_info "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
        fi
    fi
}

# Function to configure wireless interface
configure_wireless() {
    print_status "Configuring wireless interface..."
    
    # Check for wireless interfaces
    local interfaces=$(iwconfig 2>/dev/null | grep -E "^[a-zA-Z0-9]+" | cut -d' ' -f1)
    
    if [ -n "$interfaces" ]; then
        print_success "Found wireless interfaces:"
        echo "$interfaces" | while read -r interface; do
            print_info "  - $interface"
        done
        
        # Check monitor mode support
        for interface in $interfaces; do
            if iw phy | grep -q "Supported interface modes.*monitor"; then
                print_success "$interface supports monitor mode"
            else
                print_warning "$interface may not support monitor mode"
            fi
        done
    else
        print_warning "No wireless interfaces found"
        print_info "Make sure your wireless adapter is connected and recognized"
    fi
}

# Function to create desktop shortcuts
create_shortcuts() {
    print_status "Creating desktop shortcuts..."
    
    # Create desktop directory if it doesn't exist
    if [ -d "/home" ]; then
        for user_home in /home/*; do
            if [ -d "$user_home" ]; then
                local username=$(basename "$user_home")
                local desktop_dir="$user_home/Desktop"
                
                if [ -d "$desktop_dir" ]; then
                    # Create shortcut for basic script
                    cat > "$desktop_dir/WiFi Pentest Basic.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=WiFi Pentest Basic
Comment=Basic WiFi penetration testing script
Exec=sudo /usr/local/bin/wifi_pentest.sh
Icon=network-wireless
Terminal=true
Categories=Network;Security;
EOF
                    
                    # Create shortcut for advanced script
                    cat > "$desktop_dir/WiFi Pentest Advanced.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=WiFi Pentest Advanced
Comment=Advanced WiFi penetration testing script with hashcat
Exec=sudo /usr/local/bin/wifi_pentest_advanced.sh
Icon=network-wireless
Terminal=true
Categories=Network;Security;
EOF
                    
                    # Make shortcuts executable
                    chmod +x "$desktop_dir/WiFi Pentest Basic.desktop"
                    chmod +x "$desktop_dir/WiFi Pentest Advanced.desktop"
                    chown "$username:$username" "$desktop_dir/WiFi Pentest"*.desktop
                    
                    print_success "Created shortcuts for user: $username"
                fi
            fi
        done
    fi
}

# Function to install scripts to system
install_scripts() {
    print_status "Installing scripts to system..."
    
    # Copy scripts to /usr/local/bin
    if [ -f "wifi_pentest.sh" ]; then
        cp wifi_pentest.sh /usr/local/bin/
        chmod +x /usr/local/bin/wifi_pentest.sh
        print_success "Basic script installed to /usr/local/bin/wifi_pentest.sh"
    fi
    
    if [ -f "wifi_pentest_advanced.sh" ]; then
        cp wifi_pentest_advanced.sh /usr/local/bin/
        chmod +x /usr/local/bin/wifi_pentest_advanced.sh
        print_success "Advanced script installed to /usr/local/bin/wifi_pentest_advanced.sh"
    fi
}

# Function to create configuration file
create_config() {
    print_status "Creating configuration file..."
    
    cat > /etc/wifi_pentest.conf << EOF
# WiFi Penetration Testing Configuration
# Default settings for WiFi penetration testing scripts

# Default wireless interface
DEFAULT_INTERFACE=wlan0

# Default wordlist
DEFAULT_WORDLIST=/usr/share/wordlists/rockyou.txt

# Hashcat settings
HASHCAT_MODE=2500
GPU_DEVICE=0

# Attack settings
ATTACK_TIMEOUT=300
DEAUTH_COUNT=5

# Logging
LOG_DIR=/var/log/wifi_pentest
TEMP_DIR=/tmp/wifi_pentest

# Legal notice
LEGAL_NOTICE="This tool is for authorized penetration testing only. Use responsibly and legally."
EOF
    
    print_success "Configuration file created: /etc/wifi_pentest.conf"
}

# Function to set up logging
setup_logging() {
    print_status "Setting up logging..."
    
    # Create log directory
    mkdir -p /var/log/wifi_pentest
    
    # Create logrotate configuration
    cat > /etc/logrotate.d/wifi_pentest << EOF
/var/log/wifi_pentest/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 644 root root
}
EOF
    
    print_success "Logging configured"
}

# Function to display installation summary
show_summary() {
    echo -e "\n${GREEN}=== Installation Summary ===${NC}"
    echo ""
    
    # Check installed tools
    local tools=("aircrack-ng" "hashcat" "hcxdumptool" "reaver" "wifite")
    for tool in "${tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            print_success "$tool: Installed"
        else
            print_warning "$tool: Not installed"
        fi
    done
    
    # Check wordlists
    if [ -f "/usr/share/wordlists/rockyou.txt" ]; then
        print_success "rockyou.txt: Available"
    else
        print_warning "rockyou.txt: Not found"
    fi
    
    # Check wireless interfaces
    local interfaces=$(iwconfig 2>/dev/null | grep -E "^[a-zA-Z0-9]+" | cut -d' ' -f1)
    if [ -n "$interfaces" ]; then
        print_success "Wireless interfaces: Found"
        echo "$interfaces" | while read -r interface; do
            print_info "  - $interface"
        done
    else
        print_warning "Wireless interfaces: None found"
    fi
    
    echo ""
    print_info "Scripts installed to:"
    print_info "  - /usr/local/bin/wifi_pentest.sh"
    print_info "  - /usr/local/bin/wifi_pentest_advanced.sh"
    
    echo ""
    print_info "Usage examples:"
    print_info "  sudo wifi_pentest.sh"
    print_info "  sudo wifi_pentest_advanced.sh -i wlan1 -w /path/to/wordlist.txt"
    
    echo ""
    print_warning "IMPORTANT: Only use these tools on networks you own or have permission to test!"
}

# Main installation function
main() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║              WiFi Penetration Testing Tools Installer        ║"
    echo "║                        Kali Linux Edition                     ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    # Check prerequisites
    check_root
    check_kali
    
    # Installation steps
    update_system
    install_basic_deps
    install_aircrack
    install_hashcat
    install_additional_tools
    install_wordlists
    configure_wireless
    install_scripts
    create_config
    setup_logging
    create_shortcuts
    
    # Show summary
    show_summary
    
    print_success "Installation completed successfully!"
    print_info "You can now use the WiFi penetration testing scripts."
}

# Run main function
main "$@" 