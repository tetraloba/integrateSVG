# from xml.etree import ElementTree as ET
from xml.dom import minidom as md
import re

from .mylib.SVG4Python.svg4py.svg import SVG, RGB

class SVG_ext(SVG):
    def image(self, path: str, width, height, x, y):
        self.fp.write(f'<image xlink:href="{path}" width="{width}" height="{height}" x="{x}" y="{y}" />\n')
        return None
    
    def import_svg(self, path: str, x = 0, y = 0, width = None, height = None):
        document = md.parse(path)
        element_svg = document.getElementsByTagName('svg')[0]
        original_width = float(re.sub('[^\d.]', '', element_svg.getAttribute("width"))) # 数字とドット(小数点)以外を削除
        original_height = float(re.sub('[^\d.]', '', element_svg.getAttribute("height")))
        if width is None:
            width = original_width
        if height is None:
            height = original_height
        translate = (x, y)
        scale = (width / original_width, height / original_height)
        self.fp.write(f'<g transform="translate({translate[0]} {translate[1]}) scale({scale[0]} {scale[1]})" >\n')
        for child_node in element_svg.childNodes:
            child_node.writexml(self.fp)
        self.fp.write("</g>\n")

