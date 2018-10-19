from flask import Flask, render_template, request
import re
import math
app = Flask(__name__)

#new question- Rounding off to nearest palindrome-2 digit inputs only- Easy question
@app.route('/first', methods=["post","get"] )
def first():
    inputFirst = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            x=int(request.form['input'])
            if(x%10 == x):
                inputFirst= x
            elif(x%100 ==x):
                if(x%11 < 6):
                    n= x- (x%11)
                else:
                    n= x + (11-(x)%11)
                inputFirst= n
            else:
                inputFirst = 'You just entered an invalid integer.Look at the instruction.'
        else:
            inputFirst = 'Invalid Input'
    return render_template('first.html', input=inputFirst)

'''New question-Square of first digit plus rest of the numbers
then square of second number and rest added and repeat. Eg- i/p 1234. working-> 1^2 + 2 + 3 + 4=10    2^2 + 3 + 4= 11  3^2 + 4= 13   4^2= 16. O/p is 10 11 13 16'''

@app.route('/second', methods=["post","get"] )
def second():
    inputSecond = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            tot=[]
            n=int(request.form['input'])
            li=str(n)
            for i in range(len(li)):
                sum= int(li[i])**2
                for j in range(i+1,len(li)):
                    sum+=int(li[j])
                tot.append(str(sum))
                sum=0
            inputSecond= " ".join(tot)
        else:
            inputSecond = 'Invalid Input'
    return render_template('second.html', input=inputSecond)


'''new question- Takes a string and prints all the characters at prime number positions. Eg- i/p- Shithij o/p- hihj'''
@app.route('/third', methods=["post","get"] )
def third():
    inputThird = None
    if request.method == "POST":
        if(len(request.form['input'])>1):
            def primecheck(n):
                  if n <= 1:
                    return False
                  for i in range(2, n):
                    if n % i==0:
                        return False
                  return True

            def prime_index(n):
                p = list(n)
                s = ""
                for i in range (2, len(p) + 1):
                    if primecheck(i):
                        s = s + n[i-1]
                li.append(s)

            n= request.form['input']
            li=[]
            prime_index(n)
            inputThird= " ".join(li)
        else:
            inputThird= "Invalid input for this question"

    return render_template('third.html', input=inputThird)


#new question-Heron's formula to find area of a triangle
@app.route('/fourth', methods=["post","get"] )
def fourth():
    inputFourth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            a,b,c = request.form['input'].split()
            a,b,c = int(a), int(b), int(c)
            if(a+b>c and a+c>b and b+c>a):
                s= (a+b+c)/2
                inputFourth = float((s*(s-a)*(s-b)*(s-c))**0.5)
            else:
                 inputFourth = 'Invalid input for this question'
        else:
            inputFourth = 'Invalid Input'
    return render_template('fourth.html', input=inputFourth)


#Find the sum of squares of digits multiplying each square with (-1)^n, n being the digit position. I/p is 1234. O/p is 1^2 - 2^2 + 3^2 - 4^2= -10.
@app.route('/fifth', methods=["post","get"] )
def fifth():
    inputFifth = None
    if request.method == "POST":
        num=int(request.form['input'])
        digits=[]
        sum=0
        while(num>0):
            rem=num%10
            num=num//10
            digits.append(rem)
        list.reverse(digits)
        for i in range(len(digits)):
            sum=sum+((-1)**(i))*((digits[i])**2)
        inputFifth=sum
    return render_template('fifth.html', input=inputFifth)

'''New question- Find sum until 1 digit remains. Eg-9876-i/p  9+8+7+6=30, 3+0=3, 3-o/p'''
@app.route('/sixth', methods=["post","get"] )
def sixth():
    inputSixth = None
    if request.method == "POST":
        if re.search('[0-9]', request.form['input']):
            n= int(request.form['input'])
            sum= 0
            while(n>0 or sum>9):
                if(n == 0):
                    n= sum
                    sum= 0
                sum+= n%10
                n//= 10
            inputSixth= sum
        else:
            inputSixth = 'Invalid Input'
    return render_template('sixth.html', input=inputSixth)


#Sum of the odd digits in a number to the power of themselves. I/p- 2331. O/p is 3^3 + 3^3 + 1^1 = 55 . i/p is 123 o/p is 1^1+ 3^3 = 28
@app.route('/seventh', methods=["post","get"] )
def seventh():
    inputSeventh = None
    if request.method == "POST":
            num= int(request.form['input'])
            digits=[]
            sum=0
            while(num>0):
                rem=num%10
                num=num//10
                digits.append(rem)
                digits.reverse()
            for i in range(len(digits)):
                if(digits[i]%2!=0):
                    sum=sum+(digits[i]**digits[i])
            inputSeventh=sum
    return render_template('seventh.html', input=inputSeventh)


#Distance formula sum with a 4 digit input. i/p is 2345, o/p distance formula between (2,4) and (3,5)- This is the hard question
@app.route('/eighth', methods=["post","get"] )
def eighth():
    inputEighth = None
    if request.method == "POST":
            x=int(request.form['input'])
            li=[]
            while(x>0):
                rem=x%10
                x=x//10
                li.append(rem)
            list.reverse(li)
            inputEighth=((li[0]-li[2])**2+(li[1]-li[3])**2)**0.5
    return render_template('eighth.html', input=inputEighth)


@app.route('/', methods=["post","get"] )
def opening():
    return render_template('opening.html')

@app.route('/actualend', methods=["post","get"] )
def actualend():
    return render_template('actualend.html')

@app.route('/end', methods=["post","get"] )
def end():
    return render_template('end.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
