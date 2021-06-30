# Akai AX73 and VX90 MIDI System Exclusive (Sysex) Grammar

![Akai AX73 screenshot](https://github.com/codemechanic/ax73-vx90-sysex-grammar/blob/main/images/ax73pic40.jpg?raw=true)

The Akai AX73 and VX90 are six voice analog synthesizers released in 1986 (the VX90 is the rack mount version of the AX73). They used voltage controlled analog oscillators (VCO) as opposed to the more common digitally controlled analog oscillators (DCO) of the time. The AX73 and VX90 have the ability to interface with Akai's samplers (S612, S700, S900, and S950) using a 13 pin DIN sampler connect cable (Akai DD-X5013). Both the AX73 and VX90 run the same OS and firmware EPROM, with the only difference being that the AX73 allows a keyboard "split", while the VX90 does not.

This grammar file maps the structure of the MIDI System Exclusive File Format for the [Akai AX73 and VX90](https://en.wikipedia.org/wiki/Akai#AX_series_analog_synthesizers), and is based on the generic [MIDI System Exclusive (Sysex) Grammar](https://github.com/codemechanic/midi-sysex-grammar).

Grammar files provide an interface for editing and translating human readable values to and from the binary file, and are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows. Grammars are stored as XML, support both Python and Lua scripting languages, and can export to C structs as well as inherit structures from object oriented languages.

The grammar files provided here are used for interpreting Non Real Time Universal System Exclusive Messages.

## Tauntek firmware

Bob Grieb of [Tauntek](http://tauntek.com) has released a new  [firmware image for the AX73 and VX90](http://www.tauntek.com/AX73.htm) that brings these synths up to date and enables reception of MIDI CC parameter changes. Patch data can also be loaded and saved over MIDI rather than relying on the dedicated Cassette Tape outputs.

**Improvements:**
1. Reception of MIDI continuous controller (CC) data
2. Save and Load patch data as MIDI Sysex

## Useage

The files found in this repository are intended to be used in conjunction with the [Tauntek AX73 firmware](http://www.tauntek.com/AX73.htm). Analyzing AX73 Sysex is possible without the firmware, however loading the AX73 Sysex over MIDI requires that you have the Tauntek firmware installed.

1. Download the [akai_ax73_vx90_sysex.grammar](https://github.com/codemechanic/ax73-vx90-sysex-grammar/blob/main/grammar/ax73-vx90-sysex.grammar?raw=true) and open the grammar with Synalize It! or Hexinator.
2. Open an Akai AX73 or VX90 MIDI Sysex file. If you don't have one available you can download the [factory OSCar Sysex file](https://github.com/codemechanic/oscar-sysex-grammar/blob/main/sysex/factory/FactoryPatch_Wavetable.syx?raw=true) that is provided as a part of this repository.
3. Apply the MIDI Sysex grammar to the Sysex file.

![AX73 Sysex screenshot](https://github.com/codemechanic/ax73-vx90-sysex-grammar/blob/main/images/screenshot_1.png?raw=true)

## Details and Charts
* [Tauntek MIDI CC Chart](./manual/AX73_VX90_MIDI_CC.md)
* [AX73 and VX90 Voice Chart](./manual/AX73_VX90_voice_chart.md)
* [Roland GK-13 13-pin DIN guitar cable](./manual/GR15_cable_details.md)

## Special Thanks
* Bob Grieb for creating the updated firmware for the Akai AX73 and VX90
