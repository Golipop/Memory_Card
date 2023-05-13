#Библиотека
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QPushButton, QWidget, QRadioButton, QMessageBox, QHBoxLayout, QButtonGroup, QVBoxLayout, QLabel
from random import shuffle, randint

#КЛАСС КУЕСТИОН-----------------------------------------

class Question():
    def __init__ (self, question, r_ans, wrong1, wrong2, wrong3):
        self.r_ans = r_ans
        self.question = question
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#Cписок-------------------------------------------------


question_list = list()

question_list.append(Question('В каком году основали Санкт-Петербург','1703','1700','1647','974'))
question_list.append(Question('В какой стране более одной столицы?','ЮАР','Россия','США','Индия'))
question_list.append(Question('Какого газа в атмосфере Земли больше всего?','Азот','Кислород','Водород','Магний'))
question_list.append(Question('Какая планета расположена ближе всех к Солнцу?','Меркурий','Венера','Марс','Нептун'))
question_list.append(Question('Столицей какого государства является Нью-Йорк?','Это не столица','США','Испания','Индия'))
question_list.append(Question('Самая глубокая река на Земле','Конго','Алания','Амазонка','Енисей'))
question_list.append(Question('Какие из указанных явлений не изучаются физикой?','Передача информации','Передача усилия','Передача электричества','Передача тепла'))
question_list.append(Question('Как называлась территория, где Петр I начал строительство Санкт-Петербурга?','Ингерманландия','Автрия','Австралия','Испания'))
question_list.append(Question('Какие два элемента входят в состав аммиака?','Азот и водород','Кислород и алюминий','Спирт и ртуть','Азот и ртуть'))
question_list.append(Question('Как переводится слово «аллегория» с греческого?','Иносказания','Перевод','Описание','Рассказ'))

#Приложение---------------------------------------------

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)

main_win.total = 0
main_win.score = 0

main_win.cur_question = -1
#Виджеты------------------------------------------------

text_ans = QLabel('Вопрос')
button_ans = QPushButton('Ответить')

Rb = QGroupBox('Варианты ответов')
ans_1 = QRadioButton('Вариант 1')
ans_2 = QRadioButton('Вариант 2')
ans_3 = QRadioButton('Вариант 3')
ans_4 = QRadioButton('Вариант 4')


#Линии--------------------------------------------------

line_group = QHBoxLayout()
line_text = QHBoxLayout()
line_button = QHBoxLayout()


line_h1 = QHBoxLayout()
line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()

m_line = QVBoxLayout()

line_v1.addWidget(ans_1)
line_v1.addWidget(ans_2)
line_v2.addWidget(ans_3)
line_v2.addWidget(ans_4)

line_h1.addLayout(line_v1)
line_h1.addLayout(line_v2)


Rb.setLayout(line_h1)

line_text.addWidget(text_ans, alignment = Qt.AlignCenter)
line_group.addWidget(Rb)
line_button.addStretch(1)
line_button.addWidget(button_ans, stretch = 3)
line_button.addStretch(1)

m_line.addLayout(line_text)
m_line.addLayout(line_group)
m_line.addLayout(line_button)

m_line.setSpacing(5)



#Результат----------------------------------------------

ansRB = QGroupBox('Результат теста')
ans_predict = QLabel('Правильно/Неправильно')
ans = QLabel('Правильный ответ')


#Скрываю прошлый бокс и новый подключаю на ту же самую линию что и ту

ansRB.hide()

ans_line_V = QVBoxLayout()
ans_line_V.addWidget(ans_predict, alignment=(Qt.AlignLeft | Qt.AlignTop))
ans_line_V.addWidget(ans, alignment= Qt.AlignHCenter)

ansRB.setLayout(ans_line_V)

line_group.addWidget(ansRB)


#Подключение обработки нажатия на кнопну

radio_group = QButtonGroup()
radio_group.addButton(ans_1)
radio_group.addButton(ans_2)
radio_group.addButton(ans_3)
radio_group.addButton(ans_4)

def show_result():
    Rb.hide()
    ansRB.show()
    button_ans.setText('Следующий вопрос')

def show_question():
    ansRB.hide()
    Rb.show()
    button_ans.setText('Ответить')
    #...
    radio_group.setExclusive(False)
    ans_1.setChecked(False)
    ans_2.setChecked(False)
    ans_3.setChecked(False)
    ans_4.setChecked(False)
    radio_group.setExclusive(True)


#-------------------------------------------------------


answer_list = [ans_1, ans_2, ans_3, ans_4]

#перемешивает список с ответами и вопросами
def ask(q:Question):
    shuffle(answer_list)
    answer_list[0].setText(q.r_ans)
    answer_list[1].setText(q.wrong1)
    answer_list[2].setText(q.wrong2)
    answer_list[3].setText(q.wrong3)
    text_ans.setText(q.question)
    ans.setText(q.r_ans)
    show_question()

def show_correct(res):
    ans_predict.setText(res)
    show_result()

def check_answer():
    if answer_list[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    if answer_list[1].isChecked() or answer_list[2].isChecked() or answer_list[3].isChecked():
        show_correct('Неправильно')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Процент правильных овтетов:', str(round(main_win.score / main_win.total * 100, 2)))


#След. вопрос-------------------------------------------------


def next_question():
    if len(question_list) > 0:
        cur_question = randint(0, len(question_list) - 1)
        q = question_list[cur_question]
        main_win.total += 1
        ask(q)
        if main_win.total > 0:
            question_list.remove(question_list[cur_question])
    else:
        text_ans.setText('Тест завершен')
        button_ans.hide()
        ans_predict.setText('Процент правильных овтетов: '+ str(round(main_win.score / main_win.total * 100, 2)))
        ans.setText('Всего вопросов: ' + str(main_win.total) + '  |  ' + 'Правильных ответов: ' + str(main_win.score))
    
    

#Клик--------------------------------------------------------


def click_OK():
    if button_ans.text() == 'Ответить':
        check_answer()
    else:
        next_question()


button_ans.clicked.connect(click_OK)


#-------------------------------------------------------
main_win.setLayout(m_line)


next_question()
main_win.show()
app.exec_()
#-------------------------------------------------------