import random
import matplotlib.pyplot as plt
import numpy as np


class CityGrid:
    def __init__(self, rows, cols, obstacle_prob=0.3):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))  # 0 представляет собой пустой блок
        self.obstacle_prob = obstacle_prob
        self.towers = []  # хранения позиций башен

        self.place_obstacles()

    def place_obstacles(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < self.obstacle_prob:
                    self.grid[row, col] = 1  # 1 препятствие

    def visualize(self):
        plt.imshow(self.grid, cmap='Greys', interpolation='nearest')
        plt.title('City Grid')
        plt.show()

    def place_tower(self, row, col, radius):
        if self.grid[row, col] == 0:
            self.grid[row, col] = 2  # 2 башни
            self.towers.append((row, col, radius))
            self.visualize_towers()

    def visualize_towers(self):
        plt.imshow(self.grid, cmap='Greys', interpolation='nearest')
        for tower in self.towers:
            tower_row, tower_col, radius = tower
            coverage = np.zeros((self.rows, self.cols))
            for row in range(max(0, tower_row - radius), min(self.rows, tower_row + radius + 1)):
                for col in range(max(0, tower_col - radius), min(self.cols, tower_col + radius + 1)):
                    coverage[row, col] = 1

            plt.imshow(coverage, cmap='Blues', alpha=0.3, interpolation='nearest')

        plt.title('Towers and Coverage')
        plt.show()

    def optimize_tower_placement(self, tower_cost, budget):
        # Ваш алгоритм оптимизации с учетом стоимости башни и бюджета
        pass

    def visualize_tower_placement(self):
        plt.imshow(self.grid, cmap='Greys', interpolation='nearest')
        plt.title('Optimized Tower Placement')
        plt.show()

    def find_reliable_path(self, tower1_row, tower1_col, tower2_row, tower2_col):
        # алгоритм поиска пути на основе расстояния
        distance = abs(tower1_row - tower2_row) + abs(tower1_col - tower2_col)
        return [(tower1_row, tower1_col), (tower2_row, tower2_col)], distance

    def visualize_reliable_path(self, path):
        path_array = np.zeros((self.rows, self.cols))
        for point in path:
            path_array[point[0], point[1]] = 1

        plt.imshow(path_array, cmap='Reds', alpha=0.7, interpolation='nearest')
        plt.title('Reliable Path')
        plt.show()


# Задача 1: Создание CityGrid и визуализация
city = CityGrid(10, 10)
city.visualize()

# Задача 2: Разместить вышку и визуализировать ее покрытие
city.place_tower(5, 5, 2)

# Задача 3: Оптимизация размещения башен и визуализация
city.optimize_tower_placement(tower_cost=10, budget=50)
city.visualize_tower_placement()

# Задача 5: Визуализация вышек и их покрытия
city.visualize_towers()

# Задача 4: Найти надежный путь и визуализировать
path, distance = city.find_reliable_path(1, 1, 8, 8)
print(f"Reliable Path: {path}, Distance: {distance}")
city.visualize_reliable_path(path)
