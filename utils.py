"""NickBypassBot // utilities.

Pure presentation helpers. Nothing here touches the network, the filesystem
outside of stdout, or any secret. It is all fake UI to make the prank feel
over-engineered.
"""

from __future__ import annotations

import random
import sys
import time

# Deterministic-but-noisy bytes used to make the "decryption" output look
# convincing. Same input -> same noise, so the prank is reproducible.
_HEX = "0123456789abcdef"
_BINS = "01"


def clear_line() -> None:
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()


def fake_progress(label: str, total: int = 30, delay: float = 0.04) -> None:
    """Print an animated progress bar that looks important and does nothing."""
    bar_width = 32
    for i in range(total + 1):
        pct = int((i / total) * 100)
        filled = int((i / total) * bar_width)
        bar = "#" * filled + "-" * (bar_width - filled)
        clear_line()
        sys.stdout.write(f"  {label} [{bar}] {pct:3d}%")
        sys.stdout.flush()
        # tiny jitter so it feels "real"
        time.sleep(delay + random.uniform(0, 0.02))
    sys.stdout.write("\n")


def hex_dump(lines: int = 6, width: int = 39) -> None:
    """Spit out a wall of fake hex that looks like a memory dump."""
    for _ in range(lines):
        row = "".join(random.choice(_HEX) for _ in range(width))
        sys.stdout.write(f"  0x{random.randint(0x1000, 0xFFFF):04x}  {row}\n")
    sys.stdout.flush()


def binary_rain(lines: int = 4, width: int = 48) -> None:
    """A little matrix-ish binary flicker for flavor."""
    for _ in range(lines):
        row = "".join(random.choice(_BINS) for _ in range(width))
        sys.stdout.write(f"  {row}\n")
        time.sleep(0.03)
    sys.stdout.flush()


def spinner(text: str, seconds: float = 1.2) -> None:
    """A classic CLI spinner that spins for a bit and stops."""
    frames = "|/-\\"
    end = time.time() + seconds
    i = 0
    while time.time() < end:
        clear_line()
        sys.stdout.write(f"  {text} {frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(0.06)
        i += 1
    clear_line()
    sys.stdout.write(f"  {text} done\n")


def banner(text: str) -> None:
    line = "=" * max(len(text) + 4, 40)
    sys.stdout.write("\n" + line + "\n")
    sys.stdout.write(f"  {text}\n")
    sys.stdout.write(line + "\n\n")
    sys.stdout.flush()
