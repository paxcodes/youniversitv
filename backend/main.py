from fastapi import FastAPI

app = FastAPI()

PLAYLISTS = [
    "PLlVtbbG169nGccbp8VSpAozu3w9xSQJoY", # Azure Masterclass (AZ-104)
    "PLlVtbbG169nFr8RzQ4GIxUEznpNR53ERq", # DevOps Masterclass
    "PLIFyRwBY_4bTwRX__Zn4-letrtpSj1mzY", # Practical TLS
]

@app.get("/playlists")
async def read_playlists():
    return PLAYLISTS
