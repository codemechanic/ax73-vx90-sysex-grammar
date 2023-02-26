# Akai AX73 and VX90 MIDI System Exclusive (Sysex) Grammar

![Akai AX73 screenshot](./images/ax73_transparent.png?raw=true)

The **Akai AX73** and **VX90** are six voice analog synthesizers released in 1986, with the VX90 being the rack mount version of the AX73. They used voltage controlled analog oscillators or VCOs as opposed to the more common digitally controlled analog oscillators or DCOs of the time. The AX73 and VX90 have the ability to interface with the Akai S612, S700, S900, and S950 samplers using an Akai DD-X5013 or 13 pin DIN sampler connect cable. Both the AX73 and VX90 run the same operating system and firmware EPROM, with the only difference between the two being how the keyboard "split" is handled.

The grammar files provided here map the structure of the MIDI System Exclusive File Format for the [Akai AX73 and VX90](https://en.wikipedia.org/wiki/Akai#AX_series_analog_synthesizers), and are based on the generic [MIDI System Exclusive (Sysex) Grammar](https://github.com/codemechanic/midi-sysex-grammar). These files are useful for interpreting Non Real Time Universal System Exclusive Messages.

Grammar files provide an interface for editing and translating human readable values to and from the binary file, and are used in conjunction with the hex and binary file analysis tools [Synalize It!](https://www.synalysis.net) on macOS and [Hexinator](https://hexinator.com) on Windows. Grammars are stored as XML, support both Python and Lua scripting languages, and can export to C structs as well as inherit structures from object oriented languages.

## Tauntek Firmware

[Tauntek](http://tauntek.com) has released a new [firmware image for the AX73 and VX90](http://www.tauntek.com/AX73.htm) that enables reception of [MIDI CC parameter changes](./docs/ax73_vx90_midi_cc.md). Patch data can also be loaded and saved over MIDI rather than relying on the dedicated cassette tape outputs.

**Improvements:**
1. Reception of [MIDI continuous controller (CC)](./docs/ax73_vx90_midi_cc.md) data
2. Save and Load patch data as MIDI Sysex

For more information on using the Tauntek firmware and assigning MIDI controller data, please refer to the [firmware notes](./docs/ax73_vx90_tauntek_notes.md) included here, or the [PDF version](http://www.tauntek.com/ax73ccmap.pdf) available on the Tauntek website.

## Useage

The files found here are intended to be used in conjunction with the [Tauntek AX73 firmware](http://www.tauntek.com/AX73.htm). Analyzing AX73 and VX90 Sysex is possible without the firmware, however controlling those synths with Midi CCs and/or loading or saving Sysex over MIDI requires that you have the Tauntek firmware installed.

1. Download the [akai_ax73_vx90_sysex.grammar](./grammar/ax73_vx90_sysex.grammar?raw=true) and open the grammar with Synalize It! or Hexinator.
2. Open an Akai AX73 or VX90 MIDI Sysex file. If you don't have one available you can download the [AX73 Sysex files](./sysex/factory/FactoryPatch_Wavetable.syx?raw=true) that are provided as a part of this repository.
3. Apply the MIDI Sysex grammar to the Sysex file.

![AX73 Sysex screenshot](./images/screenshot_1.png?raw=true)

## Documentation and Charts
* [Akai AX73 VX90 Sysex Format](./docs/ax73_vx90_sysex_format.md)
* [Akai AX73 and VX90 Voice Chart](./docs/ax73_vx90_voice_chart.md)
* [Akai DD-X5013 and Roland GK-13 13-pin DIN cables](./docs/ddx5013_and_gr15_din_cables.md)
* [Tauntek AX73 and VX90 MIDI CC Chart](./docs/ax73_vx90_midi_cc.md)
* [Tauntek AX73 and VX90 Firmware Notes](./docs/ax73_vx90_tauntek_notes.md)

## Special Thanks
* Bob Grieb and [Tauntek](http://tauntek.com) for authoring the updated firmware for the Akai AX73 and VX90.
