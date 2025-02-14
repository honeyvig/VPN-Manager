import subprocess
import os
import sys
import time

# Path to configuration files (you would normally have these for your clients)
WIREGUARD_CONFIG_PATH = "/etc/wireguard/wg0.conf"
OPENVPN_CONFIG_PATH = "/etc/openvpn/client.ovpn"
IKEV2_CONFIG_PATH = "/etc/ipsec.conf"  # Assuming you use strongSwan for IKEv2

# Function to start WireGuard VPN
def start_wireguard():
    try:
        print("Starting WireGuard VPN...")
        # Ensure WireGuard config exists
        if os.path.exists(WIREGUARD_CONFIG_PATH):
            # Start WireGuard using wg-quick
            subprocess.run(['sudo', 'wg-quick', 'up', 'wg0'], check=True)
            print("WireGuard VPN started successfully!")
        else:
            print("WireGuard config not found!")
    except subprocess.CalledProcessError as e:
        print(f"Error starting WireGuard VPN: {e}")
        sys.exit(1)

# Function to stop WireGuard VPN
def stop_wireguard():
    try:
        print("Stopping WireGuard VPN...")
        subprocess.run(['sudo', 'wg-quick', 'down', 'wg0'], check=True)
        print("WireGuard VPN stopped successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping WireGuard VPN: {e}")
        sys.exit(1)

# Function to start OpenVPN
def start_openvpn():
    try:
        print("Starting OpenVPN...")
        # Ensure OpenVPN config exists
        if os.path.exists(OPENVPN_CONFIG_PATH):
            subprocess.run(['sudo', 'openvpn', '--config', OPENVPN_CONFIG_PATH], check=True)
            print("OpenVPN started successfully!")
        else:
            print("OpenVPN config not found!")
    except subprocess.CalledProcessError as e:
        print(f"Error starting OpenVPN: {e}")
        sys.exit(1)

# Function to stop OpenVPN
def stop_openvpn():
    try:
        print("Stopping OpenVPN...")
        subprocess.run(['sudo', 'killall', 'openvpn'], check=True)
        print("OpenVPN stopped successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping OpenVPN: {e}")
        sys.exit(1)

# Function to start IKEv2 (strongSwan)
def start_ikev2():
    try:
        print("Starting IKEv2 VPN...")
        # Ensure strongSwan is installed and configured
        if os.path.exists(IKEV2_CONFIG_PATH):
            subprocess.run(['sudo', 'ipsec', 'up', 'ikev2'], check=True)
            print("IKEv2 VPN started successfully!")
        else:
            print("IKEv2 config not found!")
    except subprocess.CalledProcessError as e:
        print(f"Error starting IKEv2 VPN: {e}")
        sys.exit(1)

# Function to stop IKEv2 VPN
def stop_ikev2():
    try:
        print("Stopping IKEv2 VPN...")
        subprocess.run(['sudo', 'ipsec', 'down', 'ikev2'], check=True)
        print("IKEv2 VPN stopped successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping IKEv2 VPN: {e}")
        sys.exit(1)

# Main function to control VPNs
def manage_vpn(protocol, action):
    if protocol == "wireguard":
        if action == "start":
            start_wireguard()
        elif action == "stop":
            stop_wireguard()
        else:
            print("Invalid action for WireGuard VPN")
    
    elif protocol == "openvpn":
        if action == "start":
            start_openvpn()
        elif action == "stop":
            stop_openvpn()
        else:
            print("Invalid action for OpenVPN")
    
    elif protocol == "ikev2":
        if action == "start":
            start_ikev2()
        elif action == "stop":
            stop_ikev2()
        else:
            print("Invalid action for IKEv2")
    else:
        print("Invalid protocol. Choose from 'wireguard', 'openvpn', or 'ikev2'.")

# Command-line interface (CLI) for interacting with the VPN system
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vpn_manager.py <protocol> <action>")
        print("<protocol> should be one of: 'wireguard', 'openvpn', 'ikev2'")
        print("<action> should be either 'start' or 'stop'")
        sys.exit(1)

    protocol = sys.argv[1].lower()
    action = sys.argv[2].lower()

    manage_vpn(protocol, action)
