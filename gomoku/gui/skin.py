# coding=utf-8
# coding=utf-8
import os
import sys

DIRNAME = os.path.dirname(os.path.abspath(__file__))
if DIRNAME not in sys.path:
    sys.path.insert(0, DIRNAME)

PROJECT = os.path.abspath(os.path.join(__file__, '../..'))
if PROJECT not in sys.path:
    sys.path.insert(0, PROJECT)


SKINSPATH = os.path.join(PROJECT, 'gui/skins')

WINDOW_UI = os.path.join(SKINSPATH, 'window.ui')
ICON_IMAGE = os.path.join(SKINSPATH, 'favicon.ico')
BOARD_IMAGE = os.path.join(SKINSPATH, 'board.png')
BLACK_IMAGE = os.path.join(SKINSPATH, 'black.png')
WHITE_IMAGE = os.path.join(SKINSPATH, 'white.png')
BLACK_BORDER_IMAGE = os.path.join(SKINSPATH, 'black_border.png')
WHITE_BORDER_IMAGE = os.path.join(SKINSPATH, 'white_border.png')

LABEL_STYLE = '''
<html>
<body>
<p align="center">
    <span style=" font-size:14pt; font-weight:600;">
        {text}
    </span>
</p>
</body>
</html>
'''
