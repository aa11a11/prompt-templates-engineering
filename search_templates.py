#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提示词模板搜索工具
用于快速查找和浏览提示词模板库中的模板
"""

import os
import sys
from pathlib import Path

class TemplateSearcher:
    def __init__(self, templates_dir="templates"):
        self.templates_dir = Path(templates_dir)
        self.templates = []
        self.load_templates()
    
    def load_templates(self):
        """加载所有模板文件"""
        if not self.templates_dir.exists():
            print(f"错误: 模板目录 '{self.templates_dir}' 不存在")
            return
        
        for category_dir in self.templates_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                for template_file in category_dir.glob("*.md"):
                    self.templates.append({
                        'category': category,
                        'name': template_file.stem,
                        'path': template_file
                    })
    
    def search(self, keyword):
        """根据关键词搜索模板"""
        keyword = keyword.lower()
        results = []
        
        for template in self.templates:
            # 搜索分类名、模板名和文件内容
            if (keyword in template['category'].lower() or 
                keyword in template['name'].lower()):
                results.append(template)
                continue
            
            # 搜索文件内容
            try:
                with open(template['path'], 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    if keyword in content:
                        results.append(template)
            except Exception as e:
                print(f"警告: 读取文件 {template['path']} 失败: {e}")
        
        return results
    
    def list_all(self):
        """列出所有模板"""
        if not self.templates:
            print("没有找到任何模板")
            return
        
        categories = {}
        for template in self.templates:
            category = template['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(template)
        
        print("\n=== 提示词模板库 ===\n")
        for category, templates in sorted(categories.items()):
            print(f"📁 {category}")
            for template in templates:
                print(f"  - {template['name']}")
            print()
    
    def show_template(self, template_path):
        """显示模板内容"""
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                print(f.read())
        except Exception as e:
            print(f"错误: 无法读取模板文件: {e}")
    
    def display_results(self, results):
        """显示搜索结果"""
        if not results:
            print("没有找到匹配的模板")
            return
        
        print(f"\n找到 {len(results)} 个相关模板:\n")
        for i, template in enumerate(results, 1):
            print(f"{i}. [{template['category']}] {template['name']}")
            print(f"   路径: {template['path']}")
            print()

def print_usage():
    """打印使用说明"""
    print("""
提示词模板搜索工具

用法:
  python search_templates.py [选项] [关键词]

选项:
  -l, --list              列出所有模板
  -s, --search <关键词>   搜索包含关键词的模板
  -v, --view <路径>       查看指定模板的内容
  -h, --help              显示帮助信息

示例:
  python search_templates.py -l                    # 列出所有模板
  python search_templates.py -s 写作               # 搜索写作相关模板
  python search_templates.py -s 代码审查           # 搜索代码审查模板
  python search_templates.py -v templates/写作/文章写作.md  # 查看指定模板
""")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    searcher = TemplateSearcher()
    
    command = sys.argv[1]
    
    if command in ['-h', '--help']:
        print_usage()
    elif command in ['-l', '--list']:
        searcher.list_all()
    elif command in ['-s', '--search']:
        if len(sys.argv) < 3:
            print("错误: 请提供搜索关键词")
            return
        keyword = sys.argv[2]
        results = searcher.search(keyword)
        searcher.display_results(results)
    elif command in ['-v', '--view']:
        if len(sys.argv) < 3:
            print("错误: 请提供模板路径")
            return
        template_path = sys.argv[2]
        searcher.show_template(template_path)
    else:
        # 默认为搜索
        results = searcher.search(command)
        searcher.display_results(results)

if __name__ == "__main__":
    main()
