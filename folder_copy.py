import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder(title):
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=title)
    return folder

def copy_folders(source, destination):
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)

def main():
    source = select_folder("소스 폴더 선택")
    if not source:
        print("소스 폴더가 선택되지 않았습니다.")
        return

    destination = select_folder("대상 폴더 선택")
    if not destination:
        print("대상 폴더가 선택되지 않았습니다.")
        return

    try:
        copy_folders(source, destination)
        messagebox.showinfo("완료", "폴더 복사가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"오류 발생: {e}")

if __name__ == "__main__":
    main()