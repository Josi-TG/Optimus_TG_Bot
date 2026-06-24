from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from telegram import Update

from src.config.settings import TOKEN, WEBHOOK_URL
from src.telegram_app import build_application

telegram_app = build_application()

@asynccontextmanager

async def lifespan(app: FastAPI):
    await telegram_app.initialize()

    await telegram_app.bot.set_webhook(WEBHOOK_URL)

    print(f"Webhook set to: {WEBHOOK_URL}")

    yield

    await telegram_app.shutdown()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"status: alive"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    update = Update.de_json(
        data,
        telegram_app.bot
    )

    await telegram_app.process_update(update)

    return {"ok": True}

@app.get("/health")
async def health():
    return {"status": "healthy"}