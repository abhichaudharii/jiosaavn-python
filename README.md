# [JioSaavn-Python](https://github.com/abhichaudharii/jiosaavn-python)

An unofficial Python3 wrapper for JioSaavn, a popular Indian music streaming service.. I am in no way affiliated with [JioSaavn](https://www.jiosaavn.com/), use at your own risk.

### Show some ❤️ and ⭐ the repo to support the project. It will motivate me to keep this project alive.
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-orange)](https://t.me/ab_projects) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

### Hire Me: [Abhi Chaudhari](https://www.freelancer.com/hireme/abhichaudharii)!


## Features
- Get New Releases
- Get Song Lyrics
- Get Song Info
- Get Song Direct Download Link
- Get Featured Playlists
- Get Playlist Songs
- Get Top Charts
- Get Top Artists
- Get Artist's Top Songs
- Search for Songs
- Search for Albums
- Search for Artists
- Search for Playlists
- Search for Podcasts
- Search Top Queries

###  Getting it
To download jiosaavn-python, either fork this github repo or simply use Pypi via pip.
```bash
pip install jiosaavn-python
```

#### Get New Releases

You can use the following code to get new releases from `JioSaavn`. The below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword. We are using `limit=2` to limit the number of results returned.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_new_releases(page=1, limit=2))
print(json.dumps(data, indent=4))
```

#### Get Song Lyrics

You can use the following code to get song lyrics from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_song_lyrics("https://www.jiosaavn.com/song/srivalli/RBpGRidYdVI"))
print(json.dumps(data, indent=4))
```

#### Get Song Info

You can use the following code to get song info from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_song_details("https://www.jiosaavn.com/song/srivalli/RBpGRidYdVI"))
print(json.dumps(data, indent=4))
```

#### Get Song Direct Download Link

You can use the following code to get a song direct download from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_song_direct_link("https://www.jiosaavn.com/song/srivalli/RBpGRidYdVI"))
print(json.dumps(data, indent=4))
```

#### Get Featured Playlists

You can use the following code to get featured playlists from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword. We are using `limit=2` to limit the number of results returned.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_featured_playlists(page=1, limit=2))
print(json.dumps(data, indent=4))
```

#### Get Playlist Songs

You can use the following code to get playlist songs from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword. We are using `limit=2` to limit the number of results returned

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_playlist_songs("https://www.jiosaavn.com/featured/the-landers/2-aGcw5eLvQwkg5tVhI3fw__", page=1, limit=2))
print(json.dumps(data, indent=4))
```

#### Get Top Charts

You can use the following code to top charts from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_top_charts())
print(json.dumps(data, indent=4))
```

#### Get Top Artists

You can use the following code to get top artists from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_top_artists())
print(json.dumps(data, indent=4))
```

#### Get Artist's Top Songs

You can use the following code to get the artist's top songs from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword. We are using `limit=2` to limit the number of results returned.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.get_artist_top_songs("https://www.jiosaavn.com/artist/allu-arjun-songs/BGi8EcKdZXk_", limit=2))
print(json.dumps(data, indent=4))
```

#### Search for Songs

You can use the following code to search songs from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.search_songs("Narayan mil jayega"))
print(json.dumps(data, indent=4))
```

#### Search for Albums

You can use the following code to search albums from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.search_albums("Narayan mil jayega"))
print(json.dumps(data, indent=4))
```

#### Search for Artists

You can use the following code to search artists from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.search_artists("Allu Arjun"))
print(json.dumps(data, indent=4))
```

#### Search for Playlists

You can use the following code to search playlists from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.search_playlists("Krishna"))
print(json.dumps(data, indent=4))
```

#### Search for Podcasts

You can use the following code to search podcasts from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.search_podcasts("Krishan"))
print(json.dumps(data, indent=4))
```

#### Search Top Queries

You can use the following code to search top queries from `JioSaavn`. You can pass Song `ID/LINK` Below code shows the example using `asyncio` but you can also use the following in the async function with the `await` keyword.

```python
import json
import asyncio
from jiosaavn import JioSaavn

saavn = JioSaavn()
data = asyncio.run(saavn.search_topquery("the landers"))
print(json.dumps(data, indent=4))
```

### Todo
- [ ] Add download support for album
- [ ] Add download support for playlist
- [ ] Add download support for podcasts
- [ ] Add get details feature for album
- [ ] Add get details feature for atrist
- [ ] Add get details feature for playlist
- [ ] Add get details feature for podcasts


License
----

MIT License

Copyright (c) 2023 Abhishek Chaudhari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
