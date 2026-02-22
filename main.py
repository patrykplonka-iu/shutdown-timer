import tkinter as tk
import engine
from tkinter import messagebox


def main() -> None:
    root = tk.Tk()
    root.title("Czasowy Wyłącznik Komputera")
    root.geometry("350x150")

    label = tk.Label(root, text="Podaj minuty i kliknij 'Zaplanuj'.")
    label.pack(pady=10)

    entry_minutes = tk.Entry(root)
    entry_minutes.pack()
    status_label = tk.Label(root, text="Status: czekam na akcję.")
    status_label.pack(pady=5)

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    button_schedule = tk.Button(
        buttons_frame,
        text="Zaplanuj",
        command=lambda: print("Zaplanowano wyłączenie")
    )

    def on_schedule_click():
        text = entry_minutes.get().strip()
        try:
            minutes = int(text)
        except ValueError:
            status_label.config(text="Błąd: wpisz liczbę całkowitą (np. 10).")
            return
        
        if minutes < 1:
            status_label.config(text="Błąd: liczba minut musi być większa lub równa 1.")
            return

        confirm = messagebox.askyesno(
            "Potwierdzenie",
            f"Czy na pewno chcesz zaplanować wyłączenie komputera za {minutes} minut?"
        )
        if not confirm:
            status_label.config(text="Anulowano przez użytkownika.")
            return
        else:
            engine.shutdown_schedule(engine.minutes_to_seconds(minutes))
            
        seconds = engine.minutes_to_seconds(minutes)
        status_label.config(text=f"OK: {minutes} min = {seconds} s")
        entry_minutes.delete(0, tk.END)


    button_schedule.config(command=on_schedule_click)

    button_schedule.pack(side=tk.LEFT, padx=5)

    def on_cancel_click():
        engine.shutdown_cancel()
        status_label.config(text="OK: anulowano zaplanowane wyłączenie (jeśli było).")

    button_cancel = tk.Button(
        buttons_frame,
        text="Anuluj",
        command=on_cancel_click
    )
    button_cancel.pack(side=tk.LEFT, padx=5)

    def on_status_click():
        msg = engine.shutdown_status()
        status_label.config(text=f"Status: {msg}", wraplength=340)

    button_status = tk.Button(
        buttons_frame,
        text="Status",
        command=on_status_click
    )
    button_status.pack(side=tk.LEFT, padx=5)


    root.mainloop()

if __name__ == "__main__":
    main()
