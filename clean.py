import os
import re

def clean_duplicate_files():
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 正则表达式匹配带有 (1), (2), (3) 等后缀的文件名
    # 例如：匹配 "测试文件 (1).txt" 或 "图片(2).png"
    pattern = re.compile(r'^(.*?)(\s*\(\d+\))(\.[a-zA-Z0-9_]+)?$')
    
    deleted_files = []
    
    print(f"开始扫描目录: {current_dir}\n")
    
    for filename in os.listdir(current_dir):
        filepath = os.path.join(current_dir, filename)
        
        # 只处理文件，跳过文件夹
        if not os.path.isfile(filepath):
            continue
            
        match = pattern.match(filename)
        if match:
            base_name = match.group(1)
            extension = match.group(3) if match.group(3) else ""
            original_filename = f"{base_name}{extension}"
            
            try:
                os.remove(filepath)
                deleted_files.append(filename)
                print(f"[-] 成功清除: {filename} (对应原始文件: {original_filename})")
            except Exception as e:
                print(f"[x] 清除失败: {filename}, 错误: {e}")
                    
    print("\n" + "="*40)
    print("清理完成！")
    print(f"共清除了 {len(deleted_files)} 个重复文件。")
    if deleted_files:
        print("清除列表:")
        for df in deleted_files:
            print(f"  - {df}")

if __name__ == "__main__":
    clean_duplicate_files()
    input("\n按任意键退出...")
