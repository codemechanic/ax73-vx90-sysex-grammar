## Akai AX73 VX90 Tauntek Firmware Notes<sup>[1](#tauntek)</sup>

When configuring a controller to use the [MIDI CCs](../docs/ax73_vx90_midi_cc.md), assign CCs like the 2 and 4 parameter CCs to switches, NOT to sliders. Using a slider for something like the LFO Waveform will send duplicate requests to the synth as the slider is moved between its threshold values. The synthesizer doesn't detect that the same option is being selected each time, and CPU resources will be wasted processing control changes that don't actually change anything. Also, in the case of something like the LFO Waveform, the firmware may also reset certain LFO variables each time the waveform is selected, even if it was the same one that was already selected. This is because with the original controls there was no way to select the same option over and over again, and the firmware was not designed to handle this.

To save all patches via MIDI sysex, initiate a tape save. The [sysex dump (exactly 5205 bytes)](../docs/ax73_vx90_sysex_format.md) always contains all of the patches. After the MIDI data has been sent, the tape save operation will take place. It can take awhile to save out all 10 banks over the tape output. You can save time by selecting just one bank prior to initiating the tape save.

```
1. TAPE
2. 0/Save
3. DOWN
4. 0/Save
```

should do it. That will only send bank 9 to the tape output.

To load the patches via MIDI, just send the sysex file back to the AX73 with Memory Protect off. Do not select TAPE mode. Just have the synth in normal operating mode. Note that loading the patches into RAM via sysex does not refresh the currently selected patch. You won't see any change on the display and the currently loaded patch will play as before, until you load it again, then you will get the new one.

**Note:** You may need to slow down the MIDI transfer when sending the sysex to the AX73 or VX90. To do this in MIDI OX, set the buffer size to 1 and add a delay between buffers. Also, it's possible the MIDI pitch wheel messages could interfere with loading patches via sysex. Please ensure that nothing is sending these messages when you are loading a sysex patch file.

<sub><a name="tauntek">1.</a> The [PDF version of this information](http://www.tauntek.com/ax73ccmap.pdf) was written by R. Grieb March 28, 2021 and is available on the [Tauntek](http://tauntek.com) website.</sub>
