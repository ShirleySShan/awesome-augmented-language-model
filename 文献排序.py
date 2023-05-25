# 打开并读取文本文件中的参考文献列表
with open('reference525.txt', 'r') as file:
    references = file.readlines()

# 对参考文献进行排序
references.sort(key=lambda x: x.split(',')[0])

# 写入排序后的参考文献到新的文本文件
with open('sorted_references525.txt', 'w') as file:
    for reference in references:
        file.write(reference)
        file.write('\n')  # 插入空行