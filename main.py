import sys
import time
import numpy as np

from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import *
from PyQt6.QtCore import *

def clear_line():
    main_window.line_clr.clear()


def focus(event):
    main_window.centralwidget.setFocus()
    btn: QPushButton = QPushButton(main_window)
    btn.setGeometry(event.pos().x(), event.pos().y(), 25, 25)
    btn.setStyleSheet("""
    background-color: rgb(127, 127, 127);
    """)

    def click():
        btn.deleteLater()

    btn.clicked.connect(click)
    btn.show()
def coord(event):
    main_window.lbl_coord.setText(f"({event.pos().x()}; {event.pos().y()})")
def change_text_line_edit1():
    main_window.line_clr.setText(main_window.line_edit.text())
def change_text_line_edit2():
    main_window.line_edit.setText(main_window.line_clr.text())
def pix():
    if main_window.check_box_pix.isChecked():
        main_window.label_pix.setPixmap(QPixmap('cat2.jpg').scaled(200, 200))
    else:
        main_window.label_pix.setText(" ")
def cat(event):

    main_window.label_pix.setPixmap(QPixmap('cat3.jpg').scaled(200, 200))
def get_answer():
    if main_window.rb_answer1.isChecked():
        main_window.label_answer1.setPixmap(QPixmap('true.jpg').scaled(25, 25))
        main_window.label_answer2.setText(" ")
        main_window.label_answer3.setText(" ")
        btn_super.setText("вы молодец!")
    elif main_window.rb_answer2.isChecked():
        main_window.label_answer2.setPixmap(QPixmap('false.jpg').scaled(25, 25))
        main_window.label_answer1.setText(" ")
        main_window.label_answer3.setText(" ")
        btn_super.setText("попробуйте еще раз!")
    else:
        main_window.label_answer3.setPixmap(QPixmap('false.jpg').scaled(25, 25))
        main_window.label_answer1.setText(" ")
        main_window.label_answer2.setText(" ")
        btn_super.setText("попробуйте еще раз!")
    btn_super.show()

def hard():
    main_window.label_answer1.setText(" ")
    main_window.label_answer2.setText(" ")
    main_window.label_answer3.setText(" ")
    main_window.rb_answer1.setChecked(False)
    main_window.rb_answer2.setChecked(False)
    main_window.rb_answer3.setChecked(False)
    btn_super.close()

def change_background():
    color = main_window.combo_box_background.currentText()
    if color == "Серый": rgb = "rgb(221, 221, 221)"
    elif color == "Светло фиолетовый": rgb = "rgb(221,160,221)"
    elif color == "Синий синий иней": rgb = "rgb(175,218,252)"
    elif color == "Магическая мята": rgb = "rgb(170,240,209)"
    elif color == "Розовый щербет": rgb = "rgb(247,143,167)"
    elif color == "Канареечный": rgb = "rgb(255,255,153)"
    main_window.centralwidget.setStyleSheet(f"""background-color: {rgb}""")

def start():
    timer.start(100)
def stop():
    timer.stop()

def progress_bar():
    obj: QProgressBar = main_window.progress_bar_time
    obj.setValue(obj.value() + 1)
    if obj.value() > 100:
        timer.stop()

def get_value():
    value = main_window.vertical_slider.value()
    main_window.lbl_slider.setText(f"{value}")

def changed_event(event):

    a = np.random.choice(range(256))
    b = np.random.choice(range(256))
    c = np.random.choice(range(256))

    main_window.widget_paint.setStyleSheet(
        f"""
        background-color: rgb({a}, {b}, {c});
        """
    )

def monkey_press(event):
    main_window.label_monkey.setPixmap(QPixmap('right.jpg').scaled(200, 200))

def monkey_release(event):
    main_window.label_monkey.setPixmap(QPixmap('left.jpg').scaled(200, 200))

def pain_press(event):
    if int(event.key()) == ord('N') or int(event.key()) == ord('Т'):
        main_window.label_pain.setPixmap(QPixmap('eg.jpg').scaled(200, 200))

def pain_release(event):
    if int(event.key()) == ord('M') or int(event.key()) == ord('Ь'):
        main_window.label_pain.setPixmap(QPixmap('eg_giga.jpg').scaled(200, 200))

def hor():
    main_window.progressBar_hor.setValue(main_window.horizontalSlider_bar.value())

