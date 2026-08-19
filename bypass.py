

from __future__ import annotations

import random
import time

from utils import fake_progress, hex_dump, binary_rain, spinner


# A pool of scary-sounding stage names. They mean nothing.
_STAGES = [
    "Initializing MTProto socket",
    "Resolving DC cluster nodes",
    "Loading nonce cache",
    "Spoofing device fingerprint",
    "Rebinding session container",
    "Injecting nick payload",
    "Flushing exploit queue",
    "Sealing artifact vault",
]


def warmup() -> None:
    """Pretend to bootstrap an exploit runtime."""
    spinner("Booting NickBypass runtime")
    binary_rain(lines=3, width=40)


def run_chain(target: str = "self") -> None:
    """Run the (entirely fake) bypass chain against a target string.

    `target` is just text to echo back so the banner feels personalized.
    It is never sent anywhere.
    """
    print(f"[*] Target acquired: {target}")
    print("[*] Selecting optimal exploit vector ...")

    # Shuffle the stage list so each run looks a little different.
    stages = _STAGES[:]
    random.shuffle(stages)

    for idx, stage in enumerate(stages, 1):
        fake_progress(f"({idx}/{len(stages)}) {stage}", total=random.randint(18, 30))
        # a sprinkling of fake hex between stages for flavor
        if idx % 2 == 0:
            hex_dump(lines=2, width=24)

    # Deliberately anticlimactic "artifact" reveal that leads into the
    # real reveal in core.reveal().
    print("[*] Artifact extracted. Decrypting vault ...")
    time.sleep(0.6)
    hex_dump(lines=4, width=32)
