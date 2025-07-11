# AIPT: Autonomous APT Framework

**WARNING: This tool is extremely powerful and dangerous. Use only in authorized, isolated, and legal environments.**

AIPT is an autonomous advanced persistent threat simulation framework for Kali Linux. It uses Ollama (with the `huihui_ai/qwen2.5-coder-abliterate` model) to generate and execute commands automatically, based on a user-provided objective. All commands are executed without confirmation.

## Features
- Prompts for an attack objective
- Uses Ollama to generate the next best command
- Executes each command automatically
- Displays commands and outputs in the terminal
- Loops indefinitely, never stopping

## Installation

1. Ensure you have Python 3, Ollama, and the required model installed on your system.
2. Clone or copy this repository to your Kali machine.
3. Run the install script:

```bash
cd AIPT
chmod +x install_aipt.sh
./install_aipt.sh
```

4. Now you can run the tool with:

```bash
sudo AIPT
```

## Usage

- When prompted, enter your attack objective.
- The tool will begin generating and executing commands automatically.
- Commands and their outputs will be shown in the terminal.
- To stop, press `Ctrl+C`.

## Disclaimer

This tool is for educational, research, and authorized penetration testing use **only**. Unauthorized use is illegal and unethical. The authors assume no liability for misuse. 