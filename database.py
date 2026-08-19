"""NickBypassBot // database.

A deliberately menacing-looking "vault" that actually stores nothing.

The whole point of this file is to look like a serious credential store
(keys, sessions, "extracted artifacts") while in reality it only keeps
a few strings in memory for the duration of the prank and then throws
them away. There is no disk persistence and no network sync.
"""

from __future__ import annotations

import time
from typing import Dict, Optional


class Vault:
    """In-memory, ephemeral, never-persisted fake vault.

    Anything you .put() into it lives only until the process exits and is
    never written to disk or sent over the network.
    """

    def __init__(self) -> None:
        self._store: Dict[str, str] = {}
        self._opened_at = time.time()

    def put(self, key: str, value: str) -> None:
        # Pretend this is a big deal. It isn't.
        self._store[key] = value

    def get(self, key: str) -> Optional[str]:
        return self._store.get(key)

    def count(self) -> int:
        return len(self._store)

    def seal(self) -> None:
        """Erase everything. Called at the end of every run."""
        self._store.clear()

    def uptime(self) -> float:
        return time.time() - self._opened_at


# A module-level instance used by the prank flow. It never leaves memory.
VAULT = Vault()
