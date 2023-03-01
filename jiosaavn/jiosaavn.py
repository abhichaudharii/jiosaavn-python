import httpx
from random import choice

REQ_TIMEOUT = 20
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
]

headers = {
    "User-Agent": "",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://www.jiosaavn.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


class JioSaavn:
    """An unofficial Python3 wrapper for JioSaavn, a popular Indian music streaming service.."""

    def __init__(self):
        self.api_url = "https://www.jiosaavn.com/api.php"
        self.api_client = httpx.AsyncClient(timeout=REQ_TIMEOUT)
        self.api_client.headers.update(headers)

        self.user_agents = USER_AGENTS
        self._set_random_user_agent()

    def _set_random_user_agent(self):
        """Setting unique user agent on every in the instance. Just to be safe"""

        random_user_agent = choice(self.user_agents)
        self.api_client.headers.update({"User-Agent": random_user_agent})

    async def _format_response(self, response):
        """Returns the formatted response"""

        if isinstance(response, list):
            return {"data": response}
        elif isinstance(response, dict):
            if "data" in response:
                return response
            else:
                return {"data": response}

    async def _get_id_from_url(self, url):
        """Splits given URL and returns the corresponding id"""

        return url.split("/")[-1]

    async def get_new_releases(self, page=1, limit=50):
        """Finds new releases from JioSaavn with given page and limit"""

        params = {
            "api_version": "4",
            "_format": "json",
            "__call": "content.getAlbums",
            "p": str(page),
            "ctx": "web6dot0",
            "_marker": "0",
            "n": str(limit),
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = resp.json()
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def get_featured_playlists(self, page=1, limit=50):
        """Finds featured playlists from JioSaavn with given page and limit"""

        params = {
            "__call": "content.getFeaturedPlaylists",
            "fetch_from_serialized_files": "true",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
            "ctx": "web6dot0",
            "p": str(page),
            "n": str(limit),
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def get_playlist_songs(self, playlist_id, page=1, limit=1):
        """Finds songs from passed playlist ID/URL from JioSaavn with given page and limit"""

        # Checking if the user has passed the URL or id
        if "jiosaavn" in playlist_id:
            playlist_id = await self._get_id_from_url(playlist_id)

        params = {
            "__call": "webapi.get",
            "token": playlist_id,
            "type": "playlist",
            "p": str(page),
            "n": str(limit),
            "includeMetaTags": "0",
            "ctx": "web6dot0",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def get_top_charts(self):
        """Finds top charts from JioSaavn"""

        params = {
            "__call": "content.getCharts",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
            "ctx": "web6dot0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def get_top_artists(self):
        """Finds top artists from JioSaavn"""

        params = {
            "__call": "social.getTopArtists",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
            "ctx": "web6dot0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def get_artist_top_songs(self, singer_id, page=1, limit=1):
        """Finds songs from passed artist ID/URL from JioSaavn with given page and limit"""

        # Checking if the user has passed the ID/URL
        if "jiosaavn" in singer_id:
            singer_id = await self._get_id_from_url(singer_id)

        params = {
            "token": singer_id,
            "p": str(page),
            "n_song": str(limit),
            "__call": "webapi.get",
            "type": "artist",
            "n_album": "0",
            "sub_type": "songs",
            "category": "",
            "sort_order": "",
            "includeMetaTags": "0",
            "ctx": "web6dot0",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json()["topSongs"])
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def get_song_details(self, song_id):
        """Finds song details for the passed id/url on JioSaavn and returns"""

        # Checking if the user has passed the ID/URL
        if "jiosaavn" in song_id:
            song_id = await self._get_id_from_url(song_id)

        print(f"[I] Finds SONG DETAILS with ID:- {song_id}")

        params = {
            "__call": "webapi.get",
            "token": song_id,
            "type": "song",
            "includeMetaTags": "0",
            "ctx": "web6dot0",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"status": resp.status_code}

    async def get_song_direct_link(self, song_id):
        """Finds song direct link for the passed ID/URL on JioSaavn and returns that"""

        songs = await self.get_song_details(song_id)
        more_info = songs["songs"][0]["more_info"]
        song_enc_url = more_info["encrypted_media_url"]
        bitrate = "320" if more_info["320kbps"] else "128"

        params = {
            "__call": "song.generateAuthToken",
            "url": song_enc_url,
            "bitrate": str(bitrate),
            "api_version": "4",
            "_format": "json",
            "ctx": "web6dot0",
            "_marker": "0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            return data["data"]["auth_url"]
        else:
            return {"status": resp.status_code}

    async def get_song_lyrics(self, song_id):
        """Finds lyrics for the passed ID/URL on JioSaavn and returns them"""

        songs = await self.get_song_details(song_id)
        song_id = songs["songs"][0]["id"]

        params = {
            "__call": "lyrics.getLyrics",
            "lyrics_id": song_id,
            "ctx": "web6dot0",
            "api_version": "4",
            "_format": "json",
            "_marker": "0",
        }
        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def search_on_saavn(self, search_query):
        """Searches a passed search query on JioSaavn."""

        params = {
            "__call": "autocomplete.get",
            "query": search_query,
            "_format": "json",
            "_marker": "0",
            "ctx": "web6dot0",
        }

        resp = await self.api_client.post(url=self.api_url, params=params)
        if resp.status_code == 200:
            data = await self._format_response(resp.json())
            data["status"] = resp.status_code
            return data
        else:
            return {"status": resp.status_code}

    async def search_songs(self, search_query):
        """Searches a passed search query on JioSaavn and returns all the songs"""

        result = await self.search_on_saavn(search_query)
        if result["status"] == 200:
            return {"status": result["status"], "data": result["data"]["songs"]["data"]}
        else:
            return {
                "status": result["status"],
                "message": "Could not find songs for the search query",
            }

    async def search_albums(self, search_query):
        """Searches a passed search query on JioSaavn and returns all the albums"""

        result = await self.search_on_saavn(search_query)
        if result["status"] == 200:
            return {
                "status": result["status"],
                "data": result["data"]["albums"]["data"],
            }
        else:
            return {
                "status": result["status"],
                "message": "Could not find albums for the search query",
            }

    async def search_playlists(self, search_query):
        """Searches a passed search query on JioSaavn and returns all the playlists"""

        result = await self.search_on_saavn(search_query)
        if result["status"] == 200:
            return {
                "status": result["status"],
                "data": result["data"]["playlists"]["data"],
            }
        else:
            return {
                "status": result["status"],
                "message": "Could not find playlists for the search query",
            }

    async def search_artists(self, search_query):
        """Searches a passed search query on JioSaavn and returns all the artists"""

        result = await self.search_on_saavn(search_query)
        if result["status"] == 200:
            return {
                "status": result["status"],
                "data": result["data"]["artists"]["data"],
            }
        else:
            return {
                "status": result["status"],
                "message": "Could not find artists for the search query",
            }

    async def search_topquery(self, search_query):
        """Searches a passed search query on JioSaavn and returns all the topquery"""

        result = await self.search_on_saavn(search_query)
        if result["status"] == 200:
            return {
                "status": result["status"],
                "data": result["data"]["topquery"]["data"],
            }
        else:
            return {
                "status": result["status"],
                "message": "Could not find top query for the search query",
            }

    async def search_podcasts(self, search_query):
        """Searches a passed search query on JioSaavn and returns all the podcasts"""

        result = await self.search_on_saavn(search_query)
        if result["status"] == 200:
            return {"status": result["status"], "data": result["data"]["shows"]["data"]}
        else:
            return {
                "status": result["status"],
                "message": "Could not find podcasts for the search query",
            }
