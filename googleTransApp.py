import sys
import googletrans
import re

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/google_ui.ui")[0]   # index 꼭 까먹지 않기!
# 디자인한 외부 ui파일 불러와서 저장

class GoogleTrans(QMainWindow, form_class):

    def __init__(self):
        super().__init__()  # calling parent class constructor

        self.setupUi(self)  # connect the UI file
        self.setWindowTitle("Google One Line Translator")   # 윈도우 타이틀
        self.setWindowIcon(QIcon("icon/google.png"))        # 윈도우 아이콘
        self.statusBar().showMessage("Google Translator App v1.0 Made By JinyK")    # 윈도우 상태표시줄

        self.trans_btn.clicked.connect(self.trans_action)   # signal
        self.init_btn.clicked.connect(self.init_action)
        self.erase_input_btn.clicked.connect(self.remove_input)
        # 여기까지는 자동완성 안됨. typo 주의

    def trans_action(self): # 번역 실행 함수 -> slot 함수
        korText = self.kor_input.text()    # 입력된 한글 텍스트 가져오기
        reg = re.compile(r'[a-zA-Z]')     # 제외할 문자열
        # result = reg.findall(korText)

        if korText == "":   # 공백 입력시 버그 처리
            print("공백입력!")
            QMessageBox.warning(self, "입력오류", "\n한글 입력란에 번역할 문장을 입력해주세요.")
        elif reg.search(korText):       # 제외할 문자열에 해당하면 오류창 띄우도록 조건문 넣기
        # elif result == []:
            print("한글이 아닌 문자 입력")
            QMessageBox.warning(self, "입력오류", "한글만 입력해주세요.")
        else:
            trans = googletrans.Translator()    # googletrans 모듈의 객체 선언

            # print(googletrans.LANGUAGES)  # -> 번역 언어의 dest 약자 찾기
            engText = trans.translate(korText, dest="en")   # 영어 번역 결과를 가져옴
            japText = trans.translate(korText, dest="ja")
            chnText = trans.translate(korText, dest="zh-cn")

            self.eng_output.append(engText.text)    # 번역된 영어 텍스트를 eng_input에 출력
            self.jap_output.append(japText.text)
            self.chn_output.append(chnText.text)

    def init_action(self):
        self.kor_input.clear()  # 입력 내용 지우기
        self.eng_output.clear()
        self.jap_output.clear()
        self.chn_output.clear()

    def remove_input(self):
        self.kor_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())
