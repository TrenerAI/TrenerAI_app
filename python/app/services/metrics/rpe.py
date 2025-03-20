def calculate_rpe(rir: int) -> int:
    """Oblicza RPE na podstawie liczby rezerwowych powtórzeń (RIR)."""
    if rir < 0:
        raise ValueError("RIR nie może być ujemny!")
    return max(1, min(10, 10 - rir))
