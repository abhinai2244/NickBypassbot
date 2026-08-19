# NickBypassBot configuration.
#
# IMPORTANT: This file only reads configuration from a LOCAL .env file on
# YOUR machine. Nothing is ever uploaded, transmitted, or sent anywhere.
# There is no telemetry, no remote endpoint, and no "phone home" code.

import os

try:
    # Optional dependency. If python-dotenv isn't installed, we just read
    # real environment variables instead.
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


class Config:
    """Local-only configuration loaded from the environment / .env file."""

    # A normal Telegram bot token, used ONLY to run the bot locally so it
    # can echo messages and trigger the prank. It never leaves this machine.
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")

    # Cosmetics only. These make the startup banner look "legit" but are
    # not used for any network operation.
    BOT_NAME = os.getenv("BOT_NAME", "NickBypassBot")
    VERSION = "4.2.0-leak"

    @staticmethod
    def validate() -> bool:
        """Return True if a bot token is present (for the optional bot mode).

        The prank CLI mode works even without a token, so a missing token
        is not fatal -- it just disables the Telegram listener.
        """
        return bool(Config.BOT_TOKEN)
