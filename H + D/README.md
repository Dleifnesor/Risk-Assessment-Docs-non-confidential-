# WiFi Penetration Testing Script

A comprehensive automated WiFi penetration testing script for Kali Linux that uses the aircrack-ng suite to capture WPA handshakes and crack passwords.

## ⚠️ **IMPORTANT LEGAL DISCLAIMER**

**This script is for educational and authorized penetration testing purposes ONLY. Using this tool against networks you do not own or have explicit permission to test is ILLEGAL and may result in criminal charges.**

- Only use on networks you own or have written permission to test
- Respect local laws and regulations
- This tool is intended for security professionals and researchers
- The authors are not responsible for any misuse of this script

## 🚀 Features

- **Automated Network Discovery**: Scans and lists all available WPA, WPA2, and WPA3 networks
- **Interactive Target Selection**: Choose your target network from a list
- **Handshake Capture**: Automatically captures WPA/WPA2 handshakes using deauthentication attacks. WPA3 (SAE/PMKID) handshakes require advanced tools and compatible hardware.
- **Password Cracking**: Integrates with aircrack-ng for WPA/WPA2 and hashcat for WPA3 (if handshake is captured)
- **Comprehensive Logging**: Detailed logs of all activities
- **Clean Interface**: Colored output and user-friendly interface
- **Error Handling**: Robust error checking and recovery
- **Cleanup**: Automatic cleanup of monitor mode and network services

## 📋 Requirements

### Hardware Requirements
- Wireless adapter with monitor mode support (WPA3 attacks require special support)
- Compatible with aircrack-ng suite

### Software Requirements
- Kali Linux (recommended) or any Linux distribution with aircrack-ng
- - WPA3 attacks require hashcat and hcxpcapngtool (see advanced script)
- Root privileges
- aircrack-ng suite
- hashcat (optional, for GPU acceleration)

## �� Installation

### 1. Install Dependencies

```bash
# Update package list
sudo apt update

# Install aircrack-ng suite
sudo apt install aircrack-ng

# Install hashcat (optional, for GPU acceleration)
sudo apt install hashcat

# Install additional tools
sudo apt install wireless-tools wpasupplicant
```

### 2. Download the Script

```bash
# Clone or download the script
wget https://raw.githubusercontent.com/your-repo/wifi_pentest.sh
chmod +x wifi_pentest.sh
```

### 3. Verify Installation

```bash
# Check if aircrack-ng is installed
aircrack-ng --help

# Check if your wireless adapter supports monitor mode
iwconfig
```

## Usage

### Supported Protocols

- WPA (PSK)
- WPA2 (PSK)
- WPA3 (SAE/PMKID, advanced/experimental, requires hashcat and hcxpcapngtool)

> **Note:** WPA3 attacks are only possible if a PMKID or SAE handshake is captured. Not all networks or adapters support this. Use the advanced script for WPA3.

### Basic Usage

```bash
# Run with default settings
sudo ./wifi_pentest.sh
```

### Advanced Usage

```bash
# Specify custom wireless interface
sudo ./wifi_pentest.sh -i wlan1

# Use custom wordlist
sudo ./wifi_pentest.sh -w /path/to/wordlist.txt

# Combine options
sudo ./wifi_pentest.sh -i wlan1 -w /usr/share/wordlists/rockyou.txt

# Show help
./wifi_pentest.sh -h
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-i, --interface` | Specify wireless interface | `wlan0` |
| `-w, --wordlist` | Specify wordlist path | `/usr/share/wordlists/rockyou.txt` |
| `-h, --help` | Show help message | N/A |

## How It Works

### 1. **Environment Setup**
- Checks for root privileges
- Verifies all dependencies are installed
- Creates temporary working directory
- Kills interfering network processes

### 2. **Monitor Mode Activation**
- Starts monitor mode on the specified wireless interface
- Creates a monitor interface (e.g., wlan0mon)

### 3. **Network Discovery**
- Scans for available WiFi networks
- Filters for WPA-protected networks only
- Displays interactive list for target selection

### 4. **Handshake Capture**
- Starts packet capture on the target network
- Identifies connected clients
- Performs deauthentication attacks to force reconnections
- Captures WPA handshake during reconnection

### 5. **Password Cracking**
- Uses aircrack-ng to attempt password cracking
- Supports custom wordlists
- Saves results to file

### 6. **Cleanup**
- Stops monitor mode
- Restarts network services
- Cleans up temporary files

## Output Files

The script creates several output files in the temporary directory:

- `capture-01.cap` - Raw packet capture file
- `cracked_password.txt` - Cracking results (if successful)
- `results.txt` - Final results summary
- `wifi_pentest.log` - Detailed activity log
- `scan-01.csv` - Network scan results

## Troubleshooting

### Common Issues

#### 1. "Failed to start monitor mode"
```bash
# Check if your adapter supports monitor mode
iwconfig

# Try different interface names
sudo ./wifi_pentest.sh -i wlan1

# Check for driver issues
dmesg | grep -i wifi
```

#### 2. "No WPA networks found"
- Ensure you're in range of WPA networks
- Check if monitor mode is working properly
- Try running the scan manually:
```bash
sudo airodump-ng wlan0mon
```

#### 3. "Failed to capture WPA handshake"
- Wait for clients to connect to the target network
- Try running the script multiple times
- Ensure the target network has active clients

#### 4. "Password not found in wordlist"
- Use a larger wordlist (e.g., rockyou.txt)
- Try different wordlists
- The password might not be in the wordlist

### Performance Tips

1. **Use GPU Acceleration**: Install hashcat for faster cracking
2. **Optimize Wordlists**: Use targeted wordlists for better success rates
3. **Multiple Attempts**: Run the script multiple times for better handshake capture
4. **Timing**: Run when target networks have active clients

## 🛡️ Security Best Practices

### For Penetration Testers
- Always obtain written permission before testing
- Document all activities thoroughly
- Use dedicated testing hardware
- Follow responsible disclosure practices

### For Network Administrators
- Use strong, unique passwords
- Enable WPA3 when possible
- Monitor for deauthentication attacks
- Implement intrusion detection systems
- Regular security audits

## 📚 Additional Resources

### Documentation
- [Aircrack-ng Documentation](https://www.aircrack-ng.org/doku.php)
- [Kali Linux Wireless Testing](https://www.kali.org/tools/)
- [WiFi Security Best Practices](https://www.wi-fi.org/security)

### Wordlists
- [RockYou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [CrackStation](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm)

### Tools
- [Hashcat](https://hashcat.net/hashcat/)
- [John the Ripper](https://www.openwall.com/john/)
- [Wifite](https://github.com/kimocoder/wifite2)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Guidelines
- Follow the existing code style
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚖️ Legal Notice

This tool is provided for educational purposes only. Users are responsible for ensuring they have proper authorization before using this tool. The authors disclaim any liability for misuse of this software.

---

**Remember: Always use this tool responsibly and legally!** 