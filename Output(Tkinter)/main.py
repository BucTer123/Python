import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("WINDOW!")

    tk.Label(root, text="Hello World!").pack()

    root.mainloop()
    exit(0)

if __name__ == "__main__":
    main()