def degree():
    value = main_window.dial_bake.value()
    main_window.label_degree.setText(f"Градус {value}")
    if 180 <= value <= 220:
        main_window.label_cookie.setPixmap(QPixmap('cookie1.jpg').scaled(200, 200))
    elif 220 < value <= 280:
        main_window.label_cookie.setPixmap(QPixmap('cookie2.jpg').scaled(200, 200))
    elif 280 < value <= 300:
        main_window.label_cookie.setPixmap(QPixmap('cookie3.jpg').scaled(200, 200))

def get_total_price():
    if main_window.lineEdit_price.text().isnumeric():
        quantity = main_window.spinBox.value()
        price = int(main_window.lineEdit_price.text())
        main_window.lineEdit_result.setText(f"{quantity*price}")
    else:
        main_window.lineEdit_price.setText("")
        main_window.lineEdit_result.setText("")
        main_window.spinBox.clear()


def get_file():
    res = QFileDialog.getOpenFileName(main_window, 'Open File', '\\PycharmProjects\\laba1', 'txt File (*.txt)')
    path = res[0]
    if path:
        with open(path, 'r', encoding="utf-8") as file:
            text = file.read()
            main_window.textEdit.setText(text)

def get_new_size(event):
    main_window.label_new_size.setText(f"({main_window.size().width()}x{main_window.size().height()})")

def clear_result():
    main_window.lineEdit_result.clear()
    main_window.spinBox.clear()
    main_window.lineEdit_price.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window: QMainWindow = uic.loadUi("design.ui")

    main_window.widget_paint.paintEvent = changed_event

    main_window.setWindowTitle("Моя программа")

    main_window.resizeEvent = get_new_size

    btn_choose_file = QAction("&Choose file", main_window)
    btn_choose_file.triggered.connect(get_file)
    file_menu = main_window.menubar.addMenu("&File")
    file_menu.addAction(btn_choose_file)

    main_window.centralwidget.mousePressEvent = focus

    main_window.btn_clear.clicked.connect(clear_line)

    main_window.centralwidget.setMouseTracking(True)
    main_window.centralwidget.mouseMoveEvent = coord

    main_window.line_edit.textChanged.connect(change_text_line_edit1)
    main_window.line_clr.textChanged.connect(change_text_line_edit2)

    main_window.check_box_pix.stateChanged.connect(pix)

    main_window.label_pix.mouseDoubleClickEvent = cat
    pixmap = QPixmap('test.jpg').scaled(170, 200)
    main_window.label_test.setPixmap(pixmap)

    main_window.rb_answer1.clicked.connect(get_answer)
    main_window.rb_answer2.clicked.connect(get_answer)
    main_window.rb_answer3.clicked.connect(get_answer)

    main_window.combo_box_background.currentIndexChanged.connect(change_background)

    timer = QTimer()
    timer.timeout.connect(progress_bar)

    main_window.btn_start.clicked.connect(start)
    main_window.btn_stop.clicked.connect(stop)


    main_window.vertical_slider.valueChanged.connect(get_value)

    btn_super: QPushButton = QPushButton(main_window.centralwidget)
    btn_super.setGeometry(240, 360, 141, 28)
    btn_super.setStyleSheet(
        """
            background-color: rgb(220, 215, 255);
        """
    )

    main_window.label_monkey.setPixmap(QPixmap('left.jpg').scaled(200, 200))
    main_window.label_monkey.mousePressEvent = monkey_press
    main_window.label_monkey.mouseReleaseEvent = monkey_release



    main_window.label_pain.setPixmap(QPixmap('eg.jpg').scaled(200, 200))
    main_window.keyPressEvent = pain_press
    main_window.keyReleaseEvent = pain_release

    main_window.horizontalSlider_bar.valueChanged.connect(hor)

    main_window.label_cookie.setPixmap(QPixmap('cookie1.jpg').scaled(200, 200))
    main_window.dial_bake.valueChanged.connect(degree)

    main_window.spinBox.valueChanged.connect(get_total_price)
    main_window.lineEdit_price.textChanged.connect(get_total_price)
    main_window.btn_clear_res.clicked.connect(clear_result)

    btn_super.close()
    btn_super.clicked.connect(hard)

    main_window.show()
    sys.exit(app.exec())