import random
import numpy as np

class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0
        self.restarts = 0

        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

        self.queens = self.get_queens()
        self.temp = self.map

    def random_restart(self):
        self.restarts += 1
        self.fit = 0
        self.map = [[0 for j in range(self.n_queen)] for i in range(self.n_queen)]
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def get_queens(self):
        queens = []
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    queens.append([i ,j ])
        return queens

    def get_attack(self, q): # determine how many pieces are attacking each queen
        score = 0
        for k in range(1, self.n_queen - q[0]):
            if self.map[q[0] + k][q[1]] == 1:
                score += 1
            if q[1] - k >= 0 and self.map[q[0] + k][q[1] - k] == 1:
                score += 1
            if q[1] + k < self.n_queen and self.map[q[0] + k][q[1] + k] == 1:
                score += 1
        return score

    def move_queen(self, q): #generate neighbors of a sqaure.
        moves = []
        moves.append([q[0] - 1, q[1]])
        moves.append([q[0] + 1, q[1]])
        moves.append([q[0], q[1] - 1])
        moves.append([q[0], q[1] + 1])
        for item in moves:
            if item[0] < 0 or item[0] >= self.n_queen or item[1] < 0 or item[1] >= self.n_queen:
                moves.remove(item)
        return (q, moves)




    def array_max(self, arr): # returns indices of max value in an array of integers
        max_index = 0
        max_value_indices = []
        count = 0
        for item in arr:
            if item > arr[max_index]:
                max_index = count
            count += 1
        count = 0
        for item in arr:
            if item == arr[max_index]:
                max_value_indices.append(count)
            count += 1
        return max_value_indices

    def worst_queen(self):
        q_scores = []
        for q in self.queens:
            q_scores.append(self.get_attack(q))
        return self.array_max(q_scores)

    def fitness(self):
        self.fit = 0
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1

    def show(self):
        print(np.matrix(self.map))
        self.fitness()
        print("Fitness: ",  self.fit)

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def get_map(self):
        return self.map

    def get_fit(self):
        return self.fit

    def set_map(self, m):
        self.map = m


if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()