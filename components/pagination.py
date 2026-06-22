# # components/pagination.py
# # Pagination controls

# import tkinter as tk
# from config import COLORS
# from components.button import Button
# from components.base import Component

# class Pagination(Component):
#     def __init__(self, parent, props=None):
#         super().__init__(parent, props)
#         self.props.setdefault('current_page', 1)
#         self.props.setdefault('total_pages', 1)
#         self.props.setdefault('on_page_change', lambda: None)

#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             frame = tk.Frame(self._container, bg=COLORS['background'])
#             frame.pack(fill=tk.X, pady=5)

#             self.label = tk.Label(frame, text=self._get_label_text(),
#                                   font=('Tahoma',9), bg=COLORS['background'], fg=COLORS['text_light'])
#             self.label.pack(side=tk.LEFT, padx=5)

#             Button(frame, props={
#                 'text': 'Prev',
#                 'variant': 'primary_light',
#                 'size': 'small',
#                 'on_click': self._prev_page
#             }).mount(frame)

#             Button(frame, props={
#                 'text': 'Next',
#                 'variant': 'primary_light',
#                 'size': 'small',
#                 'on_click': self._next_page
#             }).mount(frame)

#     def _get_label_text(self):
#         current = self.props.get('current_page', 1)
#         total = self.props.get('total_pages', 1)
#         return f"Page {current} of {total}"

#     def _prev_page(self):
#         current = self.props.get('current_page', 1)
#         if current > 1:
#             self.props['current_page'] = current - 1
#             self.props.get('on_page_change')(self.props['current_page'])
#             self.render()

#     def _next_page(self):
#         current = self.props.get('current_page', 1)
#         total = self.props.get('total_pages', 1)
#         if current < total:
#             self.props['current_page'] = current + 1
#             self.props.get('on_page_change')(self.props['current_page'])
#             self.render()