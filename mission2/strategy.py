from abc import ABC, abstractmethod


class PointBridge(ABC):

    @abstractmethod
    def calculate_point(self, point, day_counts):
        pass

    @abstractmethod
    def get_day_point(self, day_index):
        pass

    @abstractmethod
    def calculate_grade(self, point):
        pass

    @abstractmethod
    def is_removable(self, point, day_count):
        pass

class NormalPointBridge(PointBridge):
    def __init__(self):
        self.day_point = [1, 1, 3, 1, 1, 2, 2]
        self.grades = ["NORMAL", "SILVER", "GOLD"]

    def calculate_point(self, point, day_counts):
        result = point
        if day_counts[2] > 9:
            result += 10
        if (day_counts[5] + day_counts[6]) > 9:
            result += 10
        return result

    def get_day_point(self, day_index):
        return self.day_point[day_index]

    def calculate_grade(self, point):
        grade_index = 2 if point >=50 else 1 if point >= 30 else 0
        return self.grades[grade_index]

    def is_removable(self, point, day_counts):
        grade_index = 2 if point >= 50 else 1 if point >= 30 else 0
        return grade_index not in (1, 2) and day_counts[2] == 0 and (day_counts[5] + day_counts[6]) == 0
