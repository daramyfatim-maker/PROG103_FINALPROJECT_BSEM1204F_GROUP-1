# # pages/patients_page.py
# # Patients page with CRUD, search, pagination

# import tkinter as tk
# from tkinter import ttk, messagebox, filedialog
# from config import COLORS
# from components.base import Component
# from components.button import Button
# from components.table import Table
# from components.search_bar import SearchBar
# from components.pagination import Pagination
# from components.calendar_picker import CalendarPicker
# from utils.helpers import calculate_age, validate_contact
# import re

# class PatientsPage(Component):
#     def __init__(self, parent, props=None):
#         super().__init__(parent, props)
#         self.state = {
#             'patients': [],
#             'total': 0,
#             'offset': 0,
#             'limit': 20,
#             'selected_id': None,
#             'search_results': None
#         }

#     def render(self):
#         if self._container and self._mounted:
#             for widget in self._container.winfo_children():
#                 widget.destroy()

#             page = tk.Frame(self._container, bg=COLORS['background'])
#             self._build_form(page)
#             self._build_search_bar(page)
#             self._build_table(page)
#             self._build_pagination(page)
#             page.pack(fill=tk.BOTH, expand=True)

#     def _build_form(self, parent):
#         top = tk.Frame(parent, bg=COLORS['background'])
#         top.pack(fill=tk.X, pady=(0,5))

#         form = tk.Frame(top, bg=COLORS['card'], relief=tk.RAISED, bd=1)
#         form.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10), ipadx=10, ipady=10)

#         row1 = tk.Frame(form, bg=COLORS['card'])
#         row1.pack(fill=tk.X, pady=2)
#         row2 = tk.Frame(form, bg=COLORS['card'])
#         row2.pack(fill=tk.X, pady=2)

#         def make_label(text):
#             return tk.Label(row1, text=text, font=('Tahoma',9,'bold'), bg=COLORS['card'], fg=COLORS['text'])
#         def make_entry():
#             return tk.Entry(row1, font=('Tahoma',10), width=15, relief=tk.FLAT,
#                             bg=COLORS['background'], fg=COLORS['text'])

#         make_label("Name").pack(side=tk.LEFT, padx=(0,5))
#         self.entry_name = make_entry()
#         self.entry_name.pack(side=tk.LEFT, padx=(0,10))

#         make_label("Gender").pack(side=tk.LEFT, padx=(0,5))
#         self.gender_var = tk.StringVar(value='Male')
#         for g in ['Male','Female','Other']:
#             tk.Radiobutton(row1, text=g, variable=self.gender_var, value=g,
#                            bg=COLORS['card'], fg=COLORS['text'], selectcolor='#d4e6f1',
#                            font=('Tahoma',9)).pack(side=tk.LEFT, padx=(0,5))

#         make_label("Status").pack(side=tk.LEFT, padx=(0,5))
#         self.status_var = tk.StringVar(value='Active')
#         for s in ['Active','Inactive','Pending']:
#             tk.Radiobutton(row1, text=s, variable=self.status_var, value=s,
#                            bg=COLORS['card'], fg=COLORS['text'], selectcolor='#d4e6f1',
#                            font=('Tahoma',9)).pack(side=tk.LEFT, padx=(0,5))

#         make_label("Blood").pack(side=tk.LEFT, padx=(0,5))
#         self.blood_var = tk.StringVar(value='O+')
#         blood_combo = ttk.Combobox(row1, textvariable=self.blood_var,
#                                    values=['A+','A-','B+','B-','O+','O-','AB+','AB-'],
#                                    font=('Tahoma',9), width=5, state='readonly')
#         blood_combo.pack(side=tk.LEFT, padx=(0,5))

