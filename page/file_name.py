import json
import os
import tkinter as tk
import tkinter.messagebox as msgbox

def get_user_input(*entries):
    return [entry.get() for entry in entries]


def verify_user(*entries):
    values = get_user_input(*entries)

    if len(values) < 2:
        return False

    username, password = values[0], values[1]

    if not username or not password:
        return False

    filepath = r"data\users.json"

    if not os.path.exists(filepath):
        return False

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            users = json.loads(content) if content else []
    except Exception:
        return False

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False


def conformlogin(*entries, root=None):
    if verify_user(*entries):
        if root:
            root.destroy()
        import main
        main.main()
    else:
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        msgbox.showerror(
            title="警告",
            message="输入的密码或用户名错误"
        )




