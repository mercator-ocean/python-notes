def fibonacci(max):
    previous_value = 1
    valeur = 1
    if max >= 1:
        yield previous_value
        yield valeur

    while True:
        previous_value, valeur = valeur, valeur + previous_value
        if valeur > max:
            break
        else:
            yield valeur

for i in fibonacci(100):
    print(i)
