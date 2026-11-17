# Ideal Two-Bit Flash ADC Architecture

Signal path:

```text
Analog input VIN ───────┬── comparator VIN >= 3V ─┐
                        ├── comparator VIN >= 2V ─┤── thermometer encoder ── 2-bit code
                        └── comparator VIN >= 1V ─┘
Reference 4V ── resistor ladder ── 1V / 2V / 3V
```

## Truth table (ideal convention)

| Input range | C3 C2 C1 | Binary output |
|---|---|---|
| 0 <= VIN < 1 V | 000 | 00 |
| 1 <= VIN < 2 V | 001 | 01 |
| 2 <= VIN < 3 V | 011 | 10 |
| 3 <= VIN <= 4 V | 111 | 11 |

Comparator output is 1 when VIN is greater than or equal to its threshold. At voltages above the reference, this ideal demonstration saturates at code 11.

## Questions to investigate
1. How do comparator input offsets shift transition voltages?
2. How does resistor mismatch affect threshold spacing?
3. How can asynchronous switching cause transient invalid thermometer codes?
4. What additional circuitry is needed for a practical clocked ADC?
