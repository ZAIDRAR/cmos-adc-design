# Experiment 01 — Ideal Two-Bit Flash ADC

**Status:** Planned

## Objective
Create and validate a 2-bit flash ADC architecture using a reference ladder, three comparators and a thermometer-to-binary encoder.

## Planned setup
- Reference voltage: 4 V
- Nominal thresholds: 1 V, 2 V and 3 V
- Input stimulus: slow DC sweep from 0 V to 4 V
- Outputs: comparator thermometer bits and binary code

## Steps
1. Calculate thresholds from the reference ladder.
2. Draw the comparator bank and verify input polarities.
3. Choose documented comparator models or behavioral comparators in LTspice.
4. Implement thermometer-to-binary encoding and explain any logic thresholds/logic models used.
5. Apply a slow DC sweep or ramp and plot the input voltage and code transitions.
6. Compare the code against the Python reference model.
7. Explain limitations of ideal comparators, switching delay and real-world logic interfacing.

## Evidence to upload
- Original `.asc` schematic and any model files allowed by license
- Input waveform, comparator outputs and binary outputs
- Measured threshold values and simulation version
- Report comparing observed and predicted code boundaries

No completed circuit, waveforms or results are claimed by this document.
