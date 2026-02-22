import os
_shutdown_seconds: int | None = None

def minutes_to_seconds(minutes: int) -> int:
    # Funkcja konwertuje minuty na sekundy
    if minutes < 0:
        raise ValueError("Liczba minut nie może być ujemna.")
    return minutes * 60


def shutdown_schedule(seconds: int) -> None:
    # Funkcja planuje wyłączenie komputera po określonym czasie
    global _shutdown_seconds
    if seconds <= 0:
        raise ValueError("Liczba sekund musi być > 0.")
    os.system(f"shutdown -s -t {seconds}")
    _shutdown_seconds = seconds


def shutdown_cancel() -> None:
    # Funkcja anuluje zaplanowane wyłączenie komputera
    global _shutdown_seconds
    os.system("shutdown -a")
    _shutdown_seconds = None


def shutdown_status() -> str:
    # Funkcja sprawdza status zaplanowanego wyłączenia komputera
    if _shutdown_seconds is None:
        return "Brak zaplanowanego wyłączenia."
    return f"Zaplanowano wyłączenie za {_shutdown_seconds} sekund."