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


kmi_defs = (
    # MERGE NODES
    # NWMergeNodes with Ctrl (AUTO).
    ('zh_object.unselect_select', 'NUMPAD_0', 'PRESS', True, False, False,
        (('mode', 'MIX'), ('merge_type', 'AUTO'),), "Merge Nodes (Automatic)hahaha"),
    ('zh_object.unselect_select', 'ZERO', 'PRESS', True, False, False,
        (('mode', 'MIX'), ('merge_type', 'AUTO'),), "Merge Nodes (Automatic)hehehe"),
    ('zh_object.unselect_select', 'ZERO', 'PRESS', True, False, False,
        (('mode', 'MIX'), ('merge_type', 'AUTO'),), "Merge Nodes (Automatic)xixixi"),
)

def nice_hotkey_name(punc):
    # convert the ugly string name into the actual character
    pairs = (
        ('LEFTMOUSE', "LMB"),
        ('MIDDLEMOUSE', "MMB"),
        ('RIGHTMOUSE', "RMB"),
        ('WHEELUPMOUSE', "Wheel Up"),
        ('WHEELDOWNMOUSE', "Wheel Down"),
        ('WHEELINMOUSE', "Wheel In"),
        ('WHEELOUTMOUSE', "Wheel Out"),
        ('ZERO', "0"),
        ('ONE', "1"),
        ('TWO', "2"),
        ('THREE', "3"),
        ('FOUR', "4"),
        ('FIVE', "5"),
        ('SIX', "6"),
        ('SEVEN', "7"),
        ('EIGHT', "8"),
        ('NINE', "9"),
        ('OSKEY', "Super"),
        ('RET', "Enter"),
        ('LINE_FEED', "Enter"),
        ('SEMI_COLON', ";"),
        ('PERIOD', "."),
        ('COMMA', ","),
        ('QUOTE', '"'),
        ('MINUS', "-"),
        ('SLASH', "/"),
        ('BACK_SLASH', "\\"),
        ('EQUAL', "="),
        ('NUMPAD_1', "Numpad 1"),
        ('NUMPAD_2', "Numpad 2"),
        ('NUMPAD_3', "Numpad 3"),
        ('NUMPAD_4', "Numpad 4"),
        ('NUMPAD_5', "Numpad 5"),
        ('NUMPAD_6', "Numpad 6"),
        ('NUMPAD_7', "Numpad 7"),
        ('NUMPAD_8', "Numpad 8"),
        ('NUMPAD_9', "Numpad 9"),
        ('NUMPAD_0', "Numpad 0"),
        ('NUMPAD_PERIOD', "Numpad ."),
        ('NUMPAD_SLASH', "Numpad /"),
        ('NUMPAD_ASTERIX', "Numpad *"),
        ('NUMPAD_MINUS', "Numpad -"),
        ('NUMPAD_ENTER', "Numpad Enter"),
        ('NUMPAD_PLUS', "Numpad +"),
    )
    nice_punc = False
    for (ugly, nice) in pairs:
        if punc == ugly:
            nice_punc = nice
            break
    if not nice_punc:
        nice_punc = punc.replace("_", " ").title()
    return nice_punc


# Principled prefs
class NWPrincipledPreferences(bpy.types.PropertyGroup):
    base_color: StringProperty(
        name='Base Color',
        default='diffuse diff albedo base col color',
        description='Naming Components for Base Color maps')
    sss_color: StringProperty(
        name='Subsurface Color',
        default='sss subsurface',
        description='Naming Components for Subsurface Color maps')
    metallic: StringProperty(
        name='Metallic',
        default='metallic metalness metal mtl',
        description='Naming Components for metallness maps')
    specular: StringProperty(
        name='Specular',
        default='specularity specular spec spc',
        description='Naming Components for Specular maps')
    normal: StringProperty(
        name='Normal',
        default='normal nor nrm nrml norm',
        description='Naming Components for Normal maps')
    bump: StringProperty(
        name='Bump',
        default='bump bmp',
        description='Naming Components for bump maps')
    rough: StringProperty(
        name='Roughness',
        default='roughness rough rgh',
        description='Naming Components for roughness maps')
    gloss: StringProperty(
        name='Gloss',
        default='gloss glossy glossyness',
        description='Naming Components for glossy maps')
    displacement: StringProperty(
        name='Displacement',
        default='displacement displace disp dsp height heightmap',
        description='Naming Components for displacement maps')


# 配置
class ZHToolPreferences00(bpy.types.AddonPreferences):
    bl_idname = '__package__'


    merge_hide: EnumProperty(
        name="Hide Mix nodes",
        items=(
            ("ALWAYS", "Always", "Always collapse the new merge nodes"),
            ("NON_SHADER", "Non-Shader", "Collapse in all cases except for shaders"),
            ("NEVER", "Never", "Never collapse the new merge nodes")
        ),
        default='NON_SHADER',
        description="When merging nodes with the Ctrl+Numpad0 hotkey (and similar) specify whether to collapse them or show the full node with options expanded")
    merge_position: EnumProperty(
        name="Mix Node Position",
        items=(
            ("CENTER", "Center", "Place the Mix node between the two nodes"),
            ("BOTTOM", "Bottom", "Place the Mix node at the same height as the lowest node")
        ),
        default='CENTER',
        description="When merging nodes with the Ctrl+Numpad0 hotkey (and similar) specify the position of the new nodes")

    show_hotkey_list: BoolProperty(
        name="Show Hotkey List",
        default=False,
        description="Expand this box into a list of all the hotkeys for functions in this addon"
    )
    hotkey_list_filter: StringProperty(
        name="        Filter by Name",
        default="",
        description="Show only hotkeys that have this text in their name"
    )
    show_principled_lists: BoolProperty(
        name="Show Principled naming tags",
        default=False,
        description="Expand this box into a list of all naming tags for principled texture setup"
    )
    principled_tags: bpy.props.PointerProperty(type=NWPrincipledPreferences)

    



    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "merge_position")
        col.prop(self, "merge_hide")

        box = layout.box()
        col = box.column(align=True)
        col.prop(self, "show_principled_lists", text='Edit tags for auto texture detection in Principled BSDF setup', toggle=True)
        if self.show_principled_lists:
            tags = self.principled_tags

            col.prop(tags, "base_color")
            col.prop(tags, "sss_color")
            col.prop(tags, "metallic")
            col.prop(tags, "specular")
            col.prop(tags, "rough")
            col.prop(tags, "gloss")
            col.prop(tags, "normal")
            col.prop(tags, "bump")
            col.prop(tags, "displacement")

        box = layout.box()
        col = box.column(align=True)
        hotkey_button_name = "Show Hotkey List"
        if self.show_hotkey_list:
            hotkey_button_name = "Hide Hotkey List"
        col.prop(self, "show_hotkey_list", text=hotkey_button_name, toggle=True)
        if self.show_hotkey_list:
            col.prop(self, "hotkey_list_filter", icon="VIEWZOOM")
            col.separator()
            for hotkey in kmi_defs:
                if hotkey[7]:
                    hotkey_name = hotkey[7]

                    if self.hotkey_list_filter.lower() in hotkey_name.lower():
                        row = col.row(align=True)
                        row.label(text=hotkey_name)
                        keystr = nice_hotkey_name(hotkey[1])
                        if hotkey[4]:
                            keystr = "Shift " + keystr
                        if hotkey[5]:
                            keystr = "Alt " + keystr
                        if hotkey[3]:
                            keystr = "Ctrl " + keystr
                        row.label(text=keystr)
