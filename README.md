# Akai AX73 and VX90 MIDI System Exclusive (Sysex) Grammar

![Akai AX73 screenshot](https://github.com/codemechanic/ax73-vx90-sysex-grammar/blob/main/images/ax73pic40.jpg?raw=true)

This grammar file maps the structure of the MIDI System Exclusive File Format for the [Akai](https://en.wikipedia.org/wiki/OSC_OSCar), and is based on the generic [MIDI System Exclusive (Sysex) Grammar](https://github.com/codemechanic/midi-sysex-grammar).

The Akai AX73 is a six voice analog synthesizers released in 1986 (the VX90 is the rack mount version). The AX73 included voltage controlled analog oscillators (VCO) as opposed to the more common digitally controlled analog oscillators (DCO) of the time. The AX73 and VX90 have the ability to interface with Akai's S900 and S950 samplers, and the AX73 supports keyboard "splitting" while the VX90 does not.

Grammar files provide an interface for editing and translating human readable values to and from the binary file, and are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows. Grammars are stored as XML, support both Python and Lua scripting languages, and can export to C structs as well as inherit structures from object oriented languages.

The grammar files provided here are used for interpreting Non Real Time Universal System Exclusive Messages.


## Useage

The files found in this repository are intended to be used in conjunction with the [Tauntek AX73 firmware](http://www.tauntek.com/AX73.htm). Analyzing AX73 Sysex is possible without the firmware, however loading the AX73 Sysex over MIDI requires that the Tauntek firmware is installed.

1. Download the [akai_ax73_vx90_sysex.grammar](https://github.com/codemechanic/ax73-vx90-sysex-grammar/blob/main/grammar/ax73-vx90-sysex.grammar?raw=true) and open the grammar with Synalize It! or Hexinator.
2. Open an Akai AX73 or VX90 MIDI Sysex file. If you don't have one available you can download the [factory OSCar Sysex file](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatch_Wavetable.syx?raw=true) that is provided as a part of this repository.
3. Apply the MIDI Sysex grammar to the Sysex file.


![AX73 Sysex screenshot](https://github.com/codemechanic/ax73-vx90-sysex-grammar/blob/main/images/screenshot_1.png?raw=true)


## Tauntek firmware

Bob Grieb of [Tauntek](http://tauntek.com) has released a new  [firmware image for the AX73 and VX90](http://www.tauntek.com/AX73.htm) that brings these synths up to date and allows patch data to be exported over MIDI, rather than as audio. The Tauntek firmware also enables MIDI CC parameter changes over MIDI as well.

**Improvements:**
1. Save and Load patch data as MIDI Sysex.
2. MIDI CC reception for parameter changes.


## Tauntek MIDI CC Parameter Assignments

| CC Dec | CC Hex | Midi 2.0 Function | AX73 Ref | AX73 Function | AX73 Value Notes |
| - | - | - | - | - | - |
| 0 | 0 | Bank Select (MSB) | | | |
| 1 | 1 | Modulation Wheel (MSB) | | Mod wheel | Handled by original AX73 code |
| 2 | 2 | Breath Controller (MSB) | | | |
| 3 | 3 | | | | |
| 4 | 4 | Foot Controller (MSB) | | | |
| 5 | 5 | Portamento Time (MSB) | | | |
| 6 | 6 | Data Entry (MSB) | | | |
| 7 | 7 | Channel Volume (MSB) | | Volume | Handled by original AX73 code using VCA EG depth |
| 8 | 8 | Balance (MSB) | | | |
| 9 | 9 | | | | |
| 10 | 0A | Pan (MSB) | | | |
| 11 | 0B | Expression (MSB) | | | |
| 12 | 0C | Effect Control 1 (MSB) | | | |
| 13 | 0D | Effect Control 2 (MSB) | | | |
| 14 | 0E | | E00 | VCO Octave | 0-31: 16', 32-63: 8', 64-95: 4', 96-127: 2' |
| 15 | 0F | | E01 | VCO waveform | 0-31: Saw, 32-63: Tri, 64-95: Pulse, 96-127 Saw+Tri |
| 16 | 10 | General Purpose Controller 1 (MSB) | E02 | VCO Pulse Width | 0-127 |
| 17 | 11 | General Purpose Controller 2 (MSB) | E03 | VCO PWMS | 0-127 |
| 18 | 12 | General Purpose Controller 3 (MSB) | E04 | VCO EG Depth | 0-127 |
| 19 | 13 | General Purpose Controller 4 (MSB) | E05 | Noise on/off | 0-63: Noise Off, 64-127: Noise On |
| 20 | 14 | | E06 | Sampler Enable | 0-63: Sampler not enabled, 64-127: Sampler Enabled |
| 21 | 15 | | E07 | A/B Balance | 0-127 |
| 22 | 16 | | E12 | VCF OWFM | 0-127 |
| 23 | 17 | | E13 | VCF EG Depth/Pol | 0-127 0: -50, 64: 0, 127: +50 |
| 24 | 18 | | E14 | VCF Key Follow | 0-127 |
| 25 | 19 | | E15 | VCF Velo | 0: -50, 64: 0, 127: +50 |
| 26 | 1A | | E16 | HPF | 0-127 |
| 27 | 1B | | E20 | EG Sel | 0-63: Filter uses EGA, 64-127: Filter uses EGO |
| 28 | 1C | | E22 | EGA Decay | 0-127 VCA always uses this EG |
| 29 | 1D | | E23 | EGA Sustain | 0-127 |
| 30 | 1E | | E25 | EGO Attack | 0-127 VCO always uses this EG |
| 31 | 1F | | E26 | EGO Decay | 0-127 |
| 32 | 20 | Bank Select (LSB) | E27 | EGO Sustain | 0-127 |
| 33 | 21 | Modulation Wheel (LSB) | E28 | EGO Release 0-127 | 0-127 |
| 34 | 22 | Breath Controller (LSB) | E30 | VCA Level | 0-127 |
| 35 | 23 | | E31 | VCA Velo | 0-127 0: -50, 64: 0, 127: +50 |
| 36 | 24 | Foot Controller (LSB) | E40 | LFO destination | 0-31: Off, 32-63: VCO, 64-95: VCF, 96-127: VCA |
| 37 | 25 | Portamento Time (LSB) | E41 | LFO waveform | 0-24: DnSaw, 25-49: UpSaw, 50-74: Tri, 75-99: Square, 100-127: Random |
| 38 | 26 | Data Entry (LSB) | E42 | LFO freq | 0-127 |
| 39 | 27 | Channel Volume (LSB) | E43 | LFO depth | 0-127 |
| 40 | 28 | Balance (LSB) | E44 | LFO delay | 0-127 |
| 41 | 29 | | E45 | Chorus | 0-42: Chorus off, 43-85: Mode 1, 86-127: Mode 2 |
| 42 | 2A | Pan (LSB) | E50 | Assign | 0-42: Poly, 43-85: Dual, 86-127: Unison |
| 43 | 2B | Expression (LSB) | E51 | Sol Port | 0-127 |
| 44 | 2C | Effect Control 1 (LSB) | E52 | Detune | 0-127 |
| 45 | 2D | Effect Control 2 (LSB) | E60 | Wh Bnd O  | 0-127 mapped to 0-12 |
| 46 | 2E | | E61 | Wh Bnd F  | 0-127 |
| 47 | 2F | | E62 | Wh Mod | 0-127 |
| 48 | 30 | General Purpose Controller 1 (LSB) | E70 | MIDI SP | 0-42: Off, 43-85: Upp, 86-127: Low |
| 49 | 31 | General Purpose Controller 2 (LSB) | | | |
| 50 | 32 | General Purpose Controller 3 (LSB) | | | |
| 51 | 33 | General Purpose Controller 4 (LSB) | | | |
| 52 | 34 | | | | |
| 53 | 35 | | | | |
| 54 | 36 | | | | |
| 55 | 37 | | | | |
| 56 | 38 | | | | |
| 57 | 39 | | | | |
| 58 | 3A | | | | |
| 59 | 3B | | | | |
| 60 | 3C | | | | |
| 61 | 3D | | | | |
| 62 | 3E | | | | |
| 63 | 3F | | | | |
| 64 | 40 | Sustain Pedal | | Sustain | 0-127 Sustain pedal, handled by original AX73 code |
| 65 | 41 | Portamento On/Off | | | |
| 66 | 42 | Sostenuto | | | |
| 67 | 43 | Soft Pedal | | | |
| 68 | 44 | Legato Footswitch | | | |
| 69 | 45 | Hold 2 | | | |
| 70 | 46 | Sound Controller 1 (default: Sound Variation) | | | |
| 71 | 47 | Sound Controller 2 (default: Timbre / Harmonic Quality) | E11 | VCF Resonance | 0-127 |
| 72 | 48 | Sound Controller 3 (default: Release Time) | E24 | VCA Release | 0-127 |
| 73 | 49 | Sound Controller 4 (default: Attack Time) | E21 | VCA Attack | 0-127 |
| 74 | 4A | Sound Controller 5 (default: Brightness) | E10 | VCF Cutoff | 0-127 |
| 75 | 4B | Sound Controller 6 (GM2 default: Decay Time) | | | |
| 76 | 4C | Sound Controller 7 (GM2 default: Vibrato Rate) | | | |
| 77 | 4D | Sound Controller 8 (GM2 default: Vibrato Depth) | | | |
| 78 | 4E | Sound Controller 9 (GM2 default: Vibrato Delay) | | | |
| 79 | 4F | Sound Controller 10 (GM2 default: Undefined) | | | |
| 80 | 50 | General Purpose Controller 5 | | | |
| 81 | 51 | General Purpose Controller 6 | | | |
| 82 | 52 | General Purpose Controller 7 | | | |
| 83 | 53 | General Purpose Controller 8 | | | |
| 84 | 54 | Portamento Control | | | |
| 85 | 55 | | | | |
| 86 | 56 | | | | |
| 87 | 57 | | | | |
| 88 | 58 | | | | |
| 89 | 59 | | | | |
| 90 | 5A | | | | |
| 91 | 5B | Effects 1 Depth (default: Reverb Send) | | | |
| 92 | 5C | Effects 2 Depth (default: Tremolo Depth) | | | |
| 93 | 5D | Effects 3 Depth (default: Chorus Send) | | | |
| 94 | 5E | Effects 4 Depth (default: Celeste [Detune] Depth) | | | |
| 95 | 5F | Effects 5 Depth (default: Phaser Depth) | | | |
| 96 | 60 | Data Increment | | | |
| 97 | 61 | Data Decrement | | | |
| 98 | 62 | Non-Registered Parameter Number (LSB) | | | |
| 99 | 63 | Non-Registered Parameter Number (MSB) | | | |
| 100 | 64 | Registered Parameter Number (LSB) | | | |
| 101 | 65 | Registered Parameter Number (MSB) | | | |
| 102 | 66 | | | | |
| 103 | 67 | | | | |
| 104 | 68 | | | | |
| 105 | 69 | | | | |
| 106 | 6A | | | | |
| 107 | 6B | | | | |
| 108 | 6C | | | | |
| 109 | 6D | | | | |
| 110 | 6E | | | | |
| 111 | 6F | | | | |
| 112 | 70 | | | | |
| 113 | 71 | | | | |
| 114 | 72 | | | | |
| 115 | 73 | | | | |
| 116 | 74 | | | | |
| 117 | 75 | | | | |
| 118 | 76 | | | | |
| 119 | 77 | | | | |
| 120 | 78 | All Sound Off | | | |
| 121 | 79 | Reset All Controllers | | | |
| 122 | 7A | Local Control On/Off | | | |
| 123 | 7B | All Notes Off | | All notes off | Value not used, handled by original AX60 code |
| 124 | 7C | Omni Mode Off | | | |
| 125 | 7D | Omni Mode On | | | |
| 126 | 7E | Poly Mode Off | | | |
| 127 | 7F | Poly Mode On | | | |

* These values are also provided on the Tauntek website as [ax73ccmap.pdf](http://www.tauntek.com/ax73ccmap.pdf)

## Known patch names

| Number | Name |
|-|-|
| 1 | Sample Patch |

## Todo
* Stuff

## Special Thanks
* Bob Grieb for authoring the updated firmware for the Akai AX73 and VX90
