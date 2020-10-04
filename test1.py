import tkinter.ttk as _ttk
import tkinter as _tk

class QEntry(_ttk.Widget):
    def __init__(self, master):
        super(QEntry, self).__init__(master, "ttk::entry", {"class": "TEntry", "style": "QEntry"})


def init(widget=None):
    flat = "flat"

    s = _ttk.Style()
    s.theme_create("QUI", "default")
    s.theme_use("QUI")
    s.layout("QEntry", [('Entry.highlight', {'border': 0,'sticky': 'nswe','children': [('Entry.border', {'border': 0,'sticky': 'nswe','children': [('Entry.padding', {'sticky': 'nswe','children': [('Entry.textarea', {'sticky': 'nswe','border': 0})]})]}), ('Entry.bd', {'sticky': 'nswe','border': 0,'children': [('Entry.padding', {'sticky': 'nswe','children': [('Entry.textarea', {'sticky': 'nswe'})]})]})]})])
    s.theme_settings("QUI", {"QEntry": {"configure": {"padding": 4},"map": {"relief": [("active", flat),("focus", flat),("!disabled", flat),("disabled", flat)],"background": [("active", "#00afaf"),("focus", "#6f6f6f"),("!disabled", "#6f6f6f"),("disabled", "#8f8f8f")],"bordercolor": [("active", "#00afaf"),("focus", "#00afaf"),("!disabled", "#6f6f6f"),("disabled", "#5f5f5f")],"foreground": [("active", "#ffffff"),("focus", "#ffffff"),("!disabled", "#afafaf"),("disabled", "#5f5f5f")],}}})

if __name__ == '__main__':
    root = _tk.Tk()
    root.wm_minsize(200, 150)
    init(root)

    frame = _tk.Frame(root)
    entry = QEntry(frame)
    entry.pack(pady=1)
    frame.pack(fill="both", expand=True)

    root.mainloop()
