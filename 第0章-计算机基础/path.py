import os
import sys

# 打印当前工作目录（绝对路径）
print("当前工作目录:", os.getcwd())

# 假设我们有一个名为"data.txt"的文件在当前目录
# 使用相对路径打开文件
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("使用相对路径读取文件内容:", content[:50] + "...")
except FileNotFoundError:
    print("文件未找到（使用相对路径）")

# 使用绝对路径打开同一个文件
try:
    absolute_path = os.path.join(os.getcwd(), "data.txt")
    with open(absolute_path, "r") as file:
        content = file.read()
        print("使用绝对路径读取文件内容:", content[:50] + "...")
except FileNotFoundError:
    print("文件未找到（使用绝对路径）")

# 打印Python解释器的路径
print("Python解释器路径:", sys.executable)

# 打印当前脚本的路径
print("当前脚本的绝对路径:", os.path.abspath(__file__))

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
print("脚本所在目录:", script_dir)

# 使用相对于脚本目录的路径
try:
    config_path = os.path.join(script_dir, "config.ini")
    with open(config_path, "r") as file:
        content = file.read()
        print("配置文件内容:", content[:50] + "...")
except FileNotFoundError:
    print("配置文件未找到")

# 访问上一级目录中的文件
try:
    parent_dir = os.path.dirname(script_dir)
    parent_file = os.path.join(parent_dir, "parent_data.txt")
    with open(parent_file, "r") as file:
        content = file.read()
        print("父目录文件内容:", content[:50] + "...")
except FileNotFoundError:
    print("父目录文件未找到")
