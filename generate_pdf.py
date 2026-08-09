#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 GitBook 的 HTML 生成带目录的 PDF
"""

import os
import re
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.chapter_count = 0
        # 添加中文字体
        self.add_font('MSYH', '', 'C:/Windows/Fonts/msyh.ttc', uni=True)
        self.add_font('MSYH', 'B', 'C:/Windows/Fonts/msyhbd.ttc', uni=True)
        
    def header(self):
        self.set_font('MSYH', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Cloud Native Spring in Action - 中文翻译', 0, 0, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('MSYH', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.chapter_count += 1
        self.set_font('MSYH', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f'{self.chapter_count}. {title}', 0, 1)
        self.ln(5)
    
    def section_title(self, title):
        self.set_font('MSYH', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, title, 0, 1)
        self.ln(3)
    
    def sub_title(self, title):
        self.set_font('MSYH', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, title, 0, 1)
        self.ln(2)
    
    def body_text(self, text):
        self.set_font('MSYH', '', 10)
        self.set_text_color(0, 0, 0)
        # 处理多行文本
        for line in text.split('\n'):
            if line.strip():
                self.multi_cell(0, 5, line)
                self.ln(2)
    
    def code_block(self, code):
        self.set_font('Courier', '', 8)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(0, 0, 0)
        # 处理代码块
        for line in code.split('\n'):
            if line.strip():
                self.cell(0, 4, '  ' + line, 0, 1, fill=True)
        self.ln(3)
    
    def add_toc_entry(self, title, level=0):
        self.set_font('MSYH', '', 10)
        indent = '  ' * level
        self.cell(0, 6, f'{indent}{title}', 0, 1)


def extract_content_from_html(html_file):
    """从 HTML 文件提取文本内容"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 简单的 HTML 到文本转换
    # 移除脚本和样式
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    
    # 提取标题
    titles = re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', content, re.DOTALL)
    
    # 提取段落
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
    
    # 提取代码块
    codes = re.findall(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', content, re.DOTALL)
    
    return titles, paragraphs, codes


def generate_pdf():
    """主函数：生成 PDF"""
    print("开始生成 PDF...")
    
    base_dir = "D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate"
    
    # 创建 PDF 对象
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # 添加封面页
    pdf.add_page()
    pdf.set_font('MSYH', 'B', 24)
    pdf.ln(40)
    pdf.cell(0, 15, 'Cloud Native Spring in Action', 0, 1, 'C')
    pdf.set_font('MSYH', '', 16)
    pdf.cell(0, 10, 'With Spring Boot and Kubernetes', 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font('MSYH', '', 12)
    pdf.cell(0, 8, '中文翻译', 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font('MSYH', '', 10)
    pdf.cell(0, 6, '作者：Thomas Vitale', 0, 1, 'C')
    pdf.cell(0, 6, '翻译：社区贡献', 0, 1, 'C')
    pdf.cell(0, 6, '翻译工具：AI 辅助', 0, 1, 'C')
    
    # 添加目录页
    pdf.add_page()
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 10, '目录', 0, 1)
    pdf.ln(5)
    
    # 读取各章并生成 PDF
    for chapter_dir in sorted(os.listdir(base_dir)):
        if chapter_dir.startswith('0') or chapter_dir.startswith('1'):
            chapter_path = os.path.join(base_dir, chapter_dir)
            if os.path.isdir(chapter_path):
                # 读取 Introduction.md 获取章标题
                intro_file = os.path.join(chapter_path, 'Introduction.md')
                if os.path.exists(intro_file):
                    with open(intro_file, 'r', encoding='utf-8') as f:
                        intro_content = f.read()
                    
                    # 提取章标题
                    title_match = re.search(r'^#\s+(.+)$', intro_content, re.MULTILINE)
                    if title_match:
                        chapter_title = title_match.group(1).strip()
                        pdf.add_toc_entry(chapter_title)
                        
                        # 添加章节页
                        pdf.add_page()
                        pdf.chapter_title(chapter_title)
                        
                        # 添加章节简介
                        intro_text = re.sub(r'^#\s+.+$', '', intro_content, flags=re.MULTILINE).strip()
                        if intro_text:
                            pdf.body_text(intro_text)
                        
                        # 读取小节文件
                        for md_file in sorted(os.listdir(chapter_path)):
                            if md_file.endswith('.md') and md_file != 'Introduction.md' and md_file != 'SUMMARY.md':
                                file_path = os.path.join(chapter_path, md_file)
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    section_content = f.read()
                                
                                # 提取小节标题
                                section_title_match = re.search(r'^#{1,3}\s+(.+)$', section_content, re.MULTILINE)
                                if section_title_match:
                                    section_title = section_title_match.group(1).strip()
                                    pdf.add_toc_entry(section_title, level=1)
                                    
                                    # 添加小节内容
                                    pdf.section_title(section_title)
                                    
                                    # 提取正文内容
                                    lines = section_content.split('\n')
                                    in_code = False
                                    code_buffer = []
                                    
                                    for line in lines:
                                        if line.strip().startswith('```'):
                                            if in_code:
                                                # 结束代码块
                                                pdf.code_block('\n'.join(code_buffer))
                                                code_buffer = []
                                                in_code = False
                                            else:
                                                # 开始代码块
                                                in_code = True
                                        elif in_code:
                                            code_buffer.append(line)
                                        elif line.strip() and not line.strip().startswith('#'):
                                            # 正文内容
                                            pdf.body_text(line)
    
    # 保存 PDF
    output_file = "D:/ProjectFile/cloud-native-spring-in-action-translate/云原生Spring实战-中文翻译-完整版.pdf"
    pdf.output(output_file)
    print(f"PDF 已生成: {output_file}")
    print(f"共 {pdf.chapter_count} 章")


if __name__ == "__main__":
    generate_pdf()
