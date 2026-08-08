import os
import markdown

def read_all_markdown():
    content = []
    base_dir = "D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate"
    
    # 读取 Welcome
    welcome_file = os.path.join(base_dir, "Welcome.md")
    if os.path.exists(welcome_file):
        with open(welcome_file, 'r', encoding='utf-8') as f:
            content.append(f.read())
    
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

def generate_html(markdown_content):
    html_content = markdown.markdown(
        markdown_content,
        extensions=['tables', 'fenced_code']
    )
    
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>云原生 Spring 实战 中文翻译</title>
    <style>
        body {{ font-family: "Microsoft YaHei", sans-serif; line-height: 1.8; max-width: 900px; margin: 0 auto; padding: 40px; font-size: 14px; }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 15px; page-break-before: always; }}
        h1:first-of-type {{ page-break-before: avoid; }}
        h2 {{ color: #34495e; margin-top: 40px; }}
        h3 {{ color: #7f8c8d; }}
        code {{ background: #ecf0f1; padding: 2px 6px; border-radius: 3px; font-family: Consolas, monospace; }}
        pre {{ background: #2c3e50; color: #ecf0f1; padding: 20px; border-radius: 5px; overflow-x: auto; }}
        pre code {{ background: transparent; color: inherit; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #bdc3c7; padding: 12px; text-align: left; }}
        th {{ background: #ecf0f1; font-weight: bold; }}
        blockquote {{ border-left: 4px solid #3498db; margin: 20px 0; padding: 15px 25px; background: #f8f9fa; color: #555; }}
        img {{ max-width: 100%; height: auto; }}
        hr {{ border: none; border-top: 1px solid #ecf0f1; margin: 40px 0; }}
        @media print {{
            body {{ font-size: 12pt; }}
            h1 {{ page-break-before: always; }}
            pre {{ white-space: pre-wrap; word-wrap: break-word; }}
        }}
    </style>
</head>
<body>
    <h1 style="text-align: center; page-break-before: avoid;">云原生 Spring 实战 中文翻译</h1>
    <p style="text-align: center; color: #7f8c8d;"><em>Cloud Native Spring in Action With Spring Boot and Kubernetes</em></p>
    <p style="text-align: center;"><strong>作者：Thomas Vitale</strong></p>
    <p style="text-align: center; color: #95a5a6;">翻译基于 AI 辅助完成</p>
    <hr>
    {html_content}
</body>
</html>"""
    return full_html

def main():
    print("读取 markdown 文件...")
    markdown_content = read_all_markdown()
    
    print("生成 HTML...")
    html_content = generate_html(markdown_content)
    
    output_file = "D:/ProjectFile/cloud-native-spring-in-action-translate/云原生Spring实战-中文翻译.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML 已生成: {output_file}")
    print("请在浏览器中打开此文件，然后使用 Ctrl+P 打印为 PDF")

if __name__ == "__main__":
    main()
