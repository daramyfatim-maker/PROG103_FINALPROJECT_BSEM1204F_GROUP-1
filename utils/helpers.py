# # utils/helpers.py
# # Utility functions for age calculation, validation, etc.

# import re
# from datetime import datetime

# def calculate_age(birth_date):
#     if not birth_date:
#         return 'N/A'
#     try:
#         birth = datetime.strptime(birth_date, '%Y-%m-%d')
#         today = datetime.now()
#         age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
#         return str(age)
#     except:
#         return 'N/A'

# def validate_contact(contact):
#     if not contact:
#         return True
#     pattern = r'^[738]\d{7}$'
#     return re.match(pattern, contact) is not None

# def get_status_count(status, stats):
#     for s, c in stats.get('status', []):
#         if s == status:
#             return c
#     return 0