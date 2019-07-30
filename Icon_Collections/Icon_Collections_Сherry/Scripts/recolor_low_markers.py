# -*- coding: utf-8 -*-
"""
Group repainting of icons for marking secondary places.
(Групповое перекрашивание иконок для маркировки вторичных мест.)

sudo apt install libxml2-dev libxslt-dev python-dev
pip install lxml
"""
import os
from lxml import html


path_dir = "/home/genkosta/Видео/low_markers"  # Path to Icon Directory. (Путь к директории иконок.)
background_fill_color = ""  # General background. (Общий фон.)
background_stroke_color = ""  # General stroke. (Общая обводка.)
object_color = ""  # Object color. (Цвет изображения объекта.)

svg_name_list = os.listdir(path=path_dir)

for svg_name in svg_name_list:
    svg_path = "{0}/{1}".format(path_dir, svg_name)
    result = ""

    with open(svg_path, mode="r") as svg_file:
        svg_content = svg_file.read()
        tree = html.fromstring(svg_content)

        # background polygon
        tree.xpath("//path")[0].set("fill", background_fill_color)
        tree.xpath("//path")[0].set("stroke", background_stroke_color)

        # object
        for item_g in tree.xpath("//g"):
            item_g.set("fill", object_color)

        for item_path in tree.xpath("//path")[1:]:
            item_path.set("fill", object_color)

        result = html.tostring(tree).decode("utf-8")

    result = result.replace("viewbox", "viewBox")\
        .replace("></path>", "/>")\
        .replace("></ellipse>", "/>")

    with open(svg_path, mode="w") as w_svg_file:
        w_svg_file.write(result)
