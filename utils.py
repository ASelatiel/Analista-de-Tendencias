from os import path
import os, errno, sys, re
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def save():
    file = filedialog.asksaveasfile (initialdir="/", defaultextension='.pdf',filetypes=[("PDF",".pdf"),("Todos los archivos", ".*")])