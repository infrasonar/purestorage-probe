def opt_float(inp: int | float | None):
    return None if inp is None else float(inp)


def opt_sorted(inp: list | None) -> list | None:
    return None if inp is None else sorted(inp)


def opt_ms_to_sec(ts: int | None) -> int | None:
    if ts is None:
        return
    return ts // 1000
