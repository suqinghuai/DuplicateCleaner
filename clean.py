import os
import re

def clean_duplicate_files():
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 正则表达式匹配带有 (1), (2), (3) 等后缀的文件名
    # 例如：匹配 "测试文件 (1).txt" 或 "图片(2).png"
    pattern = re.compile(r'^(.*?)(\s*\(\d+\))(\.[a-zA-Z0-9_]+)?$')
    
    deleted_files = []
    skipped_files = []
    
    print(f"开始扫描目录及其子目录: {current_dir}\n")
    
    for root, _, files in os.walk(current_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            match = pattern.match(filename)
            if match:
                base_name = match.group(1)
                extension = match.group(3) if match.group(3) else ""
                original_filename = f"{base_name}{extension}"
                original_filepath = os.path.join(root, original_filename)
                
                if os.path.exists(original_filepath):
                    # 检查文件大小是否一致
                    if os.path.getsize(filepath) == os.path.getsize(original_filepath):
                        try:
                            os.remove(filepath)
                            deleted_files.append(filepath)
                            print(f"[-] 成功清除: {filepath} (对应原始文件: {original_filepath})")
                        except Exception as e:
                            print(f"[x] 清除失败: {filepath}, 错误: {e}")
                    else:
                        skipped_files.append(filepath)
                        print(f"[!] 跳过文件: {filepath} (文件大小不一致)")
                else:
                    skipped_files.append(filepath)
                    print(f"[!] 跳过文件: {filepath} (原始文件不存在)")
    
    print("\n" + "="*40)
    print("清理完成！")
    print(f"共清除了 {len(deleted_files)} 个重复文件。")
    if deleted_files:
        print("清除列表:")
        for df in deleted_files:
            print(f"  - {df}")
    
    print(f"\n共跳过了 {len(skipped_files)} 个文件。")
    if skipped_files:
        print("跳过列表:")
        for sf in skipped_files:
            print(f"  - {sf}")

if __name__ == "__main__":
    clean_duplicate_files()
    input("\n按任意键退出...")
