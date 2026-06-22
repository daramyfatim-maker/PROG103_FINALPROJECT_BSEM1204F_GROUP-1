# # pages/reports_page.py
# # Reports page – generate PDF reports

# import tkinter as tk
# from tkinter import messagebox
# from config import COLORS
# from components.base import Component
# from components.calendar_picker import CalendarPicker

# class ReportsPage(Component):
#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             page = tk.Frame(self._container, bg=COLORS['background'])

#             tk.Label(page, text="Generate PDF Reports", font=('Tahoma',20,'bold'),
#                      bg=COLORS['background'], fg=COLORS['primary']).pack(pady=(40,20))

#             btn_frame = tk.Frame(page, bg=COLORS['background'])
#             btn_frame.pack(pady=20)

#             for period, label in [('weekly','Weekly Report'), ('monthly','Monthly Report'), ('yearly','Yearly Report')]:
#                 tk.Button(btn_frame, text=label, command=lambda p=period: self._gen_report(p),
#                           bg=COLORS['primary_light'], fg='white', font=('Tahoma',11,'bold'),
#                           relief=tk.FLAT, padx=30, pady=15, cursor='hand2').pack(side=tk.LEFT, padx=10)

#             custom_frame = tk.Frame(page, bg=COLORS['background'])
#             custom_frame.pack(pady=20)
#             tk.Label(custom_frame, text="Custom Range:", font=('Tahoma',12,'bold'),
#                      bg=COLORS['background'], fg=COLORS['primary']).pack(side=tk.LEFT, padx=(0,10))

#             self.start_date_var = tk.StringVar()
#             self.end_date_var = tk.StringVar()

#             tk.Button(custom_frame, text="Start Date", command=lambda: CalendarPicker(self._container, self._set_start_date),
#                       bg=COLORS['secondary'], fg='white', font=('Tahoma',9,'bold'),
#                       relief=tk.FLAT, padx=10, pady=5, cursor='hand2').pack(side=tk.LEFT, padx=5)
#             self.start_label = tk.Label(custom_frame, text="None", font=('Tahoma',9),
#                                         bg=COLORS['background'], fg=COLORS['text_light'])
#             self.start_label.pack(side=tk.LEFT, padx=5)

#             tk.Button(custom_frame, text="End Date", command=lambda: CalendarPicker(self._container, self._set_end_date),
#                       bg=COLORS['secondary'], fg='white', font=('Tahoma',9,'bold'),
#                       relief=tk.FLAT, padx=10, pady=5, cursor='hand2').pack(side=tk.LEFT, padx=10)
#             self.end_label = tk.Label(custom_frame, text="None", font=('Tahoma',9),
#                                       bg=COLORS['background'], fg=COLORS['text_light'])
#             self.end_label.pack(side=tk.LEFT, padx=5)

#             tk.Button(custom_frame, text="Generate Report", command=self._generate_custom_report,
#                       bg=COLORS['success'], fg='white', font=('Tahoma',11,'bold'),
#                       relief=tk.FLAT, padx=20, pady=8, cursor='hand2').pack(side=tk.LEFT, padx=20)

#             tk.Label(page, text="Reports include summary statistics, patient list, and a chart.",
#                      font=('Tahoma',11), bg=COLORS['background'], fg=COLORS['text_light']).pack(pady=20)

#             page.pack(fill=tk.BOTH, expand=True)

#     def _set_start_date(self, date_str):
#         self.start_date_var.set(date_str if date_str else '')
#         self.start_label.config(text=date_str if date_str else 'None')

#     def _set_end_date(self, date_str):
#         self.end_date_var.set(date_str if date_str else '')
#         self.end_label.config(text=date_str if date_str else 'None')

#     def _generate_custom_report(self):
#         start = self.start_date_var.get()
#         end = self.end_date_var.get()
#         if not start or not end:
#             messagebox.showwarning("Missing Dates", "Please select both dates.")
#             return
#         if start > end:
#             messagebox.showwarning("Invalid Range", "Start must be before end.")
#             return
#         fname = self.props.get('controller').generate_pdf_report('custom', start, end)
#         if fname:
#             messagebox.showinfo("Report", f"Report saved: {fname}")
#         else:
#             messagebox.showinfo("Report", "No data for this range.")

#     def _gen_report(self, period):
#         fname = self.props.get('controller').generate_pdf_report(period)
#         if fname:
#             messagebox.showinfo("Report", f"Report saved: {fname}")
#         else:
#             messagebox.showinfo("Report", "No data for this period.")