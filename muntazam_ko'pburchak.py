# #
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# # Funksiya, muntazam poligonni chizish uchun
# def plot_regular_polygon(sides=11):
#     # Har bir uchburchak orasidagi burchak
#     angle = 2 * np.pi / sides
#     # Poligonning vertikalari koordinatalarini saqlash uchun ro'yxat
#     points = []
#
#     for i in range(sides):
#         # Har bir vertikaning x va y koordinatalarini hisoblash
#         x = np.cos(i * angle)
#         y = np.sin(i * angle)
#         points.append((x, y))
#
#     # Poligonni yopish uchun birinchi nuqtani qo'shish
#     points.append(points[0])
#
#     # x va y koordinatalarini ajratish
#     x_vals, y_vals = zip(*points)
#
#     # Poligonni chizish
#     plt.figure(figsize=(6, 6))
#     plt.plot(x_vals, y_vals, 'b-', linewidth=2)
#     plt.fill(x_vals, y_vals, 'skyblue', alpha=0.5)
#
#     # Teng o'lchamda chizish
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.title(f'Muntazam {sides}-burchak')
#     plt.grid(True)
#     plt.show()
#
#
# # Muntazam 11-burchakni chizish
# plot_regular_polygon(11)
#
