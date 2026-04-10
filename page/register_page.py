import tkinter as tk
from tkinter import ttk
import json
import os
# class RegisterPage:
#     def __init__(self):
#         pass


def register():
    # 创建注册窗口
    window=tk.Tk()
    window.title("注册页面")
    window.geometry("800x600")
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=800, height=600, bg="#1a1a2e")
    canvas.place(x=0, y=0)

    # 标题
    canvas.create_text(400, 70, text="坦克大战 - 注册入口",
                       fill="#ffcc00", font=("黑体", 32, "bold"))

    canvas.create_rectangle(100, 160, 700, 460, outline="#4466bb", width=3)

    # 用户名标签
    lbl_user = tk.Label(window, text="用户名", bg="#1a1a2e", fg="white", font=("黑体", 14))
    lbl_user.place(x=250, y=200)

    entry_user = ttk.Entry(window, font=("黑体", 14), width=20)
    entry_user.place(x=350, y=200, width=200, height=35)

    # 密码标签
    lbl_pwd = tk.Label(window, text="密  码", bg="#1a1a2e", fg="white", font=("黑体", 14))
    lbl_pwd.place(x=250, y=260)

    entry_pwd = ttk.Entry(window, font=("黑体", 14), width=20, show="*")
    entry_pwd.place(x=350, y=260, width=200, height=35)

    def do_register():
        username = entry_user.get()
        password = entry_pwd.get()
        filepath = r"C:\Users\星河\Desktop\模拟\data\users.json"
        # os.makedirs(os.path.dirname(filepath), exist_ok=True)
        users = []
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    users = json.loads(content)

        users.append({"username": username, "password": password})
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
        window.destroy()

    # 注册按钮
    btn_reg = tk.Button(window, text="确定注册", bg="#1976d2", fg="white",command=do_register)
    btn_reg.place(x=300, y=330, width=200, height=45)

    window.mainloop()
