# # pages/home_page.py
# # Home page component

# import tkinter as tk
# from config import COLORS
# from components.base import Component
# from utils.helpers import get_status_count

# class HomePage(Component):
#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             page = tk.Frame(self._container, bg=COLORS['background'])

#             # Header
#             header = tk.Frame(page, bg=COLORS['primary'], height=130)
#             header.pack(fill=tk.X, pady=(0,15))
#             stripe = tk.Frame(header, bg=COLORS['secondary'], height=5)
#             stripe.pack(side=tk.BOTTOM, fill=tk.X)

#             user = self.props.get('user')
#             name = user['full_name'] if user else 'User'
#             tk.Label(header, text=f"Welcome back, {name}", font=('Tahoma',22,'bold'),
#                      bg=COLORS['primary'], fg='white').pack(pady=(25,0))
#             tk.Label(header, text="Here's your hospital management dashboard",
#                      font=('Tahoma',13), bg=COLORS['primary'], fg='#F5C6D0').pack()

#             # Stats cards
#             stats = self.props.get('stats', {})
#             card_frame = tk.Frame(page, bg=COLORS['background'])
#             card_frame.pack(fill=tk.X, pady=10, padx=10)

#             cards = [
#                 ('total', f"Total Patients: {stats.get('total', 0)}", COLORS['primary_light']),
#                 ('active', f"Active: {get_status_count('Active', stats)}", COLORS['success']),
#                 ('pending', f"Pending: {get_status_count('Pending', stats)}", COLORS['warning']),
#                 ('days', f"Days Active: {len(stats.get('daily', []))}", COLORS['secondary'])
#             ]
#             for i, (key, text, color) in enumerate(cards):
#                 card = tk.Frame(card_frame, bg=COLORS['card'], relief='ridge', bd=3, width=220, height=100)
#                 card.grid(row=0, column=i, padx=15, pady=10, sticky='nsew')
#                 card.grid_propagate(False)
#                 tk.Label(card, text=text, font=('Tahoma',16,'bold'),
#                          bg=COLORS['card'], fg=color).pack(pady=(25,0))
#             for i in range(4):
#                 card_frame.grid_columnconfigure(i, weight=1)

#             # Quick actions
#             tk.Label(page, text="Quick Actions", font=('Tahoma',18,'bold'),
#                      bg=COLORS['background'], fg=COLORS['primary']).pack(pady=(20,10))
#             action_frame = tk.Frame(page, bg=COLORS['background'])
#             action_frame.pack(pady=10)
#             for text, cmd, color in [
#                 ('Add Patient', lambda: self.props.get('navigate')('patients'), COLORS['success']),
#                 ('View Charts', lambda: self.props.get('navigate')('charts'), COLORS['primary_light']),
#                 ('Generate Report', lambda: self.props.get('navigate')('reports'), COLORS['secondary'])
#             ]:
#                 tk.Button(action_frame, text=text, command=cmd,
#                           bg=color, fg='white', font=('Tahoma',11,'bold'),
#                           relief=tk.FLAT, padx=25, pady=10, cursor='hand2').pack(side=tk.LEFT, padx=15)

#             # Recent patients
#             recent = self.props.get('recent', [])
#             if recent:
#                 tk.Label(page, text="Recently Registered", font=('Tahoma',14,'bold'),
#                          bg=COLORS['background'], fg=COLORS['primary']).pack(pady=(20,5))
#                 for name, date in recent:
#                     tk.Label(page, text=f"• {name}  ({date})", font=('Tahoma',10),
#                              bg=COLORS['background'], fg=COLORS['text_light']).pack(anchor=tk.W, padx=20, pady=2)

#             tk.Label(page, text="Medica v5.0 | Sierra Leone | Open Source",
#                      font=('Tahoma',9), bg=COLORS['background'], fg=COLORS['text_light']).pack(side=tk.BOTTOM, pady=10)

#             page.pack(fill=tk.BOTH, expand=True)