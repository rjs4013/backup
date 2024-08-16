def compare_files(file1, file2):
    with open("a.txt", 'r') as f1, open("b.txt", 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    differences = [(i, lines1[i], lines2[i]) for i in range(min(len(lines1), len(lines2))) if lines1[i] != lines2[i]]
    if len(lines1) != len(lines2):
        differences.extend([(i, lines1[i], '') for i in range(len(lines2), len(lines1))])
        differences.extend([(i, '', lines2[i]) for i in range(len(lines1), len(lines2))])

    return differences

file1 = 'data1.txt'
file2 = 'data2.txt'

differences = compare_files(file1, file2)
for diff in differences:
    index, line1, line2 = diff
    print(f"Line {index + 1}:")
    print(f"  File1: {line1.strip()}")
    print(f"  File2: {line2.strip()}")