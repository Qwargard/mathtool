import sys
import math


MAX_VALUE = 10000
def main():
    # Разбор параметров командной строки
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print(f"mathtool — решение уравнений вида A*x^2 + B*x + C = 0\n\nИспользование:\n    python mathtool.py                         вывод справки\n    python mathtool.py --help                  вывод справки\n    python mathtool.py solve                   ввод коэффициентов с клавиатуры\n    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами\n\nКоэффициенты A, B, C — целые числа, по модулю не превышающие {MAX_VALUE}")
        sys.exit(0)
    if sys.argv[1] != "solve":
        print("Неизвестная команда", file=sys.stderr)
        sys.exit(1)
    if sys.argv[1] == "solve" and len(sys.argv) == 2:
        a = input("Введите A: ")
        b = input("Введите B: ")
        c = input("Введите C: ")
    elif sys.argv[1] == "solve" and len(sys.argv) == 8:
        if sys.argv[2] != "-a" and sys.argv[4] != "-b" and sys.argv[6] != "-c":
            print("Неизвестный параметр", file=sys.stderr)
            sys.exit(1)
        a=sys.argv[3]
        b=sys.argv[5]
        c=sys.argv[7]
    else:
        print("Неверный набор параметров", file=sys.stderr) 
        sys.exit(1)

    # Получение и преобразование исходных данных в целые числа
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
           print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
           sys.exit(1)

    # Проверка значений на соответствие ограничениям
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
            print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
            sys.exit(1)

    # Решение уравнения и вывод результата
    if a == 0:
       if b != 0:
              print("Уравнение линейное")
              x = -c / b
              print(f"x = {x:.3f}")
       else:
              print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
              sys.exit(1)
    else:
        print("Уравнение квадратное")
        D = b**2 - 4*a*c
        print(f"Дискриминант: {D}")

        if D > 0:
               x1 = (-b + math.sqrt(D))/(2*a)
               x2 = (-b - math.sqrt(D))/(2*a)
               print(f"x1 = {x1:.3f}")
               print(f"x2 = {x2:.3f}")
        elif D == 0:
               x = -b / 2*a
               print(f"x = {x:.3f}")
        else:
               print("Действительных корней нет")



main()