# # pages/charts_page.py
# # Charts page with Matplotlib visualisations

# import tkinter as tk
# from config import COLORS
# from components.base import Component
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# import numpy as np

# class ChartsPage(Component):
#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             page = tk.Frame(self._container, bg=COLORS['background'])
#             page.pack_propagate(False)
#             page.config(height=700)

#             stats = self.props.get('stats', {})
#             if not stats:
#                 tk.Label(page, text="No data available", font=('Tahoma',14),
#                          bg=COLORS['background'], fg=COLORS['text_light']).pack(expand=True)
#                 page.pack(fill=tk.BOTH, expand=True)
#                 return

#             fig_bg = COLORS['background']
#             text_color = COLORS['text']
#             fig = plt.Figure(figsize=(15,8), dpi=90, facecolor=fig_bg)
#             plt.rcParams['text.color'] = text_color
#             plt.rcParams['axes.labelcolor'] = text_color
#             plt.rcParams['xtick.color'] = text_color
#             plt.rcParams['ytick.color'] = text_color

#             # Gender bar
#             ax1 = fig.add_subplot(241)
#             gd = dict(stats.get('gender', []))
#             vals = [gd.get('Male',0), gd.get('Female',0), gd.get('Other',0)]
#             bars = ax1.bar(['Male','Female','Other'], vals, color=['#2e86c1','#e74c3c','#95a5a6'])
#             ax1.set_title('Gender', color=text_color)
#             ax1.set_ylabel('Count', color=text_color)
#             ax1.set_facecolor(fig_bg)
#             ax1.tick_params(colors=text_color)
#             for bar,v in zip(bars,vals):
#                 ax1.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, str(v), ha='center', va='bottom', color=text_color)

#             # Status bar
#             ax2 = fig.add_subplot(242)
#             sd = dict(stats.get('status', []))
#             vals = [sd.get('Active',0), sd.get('Inactive',0), sd.get('Pending',0)]
#             bars = ax2.bar(['Active','Inactive','Pending'], vals, color=['#27ae60','#e74c3c','#f39c12'])
#             ax2.set_title('Status', color=text_color)
#             ax2.set_ylabel('Count', color=text_color)
#             ax2.set_facecolor(fig_bg)
#             ax2.tick_params(colors=text_color)
#             for bar,v in zip(bars,vals):
#                 ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, str(v), ha='center', va='bottom', color=text_color)

#             # Age distribution
#             ax3 = fig.add_subplot(243)
#             age_groups = dict(stats.get('age_groups', []))
#             all_groups = ['0-17','18-30','31-50','51-65','65+']
#             counts = [age_groups.get(g,0) for g in all_groups]
#             bars = ax3.bar(all_groups, counts, color=['#3498db','#2ecc71','#f1c40f','#e67e22','#e74c3c'])
#             ax3.set_title('Age Distribution', color=text_color)
#             ax3.set_ylabel('Count', color=text_color)
#             ax3.set_facecolor(fig_bg)
#             ax3.tick_params(colors=text_color, rotation=45)
#             for bar,v in zip(bars,counts):
#                 ax3.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, str(v), ha='center', va='bottom', color=text_color)

#             # Gender pie
#             ax4 = fig.add_subplot(244)
#             if sum(vals)>0:
#                 ax4.pie([gd.get('Male',0), gd.get('Female',0), gd.get('Other',0)],
#                         labels=['Male','Female','Other'], colors=['#2e86c1','#e74c3c','#95a5a6'],
#                         autopct='%1.1f%%', startangle=90, textprops={'color':text_color})
#             ax4.set_title('Gender %', color=text_color)

#             # Status pie
#             ax5 = fig.add_subplot(245)
#             if sum(vals)>0:
#                 ax5.pie([sd.get('Active',0), sd.get('Inactive',0), sd.get('Pending',0)],
#                         labels=['Active','Inactive','Pending'], colors=['#27ae60','#e74c3c','#f39c12'],
#                         autopct='%1.1f%%', startangle=90, textprops={'color':text_color})
#             ax5.set_title('Status %', color=text_color)

#             # Daily registrations
#             ax6 = fig.add_subplot(246)
#             daily = stats.get('daily', [])
#             if daily:
#                 dates = [d[0] for d in daily]
#                 counts = [d[1] for d in daily]
#                 if len(dates)>30:
#                     dates=dates[-30:]; counts=counts[-30:]
#                 ax6.plot(dates, counts, marker='o', color=COLORS['primary'], linewidth=2)
#                 ax6.fill_between(dates, counts, alpha=0.25, color=COLORS['primary_light'])
#                 ax6.set_title('Daily Registrations (30d)', color=text_color)
#                 ax6.set_xlabel('Date', color=text_color)
#                 ax6.set_ylabel('Count', color=text_color)
#                 ax6.set_facecolor(fig_bg)
#                 ax6.tick_params(colors=text_color)
#                 plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, fontsize=8)
#                 if len(counts)>1:
#                     z = np.polyfit(range(len(counts)), counts, 1)
#                     trend = np.poly1d(z)
#                     ax6.plot(dates, trend(range(len(counts))), '--', color=COLORS['accent'], label='Trend')
#                     ax6.legend(facecolor=fig_bg, edgecolor=COLORS['border'], labelcolor=text_color)

#             # Visits per day
#             ax7 = fig.add_subplot(247)
#             visits = stats.get('visits_daily', [])
#             if visits:
#                 dates = [v[0] for v in visits]
#                 counts = [v[1] for v in visits]
#                 ax7.bar(dates, counts, color=COLORS['secondary'], edgecolor='none')
#                 ax7.set_title('Visits per Day (30d)', color=text_color)
#                 ax7.set_xlabel('Date', color=text_color)
#                 ax7.set_ylabel('Visits', color=text_color)
#                 ax7.set_facecolor('none')
#                 ax7.tick_params(colors=text_color)
#                 plt.setp(ax7.xaxis.get_majorticklabels(), rotation=45, fontsize=8)
#             else:
#                 ax7.text(0.5,0.5,'No visit data', ha='center', va='center', color=text_color, transform=ax7.transAxes)
#                 ax7.set_title('Visits per Day', color=text_color)
#                 ax7.set_facecolor('none')

#             # Summary
#             ax8 = fig.add_subplot(248)
#             ax8.axis('off')
#             summary = f"""
#     Summary
#     Total: {stats.get('total', 0)}
#     Gender: M {gd.get('Male',0)}  F {gd.get('Female',0)}  O {gd.get('Other',0)}
#     Status: A {sd.get('Active',0)}  I {sd.get('Inactive',0)}  P {sd.get('Pending',0)}
#     Days: {len(daily)}
#     Visits: {sum(c for _,c in stats.get('visits_daily', []))}
#             """
#             ax8.text(0.1,0.9, summary, transform=ax8.transAxes, fontsize=9,
#                      verticalalignment='top', fontfamily='monospace',
#                      bbox=dict(boxstyle='round', facecolor=COLORS['card'], alpha=0.9, edgecolor=COLORS['border']),
#                      color=text_color)

#             fig.tight_layout(pad=3.0)

#             container = tk.Frame(page, bg=COLORS['background'])
#             container.pack(fill=tk.BOTH, expand=True)

#             canvas = FigureCanvasTkAgg(fig, master=container)
#             toolbar = NavigationToolbar2Tk(canvas, container)
#             toolbar.update()
#             toolbar.pack(side=tk.TOP, fill=tk.X)
#             canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

#             page.pack(fill=tk.BOTH, expand=True)