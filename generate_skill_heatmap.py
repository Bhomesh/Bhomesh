# generate_skill_heatmap.py
import sys, yaml
from pathlib import Path
data = yaml.safe_load(open(sys.argv[1]))
skills = data["skills"]
# skills: list of {name: "Terraform", score: 90}
max_cols = 6
cell = 110
width = cell * max_cols
rows = (len(skills)+max_cols-1)//max_cols
height = rows * cell
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">']
for i,s in enumerate(skills):
    col = i % max_cols
    row = i // max_cols
    x = col*cell
    y = row*cell
    intensity = int(255 - (s["score"]/100)*180)
    color = f'rgb({intensity},{intensity},{255})'
    svg.append(f'<rect x="{x+10}" y="{y+10}" width="{cell-20}" height="{cell-20}" rx="10" fill="{color}" />')
    svg.append(f'<text x="{x+cell/2}" y="{y+cell/2+6}" font-family="sans-serif" font-size="14" text-anchor="middle" fill="#001" >{s["name"]} ({s["score"]})</text>')
svg.append('</svg>')
Path(sys.argv[2]).write_text("\n".join(svg))
print("heatmap written")
