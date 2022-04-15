def double_char(s: str) -> str:
    return "".join(l*2 for l in s)

print(double_char("Hello"))