#!/usr/bin/env python

# This script is intended to be run from within the Akai AX73 and VX90 MIDI Sysex Grammar file

# AX73 VX90 VCO Octave byte
#
# VCO Octave Labels 0-3

from enum import Enum
valueLabels = Enum('VCO Octave', '2\', 4\', 8\', 16\'', start=0)

def parseByteRange(element, byteView, bitPos, bitLength, results):
	# this method parses data starting at bitPos, bitLength bits are remaining
	"""parseByteRange method"""

	processedBytes = 0
	initialBitLow = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (initialBitLow == 0):

			# read bits
			result = byteView.readUnsignedIntBits(bitPos+1, 7, ENDIAN_BIG)

			# return value to results
			if (result < len(valueLabels)):
				value = Value()
				value.setString(str(result) + ": " + str(valueLabels(result).name))
				results.addElement(element, 1, 0, value)
				processedBytes = 1
			else:
				print("Value out of range (0-" + str(len(valueLabels)-1) + ")")

	return processedBytes

def fillByteRange(value, byteArray, bitPos, bitLength):
	# this method translates edited values back to the file
	"""fillByteRange method"""

	# get number edited by user
	number = value.getUnsigned()

	if (number < len(valueLabels)):
		byteArray.writeUnsignedIntBits(number, bitPos, 8, ENDIAN_BIG)
	else:
		print("Input value out of range (0-" + str(len(valueLabels)-1) + "). Value not updated.")
