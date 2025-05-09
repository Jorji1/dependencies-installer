# instalar_dependencias.py

import subprocess
import sys
import platform
import os


bibliotecas_principais = [
    "pywifi",
    "netifaces",
    "scapy"
]


bibliotecas_windows = [
    "comtypes"
]

def instalar_biblioteca(nome_biblioteca):
    """Tenta instalar uma biblioteca usando pip."""
    try:
        print(f"\n--- Tentando instalar {nome_biblioteca} ---")
      
        comando = [sys.executable, "-m", "pip", "install", "--upgrade", nome_biblioteca]
        
        subprocess.check_call(comando)
        print(f"[SUCESSO] Biblioteca '{nome_biblioteca}' instalada/atualizada com sucesso.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao instalar '{nome_biblioteca}'. Erro: {e}")
        print(f"       Por favor, tente instalar manualmente: pip install {nome_biblioteca}")
        return False
    except FileNotFoundError:
        print("[ERRO] Comando 'pip' não encontrado. Certifique-se de que Python e Pip estão instalados e no PATH do sistema.")
        sys.exit(1) # Sair se o pip não for encontrado

def verificar_privilegios_admin():
    """Verifica se o script está a ser executado com privilégios de administrador."""
    try:
        if platform.system().lower() == "windows":
            
            pass 
        else: 
            if os.geteuid() == 0:
                print("[INFO] Script está a ser executado como root/sudo.")
                return True
            else:
                print("[AVISO] Script não está a ser executado como root/sudo.")
                print("        Algumas instalações globais do pip ou operações do Scapy podem exigir privilégios elevados.")
                return False
    except AttributeError: 
        pass
    return False

def main():
    print("--- Iniciando Instalação de Dependências para o Analisador de Redes ---")
    
   

   
    for lib in bibliotecas_principais:
        if not instalar_biblioteca(lib):
           
            pass 

    
    if platform.system().lower() == "windows":
        print("\n--- Verificando dependências específicas do Windows ---")
        for lib_win in bibliotecas_windows:
            instalar_biblioteca(lib_win)
    
    print("\n\n--- Resumo da Instalação e Próximos Passos ---")
    print("Dependências Python principais verificadas/instaladas.")
    print("\nLembretes IMPORTANTES para o funcionamento do SCAPY:")
    
    if platform.system().lower() == "windows":
        print("- WINDOWS: É ESSENCIAL ter o Npcap instalado para o Scapy funcionar.")
        print("  Faça o download em https://npcap.com/")
        print("  Durante a instalação do Npcap, MARQUE a opção 'Install Npcap in WinPcap API-compatible Mode'.")
    elif platform.system().lower() == "linux":
        print("- LINUX: Scapy geralmente requer 'libpcap-dev' (ou nome similar dependendo da sua distribuição) e 'tcpdump'.")
        print("  Exemplo para Debian/Ubuntu: sudo apt-get install libpcap-dev tcpdump")
        print("  Pode ser necessário executar a ferramenta principal com 'sudo' para que o Scapy funcione.")
    elif platform.system().lower() == "darwin": # macOS
        print("- MACOS: Scapy deve funcionar, mas a ferramenta principal precisará ser executada com 'sudo' para operações de rede com Scapy.")

    print("\nLembretes para a FERRAMENTA PRINCIPAL:")
    print("- Para funcionalidades que usam Scapy (Scan LAN, Análise MITM), execute a ferramenta principal")
    print("  com privilégios de Administrador (Windows) ou sudo (Linux/macOS).")
    
    print("\n--- Instalação de dependências concluída ---")
    print("Pressione Enter para sair.")
    input()

if __name__ == "__main__":
    main()
