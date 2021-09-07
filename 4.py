import math


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_sigma(numbers, mean):
    sum = 0
    n = len(numbers)
    for xi in numbers:
        val = math.pow((xi - mean), 2)
        sum = sum + val
    sigma = math.sqrt(sum / n - 1)
    return sigma


def normal_distribution(numbers, mean, sigma):
    x1 = math.sqrt(2 * math.pi)
    denominator_value = 1 / (sigma * x1)

    res = []
    for x in numbers:
        val1 = -0.5 * math.pow(((x - mean) / sigma), 2)
        val2 = denominator_value * math.exp(val1)
        res.append(val2)
    return res


numbers = [7, 11, 11, 15, 20, 28]
mean = calculate_mean(numbers)
sigma = calculate_sigma(numbers, mean)

normal_dis = normal_distribution(numbers, mean, sigma)

print(f"Numbers (X) : \n{numbers} \n")
print(f"Normal Distribution F(X) : \n{normal_dis}")
