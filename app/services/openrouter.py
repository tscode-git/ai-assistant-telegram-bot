import httpx
from app.config import OPENROUTER_API_KEY

async def ask(messages,model):
    async with httpx.AsyncClient(timeout=60) as client:
        r=await client.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization":f"Bearer {OPENROUTER_API_KEY}"},
        json={"model":model,"messages":messages})
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
