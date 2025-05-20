import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import colorutilsqt


hex_color = "#3FAAFF"
h, s, l = colorutilsqt.converter.hex_to_hsl(hex_color)
print(f"HSL of {hex_color}: {h}, {s}%, {l}%")

new_hex = colorutilsqt.converter.hsl_to_hex(h, s, l)
print(f"Back to HEX: {new_hex}")

r, g, b = (63, 170, 255)
colorutilsqt.terminal.color_block_print(r, g, b)
colorutilsqt.terminal.color_print("Hello in color!", r, g, b)
colorutilsqt.terminal.fading_print("Lorem Ipsum", (255, 0, 20), (40, 60, 200))