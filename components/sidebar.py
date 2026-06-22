# # components/sidebar.py
# # Sidebar navigation component

# import tkinter as tk
# from config import COLORS
# from components.base import Component

# class Sidebar(Component):
#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             sidebar = tk.Frame(self._container, bg=COLORS['sidebar_bg'], width=240)
#             sidebar.pack(side=tk.LEFT, fill=tk.Y, expand=False)
#             sidebar.pack_propagate(False)

#             tk.Label(sidebar, text="Medica", font=('Tahoma',20,'bold'),
#                      bg=COLORS['sidebar_bg'], fg='white').pack(pady=(20,5))
#             tk.Label(sidebar, text="Sierra Leone", font=('Tahoma',11),
#                      bg=COLORS['sidebar_bg'], fg='#E8C4CE').pack(pady=(0,20))

#             for item in self.props.get('items', []):
#                 btn = tk.Button(sidebar, text=item.get('label', ''),
#                                 command=lambda i=item: self.props.get('on_navigate')(i),
#                                 bg=COLORS['sidebar_bg'], fg='white', font=('Tahoma',11),
#                                 relief=tk.FLAT, anchor='w', padx=20, pady=10,
#                                 activebackground=COLORS['sidebar_hover'], activeforeground='white',
#                                 bd=0, cursor='hand2')
#                 btn.pack(fill=tk.X, pady=2)

#             user = self.props.get('user')
#             if user:
#                 tk.Label(sidebar, text=f"User: {user['full_name']}",
#                          font=('Tahoma',10), bg=COLORS['sidebar_bg'], fg='#E8C4CE').pack(side=tk.BOTTOM, pady=10)