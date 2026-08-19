"""NickBypassBot // optional Telegram bot frontend.

This is an OPTIONAL, fully local Telegram bot. If you set BOT_TOKEN in your
local .env file, the bot will:
  - respond to /start with a cryptic "bypass ready" message
  - respond to /bypass by running the prank flow in the chat
  - echo anything else back at you

If no BOT_TOKEN is set, this module is simply not used and main.py runs the
prank in CLI mode instead.

NO credentials are requested from users, and NOTHING is sent anywhere except
reply messages to the same chat that talked to the bot.
"""

from __future__ import annotations

import logging

from config import Config
import core

logger = logging.getLogger("nickbypassbot.telegram")


def _safe_text(text: str, limit: int = 4000) -> str:
    """Trim text so we never blow past Telegram's message length limit."""
    text = text.strip()
    return text if len(text) <= limit else text[: limit - 3] + "..."


def run_bot() -> int:
    """Start the local Telegram bot. Returns a process exit code."""
    if not Config.validate():
        print("[telegram] No BOT_TOKEN configured. Skipping bot mode.")
        return 0

    try:
        # python-telegram-bot is an optional dependency.
        from telegram import Update
        from telegram.ext import (
            Application,
            CommandHandler,
            MessageHandler,
            ContextTypes,
            filters,
        )
    except Exception as exc:  # pragma: no cover - env dependent
        print(f"[telegram] Could not import telegram libs: {exc}")
        print("[telegram] Run: pip install -r requirements.txt")
        return 1

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            "NickBypassBot online. Send /bypass to begin. (or don't.)"
        )

    async def do_bypass(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Run the prank locally, then reply with the reveal text.
        # We capture the reveal by calling core directly; core.run prints
        # to stdout, so for the chat we send a short teaser + the punchline.
        who = update.effective_user.username or "anonymous"
        await update.message.reply_text("[*] Bypassing... please hold.")
        core.run(target=who)
        await update.message.reply_text(
            _safe_text(
                "There is no bypass. There never was.\n"
                "You just got pranked. Thanks for playing <3"
            )
        )

    async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f"[echo] {update.message.text}")

    app = Application.builder().token(Config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bypass", do_bypass))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print(f"[telegram] {Config.BOT_NAME} listening locally. Ctrl+C to quit.")
    app.run_polling()
    return 0
