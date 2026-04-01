form = input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : ")
if form == "1" :
  expression = input("수식을 입력하세요 :")
  result1 = eval(expression)
  print(expression , "결과는 ", result1 , "입니다.")

else :
  num1 = int(input("첫 번째 숫자를 입력하세요 : "))
  num2 = int(input("두 번째 숫자를 입력하세요 : "))
  result2 = (num2 - num1 + 1) * (num1 + num2) / 2
  result3 = int(result2)


  print(num1,"+...+",num2,"는",result3 ,"입니다.")