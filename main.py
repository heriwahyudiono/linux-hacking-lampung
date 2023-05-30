import os
import pyfiglet
from colorama import init, Fore
from network_scanner import scan_network

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    init()  # Inisialisasi colorama
    custom_fig = pyfiglet.Figlet(font='slant')
    colored_banner1 = Fore.RED + custom_fig.renderText('LinuxHacking') + Fore.RESET
    colored_banner2 = Fore.YELLOW + custom_fig.renderText('Lampung') + Fore.RESET
    print(colored_banner1)
    print(colored_banner2)
    print("\n")

def print_menu():
    print(Fore.CYAN + "[1] Scan Network")
    print(Fore.CYAN + "[2] Exploit Vulnerability")
    print(Fore.CYAN + "[3] Crack Password")
    print(Fore.CYAN + "[4] Exit" + Fore.RESET)

def exploit_vulnerability():
    # Logika untuk mengeksploitasi kerentanan
    print(Fore.GREEN + "Exploiting vulnerability..." + Fore.RESET)
    # Kode Anda di sini

def crack_password():
    # Logika untuk melakukan cracking password
    print(Fore.GREEN + "Cracking password..." + Fore.RESET)
    # Kode Anda di sini

def main():
    clear_screen()
    print_banner()
    print_menu()

    while True:
        choice = input(Fore.YELLOW + "\nEnter your choice: " + Fore.RESET)

        if choice == '1':
            scan_network()

        elif choice == '2':
            exploit_vulnerability()

        elif choice == '3':
            crack_password()

        elif choice == '4':
            print(Fore.RED + "Exiting..." + Fore.RESET)
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again." + Fore.RESET)

        input(Fore.MAGENTA + "Press Enter to continue..." + Fore.RESET)
        clear_screen()
        print_banner()
        print_menu()

if __name__ == '__main__':
    main()
