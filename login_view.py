# # login_view.py
# # Login view – standalone

# import tkinter as tk
# from config import COLORS

# class LoginView:
#     def __init__(self, root, controller, on_success):
#         self.root = root
#         self.controller = controller
#         self.on_success = on_success
#         self.root.title("Medica Sierra Leone - Login")
#         self.root.geometry("500x450")
#         self.root.resizable(False, False)
#         self.root.configure(bg=COLORS['background'])
#         self.center()
#         self.build()

#     def center(self):
#         w, h = 500, 450
#         x = (self.root.winfo_screenwidth() // 2) - (w // 2)
#         y = (self.root.winfo_screenheight() // 2) - (h // 2)
#         self.root.geometry(f"{w}x{h}+{x}+{y}")

#     def build(self):
#         card = tk.Frame(self.root, bg='white', relief=tk.RAISED, bd=2)
#         card.place(relx=0.5, rely=0.5, anchor='center', width=420, height=380)

#         header = tk.Frame(card, bg=COLORS['primary'], height=100)
#         header.pack(fill=tk.X)
#         accent = tk.Frame(header, bg=COLORS['secondary'], height=4)
#         accent.pack(side=tk.BOTTOM, fill=tk.X)

#         tk.Label(header, text="🏥", font=('Tahoma',24), bg=COLORS['primary'], fg='white').pack(pady=(5,0))
#         tk.Label(header, text="Medica Sierra Leone", font=('Tahoma',18,'bold'),
#                  bg=COLORS['primary'], fg='white').pack()
#         tk.Label(header, text="Hospital Management System", font=('Tahoma',10),
#                  bg=COLORS['primary'], fg='#F5C6D0').pack()

#         form = tk.Frame(card, bg='white', padx=35, pady=25)
#         form.pack(fill=tk.BOTH, expand=True)

#         tk.Label(form, text="Username", font=('Tahoma',10,'bold'),
#                  bg='white', fg=COLORS['text']).pack(anchor=tk.W, pady=(0,3))
#         self.username = tk.Entry(form, font=('Tahoma',11), bg='#F8F4F5',
#                                  relief=tk.FLAT, highlightthickness=1,
#                                  highlightcolor=COLORS['primary_light'],
#                                  highlightbackground=COLORS['border'])
#         self.username.pack(fill=tk.X, pady=(0,15), ipady=6)
#         self.username.insert(0, 'admin')

#         tk.Label(form, text="Password", font=('Tahoma',10,'bold'),
#                  bg='white', fg=COLORS['text']).pack(anchor=tk.W, pady=(0,3))
#         self.password = tk.Entry(form, font=('Tahoma',11), bg='#F8F4F5',
#                                  relief=tk.FLAT, highlightthickness=1,
#                                  highlightcolor=COLORS['primary_light'],
#                                  highlightbackground=COLORS['border'], show='*')
#         self.password.pack(fill=tk.X, pady=(0,20), ipady=6)
#         self.password.insert(0, 'admin123')

#         login_btn = tk.Button(form, text="Login", command=self.do_login,
#                               bg=COLORS['primary'], fg='white',
#                               font=('Tahoma',11,'bold'), relief=tk.FLAT,
#                               padx=40, pady=8, cursor='hand2')
#         login_btn.pack(pady=5)

#         self.status = tk.Label(form, text="", font=('Tahoma',9),
#                                bg='white', fg=COLORS['accent'])
#         self.status.pack(pady=5)

#         tk.Label(form, text="Default: admin / admin123", font=('Tahoma',8),
#                  bg='white', fg=COLORS['text_light']).pack()

#         self.root.bind('<Return>', lambda e: self.do_login())

#     def do_login(self):
#         u = self.username.get().strip()
#         p = self.password.get().strip()
#         if not u or not p:
#             self.status.config(text="Please enter both")
#             return
#         if self.controller.login(u, p):
#             self.status.config(text="Login successful!", fg=COLORS['success'])
#             self.root.after(500, self.on_success)
#         else:
#             self.status.config(text="Invalid credentials")
#             self.password.delete(0, tk.END)