import sqlite3

import tkinter as tk

from tkinter.messagebox import showinfo


class Quiz:

    def __init__(self):

        self.conn = sqlite3.connect("quiz.db")

        self.cur = self.conn.cursor()

        self.quiz_id = "1"  # выбранная викторина

        self.questions = self.get_all_questions()

        self.select_answer = tk.StringVar()

        self.select_answer.set('')

        self.widgets = None

        self.question_content = tk.Label(

            height=5,

            width=70,

            bg="#ddd",

        )

        self.question_content.pack()

        self.btn_next = tk.Button(

            text="Начать викторину?", command=self.show_next_questions

        )

        self.btn_next.pack()

    def get_all_questions(self) -> list:

        res = self.cur.execute(

            "SELECT id, content, quiz_id FROM questions WHERE quiz_id=?", (self.quiz_id)

        )

        return res.fetchall()

    def show_next_questions(self):

        if self.select_answer.get() != '':

            self.result.append(self.select_answer.get())

        else:

            self.result = []

        self.btn_next["text"] = "Следующий вопрос"

        if len(self.questions) == 0:

            self.check_answers()

        else:

            next_question = self.questions.pop()

            self.question_content["text"] = f"Вопрос: {next_question[1]}"

            self.show_radiobuttons(next_question[0])

    def destroy_radiobuttons(self):

        if self.widgets is None:
            return

        for radiobtns in reversed(self.widgets):
            radiobtns.destroy()

    def check_answers(self):

        final_res = 0

        for i in self.result:
            answer, is_right = i.split(';')

            showinfo("Результат",

                     f"Ваш ответ: {answer}\nЭто верный ответ? {'Верный' if int(is_right) else 'Неверный'}")

            final_res += int(is_right)

        showinfo('Результат',

                 f"Всего вопросов: {len(self.result)}, Вы ответили верно на {final_res} вопросов")

    def show_radiobuttons(self, question_id: int):

        self.destroy_radiobuttons()

        res = self.cur.execute(

            "SELECT id, answer, is_right FROM answers WHERE question_id=?",

            (str(question_id)),

        )

        self.widgets = []

        for answer in res:
            self.widgets.append(

                tk.Radiobutton(

                    text=f"{answer[1]}", variable=self.select_answer, value=f"{answer[1]};{answer[2]}"

                )

            )

        for widget in self.widgets:
            widget.pack()


if __name__ == "__main__":
    root = tk.Tk()

    root.geometry('450x450')

    quiz = Quiz()

    root.mainloop()