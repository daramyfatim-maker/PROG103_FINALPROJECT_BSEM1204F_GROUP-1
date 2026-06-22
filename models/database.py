# # models/database.py
# # Database class – Model layer

# import sqlite3
# from datetime import datetime, timedelta
# import random

# class Database:
#     def __init__(self, db_name="medica.db"):
#         self.db_name = db_name
#         self.conn = sqlite3.connect(db_name, check_same_thread=False)
#         self.conn.row_factory = sqlite3.Row
#         self.cursor = self.conn.cursor()
#         self.observers = []
#         self.create_tables()
#         self.insert_sample_data()

#     def add_observer(self, callback):
#         self.observers.append(callback)

#     def notify_observers(self, data=None):
#         for cb in self.observers:
#             try:
#                 cb(data)
#             except:
#                 pass

#     def close(self):
#         if self.conn:
#             self.conn.close()

#     def create_tables(self):
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL,
#             full_name TEXT,
#             role TEXT DEFAULT 'user'
#         )''')
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             full_name TEXT NOT NULL,
#             gender TEXT NOT NULL,
#             birth_date DATE,
#             status TEXT NOT NULL,
#             created_date DATE NOT NULL,
#             contact TEXT,
#             emergency_contact TEXT,
#             blood_type TEXT,
#             allergies TEXT,
#             last_visit DATE
#         )''')
#         self.cursor.execute("PRAGMA table_info(patients)")
#         columns = [col[1] for col in self.cursor.fetchall()]
#         if 'birth_date' not in columns:
#             self.cursor.execute("ALTER TABLE patients ADD COLUMN birth_date DATE")
#         if 'emergency_contact' not in columns:
#             self.cursor.execute("ALTER TABLE patients ADD COLUMN emergency_contact TEXT")
#         if 'blood_type' not in columns:
#             self.cursor.execute("ALTER TABLE patients ADD COLUMN blood_type TEXT")
#         if 'allergies' not in columns:
#             self.cursor.execute("ALTER TABLE patients ADD COLUMN allergies TEXT")
#         if 'last_visit' not in columns:
#             self.cursor.execute("ALTER TABLE patients ADD COLUMN last_visit DATE")

#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS visits (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             patient_id INTEGER NOT NULL,
#             visit_date DATE NOT NULL,
#             doctor TEXT,
#             diagnosis TEXT,
#             treatment TEXT,
#             FOREIGN KEY (patient_id) REFERENCES patients(id)
#         )''')
#         self.conn.commit()

#     def insert_sample_data(self):
#         self.cursor.execute("SELECT COUNT(*) FROM patients")
#         if self.cursor.fetchone()[0] >= 30:
#             return

#         self.cursor.execute("INSERT OR IGNORE INTO users (username,password,full_name,role) VALUES (?,?,?,?)",
#                             ('admin','admin123','Administrator','admin'))
#         self.cursor.execute("INSERT OR IGNORE INTO users (username,password,full_name,role) VALUES (?,?,?,?)",
#                             ('doctor','doctor123','Dr. Mohamed Kamara','doctor'))
#         self.cursor.execute("INSERT OR IGNORE INTO users (username,password,full_name,role) VALUES (?,?,?,?)",
#                             ('nurse','nurse123','Nurse Fatmata Sesay','nurse'))

#         first_names = ['Mohamed','Fatmata','Ibrahim','Aminata','Sulaiman','Mariama','Abdulai','Salamatu',
#                        'Mustapha','Zainab','Alhaji','Hawa','Amadu','Kadiatu','Osman','Memuna','Sorie',
#                        'Mabinty','Bakarr','Isatu','Santigie','Adama','Kanu','Foday','Mamu','Isatu','Mohamed',
#                        'Mariama','Ibrahim','Fatmata']
#         last_names = ['Koroma','Kamara','Jalloh','Sesay','Bangura','Conteh','Sankoh','Kargbo','Tarawally',
#                       'Saffa','Bah','Fofanah','Kallay','Turay','Mansaray']*2
#         statuses = ['Active','Inactive','Pending']
#         genders = ['Male','Female','Other']
#         blood_types = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
#         allergies_list = ['None','Penicillin','Sulfa','Latex','Peanuts']

