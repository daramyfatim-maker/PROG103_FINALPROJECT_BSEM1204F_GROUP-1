# # components/calendar_picker.py
# # Calendar picker modal component

# import tkinter as tk
# from tkinter import ttk
# import calendar
# from datetime import datetime
# from config import COLORS

# class CalendarPicker:
#     def __init__(self, master, callback, initial_date=None):
#         self.master = master
#         self.callback = callback
#         self.window = tk.Toplevel(master)
#         self.window.title("Select Date")
#         self.window.resizable(False, False)
#         self.window.configure(bg=COLORS['background'])
#         self.window.grab_set()

#         self.year = datetime.now().year
#         self.month = datetime.now().month
#         if initial_date:
#             try:
#                 dt = datetime.strptime(initial_date, '%Y-%m-%d')
#                 self.year = dt.year
#                 self.month = dt.month
#             except:
#                 pass

#         self.selected_date = initial_date
#         self.build()
#         self.center()

#     def center(self):
#         self.window.update_idletasks()
#         w = self.window.winfo_width()
#         h = self.window.winfo_height()
#         x = (self.window.winfo_screenwidth() // 2) - (w // 2)
#         y = (self.window.winfo_screenheight() // 2) - (h // 2)
#         self.window.geometry(f"{w}x{h}+{x}+{y}")

#     def build(self):
#         container = tk.Frame(self.window, bg=COLORS['background'], padx=10, pady=10)
#         container.pack(fill=tk.BOTH, expand=True)

#         self.date_label = tk.Label(container, text="Selected: " + (self.selected_date or "None"),
#                                    font=('Tahoma',11,'bold'), bg=COLORS['background'], fg=COLORS['text'])
#         self.date_label.pack(pady=(0,10))

#         nav = tk.Frame(container, bg=COLORS['background'])
#         nav.pack(fill=tk.X, pady=5)

#         tk.Button(nav, text="◀", command=self.prev_month,
#                   bg=COLORS['primary_light'], fg='white', relief=tk.FLAT, padx=10, cursor='hand2').pack(side=tk.LEFT)

#         self.month_var = tk.StringVar(value=calendar.month_name[self.month])
#         month_menu = ttk.Combobox(nav, textvariable=self.month_var,
#                                   values=list(calendar.month_name)[1:], width=8, state='readonly')
#         month_menu.pack(side=tk.LEFT, padx=5)
#         month_menu.bind('<<ComboboxSelected>>', lambda e: self.change_month())

#         self.year_var = tk.StringVar(value=str(self.year))
#         year_menu = ttk.Combobox(nav, textvariable=self.year_var,
#                                  values=[str(y) for y in range(1900, 2101)], width=6, state='readonly')
#         year_menu.pack(side=tk.LEFT, padx=5)
#         year_menu.bind('<<ComboboxSelected>>', lambda e: self.change_year())

#         tk.Button(nav, text="▶", command=self.next_month,
#                   bg=COLORS['primary_light'], fg='white', relief=tk.FLAT, padx=10, cursor='hand2').pack(side=tk.LEFT)

#         tk.Button(nav, text="Today", command=self.go_today,
#                   bg=COLORS['secondary'], fg='white', relief=tk.FLAT, padx=10, cursor='hand2').pack(side=tk.LEFT, padx=10)

#         self.cal_frame = tk.Frame(container, bg=COLORS['background'])
#         self.cal_frame.pack(pady=10)
#         self.draw_days()

#         action_frame = tk.Frame(container, bg=COLORS['background'])
#         action_frame.pack(pady=10)
#         tk.Button(action_frame, text="Clear", command=self.clear_date,
#                   bg=COLORS['text_light'], fg='white', font=('Tahoma',10,'bold'),
#                   relief=tk.FLAT, padx=20, pady=5, cursor='hand2').pack(side=tk.LEFT, padx=10)
#         tk.Button(action_frame, text="Cancel", command=self.window.destroy,
#                   bg=COLORS['accent'], fg='white', font=('Tahoma',10,'bold'),
#                   relief=tk.FLAT, padx=20, pady=5, cursor='hand2').pack(side=tk.LEFT)

#     def draw_days(self):
#         for widget in self.cal_frame.winfo_children():
#             widget.destroy()

#         days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
#         for i, d in enumerate(days):
#             tk.Label(self.cal_frame, text=d, font=('Tahoma',9,'bold'),
#                      bg=COLORS['background'], fg=COLORS['text']).grid(row=0, column=i, padx=2, pady=2)

#         cal = calendar.monthcalendar(self.year, self.month)
#         for row_idx, week in enumerate(cal):
#             for col_idx, day in enumerate(week):
#                 if day == 0:
#                     continue
#                 btn = tk.Button(self.cal_frame, text=str(day), width=4,
#                                 bg=COLORS['card'], fg=COLORS['text'],
#                                 relief=tk.FLAT, cursor='hand2',
#                                 command=lambda d=day: self.select_date(d))
#                 btn.grid(row=row_idx+1, column=col_idx, padx=2, pady=2)
#                 if (day == datetime.now().day and self.month == datetime.now().month and
#                     self.year == datetime.now().year):
#                     btn.config(bg=COLORS['primary_light'], fg='white')
#                 if self.selected_date:
#                     try:
#                         sel = datetime.strptime(self.selected_date, '%Y-%m-%d')
#                         if sel.year == self.year and sel.month == self.month and sel.day == day:
#                             btn.config(bg=COLORS['success'], fg='white')
#                     except:
#                         pass

#     def change_month(self):
#         month_name = self.month_var.get()
#         if month_name:
#             self.month = list(calendar.month_name).index(month_name)
#             self.draw_days()

#     def change_year(self):
#         try:
#             self.year = int(self.year_var.get())
#             self.draw_days()
#         except:
#             pass

#     def prev_month(self):
#         if self.month == 1:
#             self.month = 12
#             self.year -= 1
#         else:
#             self.month -= 1
#         self.update_controls()
#         self.draw_days()

#     def next_month(self):
#         if self.month == 12:
#             self.month = 1
#             self.year += 1
#         else:
#             self.month += 1
#         self.update_controls()
#         self.draw_days()

#     def go_today(self):
#         today = datetime.now()
#         self.year = today.year
#         self.month = today.month
#         self.update_controls()
#         self.draw_days()

#     def update_controls(self):
#         self.month_var.set(calendar.month_name[self.month])
#         self.year_var.set(str(self.year))

#     def select_date(self, day):
#         date_str = f"{self.year:04d}-{self.month:02d}-{day:02d}"
#         self.selected_date = date_str
#         self.date_label.config(text=f"Selected: {date_str}")
#         self.draw_days()
#         self.callback(date_str)
#         self.window.destroy()

#     def clear_date(self):
#         self.selected_date = None
#         self.date_label.config(text="Selected: None")
#         self.callback(None)
#         self.window.destroy()