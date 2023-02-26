# Akai AX73 VX90 Sysex Format<sup>[1](#tauntek)</sup>

The voice program block follows the 4 byte sysex header. Each voice program (patch) contains 40 ordered patch values of 1 byte each, followed by 12 ASCII bytes for the patch name. There are always 100 voice programs in the sysex file, with each patch taking up 52 bytes. The total size of the sysex is 5205 bytes.

**Header**
| Byte Index | Hex Value / Range | Description |
|-|-|-|
| 0 | F0 | Sysex Status byte (SOX) |
| 1 | 47 | Akai MIDI Manufacturer ID |
| 2 | 7B | Device ID, chosen at random |
| 3 | 73 | Product ID |

**Voice Program Data**
| Byte Index | Hex Value / Range | Description |
|-|-|-|
| 4 | 0-3 | VCO Octave (E00) |
| 5 | 0-3 | VCO Waveform (E01) |
| 6 | 0-64h | VCO Pulse Width (E02) |
| etc. | | |

**End of System Exclusive**
| Byte Index | Hex Value / Range | Description |
|-|-|-|
| 5204 | F7 | End of System Exclusive byte (EOX) |

<sub><a name="tauntek">1.</a> The [PDF version of this information](http://www.tauntek.com/ax73ccmap.pdf) was written by R. Grieb March 28, 2021 and is available on the [Tauntek](http://tauntek.com) website.</sub>