#         make_label("Birth").pack(side=tk.LEFT, padx=(0,5))
#         self.birth_date_var = tk.StringVar()
#         self.birth_btn = tk.Button(row1, text="Select", command=self._pick_birth_date,
#                                    bg=COLORS['primary_light'], fg='white', font=('Tahoma',9,'bold'),
#                                    relief=tk.FLAT, padx=5, pady=2, cursor='hand2')
#         self.birth_btn.pack(side=tk.LEFT, padx=(0,5))
#         self.birth_label = tk.Label(row1, text="None", font=('Tahoma',9), bg=COLORS['card'], fg=COLORS['text_light'])
#         self.birth_label.pack(side=tk.LEFT, padx=(0,5))

#         make_label("Contact").pack(side=tk.LEFT, padx=(0,5))
#         self.entry_contact = make_entry()
#         self.entry_contact.pack(side=tk.LEFT, padx=(0,5))

#         for text, cmd, color in [
#             ('Add', self._handle_add, COLORS['success']),
#             ('Update', self._handle_update, COLORS['primary_light']),
#             ('Delete', self._handle_delete, COLORS['accent']),
#             ('Clear', self._clear_form, COLORS['text_light']),
#             ('Export CSV', self._handle_export, COLORS['secondary'])
#         ]:
#             tk.Button(row2, text=text, command=cmd,
#                       bg=color, fg='white', font=('Tahoma',9,'bold'),
#                       relief=tk.FLAT, padx=10, pady=3, cursor='hand2').pack(side=tk.LEFT, padx=(0,5))

#     def _build_search_bar(self, parent):
#         container = tk.Frame(parent, bg=COLORS['background'])
#         container.pack(fill=tk.X, pady=5)
#         SearchBar(container, props={
#             'on_search': self._handle_search,
#             'on_clear': self._handle_clear_search
#         }).mount(container)

#     def _build_table(self, parent):
#         container = tk.Frame(parent, bg=COLORS['background'])
#         container.pack(fill=tk.BOTH, expand=True, pady=5)

#         columns = ['ID','Full Name','Gender','Birth','Status','Blood','Contact','Created']
#         widths = {'ID':50,'Full Name':180,'Gender':80,'Birth':90,
#                   'Status':90,'Blood':70,'Contact':100,'Created':110}

#         self.table = Table(container, props={
#             'columns': columns,
#             'data': [],
#             'column_widths': widths,
#             'height': 18,
#             'on_select': self._handle_select
#         })
#         self.table.mount()

#     def _build_pagination(self, parent):
#         container = tk.Frame(parent, bg=COLORS['background'])
#         container.pack(fill=tk.X, pady=5)
#         self.pagination = Pagination(container, props={
#             'current_page': 1,
#             'total_pages': 1,
#             'on_page_change': self._handle_page_change
#         })
#         self.pagination.mount()

#     def _pick_birth_date(self):
#         CalendarPicker(self._container, self._set_birth_date, initial_date=self.birth_date_var.get())

#     def _set_birth_date(self, date_str):
#         self.birth_date_var.set(date_str if date_str else '')
#         self.birth_label.config(text=date_str if date_str else 'None')

#     def _handle_select(self, values):
#         if values:
#             self.state['selected_id'] = values[0]
#             p = self.props.get('controller').get_patient(values[0])
#             if p:
#                 self.entry_name.delete(0, tk.END)
#                 self.entry_name.insert(0, p['full_name'])
#                 self.gender_var.set(p['gender'])
#                 self.birth_date_var.set(p['birth_date'] or '')
#                 self.birth_label.config(text=p['birth_date'] or 'None')
#                 self.status_var.set(p['status'])
#                 self.blood_var.set(p['blood_type'] or 'O+')
#                 self.entry_contact.delete(0, tk.END)
#                 self.entry_contact.insert(0, p['contact'] or '')

