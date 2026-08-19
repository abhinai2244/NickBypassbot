
from __future__ import annotations

import argparse
import sys

import core
from config import Config


def main() -> int:
    parser = argparse.ArgumentParser(
        description="NickBypassBot // LEAKED EDITION (prank)"
    )
    parser.add_argument(
        "--bot",
        action="store_true",
        help="run the optional local Telegram bot instead of the CLI prank",
    )
    parser.add_argument(
        "--target",
        default="self",
        help="cosmetic 'target' name shown in the banner (default: self)",
    )
    args = parser.parse_args()

    if args.bot:
        # Local-only bot mode. Requires BOT_TOKEN in the local environment.
        import telegram
        return telegram.run_bot()

    # Default: run the CLI prank. No token, no network, no credentials.
    core.run(target=args.target)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n[i] Interrupted. No data was collected or sent.")
        sys.exit(130)
