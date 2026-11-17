# ADC/DAC Architecture and CMOS Circuit Design

**Status:** Educational project initialized. No circuit simulations or measurements have yet been verified.

This repository studies how analog signals are converted to digital representations and how mixed-signal converter blocks can be implemented. It is part of [my semiconductor learning portfolio](https://github.com/ZAIDRAR/semiconductor-learning-journey).

## Initial objective
Understand and simulate a **2-bit flash ADC** at architecture level, then progress toward transistor-level CMOS comparator implementation.

### Learning stages
| Stage | Project | Status |
|---|---|---|
| 1 | Ideal 2-bit flash ADC, resistor ladder, comparators and encoder | Planned |
| 2 | 4-bit R-2R DAC and static transfer characteristic | Planned |
| 3 | Comparator with hysteresis and nonideal effects | Planned |
| 4 | Transistor-level CMOS comparator (model-dependent) | Planned |
| 5 | SAR ADC architecture and performance | Future |

## Repository folders
- [theory](theory/README.md): converter equations and concepts
- [experiments](experiments/README.md): reproducible plans
- [circuits](circuits/README.md): original LTspice `.asc` schematics when built
- [scripts](scripts/README.md): Python reference model
- [data](data/README.md): measured or exported numerical values
- [plots](plots/README.md): verified graphs
- [reports](reports/report-template.md): lab report template
- [docs](docs/architecture.md): flash ADC block architecture

## First experiment
Follow [Experiment 01 — ideal 2-bit flash ADC](experiments/01-flash-adc-2bit.md). Choose \(V_{REF}=4\,V\), giving nominal decision thresholds of 1, 2, and 3 V for an ideal 2-bit unipolar flash converter over the interval \([0,4)\,V\).

Use [scripts/ideal_flash_adc.py](scripts/ideal_flash_adc.py) for an analytical **reference** code mapping. This is not a SPICE circuit simulation.

## Next step
Build your own comparator/resistor-ladder schematic in LTspice, test it, and upload the actual `.asc` file and measured outputs. An ideal comparator design is **not yet transistor-level CMOS IC design**.

## References
- [LTspice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)
- [ngspice](https://ngspice.sourceforge.io/)