#     def _handle_add(self):
#         data = self._get_form_data()
#         if not data['full_name']:
#             messagebox.showwarning("Input Error", "Full Name is required.")
#             return
#         if data['contact'] and not validate_contact(data['contact']):
#             messagebox.showwarning("Input Error", "Contact must be a valid Sierra Leone number.")
#             return
#         try:
#             self.props.get('controller').add_patient(data)
#             messagebox.showinfo("Success", f"Patient '{data['full_name']}' added.")
#             self._clear_form()
#             self._refresh_data()
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def _handle_update(self):
#         if self.state.get('selected_id') is None:
#             messagebox.showwarning("Select", "Please select a patient.")
#             return
#         data = self._get_form_data()
#         if not data['full_name']:
#             messagebox.showwarning("Input Error", "Full Name is required.")
#             return
#         if data['contact'] and not validate_contact(data['contact']):
#             messagebox.showwarning("Input Error", "Contact must be a valid Sierra Leone number.")
#             return
#         try:
#             self.props.get('controller').update_patient(self.state['selected_id'], data)
#             messagebox.showinfo("Success", "Patient updated.")
#             self._clear_form()
#             self._refresh_data()
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def _handle_delete(self):
#         if self.state.get('selected_id') is None:
#             messagebox.showwarning("Select", "Please select a patient.")
#             return
#         if messagebox.askyesno("Confirm Delete", "Delete this patient permanently?"):
#             try:
#                 self.props.get('controller').delete_patient(self.state['selected_id'])
#                 self._clear_form()
#                 self._refresh_data()
#             except Exception as e:
#                 messagebox.showerror("Error", str(e))

#     def _handle_export(self):
#         patients = self.state.get('patients', [])
#         if not patients:
#             messagebox.showwarning("No Data", "No patients to export.")
#             return
#         filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
#         if filename:
#             if self.props.get('controller').export_csv(patients, filename):
#                 messagebox.showinfo("Export", f"Data exported to {filename}")

#     def _handle_search(self, params):
#         results = self.props.get('controller').search_patients(
#             params.get('term'),
#             params.get('search_by'),
#             params.get('blood'),
#             params.get('date_from'),
#             params.get('date_to')
#         )
#         self.state['search_results'] = results
#         self._update_table(results)

#     def _handle_clear_search(self):
#         self.state['search_results'] = None
#         self._refresh_data()

#     def _handle_page_change(self, page):
#         offset = (page - 1) * self.state.get('limit', 20)
#         self.state['offset'] = offset
#         self._refresh_data()

#     def _refresh_data(self):
#         controller = self.props.get('controller')
#         if self.state.get('search_results') is not None:
#             self._update_table(self.state['search_results'])
#         else:
#             offset = self.state.get('offset', 0)
#             limit = self.state.get('limit', 20)
#             total = controller.get_patient_count()
#             patients = controller.get_all_patients(limit, offset)
#             self.state['total'] = total
#             self.state['patients'] = patients
#             self._update_table(patients)
#             self.pagination.props['current_page'] = (offset // limit) + 1
#             self.pagination.props['total_pages'] = max(1, (total + limit - 1) // limit)
#             self.pagination.render()

#     def _update_table(self, patients):
#         data = []
#         for p in patients:
#             age = calculate_age(p['birth_date'])
#             data.append((
#                 p['id'], p['full_name'], p['gender'], age,
#                 p['status'], p['blood_type'] or 'Unknown', p['contact'] or 'N/A',
#                 p['created_date']
#             ))
#         self.table.update_data(data)

#     def _get_form_data(self):
#         return {
#             'full_name': self.entry_name.get().strip(),
#             'gender': self.gender_var.get(),
#             'birth_date': self.birth_date_var.get() or None,
#             'status': self.status_var.get(),
#             'blood': self.blood_var.get(),
#             'contact': self.entry_contact.get().strip(),
#         }

#     def _clear_form(self):
#         self.entry_name.delete(0, tk.END)
#         self.entry_contact.delete(0, tk.END)
#         self.birth_date_var.set('')
#         self.birth_label.config(text='None')
#         self.gender_var.set('Male')
#         self.status_var.set('Active')
#         self.blood_var.set('O+')
#         self.state['selected_id'] = None

#     def mount(self, container=None):
#         super().mount(container)
#         self._refresh_data()
#         return self._container