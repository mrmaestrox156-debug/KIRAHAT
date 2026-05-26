KIRAHAT v1.0
Advanced Network Reconnaissance and Security Auditing Framework
​KIRAHAT is a lightweight, high-performance terminal utility built in Python designed for independent security researchers, network administrators, and pentesters. Operating entirely through a streamlined, low-overhead command-line interface, the tool automates essential infrastructure diagnostics, service mapping, and wireless defense evaluations.
​Designed with tactical logic and strict process management, KIRAHAT acts as an orchestration layer over industry-standard binaries, providing operators with actionable insight into local networks and device resilience.
​Interface Link
https://i.postimg.cc/FKJcPNFv/Novo-projeto-536-9CC48D4.png
​Key Features
​Network Service Mapping (SCAN)
Leverages automated nmap engines to perform fast service and version detection on target nodes, isolating open ports and mapping network topology.
​Target Asset Persistence (SAVE)
Built-in logging structure that automatically stores diagnostic inputs and target identifiers to local flat files for streamlined auditing trails.
​Wireless Frame Analysis (ROUTER MASK)
Deploys raw 802.11 beacon generation via mdk4 to audit how local clients handle signal congestion and rogue access point environments.
​Load Resilience Testing (ROUTER ATTACK)
Conducts high-velocity UDP stress testing via layer-4 hping3 flooding, validating device capacity, state tables, and mitigation triggers under sustained traffic loads.
​Automated Wireless Auditing (PROCESS AIRCRACK-NG)
Integrates raw wireless interactions via aireplay-ng and sintonized interface management for direct deauthentication diagnostics.
​Installation and Setup
​Kali Linux Environment
​$ atualização
sudo apt update && sudo apt upgrade -y
​$ git
sudo apt install git python3 nmap hping3 mdk4 aircrack-ng -y
​$ cd
git clone https://github.com/mrmaestrox156-debug/KIRAHAT.git
cd KIRAHAT
python3 kirahat.py
​Termux Environment
​$ atualização
pkg update && pkg upgrade -y
​$ git
pkg install git python nmap -y
pkg install tsu root-repo -y
tsu -c "pkg install hping3 mdk4 aircrack-ng -y"
​$ cd
git clone https://github.com/mrmaestrox156-debug/KIRAHAT.git
cd KIRAHAT
tsu -c "python kirahat.py"
​Wireless Interface Configuration
​Kali Linux Monitor Mode
​$ instalação e ativação
sudo apt install aircrack-ng ethtool rfkill wireless-tools -y
sudo airmon-ng check kill
sudo airmon-ng start wlan0
iwconfig
sudo airodump-ng wlan0mon
​Termux Monitor Mode (Requires Root)
​$ instalação e ativação
tsu -c "pkg install aircrack-ng tsu wireless-tools -y"
tsu -c "airmon-ng check kill"
tsu -c "airmon-ng start wlan0"
tsu -c "iwconfig"
tsu -c "airodump-ng wlan0mon"

