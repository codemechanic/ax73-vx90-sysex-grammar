## AX73 VX90 Tauntek Firmware Notes<sup>[1](#tauntek)</sup>

When configuring a controller to use the CC's, assign parameters that map to just a few values to switches, NOT to sliders. Using a slider for something like the LFO waveform will send many identical requests to the synth as it it moved in-between the threshold values. The synth doesn't detect that the same option is being selected each time, so a lot of time may be wasted processing CC's that don't change anything. Also, in the case of something like the LFO waveform, the firmware may also reset certain LFO variables each time the waveform is selected, even if it was the same one that was already selected. This is because with the original controls there was no way to select the same option over and over again, and the firmware was not designed to handle this.

To save all patches via MIDI sysex, initiate a tape save. The sysex dump (exactly 5205 bytes) always contains all of the patches. After the MIDI data has been sent, the tape save operation will take place. This takes a while, so you may want to select just one bank for the tape save first.

1. TAPE
2. 0/Save
3. DOWN
4. 0/Save

should do it. That will only send bank 9 to the tape output.

To load the patches via MIDI, just send the sysex file back to the AX73, with Memory Protect off. Do not select TAPE mode. Just have the synth in normal operating mode. Note that loading the patches into RAM via sysex does not re-load the currently selected patch. You won't see any change on the display and the currently loaded patch will play as before, until you load it again, then you will get the new one.

Note: You may need to slow down the MIDI transfer some when sending the sysex to the AX73 or VX90. To do this in MIDI OX, set the buffer size to 1 and add a delay between buffers. Also, it's possible the MIDI pitch wheel messages could interfere with loading patches via sysex. Please ensure that nothing is placing these messages on the bus while you are loading a sysex patch file.

<sub><a name="tauntek">1.</a> The [PDF version of this information](http://www.tauntek.com/ax73ccmap.pdf) was written by R. Grieb March 28, 2021 and is available on the Tauntek website.</sub>
