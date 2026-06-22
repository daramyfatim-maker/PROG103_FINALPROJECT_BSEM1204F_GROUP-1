# # controllers/app_controller.py
# # Controller – coordinates Model and Views

# import csv
# import os
# from models.database import Database
# from config import COLORS
# import matplotlib.pyplot as plt
# import numpy as np

# MATPLOTLIB = True

# try:
#     from reportlab.lib.pagesizes import letter
#     from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
#     from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
#     from reportlab.lib import colors
#     from reportlab.lib.units import inch
#     REPORTLAB = True
# except ImportError:
#     REPORTLAB = False

# class Controller:
#     def __init__(self):
#         self.db = Database()
#         self.current_user = None
#         self._observers = []
#         self.db.add_observer(self._notify_observers)

#     def _notify_observers(self, data):
#         for cb in self._observers:
#             try:
#                 cb(data)
#             except:
#                 pass

#     def add_observer(self, cb):
#         self._observers.append(cb)

#     def login(self, username, password):
#         user = self.db.authenticate(username, password)
#         if user:
#             self.current_user = user
#             return True
#         return False

#     def logout(self):
#         self.current_user = None

#     def get_user(self):
#         return self.current_user

#     def get_user_role(self):
#         if self.current_user:
#             return self.current_user['role']
#         return None

#     def get_all_patients(self, limit=None, offset=0):
#         return self.db.get_all_patients(limit, offset)

#     def get_patient_count(self):
#         return self.db.get_patient_count()

#     def get_patient(self, pid):
#         return self.db.get_patient(pid)

#     def add_patient(self, data):
#         return self.db.add_patient(data)

#     def update_patient(self, pid, data):
#         self.db.update_patient(pid, data)

#     def delete_patient(self, pid):
#         self.db.delete_patient(pid)

#     def search_patients(self, term=None, search_by='all', blood=None, date_from=None, date_to=None):
#         return self.db.search_patients(term, search_by, blood, date_from, date_to)

#     def get_visits(self, patient_id):
#         return self.db.get_visits(patient_id)

#     def add_visit(self, patient_id, data):
#         self.db.add_visit(patient_id, data)

#     def get_stats(self):
#         return self.db.get_stats()

#     def get_recent_patients(self, limit=5):
#         return self.db.get_recent_patients(limit)

#     def get_reports_data(self, period, start_date=None, end_date=None):
#         return self.db.get_reports_data(period, start_date, end_date)

#     def export_csv(self, patients, filename):
#         if not patients:
#             return False
#         with open(filename, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             writer.writerow(['ID','Full Name','Gender','Birth Date','Status','Created','Contact','Blood Type','Allergies'])
#             for p in patients:
#                 writer.writerow([p['id'], p['full_name'], p['gender'], p['birth_date'],
#                                  p['status'], p['created_date'], p['contact'], p['blood_type'], p['allergies']])
#         return True

#     def generate_pdf_report(self, period, start_date=None, end_date=None):
#         if not REPORTLAB:
#             return None
#         data = self.get_reports_data(period, start_date, end_date)
#         if not data['records']:
#             return None
#         os.makedirs("reports", exist_ok=True)
#         pname = "Custom Range" if period == 'custom' else period.capitalize()
#         fname = f"reports/medica_{period}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

#         doc = SimpleDocTemplate(fname, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24,
#                                      textColor=colors.darkblue, alignment=1, spaceAfter=20)
#         story.append(Paragraph("Medica Sierra Leone", title_style))
#         sub = ParagraphStyle('Sub', parent=styles['Heading2'], fontSize=16,
#                              textColor=colors.darkblue, alignment=1, spaceAfter=10)
#         story.append(Paragraph(f"{pname} Patient Report", sub))
#         date_style = ParagraphStyle('Date', parent=styles['Normal'], fontSize=10,
#                                     alignment=1, textColor=colors.grey)
#         story.append(Paragraph(f"Period: {data['start_date']} to {data['end_date']}", date_style))
#         story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", date_style))
#         story.append(Spacer(1, 0.3*inch))

#         story.append(Paragraph("Summary Statistics", styles['Heading3']))
#         story.append(Spacer(1, 0.1*inch))
#         sum_data = [
#             ['Metric','Value'],
#             ['Total Patients', str(data['total'])],
#             ['Male', str(data['gender_counts']['Male'])],
#             ['Female', str(data['gender_counts']['Female'])],
#             ['Other', str(data['gender_counts']['Other'])],
#             ['Active', str(data['status_counts']['Active'])],
#             ['Inactive', str(data['status_counts']['Inactive'])],
#             ['Pending', str(data['status_counts']['Pending'])]
#         ]
#         sum_table = Table(sum_data, colWidths=[2.5*inch, 1.5*inch])
#         sum_table.setStyle(TableStyle([
#             ('BACKGROUND',(0,0),(-1,0),colors.darkblue),
#             ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
#             ('ALIGN',(0,0),(-1,-1),'CENTER'),
#             ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
#             ('FONTSIZE',(0,0),(-1,0),11),
#             ('BOTTOMPADDING',(0,0),(-1,0),10),
#             ('BACKGROUND',(0,1),(-1,-1),colors.beige),
#             ('GRID',(0,0),(-1,-1),1,colors.black),
#         ]))
#         story.append(sum_table)
#         story.append(Spacer(1, 0.3*inch))

#         if MATPLOTLIB:
#             try:
#                 fig, ax = plt.subplots(figsize=(4,2.5))
#                 genders = ['Male','Female','Other']
#                 counts = [data['gender_counts'].get(g,0) for g in genders]
#                 ax.bar(genders, counts, color=['#2e86c1','#e74c3c','#95a5a6'])
#                 ax.set_title('Gender Distribution')
#                 ax.set_ylabel('Count')
#                 chart_file = f"reports/chart_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
#                 plt.savefig(chart_file, dpi=100, bbox_inches='tight')
#                 plt.close()
#                 story.append(Paragraph("Gender Distribution Chart", styles['Heading3']))
#                 story.append(Spacer(1, 0.1*inch))
#                 story.append(Image(chart_file, width=4*inch, height=2.5*inch))
#                 story.append(Spacer(1, 0.3*inch))
#             except:
#                 pass

#         story.append(Paragraph("Patient Records", styles['Heading3']))
#         story.append(Spacer(1, 0.1*inch))
#         table_data = [['ID','Full Name','Gender','Status','Date','Contact']]
#         for r in data['records']:
#             table_data.append([
#                 str(r['id']), r['full_name'], r['gender'], r['status'],
#                 r['created_date'], r['contact'] or 'N/A'
#             ])
#         pat_table = Table(table_data, colWidths=[0.6*inch,2*inch,0.8*inch,0.8*inch,1*inch,1.2*inch])
#         pat_table.setStyle(TableStyle([
#             ('BACKGROUND',(0,0),(-1,0),colors.darkblue),
#             ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
#             ('ALIGN',(0,0),(-1,-1),'CENTER'),
#             ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
#             ('FONTSIZE',(0,0),(-1,0),9),
#             ('BOTTOMPADDING',(0,0),(-1,0),8),
#             ('BACKGROUND',(0,1),(-1,-1),colors.white),
#             ('GRID',(0,0),(-1,-1),0.5,colors.grey),
#             ('FONTSIZE',(0,1),(-1,-1),8),
#         ]))
#         story.append(pat_table)
#         story.append(Spacer(1, 0.3*inch))

#         footer = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=9,
#                                 textColor=colors.grey, alignment=1)
#         story.append(Paragraph("Medica Sierra Leone – Open Source | MIT License", footer))

#         doc.build(story)
#         return fname