from . import get_app

app = get_app()

@app.tool
async def health() -> str:
    return "OK"
