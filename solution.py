from pathlib import Path
from typing import List

def parse_trace_lines(filename: str = "trace.txt") -> List[List[str]]:
    """
    Parse lines from `trace.txt` into separate elements.

    Each non-empty line is split on whitespace, producing a list[str].
    The overall return value is a list of these per-line lists.

    Example line:
        "A START: 990000"  ->  ["A", "START:", "990000"]

    Parameters
    ----------
    filename : str
        Path to the trace file (default: "trace.txt" in the same directory).

    Returns
    -------
    List[List[str]]
        One list of string elements per input line.
    """
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"Trace file not found: {path.resolve()}")

    rows: List[List[str]] = []
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            rows.append(line.split())

    return rows


if __name__ == "__main__":
    tokens_per_line = parse_trace_lines("trace.txt")

    # Print all the parsed lines
    for row in tokens_per_line:
        print(row)
