# 需要修复的问题清单

## 问题1：清除README.md中的MEAP封面引用

**文件位置：** `cn-translate/README.md` 第5行

**当前内容：**
```markdown
![](assets/00-Vitale-CNS-MEAP-HI.png)
```

**修复为：**
```markdown
![](assets/cover.png)
```

---

## 问题2：清除welcome.md中的MEAP字样

**文件位置：** `cn-translate/welcome.md` 第3行

**当前内容：**
```markdown
感谢您购买 MEAP 版的《Cloud Native Spring In Action》。
```

**修复为：**
```markdown
感谢您购买《Cloud Native Spring In Action》。
```

---

## 问题3：替换封面图片

**操作步骤：**

1. **删除MEAP封面文件：**
   ```bash
   rm cn-translate/assets/00-Vitale-CNS-MEAP-HI.png
   ```

2. **重命名官方封面：**
   ```bash
   mv cn-translate/assets/official_cover_1.png cn-translate/assets/cover.png
   ```

3. **清理临时文件：**
   ```bash
   rm cn-translate/assets/official_cover_2.png
   ```

---

## 问题4：验证Front-matter内容

**检查点：**
- 确认Front-matter/README.md中的内容与官方PDF一致
- 确认没有MEAP相关的描述或引用

**当前状态：**
- ✅ 序言已翻译
- ✅ 前言已翻译
- ✅ 致谢已翻译
- ✅ 关于本书已翻译
- ✅ 内容基于官方PDF，无MEAP引用

---

## 问题5：抽样检查翻译内容准确性

**建议抽样章节：**
1. 第1章（Introduction）- 基础概念
2. 第3章（Getting started）- 实践内容
3. 第8章（Reactive Spring）- 高级主题
4. 第11章（Security）- 安全相关内容
5. 附录A（Development environment）- 环境配置

**检查方法：**
1. 提取官方PDF对应章节的文本
2. 与翻译内容进行对比
3. 确认翻译完整性和准确性

---

## 修复优先级

| 优先级 | 问题 | 影响 | 预计时间 |
|--------|------|------|----------|
| 高 | 清除MEAP引用 | 影响正式版本形象 | 5分钟 |
| 高 | 替换封面图片 | 影响视觉效果 | 5分钟 |
| 中 | 验证Front-matter内容 | 确保内容准确 | 10分钟 |
| 中 | 抽样检查翻译内容 | 确保翻译质量 | 30分钟 |

---

## 修复完成后的验证

1. **检查MEAP引用：**
   ```bash
   grep -rni "MEAP\|meap" cn-translate/ --include="*.md"
   ```
   预期结果：无输出

2. **检查封面文件：**
   ```bash
   ls -la cn-translate/assets/cover.png
   ```
   预期结果：文件存在，大小约2.5MB

3. **检查MEAP文件：**
   ```bash
   find cn-translate/assets/ -name "*MEAP*"
   ```
   预期结果：无输出

4. **构建验证：**
   ```bash
   cd cn-translate && honkit build
   ```
   预期结果：构建成功

---

*清单生成时间：2024年8月9日*
