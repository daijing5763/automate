from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from statechange import statechange


class Turing(object):
    def __init__(self):
        # 从文件中加载UI定义
        qfile_stats = QFile("main.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        # 创建窗口
        self.ui = QUiLoader().load(qfile_stats)

        # 获取参数
        self.a = 0
        self.n = 0
        self.m = 0

        # 初始化图灵机
        self.tape = []
        self.state = "o"
        self.point = 0

        # 按键动作
        self.ui.pushButton_start.clicked.connect(self.get_start)
        self.ui.pushButton_one.clicked.connect(self.step_one)
        self.ui.pushButton_all.clicked.connect(self.step_all)

    def get_start(self):
        # 获取首项a
        input_a = self.ui.lineEdit_a.text()
        try:
            self.a = int(input_a)
        except ValueError:
            QMessageBox.about(self.ui, "错误提示", "请输入正确的正整数a")
        if self.a < 1:
            QMessageBox.about(self.ui, "错误提升", "请输入正确的正整数a")

        # 获取项数n
        input_n = self.ui.lineEdit_n.text()
        try:
            self.n = int(input_n)
        except ValueError:
            QMessageBox.about(self.ui, "错误提示", "请输入正确的正整数n")
        if self.n < 1:
            QMessageBox.about(self.ui, "错误提示", "请输入正确的正整数n")

        # 获取公差m
        input_m = self.ui.lineEdit_m.text()
        try:
            self.m = int(input_m)
        except ValueError:
            QMessageBox.about(self.ui, "错误提示", "请输入正确的正整数m")
        if self.a < 1:
            QMessageBox.about(self.ui, "错误提示", "请输入正确的正整数m")

        # 初始化
        self.tape = ['B'] + ['1'] * self.a + ['B'] + ['1'] * self.n + ['B'] + ['1'] * self.m + ['B'] * 3
        self.state = "o"
        self.point = 0
        # 输出纸带和状态
        tape_output = self.tape[0:self.point] + ['*'] + self.tape[self.point:]
        self.ui.tape_output.setText(''.join(tape_output))
        self.ui.state_output.setText(self.state)

    def step_one(self):
        self.tape, self.state, self.point = statechange(self.tape, self.state, self.point)
        tape_output = self.tape[0:self.point] + ['*'] + self.tape[self.point:]
        self.ui.tape_output.setText(''.join(tape_output))
        self.ui.state_output.setText(self.state)
        if self.state == "nn":
            num = 0
            for s in self.tape:
                if s == "1":
                    num += 1
            QMessageBox.about(self.ui, '运行结果', f'最后的计算结果为{num}')

    def step_all(self):
        while self.state != "nn":
            self.tape, self.state, self.point = statechange(self.tape, self.state, self.point)
        num = 0
        for s in self.tape:
            if s == "1":
                num += 1
        tape_output = self.tape[0:self.point] + ['*'] + self.tape[self.point:]
        self.ui.tape_output.setText(''.join(tape_output))
        self.ui.state_output.setText(self.state)
        QMessageBox.about(self.ui, '运行结果', f'最后的计算结果为{num}')


app = QApplication([])
turing = Turing()
turing.ui.show()
app.exec_()

