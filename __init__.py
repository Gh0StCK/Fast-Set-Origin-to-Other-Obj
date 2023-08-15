bl_info = {
    "name": "Fast Set Origin to Other Obj",
    "author": "Stanislav Kolesnikov",
    "version": (1, 0, 0),
    "blender": (3, 4, 1),
    "location": "View 3D > Sidebar > FastTools",
    "description": "Allows you to quickly set the Origin of selected objects to the position of the Origin of the active object.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

import bpy
from bpy.types import Panel, Operator

def my_button_function(self, context):
    bpy.ops.object.mode_set(mode='OBJECT')
    context.scene.cursor.location = context.active_object.location
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

class FSO_OO_MyPanel(Panel):
    bl_label = "Set Origin to Other Obj"
    bl_idname = "OBJECT_PT_set_oprigin_to_other_obj_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "FastTools"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.set_oprigin_to_other_obj_button", text="Set Origin to Other Obj")

class FSO_OO_MyButton(Operator):
    bl_idname = "object.set_oprigin_to_other_obj_button"
    bl_label = "Set Origin to Other Obj"

    def execute(self, context):
        my_button_function(self, context)
        return {'FINISHED'}
    
classes = [
    FSO_OO_MyPanel,
    FSO_OO_MyButton
]

def register():
    for cl in classes:
        bpy.utils.register_class(cl)

def unregister():
    for cl in reversed(classes):
        bpy.utils.unregister_class(cl)

if __name__ == "__main__":
    register()
