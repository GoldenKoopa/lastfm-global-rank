# Last.fm Artist Gobal Listener Rank Tool

This tool fetches a Last.fm user's top artists and shows their global listener rank for each artist. The rank is completely determined by Last.fm, I do not have any information on how.
This needs to be a script and cannot be put on a website since it's not using the Last.fm api but scrapes the web. This would lead to CORS issues.

## Features

- Lists top artists from a user's Last.fm library if user is in top 32.
- Displays user's rank among all listeners for each artist.
- Shows scrobble count per artist.

## Usage

```bash
python main.py <lastfm_username>
```
or with uv:
```bash
uv run main.py <lastfm_username>
```

Example output:
```
Artist: Judith Hill
Rank: 3 | 683
Place: 2
----------------------------------------
Artist: Stars In Stereo
Rank: 4 | 660
Place: 3
----------------------------------------
Artist: Bad Seed Rising
Rank: 5 | 414
Place: 3
----------------------------------------
```

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Notes

- Only fetches data from the first page of top artists. Login would be required for more and is not supported.
- Requires an internet connection.

