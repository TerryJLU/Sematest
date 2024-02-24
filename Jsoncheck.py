import json

def check_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        # 如果需要，这里可以添加更多的逻辑来检查data的内容
        print("JSON file is valid and successfully loaded.")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 替换成你的JSON文件路径
file_path = 'path/to/your/file.json'
check_json_file(file_path)
