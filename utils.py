import struct

def AttrAccessor(function):
    return property(**function())

def rgb(rgb_bytes, size=None):
    if size is None:
        size = len(pallete_bytes)
    else:
        size *= 3

    numbers = struct.unpack('%dB' % size, rgb_bytes)
    return tuple(
        numbers[i:i + 3] for i in range(0, size - 1, 3)
        )


def indices(bytes, bytes_length=None):
    if bytes_length is None:
        bytes_length = len(bytes)

    return struct.unpack('%dB' % bytes_length, bytes)

def adjust_indices_bytes(pallete_bytes, width):
    result = ""
    
    alex_width = (width + 3) & -4
    gap = alex_width - width
    for i in range(0, len(pallete_bytes), width):
        result += pallete_bytes[i:i+width] + ('\0' * gap)
    return result
