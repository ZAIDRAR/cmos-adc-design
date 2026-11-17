# ADC and DAC Fundamentals

## ADC stages
Sampling, quantization, and binary encoding are conceptually distinct operations. A comparator-based flash ADC determines which thresholds the input crosses and then encodes the resulting thermometer code.

For an ideal unipolar \(N\)-bit converter over \(0 \le V_{IN} < V_{REF}\):

\[\Delta=\frac{V_{REF}}{2^N}\]

A 2-bit ADC with \(V_{REF}=4\,V\) has \(\Delta=1\,V\), four output codes and decision thresholds at 1, 2 and 3 V. Exact endpoint convention must always be stated.

## Flash converter
- \(2^N-1\) thresholds/comparators for a conventional flash ADC
- resistor-ladder reference voltages
- comparator thermometer outputs
- encoder mapping thermometer code to binary

## DAC concepts
An R-2R DAC forms an analog level from a binary code using a resistor network. Quantify reference voltage, code range, step size, output load and tolerance.

## Nonideal effects to investigate later
Input offset, comparator delay, reference variation, resistor mismatch, metastability, noise, INL/DNL, power and latency.

## CMOS distinction
An ideal comparator schematic demonstrates architecture. Transistor-level CMOS design requires a documented MOSFET model, transistor sizing, simulation, and nonideal performance analysis.
