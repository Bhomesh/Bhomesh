# generate_now_playing.py
import sys, os, requests
out = sys.argv[1]
api_key = os.getenv("LASTFM_API_KEY")
user = os.getenv("LASTFM_USER")
if not api_key or not user:
    # fallback SVG
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="420" height="60"><rect width="100%" height="100%" fill="#081028"/><text x="20" y="35" fill="#9be8ff" font-size="14">Not connected — configure LASTFM_API_KEY & LASTFM_USER</text></svg>'
    open(out,"w").write(svg)
    print("fallback now playing written")
    exit(0)

r = requests.get("http://ws.audioscrobbler.com/2.0/", params={
    "method":"user.getrecenttracks",
    "user":user, "api_key":api_key, "format":"json","limit":1
})
data = r.json()
track = data.get("recenttracks", {}).get("track", [])[0]
title = track.get("name","—")
artist = track.get("artist",{}).get("#text","")
svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="420" height="60"><rect width="100%" height="100%" fill="#081028"/><text x="20" y="25" fill="#9be8ff" font-size="14">{title}</text><text x="20" y="45" fill="#cbd5e1" font-size="12">{artist}</text></svg>'
open(out,"w").write(svg)
print("now playing written")
