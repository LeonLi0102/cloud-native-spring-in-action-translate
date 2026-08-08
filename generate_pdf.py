import os
import markdown
from weasyprint import HTML

# 读取所有 markdown 文件
def read_all_markdown():
    content = []
    base_dir = "D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate"
    
    # 按顺序读取各章
    for chapter_dir in sorted(os.listdir(base_dir)):
        if chapter_dir.startswith("0") or chapter_dir.startswith("1"):
            chapter_path = os.path.join(base_dir, chapter_dir)
            if os.path.isdir(chapter_path):
                # 读取 Introduction.md
                intro_file = os.path.join(chapter_path, "Introduction.md")
                if os.path.exists(intro_file):
                    with open(intro_file, 'r', encoding='utf-8') as f:
                        content.append(f.read())
                
                # 读取其他 md 文件
                for md_file in sorted(os.listdir(chapter_path)):
                    if md_file.endswith('.md') and md_file != 'Introduction.md' and md_file != 'SUMMARY.md':
                        file_path = os.path.join(chapter_path, md_file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content.append(f.read())
    
    return '\n\n---\n\n'.join(content)

# 生成 HTML
def generate_html(markdown_content):
    html_content = markdown.markdown(
        markdown_content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>云原生 Spring 实战 中文翻译</title>
        <style>
            body {{ font-family: "Microsoft YaHei", sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
            h1 {{ color: #333; border-bottom: 2px solid #333; padding-bottom: 10px; }}
            h2 {{ color: #666; margin-top: 30px; }}
            h3 {{ color: #888; }}
            code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
            pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background: #f4f4f4; }}
            blockquote {{ border-left: 4px solid #ddd; margin: 0; padding: 10px 20px; color: #666; }}
        </style>
    </head>
    <body>
        <h1>云原生 Spring 实战 中文翻译</h1>
        <p><em>Cloud Native Spring in Action With Spring Boot and Kubernetes</em></p>
        <p><strong>作者：Thomas Vitale</strong></p>
        <hr>
        {html_content}
    </body>
    </html>
    """
    return full_html

# 生成 PDF
def generate_pdf():
    print("读取 markdown 文件...")
    markdown_content = read_all_markdown()
    
    print("生成 HTML...")
    html_content = generate_html(markdown_content)
    
    # 保存 HTML
    html_file = "D:/ProjectFile/cloud-native-spring-in-action-translate/output.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("生成 PDF...")
    pdf_file = "D:/ProjectFile/cloud-native-spring-in-action-translate/云原生Spring实战-中文翻译.pdf"
    HTML(filename=html_file).write_pdf(pdf_file)
    
    print(f"PDF 已生成: {pdf_file}")

if __name__ == "__main__":
    generate_pdf()
