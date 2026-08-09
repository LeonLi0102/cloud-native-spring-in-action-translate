import pymupdf
import os
import re

doc = pymupdf.open('D:/ProjectFile/cloud-native-spring-in-action-translate/Cloud_Native_Spring_in_Action.pdf')

# Images to extract: (chapter, figure_number) -> output path
missing = []

# Chapter 3: 3.9, 3.10
for fig in [9, 10]:
    missing.append((3, fig, f'D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate/assets/ch03/3.{fig}.png'))

# Chapter 4: 4.11
missing.append((4, 11, 'D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate/assets/ch04/4.11.png'))

# Chapter 5: 5.5, 5.6
for fig in [5, 6]:
    missing.append((5, fig, f'D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate/assets/ch05/5.{fig}.png'))

# Chapter 6: 6.1 to 6.16
for fig in range(1, 17):
    missing.append((6, fig, f'D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate/assets/ch06/6.{fig}.png'))

# Chapter 15: 15.1 to 15.9
for fig in range(1, 10):
    missing.append((15, fig, f'D:/ProjectFile/cloud-native-spring-in-action-translate/cn-translate/assets/ch15/15.{fig}.png'))

# Create directories
dirs = set()
for ch, fig, path in missing:
    d = os.path.dirname(path)
    dirs.add(d)
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Search for each figure in the PDF
extracted = 0
not_found = []

for ch, fig, out_path in missing:
    search_str = f'Figure {ch}.{fig}'
    found = False
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        
        if search_str in text:
            # Check if this is the figure caption page (not just a reference)
            # The caption usually appears at the bottom of the figure
            # We'll render the page that contains the figure caption
            pix = page.get_pixmap(dpi=200)
            pix.save(out_path)
            print(f'✅ {search_str} -> {out_path} (PDF page {page_num+1})')
            extracted += 1
            found = True
            break  # Take the first occurrence
    
    if not found:
        not_found.append(f'{search_str} (ch{ch})')

doc.close()

print(f'\n共提取 {extracted}/{len(missing)} 张图片')
if not_found:
    print(f'未找到: {", ".join(not_found)}')
