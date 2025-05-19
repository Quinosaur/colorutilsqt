def print_color_block(r, g, b):
    print(f"\033[48;2;{r};{g};{b}m   \033[0m RGB({r},{g},{b})")

def print_colored_text(text, r, g, b):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")
