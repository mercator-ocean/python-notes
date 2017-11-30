#Écrivez une fonction `min_max` prenant une liste de nombres en paramètre et renvoyant le minimum et le maximum.

def min_max(liste):
    min = liste[0]
    max = liste[0]
    for value in liste[1:]:
        if value < min:
            min = value
        elif value > max:
            max = value

    return min, max

print(min_max([10, 12, 15, 5, 7]))
