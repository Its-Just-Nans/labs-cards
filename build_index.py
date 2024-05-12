from os import listdir
from pathlib import Path

PATH_INDEX = "src/index.html"

content = """
<style>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    grid-gap: 10px;
}
.grid-item {
    border: 1px solid black;
    padding: 10px;
    text-align: center;
}
.grid-item img {
    max-width: 100%;
    max-height: 100%;
}
.grid-item a {
    display: block;
}</style>"""

content += "<div class='grid-container'>"

for one_img in listdir("src/images"):
    filename = Path(one_img).stem
    content += "<div class='grid-item'>"
    content += f"<a href='{filename}.html'>"
    content += f"<span>{filename}</span>"
    content += f"<img src='images/{one_img}' alt='{one_img}' />"
    content += "</a>"
    content += "</div>"

content += "</div>"

with open(PATH_INDEX, "w") as f:
    f.write(content)
