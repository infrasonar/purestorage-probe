def opt_int(inp: int | float | None):
    return None if inp is None else int(inp)


def opt_sorted(inp: list | None) -> list | None:
    return None if inp is None else sorted(inp)
