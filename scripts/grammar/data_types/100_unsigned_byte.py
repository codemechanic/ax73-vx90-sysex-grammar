#!/usr/bin/env python

# This script is intended to be run from within the Akai AX73 and VX90 MIDI Sysex Grammar file

# AX73 VX90 100 unsigned
#
# 0 to 100

maxNum = 100

def parseByteRange(element, byteView, bitPos, bitLength, results):
	# this method parses data starting at bitPos, bitLength bits are remaining
	"""parseByteRange method"""

	processedBytes = 0
	initialBitLow = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (initialBitLow == 0):

			# read bits
			result = byteView.readUnsignedIntBits(bitPos+1, 7, ENDIAN_BIG)

			# return value to results
			if (result <= maxNum):
				value = Value()
				value.setString(str(result))
				results.addElement(element, 1, 0, value)
				processedBytes = 1
			else:
				print("Value out of range (0-" + str(maxNum) + ")")

	return processedBytes

def fillByteRange(value, byteArray, bitPos, bitLength):
	# this method translates edited values back to the file
	"""fillByteRange method"""

	bytePos = bitPos/8

	# get number edited by user
	number = value.getUnsigned()

	if (number <= maxNum):
		byteArray.replaceByte(bytePos, number)
	else:
		print("Input value out of range (0-" + str(maxNum) + "). Value not updated.")
