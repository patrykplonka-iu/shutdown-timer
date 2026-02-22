# Szkic programu do wyłączania komputera po określonym czasie
import os

def ask_minutes() -> int:
    # Funkcja pyta użytkownika o czas w minutach
    while True:
        raw = input("Podaj czas w minutach do wyłączenia komputera (0 aby anulować): ")

        try:
            minutes = int(raw)
        except ValueError:
            print("Podaj poprawną wartość.")
            continue
        if minutes < 0:
            print("Podaj liczbę większą od niczego.")
            continue

        return minutes
    
def ask_confirm() -> bool:
    # Funkcja pyta użytkownika o potwierdzenie
    while True:
        odpowiedz = input("Czy na pewno chcesz kontynuować? (tak/nie): ").lower()

        if odpowiedz == 'tak':
            return True
        if odpowiedz == 'nie':
            return False

        print("Niepoprawna odpowiedź. Proszę wpisać 'tak' lub 'nie'.")

def shutdown_cancel() -> None:
    # Funkcja anuluje zaplanowane wyłączenie komputera
    os.system("shutdown -a")
    print("Anulowano wyłączenie komputera.")

def shutdown_shedule(minutes: int) -> None:
    # Funkcja planuje wyłączenie komputera po określonym czasie
    seconds = minutes * 60
    os.system(f"shutdown -s -t {seconds}")
    print(f"OK. Komputer wyłączy się za {minutes} minut.")
    print("Aby anulować: uruchom program i wpisz 0, albo w CMD/PowerShell: shutdown -a")

def shutdown_status() -> None:
    # Funkcja sprawdza status zaplanowanego wyłączenia komputera
    result = os.popen("shutdown -a 2>&1").read()
    if "No shutdown was in progress" in result:
        print("Brak zaplanowanego wyłączenia.")
    else:
        print("Było zaplanowane wyłączenie – zostało anulowane.")

def menu():
    # Funkcja wyświetla menu i obsługuje wybory użytkownika
    print("\n=== Menu Wyłączania Komputera ===")
    print("1 – zaplanuj wyłączenie")
    print("2 – anuluj wyłączenie")
    print("3 – status")
    print("0 – wyjście")
    return input("Wybierz opcję: ").strip()

def main() -> None:
    # Główna funkcja programu
    while True:
        choice = menu()
        
        if choice == "1":
            minutes = ask_minutes()
            if ask_confirm():
                shutdown_shedule(minutes)
            else:
                print("OK, nie wyłączam.")

        elif choice == "2":
            shutdown_cancel()

        elif choice == "3":
            shutdown_status()
        
        elif choice == "0":
            print("Do widzenia!")
            break

        else: 
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
