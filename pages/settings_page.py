# # pages/settings_page.py
# # Settings page – theme switching and database reset

# import tkinter as tk
# from tkinter import ttk, messagebox
# from config import COLORS, apply_theme, current_theme
# from components.base import Component
# from models.database import Database
# import os
# import sys

# class SettingsPage(Component):
#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             page = tk.Frame(self._container, bg=COLORS['background'])

#             tk.Label(page, text="Settings", font=('Tahoma',20,'bold'),
#                      bg=COLORS['background'], fg=COLORS['primary']).pack(pady=(30,20))

#             theme_frame = tk.Frame(page, bg=COLORS['background'])
#             theme_frame.pack(fill=tk.X, pady=10, padx=40)
#             tk.Label(theme_frame, text="Theme:", font=('Tahoma',11,'bold'),
#                      bg=COLORS['background'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(0,20))
#             self.theme_var = tk.StringVar(value=current_theme)
#             theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var,
#                                        values=['light','dark'], font=('Tahoma',10), width=10, state='readonly')
#             theme_combo.pack(side=tk.LEFT)
#             theme_combo.bind('<<ComboboxSelected>>', lambda e: self.props.get('on_theme_change')(self.theme_var.get()))

#             reset_frame = tk.Frame(page, bg=COLORS['background'])
#             reset_frame.pack(fill=tk.X, pady=20, padx=40)
#             tk.Button(reset_frame, text="Reset Database (keep sample data)",
#                       command=self._handle_reset,
#                       bg=COLORS['warning'], fg='white', font=('Tahoma',10,'bold'),
#                       relief=tk.FLAT, padx=20, pady=8, cursor='hand2').pack(side=tk.LEFT)

#             tk.Label(page, text="System Information", font=('Tahoma',12,'bold'),
#                      bg=COLORS['background'], fg=COLORS['primary']).pack(pady=(30,10))
#             controller = self.props.get('controller')
#             info = f"Database: {controller.db.db_name}\nRecords: {len(controller.get_all_patients())}\nPython: {sys.version.split()[0]}\nTkinter: {tk.TkVersion}"
#             tk.Label(page, text=info, font=('Tahoma',10), bg=COLORS['background'],
#                      fg=COLORS['text_light'], justify=tk.LEFT).pack(pady=10, padx=40, anchor=tk.W)

#             page.pack(fill=tk.BOTH, expand=True)

#     def _handle_reset(self):
#         if messagebox.askyesno("Reset Database", "This will delete all patient records and reload sample data. Continue?"):
#             controller = self.props.get('controller')
#             controller.db.close()
#             db_path = controller.db.db_name
#             if os.path.exists(db_path):
#                 os.remove(db_path)
#             controller.db = Database(db_path)
#             controller.db.add_observer(controller._notify_observers)
#             controller.db.notify_observers({'action':'data_loaded'})
#             messagebox.showinfo("Reset", "Database has been reset with sample data.")
#             self.props.get('on_reset')()