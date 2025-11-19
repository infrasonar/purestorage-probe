def opt_float(inp: int | float | None):
    return None if inp is None else float(inp)


def opt_sorted(inp: list | None) -> list | None:
    return None if inp is None else sorted(inp)
