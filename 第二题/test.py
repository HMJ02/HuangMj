def check_brackets(input_str):
    stack = []
    results = ','.join(' ' for _ in range(len(input_str))).split(',')
    for i, char in enumerate(input_str):
        if char == '(':
            stack.append((char, i))
        elif char == ')':
            if not stack or i != stack[-1][1] + 1:
                results[i] = '?'  # 标记缺失的右括号
            else:
                stack.pop()

    for char, i in stack:
        results[i] = '?'  # 标记缺失的左括号

    return ''.join(results)


# 测试用例
test_cases = [
    "aaaaa((()))",
    "(sd()ga))",
    "(()",
    "))()(",
]

for test_case in test_cases:
    result = check_brackets(test_case)
    print(test_case)
    print(result)
