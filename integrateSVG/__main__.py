from integrateSVG.svg_ext import SVG_ext, RGB
from integrateSVG.config import svg_files

svg = SVG_ext('integrated.svg', 0, 0, 1920, 1080, unit='px') # SVGファイルの生成
svg.rect(0, 0, '100%', '100%', RGB(0, 0, 0), stroke_width=0) # 背景色を設定

for file_path, option in svg_files.items(): # config.pyに従ってSVGをインポート
    svg.import_svg(file_path, option['x'], option['y'], option['width'], option['height'])
