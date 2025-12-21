import tkinter as tk
from src.vocabulary_trainer.ui.menu import VocabularyTrainerGUI
# Неправильный импорт. Вам нужно было правильно заполнить `src/vocabulary_trainer/__init__.py` и здесь импорт был бы:
# from vocabulary_trainer import VocabularyTrainerGUI


def main():
    root = tk.Tk()
    root.title("WordFlow")

    root.geometry("500x400")
    root.eval("tk::PlaceWindow . center")
    root.resizable(False, False)

    VocabularyTrainerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
