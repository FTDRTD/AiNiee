from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QHBoxLayout

from qfluentwidgets import SubtitleLabel


class BaseNavigationItem(QFrame):

    def __init__(self, text: str, parent = None):
        super().__init__(parent = parent)

        self.label = SubtitleLabel("", self)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)

        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(text.replace(' ', '-'))