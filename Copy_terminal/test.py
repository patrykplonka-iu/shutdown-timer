import os
import subprocess
import tkinter as tk
from tkinter import messagebox


def shutdown_schedule(minutes: int) -> None:
    seconds = minutes * 60
    os.system(f"shutdown -s -t {seconds}")


def shutdown_cancel() -> None:
    os.system("shutdown -a")


def shutdown_status() -> str:
    """
    Windows nie daje super API do 'statusu', ale shutdown /a zwraca sensowny komunikat w konsoli.
    Najprościej: spróbować odczytać tekst z 'shutdown -a' bez anulowania? Niestety -a anuluje.
    Więc status robimy jako: komunikat + edukacja (co user ma sprawdzić).
    """
    return "Windows nie udostępnia czystego 'statusu' bez anulowania.\n" \
           "Jeśli chcesz sprawdzić, uruchom:  shutdown -a  (to ANULUJE).\n" \
           "Albo po prostu pamiętaj ile ustawiłeś."


def parse_minutes(text: str) -> int:
    text = text.strip()
    if text == "":
        raise ValueError("Puste")
    minutes = int(text)
    if minutes < 0:
        raise ValueError("Ujemne")
    return minutes


def on_schedule(entry: tk.Entry) -> None:
    try:
        minutes = parse_minutes(entry.get())
    except ValueError:
        messagebox.showerror("Błąd", "Podaj liczbę minut >= 0.")
        return

    if minutes == 0:
        shutdown_cancel()
        messagebox.showinfo("OK", "Anulowano zaplanowane wyłączenie (jeśli było).")
        return

    if not messagebox.askyesno("Potwierdzenie", f"Czy na pewno wyłączyć komputer za {minutes} minut?"):
        return

    shutdown_schedule(minutes)
    messagebox.showinfo("OK", f"Zaplanuję wyłączenie za {minutes} minut.\nAnulowanie: przycisk 'Anuluj' lub komenda: shutdown -a")


def on_cancel() -> None:
    shutdown_cancel()
    messagebox.showinfo("OK", "Anulowano zaplanowane wyłączenie (jeśli było).")


def on_status() -> None:
    messagebox.showinfo("Status", shutdown_status())


def build_ui() -> tk.Tk:
    root = tk.Tk()
    root.title("Shutdown Timer")

    tk.Label(root, text="Minuty do wyłączenia (0 = anuluj):").pack(padx=10, pady=(10, 0))
    entry = tk.Entry(root, width=20)
    entry.pack(padx=10, pady=5)
    entry.focus()

    btn_frame = tk.Frame(root)
    btn_frame.pack(padx=10, pady=10)

    tk.Button(btn_frame, text="Zaplanuj", command=lambda: on_schedule(entry)).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Anuluj", command=on_cancel).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Status", command=on_status).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Wyjście", command=root.destroy).grid(row=0, column=3, padx=5)

    return root


def main() -> None:
    app = build_ui()
    app.mainloop()


if __name__ == "__main__":
    main()
    app = build_ui()
    app.mainloop()