import tkinter as tk
from tkinter import ttk
from page import register_page
from page import file_name
# 主窗口
root = tk.Tk()
root.title("坦克大战 - 登录入口")
root.geometry("800x600")
root.resizable(False, False)

# 背景画布
canvas = tk.Canvas(root, width=800, height=600, bg="#1a1a2e")
canvas.place(x=0, y=0)

# 标题
canvas.create_text(400, 70, text="坦克大战 TANK BATTLE",
                   fill="#ffcc00", font=("黑体", 32, "bold"))

# 中间外框
canvas.create_rectangle(100, 160, 700, 460, outline="#4466bb", width=3)

# 用户名标签
lbl_user = tk.Label(root, text="用户名", bg="#1a1a2e", fg="white", font=("黑体", 14))
lbl_user.place(x=250, y=200)

# 用户名输入框
entry_user = ttk.Entry(root, font=("黑体", 14), width=20)
entry_user.place(x=350, y=200, width=200, height=35)

# 密码标签
lbl_pwd = tk.Label(root, text="密  码", bg="#1a1a2e", fg="white", font=("黑体", 14))
lbl_pwd.place(x=250, y=260)

# 密码输入框
entry_pwd = ttk.Entry(root, font=("黑体", 14), width=20, show="*")
entry_pwd.place(x=350, y=260, width=200, height=35)

# 登录按钮
btn_login = tk.Button(root, text="进入游戏", bg="#2e7d32", fg="white",
                      font=("黑体", 16, "bold"), relief=tk.RAISED, command=lambda : file_name.conformlogin(entry_user, entry_pwd, root=root))
btn_login.place(x=300, y=330, width=200, height=45)

# 注册按钮
btn_reg = tk.Button(root, text="注册账号", bg="#1976d2", fg="white",
                    font=("黑体", 14), command=register_page.register)
btn_reg.place(x=300, y=390, width=200, height=40)

# 底部版权
canvas.create_text(400, 520, text="© 2026 坦克大战小游戏",
                   fill="#888888", font=("黑体", 10))

# 简单坦克装饰（左边）
canvas.create_rectangle(80, 200, 160, 280, fill="#555555", outline="white")
canvas.create_polygon(120, 180, 100, 200, 140, 200, fill="red")

# 简单坦克装饰（右边）
canvas.create_rectangle(640, 200, 720, 280, fill="#555555", outline="white")
canvas.create_polygon(680, 180, 660, 200, 700, 200, fill="red")

root.mainloop()