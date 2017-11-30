# valeur entiere et reste de 17 divise par 5

print(17 // 5, 17 % 5)

# aire d'une sphere de rayon 5

volume = 4 / 3 * 3.14 * 5 ** 3
volume_entier = int(volume)
print(volume_entier)

# formatage de trois nombres

p1, p2, p3 = 20000, 10.95, 5
print("{:>10.2f} €\n{:>10.2f} €\n{:>10.2f} €".format(p1, p2, p3))

print("{:10.2f} €\n{:10.2f} €\n{:10.2f} €".format(p1, p2, p3))

print(("{:10.2f} €\n"*3).format(p1, p2, p3))
