import tkinter as tk
from src.vocabulary_trainer.ui.menu import VocabularyTrainerGUI


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
