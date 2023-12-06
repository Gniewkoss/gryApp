# Zadanie domowe z programowania dynamicznego

Załóżmy, że w ustalono następujące opłaty za przejechane odcinki autostradami:

| Kilometraż | Opłata |
| ---------- | ------ |
| 1-100      | 10     |
| 101-200    | 30     |
| 201-300    | 60     |
| 301-400    | 70     |
| 401-500    | 80     |
| 501-600    | 90     |
| 601-700    | 120    |
| 701-800    | 120    |
| 801-900    | 130    |
| 901-1000   | 130    |
| 1001-1100  | 150    |
| 1101-1200  | 160    |

a dodatkowo z przepisów wynika, że bramki poboru opłat możemy (ale nie musimy) stawiać w punktach odległych o 100, 200, 300, ... km od początku odcinka trasy.
Ciekawe więc, ile i gdzie bramek powinniśmy ustawić żeby zarobić jak najwięcej na autostradzie o długości 482km?

W pliku `main.py` napisz program, który przyjmie w kolejnych liniach:
- Liczbę całkowitą `N` oznaczającą liczbę wierszy w tabeli z opłatami
- `c_0`, ... `c_N`: koszty przejazdu poszczególnymi, 100-kilometrowymi odcinkami
- `L` długość odcinka autostrady na którym chcemy zarabiać pieniążki

Program powinien wydrukować na wyjście, w jednej linii, odległości odcinków na które będzie podzielona zadana trasa, by zrealizować maksymalny zysk z przejazdu.

Dla naszego przykładu, wywołanie programu mogłoby wyglądać na przykład tak:
```
12
10     
30     
60     
70     
80     
90     
120    
120    
130    
130    
150    
160
482
```

Program powinien wtedy zwrócić (mniej więcej, bo w wielu przypadkach nie ma jednego optymalnego rozwiązania)
```
200 282
```
