import matplotlib.pyplot as plt
import numpy as np

def draw_branch(ax, start_x, start_y, length, angle, level, max_level):
    if level > max_level:
        return
    
    end_x = start_x + length * np.cos(np.radians(angle))
    end_y = start_y + length * np.sin(np.radians(angle))
    
    color_intensity = level / max_level
    color = (0.5 * color_intensity, 0.2, 0.1)
    width = max(1, 5 - level * 0.5)
    
    ax.plot([start_x, end_x], [start_y, end_y], 
            color=color, linewidth=width)
    
    new_length = length * 0.7
    left_angle = angle + 45
    right_angle = angle - 45
    
    draw_branch(ax, end_x, end_y, new_length, left_angle, level + 1, max_level)
    draw_branch(ax, end_x, end_y, new_length, right_angle, level + 1, max_level)

def draw_pythagoras_tree(recursion_level):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.set_aspect('equal')
    ax.set_xlim(-300, 300)
    ax.set_ylim(-50, 400)
    ax.set_facecolor('white')
    ax.axis('off')
    
    start_x = 0
    start_y = 0
    initial_length = 100
    initial_angle = 90
    
    draw_branch(ax, start_x, start_y, initial_length, initial_angle, 1, recursion_level)
    
    plt.title(f'Дерево Піфагора (рівень рекурсії: {recursion_level})', fontsize=16)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (1-12, 0 для виходу): "))
            if level == 0:
                break
            if 1 <= level <= 12:
                draw_pythagoras_tree(level)
            else:
                print("Будь ласка, введіть число від 1 до 12")
        except ValueError:
            print("Будь ласка, введіть ціле число")

if __name__ == "__main__":
    main()