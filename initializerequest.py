#discord.py (2.1.0) function to initialize a lastfm request

import aiohttp

API_KEY = #your lastfm api key

async def lastfm_api(self, user) -> None:
    async with aiohttp.ClientSession() as session:
        params = {"api_key": API_KEY,
        "user": user,
        "method": "user.getRecentTracks",
        "limit", 1,
        "format", "json"}
        async with session.get(url="https://ws.audioscrobbler.com/2.0", params=params) as response:
            data = await response.json()

        #simple example to get the track name | all the data can be retreived from the repo
        trackName = data["recenttracks"]["track"][0]["name"]