<img width="1920" height="918" alt="c702d66a8d8375bac0b797283ce4fe6c" src="https://github.com/user-attachments/assets/8a2e4dc3-24e5-4bfe-a5ab-8e04c79712eb" />

# ComfyUI Model Merging Plugin

This is a model merging plugin for ComfyUI, offering two different model merging methods and supporting the merging of safetensors format model files.

## Update:

### 20251120

1. **Optimized module code structure, updated mergecore.cp312-win_amd64.pyd, loader.cp312-win_amd64.pyd, merge_operations.cp312-win_amd64.pyd, and graphic_manipulation.cp312-win_amd64.pyd**

2. **Automatically adapts to different Python versions**

3. **Works across platforms (Windows, Linux, macOS)**

4. **Maintains backward compatibility, supports older file naming conventions**

5. **Added support for Python version 3.13**

### 20251119

1. **Updated loader.pyd, fixed the issue of modules failing to load correctly during compilation**

2. **Updated the Windows platform compilation version: merge_operations.cp312-win_amd64.pyd (Windows), corresponding to Python version 3.12**

3. **Updated import code in model_merger_node.py**

4. **Adjusted and optimized overall code architecture**

5. **Updated node usage instructions**

### 20251117

1. **Updated main file model_merger_node.py**

2. **Updated Windows platform compilation version: merge_operations.cp312-win_amd64.pyd (Windows), corresponding to Python version 3.12**

3. **Updated loader, fixed an error caused by code indentation in the loader**

4. **Updated workflow model_merger_workflow.json, added relevant usage instructions, see workflow for details**

5. **Updated node usage instructions**

6. **Updated initial default values ​​for node selection and save mode**

### 20251116

1. **Updated Windows platform compilation version: mergecore.cp312-win_amd64.pyd (Windows), corresponding to Python version 3.12**

2. **Added loader to automatically load corresponding pre-compiled modules based on different platforms**

3. **Optimized standard merge mode file loading progress - Displays the current file number and filename being processed, tensor update statistics - Displays the number of tensors added after processing each file and the current total number of tensors**

4. **Updated the judgment logic in loader.py**

5. **Updated the Windows platform compilation version: graphic_manipulation.cp312-win_amd64.pyd (Windows), corresponding to Python version 3.12**

## Features

### Two Merging Modes

1. **Standard Model Merger (ModelMergerNode)**

- Directly loads and merges multiple safetensors model files

- Supports update mode (merging all tensors) and replacement mode (using the last file)

- Suitable for fast merging of small to medium-sized models

2. **Streaming Model Merger (StreamModelMergerNode)**

- Streaming processing of large model chunk files to avoid memory overflow

- Supports chunk copying, with customizable chunk size

- Header and encoding optimizations
- Safe merging for large models (e.g., multi-GB)

### General Features

- Supports merging multiple safetensors model files

- Provides a user-friendly interface for easily specifying input files and output paths

- Supports graphical file selection (requires tkinter)

- Detailed log output showing merging progress and results

- Supports custom output paths

## Installation Method

Method 1 (No longer required):

1. Ensure ComfyUI is installed

2. Copy this plugin directory to the `custom_nodes` folder in ComfyUI

3. Install dependencies:

```
pip install safetensors

```
For graphical file selection functionality, also install:

```
pip install tk

```
4. Restart ComfyUI

Method 2: Download the node file compressed package, extract it to the current folder, and you will get a folder named ComfyUI-Model-Merger (Note: If opening it directly reveals only a ComfyUI-Model-Merger folder instead of multiple .pyd and .py files, copy the ComfyUI-Model-Merger folder inside to ensure it contains multiple .pyd and .py files).

Copy the ComfyUI-Model-Merger folder to ComfyUI\custom_nodes.

Copy model_merger_workflow.json to ComfyUI\user\default\workflows.

## Instructions for Use

### Standard Model Merger

1. In ComfyUI, find the "Model Merger" node in the "Model Tools" category.

2. Set the following parameters in the node:

- **model_files**: Enter the path to the model files, one file path per line.

- **output_file**: Set the save path for the merged model.

- **merge_mode**: Select the merge mode (update: update merge, replace: replace).

3. Optional functions:

- **select_files**: Open the graphical file selection dialog box.

- **select_directory**: Select a folder; automatically searches for safetensors files within it.

- **select_output_file**: Select the save location for the output file.

4. Click "Queue Prompt" to run the workflow.

5. View the console output to understand the merge progress and results.

### Streaming Model Merger

1. In ComfyUI, find the "Streaming Model Merger" node in the "Model Tools" category.

