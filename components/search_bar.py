# # components/search_bar.py
# # Search bar with dropdown and date range

# import tkinter as tk
# from tkinter import ttk
# from config import COLORS
# from components.button import Button
# from components.base import Component

# class SearchBar(Component):
#     def __init__(self, parent, props=None):
#         super().__init__(parent, props)
#         self.props.setdefault('on_search', lambda: None)
#         self.props.setdefault('on_clear', lambda: None)
#         self.props.setdefault('search_by_options', ['all','name','id','status','gender','blood'])
#         self.props.setdefault('blood_options', ['All','A+','A-','B+','B-','O+','O-','AB+','AB-'])

#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             frame = tk.Frame(self._container, bg=COLORS['card'], relief=tk.RAISED, bd=1)
#             frame.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

#             tk.Label(frame, text="Search:", font=('Tahoma',9,'bold'),
#                      bg=COLORS['card'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(5,5))
#             self.search_entry = tk.Entry(frame, font=('Tahoma',10), width=18,
#                                          relief=tk.FLAT, bg=COLORS['background'], fg=COLORS['text'])
#             self.search_entry.pack(side=tk.LEFT, padx=(0,8))

#             tk.Label(frame, text="by:", font=('Tahoma',9),
#                      bg=COLORS['card'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(5,5))
#             self.search_by_var = tk.StringVar(value='all')
#             search_by_menu = ttk.Combobox(frame, textvariable=self.search_by_var,
#                                           values=self.props.get('search_by_options'),
#                                           font=('Tahoma',9), width=8, state='readonly')
#             search_by_menu.pack(side=tk.LEFT, padx=(0,8))

#             tk.Label(frame, text="Blood:", font=('Tahoma',9),
#                      bg=COLORS['card'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(10,5))
#             self.blood_var = tk.StringVar(value='All')
#             blood_menu = ttk.Combobox(frame, textvariable=self.blood_var,
#                                       values=self.props.get('blood_options'),
#                                       font=('Tahoma',9), width=6, state='readonly')
#             blood_menu.pack(side=tk.LEFT, padx=(0,8))

#             tk.Label(frame, text="Date from:", font=('Tahoma',9),
#                      bg=COLORS['card'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(10,5))
#             self.date_from = tk.Entry(frame, font=('Tahoma',10), width=10,
#                                       relief=tk.FLAT, bg=COLORS['background'], fg=COLORS['text'])
#             self.date_from.pack(side=tk.LEFT, padx=(0,5))
#             tk.Label(frame, text="to:", font=('Tahoma',9),
#                      bg=COLORS['card'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(5,5))
#             self.date_to = tk.Entry(frame, font=('Tahoma',10), width=10,
#                                     relief=tk.FLAT, bg=COLORS['background'], fg=COLORS['text'])
#             self.date_to.pack(side=tk.LEFT, padx=(0,8))

#             Button(frame, props={
#                 'text': 'Search',
#                 'variant': 'primary_light',
#                 'size': 'small',
#                 'on_click': self._handle_search
#             }).mount(frame)

#             Button(frame, props={
#                 'text': 'Clear',
#                 'variant': 'text',
#                 'size': 'small',
#                 'on_click': self._handle_clear
#             }).mount(frame)

#     def _handle_search(self):
#         self.props.get('on_search')({
#             'term': self.search_entry.get().strip(),
#             'search_by': self.search_by_var.get(),
#             'blood': self.blood_var.get() if self.blood_var.get() != 'All' else None,
#             'date_from': self.date_from.get().strip(),
#             'date_to': self.date_to.get().strip()
#         })

#     def _handle_clear(self):
#         self.search_entry.delete(0, tk.END)
#         self.blood_var.set('All')
#         self.date_from.delete(0, tk.END)
#         self.date_to.delete(0, tk.END)
#         self.props.get('on_clear')()