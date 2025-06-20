#Question 1 answer
square=lambda x:x*x

square_result=square(3)
print('question 1 =>square  1 number using lambda :',square_result)


# Question 2 answer
sum=lambda x,y:x+y
sum_result=sum(2,4)
print('question 2 =>sum tow number using lambda :',sum_result)

# Question 3 answer
def process_list(numbers, func):
    return [func(x) for x in numbers]
double_result=lambda x: x * 2
nums=[1, 2, 3, 4]
list_result=process_list(nums, double_result)
print('question 3 =>double each number in list using lambda :',list_result)


# Question 4 answer
def make_multiplier(n):
    return lambda x: x * n

inputed_n=int(input("Enter a number to create a multiplier: "))
multiplier_result = make_multiplier(inputed_n)
print('question 4 =>multiplier function using lambda :', multiplier_result(inputed_n))
