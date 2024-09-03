import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def select_folder(title):
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=title)
    return folder

def copy_java_files(source, destination, file_extension='.java'):
    copied_files = 0
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(file_extension):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(destination, file)
                
                # 중복 파일 처리
                if os.path.exists(dst_path):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dst_path):
                        new_file = f"{base}_{counter}{extension}"
                        dst_path = os.path.join(destination, new_file)
                        counter += 1
                
                shutil.copy2(src_path, dst_path)
                copied_files += 1
    return copied_files

def main():
    source = select_folder("소스 폴더 선택")
    if not source:
        print("소스 폴더가 선택되지 않았습니다.")
        return

    destination = select_folder("대상 폴더 선택")
    if not destination:
        print("대상 폴더가 선택되지 않았습니다.")
        return

    # 파일 확장자 선택 (현재는 .java만 가능)
    root = tk.Tk()
    root.title("파일 확장자 선택")
    root.geometry("300x100")

    label = tk.Label(root, text="복사할 파일 확장자 선택:")
    label.pack(pady=10)

    extensions = ['.java']  # 나중에 다른 확장자 추가 가능
    extension_var = tk.StringVar(value=extensions[0])
    extension_combo = ttk.Combobox(root, textvariable=extension_var, values=extensions, state="readonly")
    extension_combo.pack()

    def on_select():
        nonlocal extension_var
        root.quit()

    select_button = tk.Button(root, text="선택", command=on_select)
    select_button.pack(pady=10)

    root.mainloop()
    root.destroy()

    selected_extension = extension_var.get()

    try:
        copied_files = copy_java_files(source, destination, selected_extension)
        messagebox.showinfo("완료", f"복사가 완료되었습니다. 총 {copied_files}개의 {selected_extension} 파일이 복사되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"오류 발생: {e}")

if __name__ == "__main__":
    main()