"""
mergecore 加载器
"""

import os
import sys
import importlib.util

def load_mergecore():
    platforms = {
        'win32': 'mergecore_win.pyd',
        'linux': 'mergecore_linux.so', 
        'darwin': 'mergecore_mac.so'
    }
    
    current_platform = sys.platform
    compiled_file = platforms.get(current_platform)
    print(f"✓ : {current_platform}")
    print(f"✓ : {compiled_file}")
    if compiled_file:
        # 加载编译版本
        base_path = os.path.dirname(__file__)
        compiled_path = os.path.join(base_path, compiled_file)
        if os.path.exists(compiled_path):
            try:
                spec = importlib.util.spec_from_file_location("mergecore", compiled_path)
                mergecore_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mergecore_module)
                print(f"✓ 已加载编译版本: {compiled_file}")
                return mergecore_module
            except Exception as e:
                print(f"⚠️ 加载{compiled_file}编译版本失败: {e}") 
    else:
        print(f"⚠️ 缺少必要的编译文件")   
# 全局导入
ModelMergeCore = None
try:
    mergecore_module = load_mergecore()
    ModelMergeCore = getattr(mergecore_module, 'ModelMergeCore')
except Exception as e:
    print(f"❌ 无法加载 ModelMergeCore: {e}")