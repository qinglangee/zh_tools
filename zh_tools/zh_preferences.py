import bpy

from bpy.props import (
    FloatProperty,
    EnumProperty,
    BoolProperty,
    IntProperty,
    StringProperty,
    FloatVectorProperty,
    CollectionProperty,
)


# 配置
class ZHToolPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    age: IntProperty(name='age', default=8)
    name: StringProperty(name="name", default='lala')




    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "age")
        col.prop(self, "name")
