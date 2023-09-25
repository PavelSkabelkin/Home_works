# Дано двузначное и трехзначное число. Для каждого выведите на экран сумму и произведение цифр.
# Ввод пользователем двухзначного и трёхзначного числа
three_dn = int(input("Введите трехзначное число: "))
two_dn = int(input("Введите двухзначное число: "))

# Разложние на цифры трёхначного числа
fig1_three_dn = (three_dn//100) #Вычисление 1го числа
fig2_three_dn = (three_dn//10)%10 #Вычисление 2го числа
fig3_three_dn = three_dn%10 #Вычисление 3го числа

# Вычисление суммы и произведнения для трёхзначного числа
sum_for_three_dn = fig1_three_dn + fig2_three_dn + fig3_three_dn
prod_for_three_dn = fig1_three_dn * fig2_three_dn * fig3_three_dn

# Разложние на цифры двухзначного числа
fig1_two_dn = two_dn //10
fig2_two_dn = two_dn % 10

# Вычисление суммы и произведения двухзначногочисла
sum_for_two_dn = fig1_two_dn + fig2_two_dn
prod_for_two_dn = fig1_two_dn *  fig2_two_dn

# Вывод результатов
print(
  "\nТрехзначиное число:"
  f"\nПервое число:  {fig1_three_dn} \n"
  f"Второе число:  {fig2_three_dn} \n"
  f"Третье число:  {fig3_three_dn} \n"
  f"Сумма чисел: {sum_for_three_dn}\n"
  f"Произведение чисел {prod_for_three_dn} \n"
  f"\n"
  f"Двухзначное число:\n"
  f"Первое число:  {fig1_two_dn} \n"
  f"Второе число:  {fig2_two_dn} \n"
  f"Сумма чисел: {sum_for_two_dn}\n"
  f"Произведение чисел {prod_for_two_dn} \n"
)

