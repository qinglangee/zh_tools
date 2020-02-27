import bpy
import inspect

from . import preferences

from . import menus
from . menus import *
from . import operators
from . operators import *

addon_classes = [] 
class_dict = {}

# 从module中取所有的class, 没有递归
def extractClasses(modelName):
    for name, obj in inspect.getmembers(modelName):
        if inspect.isclass(obj):
            #print("class name : " + name)
            if not name in addon_classes:
                class_dict[name] = obj


# 从module中取所有子module, 没有递归
def extractModule(argName):
    for name, obj in inspect.getmembers(argName):
        #print("module item name: " + name)
        if inspect.ismodule(obj):
               extractClasses(obj)


def init():
    extractClasses(preferences)
    extractModule(menus)
    extractModule(operators)


    for item in class_dict.items():
        addon_classes.append(item[1])

def register():
    for clazz in addon_classes:
        bpy.utils.register_class(clazz)


def unregister():
    for clazz in addon_classes:
        bpy.utils.unregister_class(clazz)

