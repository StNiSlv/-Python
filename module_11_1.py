import matplotlib.pyplot as plt

# Функция для рисования каждой буквы
def draw_U(ax):
    ax.plot([0, 0], [-0.75, 1], color='blue')
    ax.plot([0, 1], [-0.75, -1], color='blue')
    ax.plot([1, 2], [-1, -1], color='blue')
    ax.plot([2, 3], [-1, -0.75], color='blue')
    ax.plot([3, 3], [-0.75, 1], color='blue')
def draw_R(ax):
    ax.plot([4, 4], [-1, 1], color='blue')
    ax.plot([4, 6], [0.5, 1], color='blue')
    ax.plot([6, 7], [1, 1], color='blue')
    ax.plot([7, 7], [1, 0.5], color='blue')
def draw_B(ax):
    ax.plot([8, 8], [-1, 1], color='blue')
    ax.plot([8, 9], [-0.75, -1], color='blue')
    ax.plot([8, 9], [0, 0.25], color='blue')
    ax.plot([9, 10], [-1, -1], color='blue')
    ax.plot([9, 10], [0.25, 0.25], color='blue')
    ax.plot([10, 11], [0.25, 0], color='blue')
    ax.plot([10, 11], [-1, -0.75], color='blue')
    ax.plot([11, 11], [-0.75, 0], color='blue')
def draw_A(ax):
    ax.plot([12, 14], [-1, 1], color='blue')
    ax.plot([13, 15], [0, 0], color='blue')
    ax.plot([14, 15], [0, 0], color='blue')
    ax.plot([14, 16], [1, -1], color='blue')
def draw_N(ax):
    ax.plot([17, 17], [-1, 1], color='blue')
    ax.plot([17, 20], [1, -1], color='blue')
    ax.plot([20, 20], [-1, 1], color='blue')

fig, ax = plt.subplots(figsize=(10, 5))
draw_U(ax)
draw_R(ax)
draw_B(ax)
draw_A(ax)
draw_N(ax)

ax.set_xlim(-1, 21)
ax.set_ylim(-1, 2)
ax.axis('off')
plt.title('URBAN', fontsize=20)
plt.show()
