import os
import pyfiglet
from colorama import init, Fore

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
    print("[1] Scan Network")
    print("[2] Exploit Vulnerability")
    print("[3] Crack Password")
    print("[4] Exit")

def scan_network():
    # Logika untuk melakukan scan jaringan
    print("Scanning network...")
    # Kode Anda di sini

def exploit_vulnerability():
    # Logika untuk mengeksploitasi kerentanan
    print("Exploiting vulnerability...")
    # Kode Anda di sini

def crack_password():
    # Logika untuk melakukan cracking password
    print("Cracking password...")
    # Kode Anda di sini

def main():
    clear_screen()
    print_banner()
    print_menu()

    while True:
        choice = input("\nEnter your choice: ")

        if choice == '1':
            scan_network()

        elif choice == '2':
            exploit_vulnerability()

        elif choice == '3':
            crack_password()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")
        clear_screen()
        print_banner()
        print_menu()

if __name__ == '__main__':
    main()
