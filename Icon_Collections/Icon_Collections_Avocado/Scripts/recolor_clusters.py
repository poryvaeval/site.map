# -*- coding: utf-8 -*-
"""
Group repainting of icons for clusters.
(Групповое перекрашивание иконок для кластеров.)

sudo apt install libxml2-dev libxslt-dev python-dev
pip install lxml
"""
import os
from lxml import html


path_dir = ""  # Path to Icon Directory. (Путь к директории иконок.)
circle_fill_color = ""  # General background. (Общий фон.)
circle_stroke_color = ""  # General stroke. (Общая обводка.)
object_color = ""  # Object color. (Цвет изображения объекта.)
svg_name_list = os.listdir(path=path_dir)

for svg_name in svg_name_list:
    svg_path = "{0}/{1}".format(path_dir, svg_name)
    result = ""

    with open(svg_path, mode="r") as svg_file:
        svg_content = svg_file.read()
        tree = html.fromstring(svg_content)

        # circle
        tree.xpath("//circle")[0].set("fill", circle_fill_color)
        tree.xpath("//circle")[0].set("stroke", circle_stroke_color)

        # object
        for item_g in tree.xpath("//g"):
            item_g.set("fill", object_color)

        for item_path in tree.xpath("//path"):
            item_path.set("fill", object_color)

        result = html.tostring(tree).decode("utf-8")

    result = result.replace("viewbox", "viewBox")\
        .replace("></path>", "/>")\
        .replace("></ellipse>", "/>")

    with open(svg_path, mode="w") as w_svg_file:
        w_svg_file.write(result)
