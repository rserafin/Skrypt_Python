# 1.1 Typy daych

# 1.1.1 Liczby
print(17/3)
print(17//3)
print(17%3)
print(5**3)
# 1.1.2 Łańcychy znaków

print('Hello World')
print("Hello World")
print('C:\some\name') #\n - nowa linia
print(r'C:\some\name')

# 1.1.3 Kontrola typów
v = 3
print(v)
v = 'abc'
print(v)
# print('abc' + 3) błąd

# 1.1.4 Listy
squares = [1, 4, 9, 16, 25]
print(squares)

# 1.1.5 Typy mutowalne i niemutowalne
# typy mutowalne: list, dict
# typy niemutowalne: int, float, str, tuple
word = 'abc'
# word[0] = 'X' error
word = 'X' + word[1:]
print(word)
squares = [1, 4, 8]
squares[1] = 10
print(squares)

# 1.1.6 Typy sekwencyjne

# 1.1.6.1 Indeksowanie
squares = [1, 4, 9, 16, 25]
print(squares[0])
print(squares[1])

print(squares[-1])
print(squares[-2])
# print(squares[7]) bład - poza zakresem

# 1.1.6.2 Slicing
print(squares[0:2])
print(squares[3:])
print(squares[:3])
print(squares[:])
print(squares[-2:])
print(squares[3:10])
print(squares[-8:2])

print(squares[1::2])

# 1.1.6.3 Kontkadenacja i powtarzanie
s1 = [1,2]
s2 = [3]
print(s1+s2)
print(2*s1)

# 1.1.6.4 Długość ciągu
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# 1.1.6.5 Operator in
s = [1, 2, 3]
print(1 in s)
print(4 in s)

s = 'abc'
print('ab' in s)
print('bx' in s)

# 1.2 Wartość None
my_none_variable = None

# 1.2.1 Wyrażenie logiczne
# operatory logiczne: or, and, not
# operatory specjalne: (not) in, is (not)
age = 10
has_age_discount = (age < 7) or (age > 65)
print(has_age_discount)

# 1.3 Instrukcje sterujące

# 1.3.1 Instrukcje warunkowe
x = 3
if x > 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# 1.3.1.1 Short-Circut Evaluation
# operatory and i or są obliczene od lewej do prawej

# 1.3.1.2 Wyrażenia warunkowe
# x = true_value if condition else false_value
x = 'even' if (5 % 2) == 0 else 'odd'
print(x)

# 1.3.2 Pętle

# 1.3.2.1 Instrukcja for
words = ['cat', 'windows']
for w in words:
    print(w, len(w))

# 1.3.2.3 Funkcja range
# range(e) - od 0 do e
# range(b, e) - od b do e
# range(b, e, s) - od b do e z krokiem s
for i in range(3):
    print(i)

# 1.3.2.4 Instrukcje break i continue
for n in range(1 ,10):
    if n % 2  == 0:
        print('even - skipped')
        continue
    if n == 5:
        break
    print(n)

# 1.4 Instrukcja pass
class MyEmptyClass:
    pass

def init():
    pass

# 1.5 Definiowanie funkcji
def is_odd(n):
    return (n % 2 == 0)
# pass-by-assignment
# argunenty są przekazywane przez referencje
# do momentu kiedy nie są zmieniane, wtedy przez wartość
def ref_demo(x):
    print("x={:2} id={}".format(x, id(x)))
    x = 42
    print("x={:2} id={}".format(x, id(x)))
x = 9
print(id(x))
ref_demo(x)
print(id(x))

# funkcje zawsze zwracaja wartość - domyślnie None
def no_return():
    pass
print(no_return())

# 1.5.1 Argumenty domyślne
def greet(n_loops, message=None):
    for i in range(n_loops):
        print(message if message is not None else '(-)')
greet(2)
greet(2, 'Hi')

i = 5
def f(arg=i):
    print(arg)
i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))

# 1.5.2 Argumenty słownikowe
def get_travel_time(distance, speed):
    return distance / speed

get_travel_time(10.8, 30)
get_travel_time(distance=10.8, speed=30)
get_travel_time(10.8, speed=30)
# get_travel_time(distance=10.8, 30) błąd
# stosowane, gdy ciężko określić przeznaczenie argumentu
# gdy funkcja przyjmuje wiele argumentów
# bądź kilka parametrów o wartościach domyślnych
def foo(n, p=None, q=None):
    pass
foo(1, q=2)

# 1.5.3 Przeciążanie funkcji
def f(n):
    return n + 42
def f(n, m):
    return n + m
f(3, 4)
# f(3) bład
# W Pythonie nie istnieje przeciążanie funkcji
# Można skorzystać z parametrów domyślnyc
def f(n, m=None):
    if m:
        return n + m + 42
    else:
        return n + 42
