# Quick Start Guide - WiFi Penetration Testing

## Quick Setup

### 1. Download and Install

```bash
# Clone or download the scripts
git clone <repository-url>
cd wifi-pentest-tools

# Make scripts executable
chmod +x *.sh

# Run the installer
sudo ./install.sh
```

### 2. Verify Installation

```bash
# Check if tools are installed
aircrack-ng --version
hashcat --version

# Check wireless interface
iwconfig
```

### 3. Run Basic Test

```bash
# Basic WiFi penetration test
sudo wifi_pentest.sh

# Advanced test with custom options
sudo wifi_pentest_advanced.sh -i wlan1 -w /usr/share/wordlists/rockyou.txt
```

## Prerequisites

- **Kali Linux** (recommended) or any Linux with aircrack-ng
- **Root privileges** (sudo access)
- **Wireless adapter** with monitor mode support (WPA3 attacks require special support)
- **Target network** you own or have permission to test

### Supported Protocols

- WPA (PSK)
- WPA2 (PSK)
- WPA3 (SAE/PMKID, advanced/experimental, requires hashcat and hcxpcapngtool)

> **Note:** WPA3 attacks are only possible if a PMKID or SAE handshake is captured. Not all networks or adapters support this. Use the advanced script for WPA3.

## Basic Usage

### Step 1: Choose Your Script

- **`wifi_pentest.sh`** - Basic version with aircrack-ng only
- **`wifi_pentest_advanced.sh`** - Advanced version with hashcat GPU acceleration

### Step 2: Run the Script

```bash
# Basic usage
sudo ./wifi_pentest.sh

# With custom interface
sudo ./wifi_pentest.sh -i wlan1

# With custom wordlist
sudo ./wifi_pentest.sh -w /path/to/wordlist.txt
```

### Step 3: Follow the Prompts

1. **Select target network** from the list
2. **Wait for handshake capture**
3. **Monitor password cracking progress**
4. **Review results**

## ⚡ Advanced Usage

### Command Line Options

```bash
# Advanced script with all options
sudo wifi_pentest_advanced.sh \
  -i wlan1 \                    # Custom interface
  -w /usr/share/wordlists/rockyou.txt \  # Custom wordlist
  -g 0 \                        # GPU device
  -t 600 \                      # 10-minute timeout
  -d 10                         # 10 deauth packets
```

### Performance Tips

1. **Use GPU acceleration** (hashcat)
2. **Choose strong wordlists** (rockyou.txt, SecLists)
3. **Run during peak hours** when networks have active clients
4. **Multiple attempts** for better handshake capture

## 🔧 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| "Failed to start monitor mode" | Check adapter compatibility, try different interface |
| "No WPA networks found" | Move closer to target, check monitor mode |
| "Handshake capture failed" | Wait for clients, try multiple times |
| "Password not found" | Use larger wordlist, try different wordlists |

### Hardware Compatibility

**Check compatibility:**
```bash
# List wireless interfaces
iwconfig

# Check monitor mode support
iw phy | grep -A 10 "Supported interface modes"
```

## Expected Results

### Successful Run Output

```
╔══════════════════════════════════════════════════════════════╗
║                    WiFi Penetration Testing                  ║
║                        Aircrack-ng Suite                     ║
╚══════════════════════════════════════════════════════════════╝

[*] Checking dependencies...
[+] All dependencies are installed
[*] Setting up environment...
[+] Environment setup complete
[*] Starting monitor mode on wlan0...
[+] Monitor mode started successfully
[*] Scanning for WiFi networks...
[+] Found 5 WPA networks

Available WPA Networks:
==================================
1. SSID: MyNetwork | BSSID: AA:BB:CC:DD:EE:FF | Channel: 6
2. SSID: OfficeWiFi | BSSID: 11:22:33:44:55:66 | Channel: 11

Select target network (1-2): 1
[+] Selected target: MyNetwork (AA:BB:CC:DD:EE:FF) on channel 6
[*] Starting handshake capture for MyNetwork...
[+] Found 2 connected client(s)
[*] Deauthenticating client: AA:BB:CC:DD:EE:FF
[+] WPA handshake captured successfully!
[*] Attempting to crack WPA password...
[+] Password cracked successfully!
[+] Network: MyNetwork
[+] Password: mypassword123
[+] Results saved to results.txt
[+] WiFi penetration test completed!
```

### Output Files

- `capture-01.cap` - Raw packet capture
- `results.txt` - Final results summary
- `wifi_pentest.log` - Detailed activity log
- `cracked_password.txt` - Cracking results (if successful)

## Legal and Ethical Use

### **IMPORTANT DISCLAIMER**

This tool is for **educational and authorized penetration testing purposes ONLY**.

**Legal Requirements:**
- Only test networks you own
- Only test networks with written permission
- Respect local laws and regulations
- Follow responsible disclosure practices

**Ethical Guidelines:**
- Document all testing activities
- Use dedicated testing hardware
- Report vulnerabilities responsibly
- Never use for malicious purposes

## Getting Help

### Documentation
- Full README: `README.md`
- Installation guide: `install.sh`
- Configuration: `/etc/wifi_pentest.conf`

### Support
- Check logs: `/var/log/wifi_pentest/`
- Verify installation: `./install.sh --verify`
- Test hardware: `iwconfig` and `iw phy`

### Common Commands

```bash
# Check script help
./wifi_pentest.sh -h

# Verify installation
sudo ./install.sh

# Check wireless interfaces
iwconfig

# Test monitor mode
sudo airmon-ng start wlan0

# Manual network scan
sudo airodump-ng wlan0mon
```

## Next Steps

1. **Practice on your own networks** first
2. **Learn about WiFi security** and WPA protocols
3. **Explore additional tools** (Wifite, Fern WiFi Cracker)
4. **Study network defense** and intrusion detection
5. **Consider certifications** (CEH, OSCP, etc.)

---

**Remember: Always use these tools responsibly and legally!** 