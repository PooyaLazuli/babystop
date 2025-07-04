
import sys
import os
'''
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    import ctypes
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)
    sys.exit()
    '''
def shutdown_computer():
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write("\nTThe computer turned off.")
    if os.name == 'nt':  # ویندوز
        os.system("shutdown /s /t 0")
    else:  # لینوکس یا مک
        os.system("shutdown -h now")
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("\nThe program was executed.")
def close_app():
    root.destroy()
import time
import tkinter as tk

# اجرای مخفی (اختیاری)
import sys
import os
if os.name == 'nt':
    try:
        import win32gui, win32con
        the_window = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_window, win32con.SW_HIDE)
    except:
        pass
# صبر به مدت 1.5 ساعت (5400 ثانیه)
wait = 3600
time.sleep(wait) 
with open('log.txt','a',encoding='utf-8') as g:
    g.write(f'\nThe program crossed the {wait} second mark.')
# نمایش صفحه تمام‌صفحه با پیام بزرگ
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)  # این خط را اضافه کنید
root.configure(bg='white')

label = tk.Label(
    root,
    text=f"You used the computer for more than ({wait}) second!",
    font=("Far_Nazanin", 38, "bold"),
    fg="black",
    bg="white")
label.place(relx=0.5, rely=0.35, anchor='center') 
entry = tk.Entry(root,bg='gray')
entry.place(rely=0.807,relx=0.35)
def check_password(event=None):
    user_text = entry.get()
    if user_text == 'sesemibazsho':
        with open('log.txt','a',encoding='utf-8') as g:
            g.write('\nPooya used the code.')
        close_app()
entry.bind('<Return>', check_password)
btn = tk.Button(root, text='  Shut Down  ',command=shutdown_computer, fg="black", bg="gray")
btn.place(rely=0.80,relx=0.475)
root.mainloop()