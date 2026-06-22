# # components/base.py
# # Base Component class (like React.Component)

# class Component:
#     def __init__(self, parent, props=None):
#         self.parent = parent
#         self.props = props or {}
#         self.state = {}
#         self.children = []
#         self._mounted = False
#         self._container = None

#     def set_state(self, new_state):
#         self.state.update(new_state)
#         self.render()

#     def mount(self, container=None):
#         self._container = container or self.parent
#         self._mounted = True
#         self.render()
#         return self._container

#     def render(self):
#         raise NotImplementedError("Subclasses must implement render()")

#     def unmount(self):
#         self._mounted = False
#         for child in self.children:
#             if hasattr(child, 'unmount'):
#                 child.unmount()
#         self.children = []

#     def add_child(self, child, container=None):
#         self.children.append(child)
#         child.mount(container or self._container)
#         return child

#     def get_container(self):
#         return self._container