# # components/button.py
# import tkinter as tk
# from config import COLORS
# from components.base import Component

# class Button(Component):
#     def __init__(self, parent, props=None):
#         super().__init__(parent, props)
#         self.props.setdefault('text', 'Button')
#         self.props.setdefault('command', lambda: None)
#         self.props.setdefault('variant', 'primary')
#         self.props.setdefault('size', 'medium')
#         self.variants = {
#             'primary': COLORS['primary'],
#             'primary_light': COLORS['primary_light'],
#             'secondary': COLORS['secondary'],
#             'success': COLORS['success'],
#             'warning': COLORS['warning'],
#             'accent': COLORS['accent'],
#             'text': 'transparent',
#         }

#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             bg = self.variants.get(self.props.get('variant'), COLORS['primary'])
#             fg = 'white' if bg != 'transparent' else COLORS['text']
#             btn = tk.Button(
#                 self._container,
#                 text=self.props.get('text'),
#                 command=self.props.get('command'),
#                 bg=bg,
#                 fg=fg,
#                 font=('Tahoma', self._get_font_size()),
#                 relief=tk.FLAT,
#                 padx=self._get_padding(),
#                 pady=self._get_padding('y'),
#                 cursor='hand2',
#                 width=self.props.get('width', 0)
#             )
#             btn.pack(side=tk.LEFT, padx=(2,2))
#             self._widget = btn

#     def _get_font_size(self):
#         sizes = {'small': 9, 'medium': 10, 'large': 12}
#         return sizes.get(self.props.get('size'), 10)

#     def _get_padding(self, axis='x'):
#         sizes = {'small': (8,4), 'medium': (12,6), 'large': (16,8)}
#         val = sizes.get(self.props.get('size'), (12,6))
#         return val[0] if axis == 'x' else val[1]