#         for i in range(30):
#             first = first_names[i % len(first_names)]
#             last = last_names[i % len(last_names)]
#             full_name = f"{first} {last}"
#             gender = random.choice(genders)
#             birth_date = (datetime.now() - timedelta(days=random.randint(6570, 29200))).strftime('%Y-%m-%d')
#             status = random.choice(statuses)
#             contact = f"7{random.randint(1000000,9999999)}"
#             emergency = f"7{random.randint(1000000,9999999)}"
#             blood = random.choice(blood_types)
#             allergy = random.choice(allergies_list)
#             days_ago = random.randint(0,90)
#             created = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
#             last_visit = (datetime.now() - timedelta(days=random.randint(0,30))).strftime('%Y-%m-%d')
#             self.cursor.execute('''INSERT INTO patients
#                 (full_name,gender,birth_date,status,created_date,contact,emergency_contact,blood_type,allergies,last_visit)
#                 VALUES (?,?,?,?,?,?,?,?,?,?)''',
#                 (full_name,gender,birth_date,status,created,contact,emergency,blood,allergy,last_visit))
#             pid = self.cursor.lastrowid
#             for _ in range(random.randint(1,3)):
#                 visit_date = (datetime.now() - timedelta(days=random.randint(0,60))).strftime('%Y-%m-%d')
#                 doctor = random.choice(['Dr. Kamara', 'Dr. Sesay', 'Dr. Koroma', 'Dr. Bangura'])
#                 diagnosis = random.choice(['Malaria', 'Typhoid', 'Respiratory infection', 'Hypertension', 'Diabetes', 'Routine checkup'])
#                 treatment = random.choice(['Antibiotics', 'Painkillers', 'Lifestyle advice', 'Referral', 'Observation'])
#                 self.cursor.execute('''INSERT INTO visits (patient_id,visit_date,doctor,diagnosis,treatment)
#                                        VALUES (?,?,?,?,?)''',
#                                     (pid, visit_date, doctor, diagnosis, treatment))
#         self.conn.commit()
#         self.notify_observers({'action':'data_loaded'})

#     # ---------- CRUD ----------
#     def get_all_patients(self, limit=None, offset=0):
#         if limit:
#             self.cursor.execute("SELECT * FROM patients ORDER BY id LIMIT ? OFFSET ?", (limit, offset))
#         else:
#             self.cursor.execute("SELECT * FROM patients ORDER BY id")
#         return self.cursor.fetchall()

#     def get_patient(self, pid):
#         self.cursor.execute("SELECT * FROM patients WHERE id=?", (pid,))
#         return self.cursor.fetchone()

#     def get_patient_count(self):
#         self.cursor.execute("SELECT COUNT(*) FROM patients")
#         return self.cursor.fetchone()[0]

#     def add_patient(self, data):
#         created = datetime.now().strftime('%Y-%m-%d')
#         self.cursor.execute('''INSERT INTO patients
#             (full_name,gender,birth_date,status,created_date,contact,emergency_contact,blood_type,allergies,last_visit)
#             VALUES (?,?,?,?,?,?,?,?,?,?)''',
#             (data['full_name'], data['gender'], data['birth_date'], data['status'], created,
#              data.get('contact',''), data.get('emergency',''), data.get('blood',''),
#              data.get('allergies',''), created))
#         self.conn.commit()
#         pid = self.cursor.lastrowid
#         self.notify_observers({'action':'add', 'id':pid})
#         return pid

#     def update_patient(self, pid, data):
#         self.cursor.execute('''UPDATE patients SET
#             full_name=?, gender=?, birth_date=?, status=?, contact=?, emergency_contact=?,
#             blood_type=?, allergies=?, last_visit=?
#             WHERE id=?''',
#             (data['full_name'], data['gender'], data['birth_date'], data['status'],
#              data.get('contact',''), data.get('emergency',''),
#              data.get('blood',''), data.get('allergies',''),
#              datetime.now().strftime('%Y-%m-%d'), pid))
#         self.conn.commit()
#         self.notify_observers({'action':'update', 'id':pid})

#     def delete_patient(self, pid):
#         self.cursor.execute("DELETE FROM visits WHERE patient_id=?", (pid,))
#         self.cursor.execute("DELETE FROM patients WHERE id=?", (pid,))
#         self.conn.commit()
#         self.notify_observers({'action':'delete', 'id':pid})

#     # ---------- Search ----------
#     def search_patients(self, term=None, search_by='all', blood=None, date_from=None, date_to=None):
#         query = "SELECT * FROM patients WHERE 1=1"
#         params = []
#         if term and term.strip():
#             term = f'%{term.strip()}%'
#             if search_by == 'id':
#                 try:
#                     query += " AND id=?"
#                     params.append(int(term.strip('%')))
#                 except:
#                     return []
#             elif search_by == 'name':
#                 query += " AND full_name LIKE ?"
#                 params.append(term)
#             elif search_by == 'status':
#                 query += " AND status LIKE ?"
#                 params.append(term)
#             elif search_by == 'gender':
#                 query += " AND gender LIKE ?"
#                 params.append(term)
#             elif search_by == 'blood':
#                 query += " AND blood_type LIKE ?"
#                 params.append(term)
#             else:
#                 query += " AND (full_name LIKE ? OR status LIKE ? OR gender LIKE ? OR blood_type LIKE ? OR CAST(id AS TEXT) LIKE ?)"
#                 params.extend([term, term, term, term, term])
#         if blood and blood != 'All':
#             query += " AND blood_type=?"
#             params.append(blood)
#         if date_from:
#             query += " AND created_date >= ?"
#             params.append(date_from)
#         if date_to:
#             query += " AND created_date <= ?"
#             params.append(date_to)
#         self.cursor.execute(query, params)
#         return self.cursor.fetchall()

