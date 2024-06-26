def renv(tab):
    n = len(tab)

    if n <= 1:
        return tab.copy()
    else:
        return renv(tab[n//2:]) + renv(tab[:n//2])

print(renv([1,2,3,4,5,6,7,8]))
