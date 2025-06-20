def multiplier(factor):
    def multiply(x):
        return x*factor
    return multiply


double_MG=multiplier(2)
print(double_MG(5))