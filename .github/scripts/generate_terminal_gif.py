
# generate_terminal_gif.py
from pathlib import Path
import time
out = Path("widgets/terminal_landing.gif")
svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="820" height="160"><rect width="100%" height="100%" fill="#000"/><text x="20" y="35" font-family="monospace" font-size="18" fill="#9be8ff">$ whoami: bhomeshrazdan</text><text x="20" y="65" font-family="monospace" font-size="16" fill="#cbd5e1">deploying infra — success</text></svg>'
Path("widgets/terminal_landing.svg").write_text(svg)
# convert to gif via cairosvg -> png -> convert (imagick) if available; here we just save an svg as placeholder
Path("widgets/terminal_landing.gif").write_bytes(b'GIF89a')  # placeholder small file for demo
print("terminal gif placeholder created")
