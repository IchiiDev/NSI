import matplotlib.pyplot as plt

graph_data = []
tab = "-----------------\n| Côté\t| Aire\t|\n-----------------\n"
taille = 1
for i in range(100):
    tab += f"| {round(taille, 3)}\t | {round(taille ** 2, 2)}\t|\n"
    taille = taille * 0.75
    graph_data.append(taille ** 2)
tab += "-----------------"
plt.plot(graph_data)
plt.ylabel("Aire")
plt.xlabel("n")
plt.show()
print(tab)
