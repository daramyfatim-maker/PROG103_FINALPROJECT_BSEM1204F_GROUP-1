# # config.py
# # Theme colours and global constants

# class Theme:
#     LIGHT = {
#         'primary': '#7B1F3A',
#         'primary_light': '#A52A4A',
#         'secondary': '#1ABC9C',
#         'accent': '#E74C3C',
#         'success': '#27AE60',
#         'warning': '#F39C12',
#         'background': '#F8F4F5',
#         'sidebar_bg': '#4A1223',
#         'sidebar_hover': '#7B1F3A',
#         'card': '#FFFFFF',
#         'card_border': '#E0D5D8',
#         'text': '#2C3E50',
#         'text_light': '#7F8C8D',
#         'border': '#D5DBDB',
#         'tree_bg': '#FFFFFF',
#         'tree_fg': '#2C3E50',
#         'tree_selected': '#A52A4A',
#     }
#     DARK = {
#         'primary': '#7B1F3A',
#         'primary_light': '#A52A4A',
#         'secondary': '#1ABC9C',
#         'accent': '#E74C3C',
#         'success': '#27AE60',
#         'warning': '#F39C12',
#         'background': '#1E1A1C',
#         'sidebar_bg': '#2A0E18',
#         'sidebar_hover': '#4A1223',
#         'card': '#2D2327',
#         'card_border': '#4A3A40',
#         'text': '#ECF0F1',
#         'text_light': '#B0BEC5',
#         'border': '#4A5A6A',
#         'tree_bg': '#2D2327',
#         'tree_fg': '#ECF0F1',
#         'tree_selected': '#A52A4A',
#     }

# current_theme = 'light'
# COLORS = Theme.LIGHT.copy()

# def apply_theme(theme_name):
#     global COLORS
#     if theme_name == 'dark':
#         COLORS = Theme.DARK.copy()
#     else:
#         COLORS = Theme.LIGHT.copy()
#     return COLORS