2. Set the following parameters in the node:

- **shard_files**: Enter the path to the shard files, one file path per line (arranged in order).

- **output_file**: Set the path to save the merged model.

- **chunk_size_mb**: Set the chunk size (MB) for large file processing.

3. Optional functions:

- **select_files**: Open a graphical file selection dialog box.

- **select_directory**: Select a folder and automatically search for safetensors files within it.

- **select_output_file**: Select the location to save the output file.

4. Click "Queue Prompt" to run the workflow.

5. View the console output to understand the merging progress and results.

## Workflow Example

This plugin includes a sample workflow file `model_merger_workflow.json`, which you can load in ComfyUI to get started quickly.

See the workflow for detailed usage instructions.

## Selection Recommendations

- **Small to Medium-Sized Models** (< 20GB): Use the standard model merger for faster speed.

- **Large Models** (≥ 20GB): Use the streaming model merger to avoid memory overflow.

- **Sharded Model Files**: Use the streaming model merger, specifically optimized for this scenario.

## Notes

- Ensure all input model files exist and are accessible.

- Merging large models may take longer and require sufficient memory.

- The merged model will be saved in the output path you specify.

- If the output directory does not exist, the plugin will create it automatically.

- The streaming merger performs file verification to ensure the integrity of the merged result.

- For sharded files, ensure the files are arranged in the correct order.

## Troubleshooting

- If you encounter the `No module named 'safetensors'` error, ensure the safetensors library is installed.

- If the file path is incorrect, check the path format and ensure correct backslash escaping (use `\\` on Windows).

- If the merge fails, check if the model file format is correct and if they are all in safetensors format. If you encounter an out-of-memory error, please use the streaming model merger and reduce the `chunk_size_mb` parameter.

- If you cannot use graphical file selection, please install tkinter: `pip install tk`

- If the streaming merge process is interrupted, please check if you have sufficient disk space.

## Technical Features

### Advantages of the Streaming Merger

- Automatic handling of header size changes

- Chunky copying to avoid large file memory consumption

- Complete file verification mechanism

- Detailed progress display and error handling

### Performance Optimization

- Intelligent memory management to promptly release unused tensors

- Support for large file chunk processing

- Automatic path normalization and error checking


# ComfyUI 模型合并插件

这是一个用于 ComfyUI 的模型合并插件，提供两种不同的模型合并方式，支持 safetensors 格式的模型文件合并。

## 更新：

### 20251120

1. **优化模块代码结构，更新mergecore.cp312-win_amd64.pyd、loader.cp312-win_amd64.pyd、merge_operations.cp312-win_amd64.pyd、graphic_manipulation.cp312-win_amd64.pyd**
2. **自动适应不同的 Python 版本**
3. **跨平台工作（Windows、Linux、macOS）**
4. **保持向后兼容性，支持旧的文件命名方式**
5. **增加对python版本3.13的支持**

### 20251119

1. **更新loader.pyd，修复模块编译无法正确加载问题**
2. **更新Windows平台编译版本：merge_operations.cp312-win_amd64.pyd (Windows)，对应python版本3.12**
3. **更新model_merger_node.py导入部分代码**
4. **调整优化整体代码架构**
5. **更新节点使用说明**

### 20251117

1. **更新主文件model_merger_node.py**
2. **更新Windows平台编译版本：merge_operations.cp312-win_amd64.pyd (Windows)，对应python版本3.12**
3. **更新loader，修复loader中代码缩进导致错误问题**
4. **更新工作流model_merger_workflow.json，添加相关使用说明，详见工作流内**
5. **更新节点使用说明**
6. **更新节点相关选择和保存模式的初始默认值**

### 20251116

1. **更新Windows平台编译版本：mergecore.cp312-win_amd64.pyd (Windows)，对应python版本3.12**
2. **添加loader加载器，根据不同平台自动加载对应预编译模块**
3. **优化标准合并模式文件加载进度 - 显示当前正在处理的文件序号和文件名、张量更新统计 - 显示每个文件处理后新增的张量数量和当前总张量数**
4. **更新了loader.py的判断逻辑**
5. **更新Windows平台编译版本：graphic_manipulation.cp312-win_amd64.pyd (Windows)，对应python版本3.12**

## 功能特性

### 两种合并模式

1. **标准模型合并器 (ModelMergerNode)**
   - 直接加载并合并多个 safetensors 模型文件
   - 支持更新模式（合并所有张量）和替换模式（使用最后一个文件）
   - 适用于中小型模型的快速合并

