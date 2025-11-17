import os
import sys
import importlib.util

def load_mergecore():
    platforms = {
        'win32': 'mergecore.cp312-win_amd64.pyd',
        'linux': 'mergecore_linux.so',
        'darwin': 'mergecore_mac.so'
    }
    
    current_platform = sys.platform
    compiled_file = platforms.get(current_platform)
    
    base_path = os.path.dirname(__file__)
    compiled_path = os.path.join(base_path, compiled_file)
    if os.path.exists(compiled_path):
        try:
            spec = importlib.util.spec_from_file_location("mergecore", compiled_path)
            mergecore_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mergecore_module)
            return mergecore_module
        except Exception as e:
            print(f"⚠️ 加载{compiled_file}编译版本失败: {e}") 
    else:
        print(f"⚠️ 缺少必要的编译文件")   

def load_graphic_manipulation():
    platforms = {
        'win32': 'graphic_manipulation.cp312-win_amd64.pyd',
        'linux': 'graphic_manipulation_linux.so', 
        'darwin': 'graphic_manipulation_mac.so'
    }
    
    current_platform = sys.platform
    compiled_file = platforms.get(current_platform)
    base_path = os.path.dirname(__file__)
    
    if compiled_file:
        compiled_path = os.path.join(base_path, compiled_file)
        
    if os.path.exists(compiled_path):
        try:
            spec = importlib.util.spec_from_file_location("graphic_manipulation", compiled_path)
            graphic_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(graphic_module)
            return graphic_module
        except Exception as e:
            print(f"⚠️ 加载{compiled_file}编译版本失败: {e}")
    else:
        print(f"⚠️ 缺少必要的编译文件")  
            
ModelMergeCore = None
GraphicManipulation = None
try:
    mergecore_module = load_mergecore()
    ModelMergeCore = getattr(mergecore_module, 'ModelMergeCore')
except Exception as e:
    print(f"❌ 无法加载 ModelMergeCore: {e}")

try:
    graphic_module = load_graphic_manipulation()
    GraphicManipulation = getattr(graphic_module, 'GraphicManipulation')
except Exception as e:
    print(f"❌ 无法加载 GraphicManipulation: {e}")