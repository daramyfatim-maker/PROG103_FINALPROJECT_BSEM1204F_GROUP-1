# # components/table.py
# # Table component with pagination and selection

# import tkinter as tk
# from tkinter import ttk
# from config import COLORS
# from components.base import Component

# class Table(Component):
#     def __init__(self, parent, props=None):
#         super().__init__(parent, props)
#         self.props.setdefault('columns', [])
#         self.props.setdefault('data', [])
#         self.props.setdefault('on_select', None)
#         self.props.setdefault('column_widths', {})
#         self.props.setdefault('height', 18)
#         self.selected_id = None

#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             style = ttk.Style()
#             style.theme_use('clam')
#             style.configure("Treeview",
#                             background=COLORS['tree_bg'],
#                             foreground=COLORS['tree_fg'],
#                             rowheight=28,
#                             font=('Tahoma',9))
#             style.configure("Treeview.Heading",
#                             background=COLORS['primary'],
#                             foreground='white',
#                             font=('Tahoma',10,'bold'))
#             style.map('Treeview',
#                       background=[('selected', COLORS['tree_selected'])],
#                       foreground=[('selected', 'white')])

#             cols = self.props.get('columns', [])
#             self.tree = ttk.Treeview(self._container, columns=cols, show='headings',
#                                      height=self.props.get('height', 18), style="Treeview")
#             widths = self.props.get('column_widths', {})
#             for col in cols:
#                 self.tree.heading(col, text=col)
#                 self.tree.column(col, width=widths.get(col, 100), anchor='w')

#             vsb = ttk.Scrollbar(self._container, orient='vertical', command=self.tree.yview)
#             hsb = ttk.Scrollbar(self._container, orient='horizontal', command=self.tree.xview)
#             self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
#             self.tree.grid(row=0, column=0, sticky='nsew')
#             vsb.grid(row=0, column=1, sticky='ns')
#             hsb.grid(row=1, column=0, sticky='ew')
#             self._container.grid_rowconfigure(0, weight=1)
#             self._container.grid_columnconfigure(0, weight=1)

#             if self.props.get('on_select'):
#                 self.tree.bind('<<TreeviewSelect>>', self._handle_select)

#             self._update_data()

#     def _update_data(self):
#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         for row in self.props.get('data', []):
#             self.tree.insert('', 'end', values=row)

#     def _handle_select(self, event):
#         sel = self.tree.selection()
#         if sel:
#             item = self.tree.item(sel[0])
#             self.selected_id = item['values'][0] if item['values'] else None
#             if self.props.get('on_select'):
#                 self.props['on_select'](item['values'])

#     def get_selected(self):
#         return self.selected_id

#     def update_data(self, data):
#         self.props['data'] = data
#         self._update_data()