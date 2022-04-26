# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.

def rgb(r, g, b):
    # your code here :)
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    return "{:02X}{:02X}{:02X}".format(r, g, b)
