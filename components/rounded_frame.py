# # components/rounded_frame.py
# # Rounded frame using canvas

# import tkinter as tk
# from config import COLORS

# def _create_rounded_rect(self, x1, y1, x2, y2, radius=10, **kwargs):
#     points = [x1+radius, y1,
#               x2-radius, y1,
#               x2, y1,
#               x2, y1+radius,
#               x2, y2-radius,
#               x2, y2,
#               x2-radius, y2,
#               x1+radius, y2,
#               x1, y2,
#               x1, y2-radius,
#               x1, y1+radius,
#               x1, y1]
#     return self.create_polygon(points, smooth=True, **kwargs)

# tk.Canvas.create_rounded_rectangle = _create_rounded_rect

# class RoundedFrame(tk.Frame):
#     def __init__(self, master, radius=10, bg=None, *args, **kwargs):
#         self.radius = radius
#         self.bg = bg if bg is not None else COLORS['card']
#         super().__init__(master, bg=self.bg, *args, **kwargs)
#         self.canvas = tk.Canvas(self, bg=self.bg, highlightthickness=0, bd=0)
#         self.canvas.pack(fill=tk.BOTH, expand=True)
#         self.bind("<Configure>", self._draw)
#         self._draw()

#     def _draw(self, event=None):
#         w = self.winfo_width()
#         h = self.winfo_height()
#         if w < 2*self.radius or h < 2*self.radius:
#             return
#         self.canvas.delete("all")
#         self.canvas.create_rounded_rectangle(0, 0, w, h, radius=self.radius,
#                                              fill=self.bg, outline=COLORS['card_border'], width=2)