from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QApplication
from trufont.drawingTools.baseTool import BaseTool


_path = QPainterPath()
_path.moveTo(0, 0)
_path.lineTo(0, 100)
_path.lineTo(100, 100)
_path.lineTo(100, 0)
_path.closeSubpath()


class ShapesTool(BaseTool):

    icon = _path
    name = QApplication.translate("ShapesTool", "Shapes")
    shortcut = "S"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._shouldMoveOnCurve = False
        self._stashedOffCurve = None
        self._targetContour = None
