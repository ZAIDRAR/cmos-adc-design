"""Ideal 2-bit flash ADC reference mapping (analytical model, not SPICE)."""

VREF = 4.0
BITS = 2

def quantize_ideal(vin: float, vref: float = VREF, bits: int = BITS) -> int:
    """Return unipolar code; clamp below zero and at/above reference."""
    if vref <= 0:
        raise ValueError("vref must be positive")
    if bits <= 0:
        raise ValueError("bits must be positive")
    n_codes = 1 << bits
    code = int(vin / (vref / n_codes))
    return min(n_codes - 1, max(0, code))

def thermometer_bits(vin: float) -> tuple[int, int, int]:
    """For 2-bit, 4V ADC return C3, C2, C1 for thresholds 3, 2, 1 V."""
    return tuple(int(vin >= threshold) for threshold in (3.0, 2.0, 1.0))

if __name__ == "__main__":
    print("Ideal 2-bit flash ADC, Vref=4V")
    print("Vin(V)  Thermometer  Binary")
    for vin in (0.0, 0.5, 1.0, 1.9, 2.0, 2.9, 3.0, 3.9, 4.0):
        therm = "".join(str(bit) for bit in thermometer_bits(vin))
        print(f"{vin:>5.1f}   {therm}          {quantize_ideal(vin):02b}")
