# -*- coding: utf-8 -*-
"""
Group redefinition of parameters of width and height for icons of markers and clusters.
(Групповое переопределение параметров ширины и высоты для иконок маркеров и кластеров.)

sudo apt install libxml2-dev libxslt-dev python-dev
pip install lxml
"""
import os
import math
from lxml import etree
from decimal import Decimal


SIZE_HEIGHT_ICONS = 60

path_dir = ""  # Path to Icon Directory. (Путь к директории иконок.)
svg_name_list = os.listdir(path=path_dir)


def get_size_correction(width, height):
    """Get size correction of image."""
    size_width, size_height = Decimal(width), Decimal(height)
    size_width = math.ceil((size_width * (SIZE_HEIGHT_ICONS / size_height)))
    return [str(size_width), str(SIZE_HEIGHT_ICONS)]


for svg_name in svg_name_list:
    svg_path = "{0}/{1}".format(path_dir, svg_name)
    result = ""

    with open(svg_path, mode="r") as svg_file:
        xml_content = svg_file.read()
        root = etree.XML(xml_content)
        width = root.get('width')
        height = root.get('height')
        correction_size = get_size_correction(width, height)
        root.set('width', correction_size[0])
        root.set('height', correction_size[1])
        result = etree.tostring(root).decode("utf-8")

    with open(svg_path, mode="w") as w_svg_file:
        w_svg_file.write(result)
