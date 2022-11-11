## Assignment Part-1
#Q1. Why do we call Python as a general purpose and high-level programming language?
#Python is a High level interpreter language and easy to learn and supports various frameworks across multiple domains of computer science.

#Q2. Why is Python called a dynamically typed language?
#Python is Dynamically types as the we are not supposed to compulsary define the varaible data type it can interpret on its own.

#Q3. List some pros and cons of Python programming language?
#Python is dynamically typed and interpreted language and easy to learn and supports vast libraries and frameworks across various fields,when it comes to con its execution time is slow compared to other programming languages.

#Q4. In what all domains can we use Python?
#Software development,Web development,testing,data science,Big data scripting and Devops and many more.

#Q5. What are variable and how can we declare them?
#varaible are symbols that defined that referes to the object 

#Q6. How can we take an input from the user in Python?

user=input()

#Q7. What is the default datatype of the value that has been taken as an input using input() function?
str

#Q8. What is type casting?
#changing data dtype of varaible is called type casting eg int to str

#Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
#yes we can by using comprehensions

[int(i) for i in input().split()]

#Q10. What are keywords?
#Keywords are some predefined and reserved words in python that have special meanings like lambda,def,if ,else,elf,for etc 

#Q11. Can we use keywords as a variable? Support your answer with reason.
#we can use keyword as varible by converting it to string

#Q12. What is indentation? What's the use of indentaion in Python?
#indentation are set of spacing rules which are to be followed while programming,python is sensetive to indentation so it is neccessary to use proper indentation

#Q13. How can we throw some output in Python?
#by using print()

#Q14. What are operators in Python?
#operators helps us in performing arithemtic,comparision,logical,boolean operations

#Q15. What is difference between / and // operators?

#'/' returns float and '//' return integer

#Q16. Write a code that gives following as an output.
#iNeuroniNeuroniNeuroniNeuron

s=iNeuron
print(s*4)

#Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
s=int(input())
if s%2==0:
   return even
else:
   return odd

#Q18. What are boolean operator?

#True or False are boolean operators

#Q19. What will the output of the following?

#1 or 0  1

#0 and 0  0

#True and False and True==false

#1 or 0 or 0 =1

#Q20. What are conditional statements in Python?
#condition statements in python are used to perform certain operations when certain conditions are fulfilled.

#Q21. What is use of 'if', 'elif' and 'else' keywords?

#if is used to apply condition on given statement else is used when condition is if is not satisfied
#elif is used when there are multiple conditions.

#Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

age=int(input())
if age>=18:
   print('"I can vote")
else:
    print("I can't vote")

#Q23. Write a code that displays the sum of all the even numbers from the given list.

numbers = [12, 75, 150, 180, 145, 525, 50]

print(sum[i for i in numbers if i%2==0])

#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

a,b,c=[int(i) for i in input().split()]
max=0
if a>b and a>c:
  max=a
elif b>a and b>c:
  max=b
else:
  max=c
print(max)

#Q25. Write a program to display only those numbers from a list that satisfy the following conditions

#- The number must be divisible by five

#- If the number is greater than 150, then skip it and move to the next number

#- If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]


for i in numbers:
   if i>500:
      break
   elif i>150:
      continue
   elif i%5==0:
      print(i)