#     # ---------- Visits ----------
#     def get_visits(self, patient_id):
#         self.cursor.execute("SELECT * FROM visits WHERE patient_id=? ORDER BY visit_date DESC", (patient_id,))
#         return self.cursor.fetchall()

#     def add_visit(self, patient_id, data):
#         self.cursor.execute('''INSERT INTO visits (patient_id, visit_date, doctor, diagnosis, treatment)
#                                VALUES (?,?,?,?,?)''',
#                             (patient_id, data['visit_date'], data['doctor'], data['diagnosis'], data['treatment']))
#         self.conn.commit()
#         self.notify_observers({'action':'add_visit', 'patient_id':patient_id})

#     # ---------- Stats ----------
#     def get_stats(self):
#         self.cursor.execute("SELECT COUNT(*) FROM patients")
#         total = self.cursor.fetchone()[0]
#         self.cursor.execute("SELECT gender, COUNT(*) FROM patients GROUP BY gender")
#         gender = self.cursor.fetchall()
#         self.cursor.execute("SELECT status, COUNT(*) FROM patients GROUP BY status")
#         status = self.cursor.fetchall()
#         self.cursor.execute('''SELECT created_date, COUNT(*)
#             FROM patients WHERE created_date >= date('now','-30 days')
#             GROUP BY created_date ORDER BY created_date''')
#         daily = self.cursor.fetchall()
#         self.cursor.execute('''
#             SELECT 
#                 CASE 
#                     WHEN (strftime('%Y', 'now') - strftime('%Y', birth_date)) < 18 THEN '0-17'
#                     WHEN (strftime('%Y', 'now') - strftime('%Y', birth_date)) BETWEEN 18 AND 30 THEN '18-30'
#                     WHEN (strftime('%Y', 'now') - strftime('%Y', birth_date)) BETWEEN 31 AND 50 THEN '31-50'
#                     WHEN (strftime('%Y', 'now') - strftime('%Y', birth_date)) BETWEEN 51 AND 65 THEN '51-65'
#                     ELSE '65+'
#                 END as age_group,
#                 COUNT(*)
#             FROM patients
#             WHERE birth_date IS NOT NULL
#             GROUP BY age_group
#         ''')
#         age_groups = self.cursor.fetchall()
#         self.cursor.execute('''
#             SELECT visit_date, COUNT(*) 
#             FROM visits 
#             WHERE visit_date >= date('now','-30 days')
#             GROUP BY visit_date
#             ORDER BY visit_date
#         ''')
#         visits_daily = self.cursor.fetchall()
#         return {'total':total,'gender':gender,'status':status,'daily':daily,
#                 'age_groups':age_groups, 'visits_daily':visits_daily}

#     def get_recent_patients(self, limit=5):
#         self.cursor.execute('''SELECT full_name, created_date FROM patients
#                                ORDER BY id DESC LIMIT ?''', (limit,))
#         return self.cursor.fetchall()

#     def get_reports_data(self, period, start_date=None, end_date=None):
#         if period == 'custom' and start_date and end_date:
#             start = start_date
#             end = end_date
#         else:
#             today = datetime.now()
#             if period == 'weekly':
#                 start = (today - timedelta(days=7)).strftime('%Y-%m-%d')
#                 end = today.strftime('%Y-%m-%d')
#             elif period == 'monthly':
#                 start = (today - timedelta(days=30)).strftime('%Y-%m-%d')
#                 end = today.strftime('%Y-%m-%d')
#             elif period == 'yearly':
#                 start = (today - timedelta(days=365)).strftime('%Y-%m-%d')
#                 end = today.strftime('%Y-%m-%d')
#             else:
#                 start = (today - timedelta(days=7)).strftime('%Y-%m-%d')
#                 end = today.strftime('%Y-%m-%d')
#         self.cursor.execute('''SELECT * FROM patients
#             WHERE created_date BETWEEN ? AND ? ORDER BY created_date DESC''', (start,end))
#         records = self.cursor.fetchall()
#         gender_counts = {'Male':0,'Female':0,'Other':0}
#         status_counts = {'Active':0,'Inactive':0,'Pending':0}
#         for r in records:
#             if r['gender'] in gender_counts: gender_counts[r['gender']] += 1
#             if r['status'] in status_counts: status_counts[r['status']] += 1
#         return {
#             'records': records,
#             'total': len(records),
#             'gender_counts': gender_counts,
#             'status_counts': status_counts,
#             'start_date': start,
#             'end_date': end
#         }

#     def authenticate(self, username, password):
#         self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
#         return self.cursor.fetchone()