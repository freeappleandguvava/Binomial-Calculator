import sympy as sp

def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def binomial_expansion(a, b, c):
    triangle = pascal(c + 1)

    result = 0
    terms = []
    for k in range(c + 1):
        binomial_c = triangle[c][k]
        term = binomial_c * (a ** (c - k)) * (b ** k)

        if isinstance(a, sp.Basic) or isinstance(b, sp.Basic):
            terms.append(f"{binomial_c} * {a}^{c-k} * {b}^{k}")
        else:
            result += term

    if terms:
        return " + ".join(terms)

    return result

def input_handler(value):
    try:
        return float(value)
    except ValueError:
        return sp.symbols(value)

a_value = input("Enter the value for a (a+b)^c: ")
b_value = input("Enter the value for b (a+b)^c: ")
c_value = int(input("Enter the exponent c (a+b)^c: "))

a = input_handler(a_value)
b = input_handler(b_value)

result = binomial_expansion(a, b, c_value)

print(f"Result:({a_value} + {b_value})^{c_value}:")
print("|--------------------------------|")
print(f"| {result} |")
print("|--------------------------------|")

