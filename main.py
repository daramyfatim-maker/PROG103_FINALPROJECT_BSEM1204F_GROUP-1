# # main.py
# # Entry point – starts the application

# import tkinter as tk
# from tkinter import messagebox
# from config import COLORS, apply_theme, current_theme
# from controllers.app_controller import Controller
# from components.sidebar import Sidebar
# from pages.home_page import HomePage
# from pages.patients_page import PatientsPage
# from pages.charts_page import ChartsPage
# from pages.reports_page import ReportsPage
# from pages.settings_page import SettingsPage
# from login_view import LoginView
# import sys

# class MedicaApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Medica Sierra Leone")
#         self.root.geometry("1400x850")
#         self.root.configure(bg=COLORS['background'])

#         self.controller = Controller()
#         self.current_page = 'home'
#         self.pages = {}

#         self._build_layout()
#         self._navigate('home')
#         self._center()

#     def _center(self):
#         w, h = 1400, 850
#         x = (self.root.winfo_screenwidth() // 2) - (w // 2)
#         y = (self.root.winfo_screenheight() // 2) - (h // 2)
#         self.root.geometry(f"{w}x{h}+{x}+{y}")

#     def _build_layout(self):
#         # Sidebar
#         self.sidebar_container = tk.Frame(self.root, bg=COLORS['sidebar_bg'])
#         self.sidebar_container.pack(side=tk.LEFT, fill=tk.Y)

#         role = self.controller.get_user_role()
#         items = []
#         if role in ['admin', 'doctor', 'nurse']:
#             items.append({'id': 'home', 'label': 'Home'})
#         if role in ['admin', 'doctor']:
#             items.append({'id': 'patients', 'label': 'Patients'})
#         if role in ['admin', 'doctor', 'nurse']:
#             items.append({'id': 'charts', 'label': 'Charts'})
#             items.append({'id': 'reports', 'label': 'Reports'})
#         if role == 'admin':
#             items.append({'id': 'settings', 'label': 'Settings'})
#         items.append({'id': 'logout', 'label': 'Logout'})

#         self.sidebar = Sidebar(self.sidebar_container, props={
#             'items': items,
#             'on_navigate': self._handle_navigation,
#             'user': self.controller.get_user()
#         })
#         self.sidebar.mount()

#         # Main content
#         self.main_container = tk.Frame(self.root, bg=COLORS['background'])
#         self.main_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#         self.content_container = tk.Frame(self.main_container, bg=COLORS['background'])
#         self.content_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

#     def _handle_navigation(self, item):
#         page_id = item.get('id')
#         if page_id == 'logout':
#             self._handle_logout()
#             return
#         self._navigate(page_id)

#     def _navigate(self, page_id):
#         self.current_page = page_id
#         stats = self.controller.get_stats()
#         recent = self.controller.get_recent_patients(5)

#         for widget in self.content_container.winfo_children():
#             widget.destroy()

#         if page_id == 'home':
#             HomePage(self.content_container, props={
#                 'user': self.controller.get_user(),
#                 'stats': stats,
#                 'recent': recent,
#                 'navigate': self._navigate
#             }).mount()

#         elif page_id == 'patients':
#             self.patients_page = PatientsPage(self.content_container, props={
#                 'controller': self.controller
#             }).mount()

#         elif page_id == 'charts':
#             ChartsPage(self.content_container, props={
#                 'stats': stats
#             }).mount()

#         elif page_id == 'reports':
#             ReportsPage(self.content_container, props={
#                 'controller': self.controller
#             }).mount()

#         elif page_id == 'settings':
#             SettingsPage(self.content_container, props={
#                 'controller': self.controller,
#                 'on_theme_change': self._handle_theme_change,
#                 'on_reset': lambda: self._navigate('home')
#             }).mount()

#     def _handle_theme_change(self, theme):
#         apply_theme(theme)
#         self.root.configure(bg=COLORS['background'])
#         self.main_container.configure(bg=COLORS['background'])
#         self.content_container.configure(bg=COLORS['background'])
#         # Rebuild sidebar and current page
#         self.sidebar_container.destroy()
#         self._build_layout()
#         self._navigate(self.current_page)

#     def _handle_logout(self):
#         if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
#             self.controller.logout()
#             self.root.destroy()
#             start_app()

# def start_app():
#     root = tk.Tk()
#     # Login view
#     controller = Controller()
#     def on_login():
#         root.destroy()
#         main_root = tk.Tk()
#         MedicaApp(main_root)
#         main_root.mainloop()
#     LoginView(root, controller, on_login)
#     root.mainloop()

# if __name__ == "__main__":
#     start_app()