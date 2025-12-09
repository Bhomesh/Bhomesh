# generate_quote_svg.py
import sys, yaml
from pathlib import Path
from random import choice
from cairosvg import svg2png

quotes = yaml.safe_load(open(sys.argv[1]))
q = choice(quotes["quotes"])
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="820" height="120">
  <rect width="100%" height="100%" fill="#0f172a"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Fira Code, monospace" font-size="20" fill="#9be8ff">{q}</text>
</svg>'''
Path(sys.argv[2]).write_text(svg)
print("quote svg written")
