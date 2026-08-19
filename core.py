

from __future__ import annotations

import time

import bypass
from database import VAULT
from utils import banner, spinner


_REVEAL = r"""
==============================================
   YOU FOUND IT. THE SECRET OF NICKBYPASSBOT
==============================================

There is no bypass. There never was.

Shut up kids -- can't make your own one? :)

You just got pranked. And yes, you starred the repo.
Thank you <3

==============================================
"""


def run(target: str = "self") -> None:
    """Run the full fake-bypass -> reveal sequence."""
    banner("NickBypassBot // LEAKED EDITION // v4.2.0")

    # Pretend to stash a "session artifact" in the vault. It's just a string
    # in memory; it is never sent anywhere and is erased at the end.
    VAULT.put("session", f"fake-session-{int(time.time())}")
    VAULT.put("target", target)

    # The theater.
    bypass.warmup()
    bypass.run_chain(target=target)

    # Dramatic pause.
    spinner("Finalizing bypass", seconds=1.0)
    time.sleep(0.5)

    # The punchline.
    print(_REVEAL)

    # Clean up the in-memory vault so nothing lingers.
    VAULT.seal()

