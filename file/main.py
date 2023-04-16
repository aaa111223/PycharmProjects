# 先定义输入文件和输出文件的路径
input_file = "input.txt"
output_file = "output.txt"
'''
将一个文件的每4行转换成一行数据并已逗号分隔，将结果写入一个新的文件
value1
value2
value3
value4
value5
value6
value7
'''

# 打开输入文件，使用 with 语句可以确保文件在使用后自动关闭
with open(input_file, "r") as f1:
    # 读取输入文件中的行到列表中
    data_lines = [line.strip() for line in f1.readlines()]

# 打开输出文件，使用 with 语句可以确保文件在使用后自动关闭
with open(output_file, "w") as f2:
    # 遍历输入数据中的每4行，组成一行数据，并写入到输出文件中
    for i in range(0, len(data_lines), 4):
        # 取出4行数据
        group_lines = data_lines[i:i+4]
        # 将4行数据拼接成一个逗号分隔的字符串，每个值之间插入空格
        group_str = ", ".join([line for line in group_lines])
        # 写入到输出文件中
        f2.write(group_str + "\n")


'''
有一行数据都每个值以逗号分隔，如何快速将这行数据分行，每行只有4个值
data_line = 'value1,value2,value3,value4,value5,value6,value7,value8,value9'
'''

# 先定义输入文件和输出文件的路径
input_file = "input.txt"
output_file = "output.txt"

# 打开输入文件，使用 with 语句可以确保文件在使用后自动关闭
with open(input_file, "r") as f1:
    # 读取输入文件中的行到列表中
    data_lines = [line.strip() for line in f1.readlines()]

# 打开输出文件，使用 with 语句可以确保文件在使用后自动关闭
with open(output_file, "w") as f2:
    # 遍历输入数据中的每一行
    for data_line in data_lines:
        # 使用与上一个示例中相同的代码将一行数据分成多行，每行只有四个值
        data_list = data_line.split(",")
        group_list = [",".join(data_list[i:i+4]) for i in range(0, len(data_list), 4)]
        # 将分行后的结果写入到输出文件中
        for group in group_list:
            f2.write(group + "\n")


'''
将一个文件按10行进行分隔生成一个新文件


'''
# 先定义输入文件和输出文件的路径
input_file = "input.txt"

# 打开输入文件，使用 with 语句可以确保文件在使用后自动关闭
with open(input_file, "r") as f:
    # 读取输入文件中的行到列表中
    data_lines = [line.strip() for line in f.readlines()]

# 计算数据行数，以 10 为单位进行分组
total_data_lines = len(data_lines)
groups = (total_data_lines + 10 - 1) // 10  # 使用 "//" 进行向上取整

# 遍历每一个数据组，将其写入新的文件中
for i in range(groups):
    # 构造新的文件名，以当前组的编号作为文件名的一部分
    output_file = "output_" + str(i + 1) + ".txt"

    # 打开输出文件，使用 with 语句可以确保文件在使用后自动关闭
    with open(output_file, "w") as f2:
        # 遍历分组中的每一个数据行，将其写入到输出文件中
        for j in range(10):
            # 计算当前行在原始数据中的索引值
            index = i * 10 + j
            # 如果当前索引超过了数据行数，则结束循环
            if index >= total_data_lines:
                break
            # 将该行数据写入到输出文件中
            f2.write(data_lines[index] + "\n")
'''
将一个文件分成5个文件
'''
# 先定义输入文件和输出文件的路径
input_file = "input.txt"

# 打开输入文件，使用 with 语句可以确保文件在使用后自动关闭
with open(input_file, "r") as f:
    # 读取输入文件中的行到列表中
    data_lines = [line.strip() for line in f.readlines()]

# 计算数据行数
total_data_lines = len(data_lines)

# 计算每个文件中应该包含的数据行数
lines_per_file = total_data_lines // 5

# 遍历每一个文件，将其写入新的文件中
for i in range(5):
    # 构造新的文件名，以当前文件的编号作为文件名的一部分
    output_file = "output_" + str(i + 1) + ".txt"

    # 打开输出文件，使用 with 语句可以确保文件在使用后自动关闭
    with open(output_file, "w") as f2:
        # 计算当前文件应该包含的起始索引和结束索引
        start_index = i * lines_per_file
        end_index = start_index + lines_per_file
        # 如果是最后一个文件，则结束索引取最后一个数据行的索引
        if i == 4:
            end_index = total_data_lines
        # 遍历计算出的索引范围内的数据行，将其写入到输出文件中
        for j in range(start_index, end_index):
            f2.write(data_lines[j] + "\n")
