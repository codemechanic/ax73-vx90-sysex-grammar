#!/usr/bin/env python

# This script is intended to be run from within the Akai AX73 and VX90 MIDI Sysex Grammar file

# AX73 VX90 50 signed
#
# -50 to 50

maxNum = 50
minNum = 0 - maxNum

def toSignedInt(number, modifier):
	number = int(number) - int(modifier)
	return number

def toUnsignedInt(number, modifier):
	number = int(number) + int(modifier)
	return number

def parseByteRange(element, byteView, bitPos, bitLength, results):
	# this method parses data starting at bitPos, bitLength bits are remaining
	"""parseByteRange method"""

	processedBytes = 0
	initialBitLow = byteView.readUnsignedIntBits(bitPos, 1, ENDIAN_BIG)

	if (initialBitLow == 0):

			# read bits
			result = byteView.readUnsignedIntBits(bitPos+1, 7, ENDIAN_BIG)
			result = toSignedInt(result, maxNum)

			# return value to results
			if (result >= minNum and result <= maxNum):
				value = Value()
				value.setString(str(result))
				results.addElement(element, 1, 0, value)
				processedBytes = 1
			else:
				print("Value out of range (" + str(minNum) + "-" + str(maxNum) + ")")

	return processedBytes

def fillByteRange(value, byteArray, bitPos, bitLength):
	# this method translates edited values back to the file
	"""fillByteRange method"""

	bytePos = bitPos/8

	number = value.getString()
	converted = toUnsignedInt(number, maxNum)

	if (abs(int(number)) <= maxNum):
		byteArray.writeUnsignedInt(converted, bytePos, 1, ENDIAN_BIG)
	else:
		print("Input value out of range (" + str(minNum) + "-" + str(maxNum) + "). Value not updated.")
