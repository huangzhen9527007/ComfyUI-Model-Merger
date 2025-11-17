"""
模型合并节点 - 用于合并多个 safetensors 模型文件
"""

# 导入操作实现
from .merge_operations import execute_merge_models, execute_stream_merge_models

class ModelMergerNode:
    """
    模型合并节点，用于合并多个 safetensors 模型文件
    """
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_files": ("STRING", {
                    "multiline": True,
                    "default": "diffusion_pytorch_model-00001-of-00007.safetensors\ndiffusion_pytorch_model-00002-of-00007.safetensors\ndiffusion_pytorch_model-00003-of-00007.safetensors\ndiffusion_pytorch_model-00004-of-00007.safetensors\ndiffusion_pytorch_model-00005-of-00007.safetensors\ndiffusion_pytorch_model-00006-of-00007.safetensors\ndiffusion_pytorch_model-00007-of-00007.safetensors",
                    "placeholder": "输入模型文件路径，每行一个"
                }),
                "output_file": ("STRING", {
                    "default": "diffusion_pytorch_model.safetensors",
                    "placeholder": "合并后的模型保存路径"
                }),
                "merge_mode": ("STRING", {
                    "default": "update",
                    "choices": ["update", "replace"]
                }),
            },
            "optional": {
                "select_files": ("BOOLEAN", {
                    "default": True,
                    "label_on": "打开文件选择",
                    "label_off": "关闭文件选择"
                }),
                "select_directory": ("BOOLEAN", {
                    "default": False,
                    "label_on": "选择文件夹",
                    "label_off": "不选择文件夹"
                }),
                "select_output_file": ("BOOLEAN", {
                    "default": True,
                    "label_on": "选择保存位置",
                    "label_off": "不选择保存位置"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("merged_file_path",)
    FUNCTION = "merge_models"
    CATEGORY = "模型工具"
    DISPLAY_NAME = "模型合并器"
    
    def merge_models(self, model_files, output_file, merge_mode="update", select_files=False, select_directory=False, select_output_file=False):
        """
        调用外部实现执行模型合并
        """
        try:
            result_file = execute_merge_models(
                model_files, output_file, merge_mode, 
                select_files, select_directory, select_output_file
            )
            return (result_file,)
        except Exception as e:
            print(f"合并过程出错: {str(e)}")
            # 返回错误信息而不是抛出异常，避免ComfyUI崩溃
            return (f"错误: {str(e)}",)

class StreamModelMergerNode:
    """
    流式模型合并节点 - 流式 safetensors 分片合并（适用于大模型）
    
    """
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "shard_files": ("STRING", {
                    "multiline": True,
                    "default": "diffusion_pytorch_model-00001-of-00007.safetensors\ndiffusion_pytorch_model-00002-of-00007.safetensors\ndiffusion_pytorch_model-00003-of-00007.safetensors\ndiffusion_pytorch_model-00004-of-00007.safetensors\ndiffusion_pytorch_model-00005-of-00007.safetensors\ndiffusion_pytorch_model-00006-of-00007.safetensors\ndiffusion_pytorch_model-00007-of-00007.safetensors",
                    "placeholder": "输入分片文件路径，每行一个，按顺序排列"
                }),
                "output_file": ("STRING", {
                    "default": "diffusion_pytorch_model.safetensors",
                    "placeholder": "合并后的输出文件路径"
                }),
                "chunk_size_mb": ("INT", {
                    "default": 64,
                    "min": 1,
                    "max": 1024,
                    "step": 1,
                    "display": "number"
                }),
            },
            "optional": {
                "select_files": ("BOOLEAN", {
                    "default": True,
                    "label_on": "打开文件选择",
                    "label_off": "关闭文件选择"
                }),
                "select_directory": ("BOOLEAN", {
                    "default": False,
                    "label_on": "选择文件夹",
                    "label_off": "不选择文件夹"
                }),
                "select_output_file": ("BOOLEAN", {
                    "default": True,
                    "label_on": "选择保存位置",
                    "label_off": "不选择保存位置"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("merged_file_path",)
    FUNCTION = "stream_merge_models"
    CATEGORY = "模型工具"
    DISPLAY_NAME = "流式模型合并器"
    
    def stream_merge_models(self, shard_files, output_file, chunk_size_mb=64, select_files=False, select_directory=False, select_output_file=False):
        """
        调用外部实现执行流式模型合并
        """
        try:
            result_file = execute_stream_merge_models(
                shard_files, output_file, chunk_size_mb,
                select_files, select_directory, select_output_file
            )
            return (result_file,)
        except Exception as e:
            print(f"合并过程出错: {str(e)}")
            import traceback
            traceback.print_exc()
            return (f"错误: {str(e)}",)

# 节点映射
NODE_CLASS_MAPPINGS = {
    "ModelMergerNode": ModelMergerNode,
    "StreamModelMergerNode": StreamModelMergerNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelMergerNode": "模型合并器",
    "StreamModelMergerNode": "流式模型合并器"
}

print("✅ 模型合并节点已成功注册")