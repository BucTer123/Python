import tkinter as tk
import tkinter.ttk as ttk

class pywork_ui:
  def new_window(screen_width, screen_height, name_window):
    root = tk.Tk()
    screen = screen_width + "x" + screen_height
    root.title(name_window)
    root.geometry(screen)

    root.mainloop()
  def ext():
    exit(0)
  def new_button(text_button):
    tk.Button(root, text=text_button)
  def new_label(text_label):
    tk.Label(root, text=text_label)
  def new_input(text_placeholder):
    text_input = tk.Label(root, text=text_placeholder)
    inputz = tk.Entry(root)
  def stylesheet(type_stylesheet):
    if type_stylesheet == "plastik":
      ttk.style("plastik")
    elif type_stylesheet == "adapta":
      ttk.style("adapta")
    elif type_stylesheet == "aquativo":
      ttk.style("aquativo")
    elif type_stylesheet == "arc":
      ttk.style("arc")
    elif type_stylesheet == "black":
      ttk.style("black")
    elif type_stylesheet == "blue":
      ttk.style("blue")
    elif type_stylesheet == "breeze":
      ttk.style("breeze")
    elif type_stylesheet == "clearlooks":
      ttk.style("clearlooks")
    elif type_stylesheet == "elegance":
      ttk.style("elegance")
    elif type_stylesheet == "equilix":
      ttk.style("equilix")
    elif type_stylesheet == "itft1":
      ttk.style("itft1")
    elif type_stylesheet == "keramic":
      ttk.style("keramic")
    elif type_stylesheet == "kroc":
      ttk.style("kroc")
    elif type_stylesheet == "radiance":
      ttk.style("radiance")
    elif type_stylesheet == "smog":
      ttk.style("smog")
    elif type_stylesheet == "winxpblue":
      ttk.style("winxpblue")
    elif type_stylesheet == "yaru":
      ttk.style("yaru")
      