2. **流式模型合并器 (StreamModelMergerNode)**
   - 流式处理大模型分片文件，避免内存溢出
   - 支持分块复制，可自定义块大小
   - Header和编码优化
   - 适用于大型模型（如多GB级别）的安全合并

### 通用功能
- 支持合并多个 safetensors 模型文件
- 提供友好的用户界面，方便指定输入文件和输出路径
- 支持图形化文件选择（需要 tkinter）
- 详细的日志输出，显示合并进度和结果
- 支持自定义输出路径

## 安装方法

方法一（此方法已不需要）：
1. 确保已安装 ComfyUI
2. 将此插件目录复制到 ComfyUI 的 `custom_nodes` 文件夹中
3. 安装依赖：
   ```
   pip install safetensors
   ```
   如需图形化文件选择功能，还需安装：
   ```
   pip install tk
   ```
4. 重启 ComfyUI

方法二：
下载节点文件压缩包，解压缩到当前文件夹，得到文件夹ComfyUI-Model-Merger（特别注意，直接打开后里面如果是ComfyUI-Model-Merger文件夹，而不是多个pyd、py文件，则复制里面的那个文件夹ComfyUI-Model-Merger，确保ComfyUI-Model-Merger文件夹打开后直接就是多个pyd、py文件），
拷贝ComfyUI-Model-Merger文件夹放至ComfyUI\custom_nodes中，
拷贝model_merger_workflow.json放入ComfyUI\user\default\workflows中。

## 使用说明

### 标准模型合并器

1. 在 ComfyUI 中，从 "模型工具" 类别中找到 "模型合并器" 节点
2. 在节点中设置以下参数：
   - **model_files**: 输入模型文件路径，每行一个文件路径
   - **output_file**: 设置合并后的模型保存路径
   - **merge_mode**: 选择合并模式（update: 更新合并，replace: 替换）
3. 可选功能：
   - **select_files**: 打开图形化文件选择对话框
   - **select_directory**: 选择文件夹，自动搜索其中的 safetensors 文件
   - **select_output_file**: 选择输出文件保存位置
4. 点击 "Queue Prompt" 运行工作流
5. 查看控制台输出，了解合并进度和结果

### 流式模型合并器

1. 在 ComfyUI 中，从 "模型工具" 类别中找到 "流式模型合并器" 节点
2. 在节点中设置以下参数：
   - **shard_files**: 输入分片文件路径，每行一个文件路径（按顺序排列）
   - **output_file**: 设置合并后的模型保存路径
   - **chunk_size_mb**: 设置分块大小（MB），用于大文件处理
3. 可选功能：
   - **select_files**: 打开图形化文件选择对话框
   - **select_directory**: 选择文件夹，自动搜索其中的 safetensors 文件
   - **select_output_file**: 选择输出文件保存位置
4. 点击 "Queue Prompt" 运行工作流
5. 查看控制台输出，了解合并进度和结果

## 工作流示例

本插件包含一个示例工作流文件 `model_merger_workflow.json`，你可以在 ComfyUI 中加载此文件来快速开始。
详细使用说明见工作流内。

## 选择建议

- **中小型模型**（< 20GB）：使用标准模型合并器，速度更快
- **大型模型**（≥ 20GB）：使用流式模型合并器，避免内存溢出
- **分片模型文件**：使用流式模型合并器，专门为此场景优化

## 注意事项

- 确保所有输入的模型文件都存在且可访问
- 合并大模型可能需要较长时间和足够的内存
- 合并后的模型将保存在你指定的输出路径
- 如果输出目录不存在，插件会自动创建
- 流式合并器会进行文件验证，确保合并结果的完整性
- 对于分片文件，请确保文件按正确的顺序排列

## 故障排除

- 如果遇到 `No module named 'safetensors'` 错误，请确保已安装 safetensors 库
- 如果文件路径不正确，请检查路径格式，确保使用了正确的反斜杠转义（Windows 下使用 `\\`）
- 如果合并失败，请检查模型文件格式是否正确，是否都是 safetensors 格式
- 如果遇到内存不足错误，请使用流式模型合并器并减小 chunk_size_mb 参数
- 如果无法使用图形化文件选择，请安装 tkinter：`pip install tk`
- 如果流式合并过程中断，请检查磁盘空间是否充足

## 技术特点

### 流式合并器的优势
- 自动处理 Header 大小变化
- 分块复制，避免大文件内存占用
- 完整的文件验证机制
- 详细的进度显示和错误处理

### 性能优化
- 智能内存管理，及时释放不再使用的张量
- 支持大文件分块处理
- 自动路径标准化和错误检查
