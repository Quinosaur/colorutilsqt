import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pycolortools


hex_color = "#3FAAFF"
h, s, l = pycolortools.converter.hex_to_hsl(hex_color)
print(f"HSL van {hex_color}: {h}, {s}%, {l}%")

new_hex = pycolortools.converter.hsl_to_hex(h, s, l)
print(f"Terug naar HEX: {new_hex}")

r, g, b = (63, 170, 255)
pycolortools.terminal.print_color_block(r, g, b)
pycolortools.terminal.print_colored_text("Hallo in kleur!", r, g, b)
