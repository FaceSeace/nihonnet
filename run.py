from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import main
import rank
import gonihon


username = ""
allcnt = 20
ans = ""
right = 0
fault = 0
cnt = 0


class rank_list(QMainWindow, rank.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def start(self):
        self.move((QDesktopWidget().screenGeometry().width() - self.geometry().width()) / 2, (QDesktopWidget().screenGeometry().height() - self.geometry().height()) / 2)
        self.pushButton.clicked.connect(self.enableparaent)
        self.pushButton.clicked.connect(self.close)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def rank(self):
        whole_info = gonihon.user_result_and_updata()
        print(whole_info)
        self.label.setText(whole_info[0])
        self.label_2.setText(whole_info[1])
        self.label_18.setText("你这回在第" + whole_info[2] + "名")
        if whole_info[2] != False:
            self.label_19.setText(whole_info[3][0])
            self.label_29.setText(whole_info[3][1])
            self.label_30.setText(whole_info[3][2])
            self.label_31.setText(whole_info[3][3]+"%")

            self.label_20.setText(whole_info[4][0])
            self.label_32.setText(whole_info[4][1])
            self.label_33.setText(whole_info[4][2])
            self.label_34.setText(whole_info[4][3]+"%")

            self.label_21.setText(whole_info[5][0])
            self.label_35.setText(whole_info[5][1])
            self.label_36.setText(whole_info[5][2])
            self.label_37.setText(whole_info[5][3]+"%")

            self.label_22.setText(whole_info[6][0])
            self.label_38.setText(whole_info[6][1])
            self.label_39.setText(whole_info[6][2])
            self.label_40.setText(whole_info[6][3]+"%")

            self.label_23.setText(whole_info[7][0])
            self.label_41.setText(whole_info[7][1])
            self.label_42.setText(whole_info[7][2])
            self.label_43.setText(whole_info[7][3]+"%")

            self.label_24.setText(whole_info[8][0])
            self.label_44.setText(whole_info[8][1])
            self.label_45.setText(whole_info[8][2])
            self.label_46.setText(whole_info[8][3]+"%")

            self.label_25.setText(whole_info[9][0])
            self.label_47.setText(whole_info[9][1])
            self.label_48.setText(whole_info[9][2])
            self.label_49.setText(whole_info[9][3]+"%")

            self.label_26.setText(whole_info[10][0])
            self.label_50.setText(whole_info[10][1])
            self.label_51.setText(whole_info[10][2])
            self.label_52.setText(whole_info[10][3]+"%")

            self.label_27.setText(whole_info[11][0])
            self.label_53.setText(whole_info[11][1])
            self.label_54.setText(whole_info[11][2])
            self.label_55.setText(whole_info[11][3]+"%")

            self.label_28.setText(whole_info[12][0])
            self.label_56.setText(whole_info[12][1])
            self.label_57.setText(whole_info[12][2])
            self.label_58.setText(whole_info[12][3]+"%")

    def enableparaent(self):
        global ex
        ex.setEnabled(True)


class window(QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def start(self):
        self.pushButton.clicked.connect(self.hide_item_name)
        self.pushButton.clicked.connect(self.submit_name)
        self.pushButton.clicked.connect(self.show_title)
        self.pushButton_2.clicked.connect(self.submit_ans)
        self.lineEdit_3.returnPressed.connect(self.submit_ans)
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_8.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton.setDefault(True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


    def unhide_item_name(self):
        self.pushButton.setVisible(True)
        self.label_6.setVisible(True)
        self.lineEdit.setVisible(True)
        self.label_7.setVisible(True)
        self.spinBox.setVisible(True)

    def hide_item_name(self):
        self.pushButton.setVisible(False)
        self.label_6.setVisible(False)
        self.lineEdit.setVisible(False)
        self.label_7.setVisible(False)
        self.spinBox.setVisible(False)
        self.unhide_item_job()

    def hide_item_job(self):
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.unhide_item_name()

    def unhide_item_job(self):
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.lineEdit_3.setVisible(True)
        self.pushButton_2.setVisible(True)

    def submit_name(self):
        global allcnt, username
        username, allcnt = self.lineEdit.text(), int(self.spinBox.text())
        gonihon.getname_and_all(username, allcnt)

    def show_title(self):
        global right, fault, cnt, allcnt
        aim = gonihon.title()
        self.label.setText(aim[0])
        bi = str(right) + "/"+ str(allcnt)
        self.label_2.setText(str(bi))

    def submit_ans(self):
        global ans, right, fault, cnt, allcnt
        self.label_4.setVisible(True)
        self.label_5.setVisible(True)
        cnt += 1
        ans = self.lineEdit_3.text()
        last_aim = self.label.text()
        last_right_ans = gonihon.get_ans(last_aim)
        self.label_5.setText(last_aim)
        self.label_4.setText(last_right_ans)
        res = gonihon.judge(ans)
        if res[0] == True:
            right += 1
        else:
            fault += 1
            self.label_3.setText("错"+str(fault)+"个")
            print(res[1])
        if cnt >= allcnt:
            self.submit_and_show_rank_list()

        self.show_title()
        self.lineEdit_3.setText("")

    def submit_and_show_rank_list(self):
        global zx, username, allcnt, ans, right, fault, cnt
        self.setEnabled(False)
        self.label_3.setText("错0个")
        self.label_2.setText("0/0")
        zx.show()
        zx.rank()
        username = ""
        allcnt = 20
        ans = ""
        right = 0
        fault = 0
        cnt = 0
        gonihon.initdata()
        self.hide_item_job()

    def click_close(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    zx = rank_list()
    sys.exit(app.exec_())

