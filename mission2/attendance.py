from typing import Dict
from strategy import PointBridge, NormalPointBridge

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


class Player:
    count = 0

    def __init__(self, name: str, p_bridge: PointBridge):
        self._id = ++Player.count
        self._name = name
        self._point = 0
        self._day_count = [0] * 7
        self.p_bridge = p_bridge

    @property
    def id_num(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def point(self):
        return self.p_bridge.calculate_point(self._point, self._day_count)

    def attend(self, day):
        day_index = days.index(day)
        self._day_count[day_index] += 1
        self._point += self.p_bridge.get_day_point(day_index)

    @property
    def grade(self):
        return self.p_bridge.calculate_grade(self._point)

    def removable(self):
        return self.p_bridge.is_removable(self._point, self._day_count)


class BaseballTraining:
    def __init__(self, p_strategy: PointBridge):
        self.players : Dict[str, Player] = {}
        self.p_strategy = p_strategy

    def process_record(self, name:str, day:str):
        if name not in self.players:
            self.players[name] = Player(name, self.p_strategy)
        player = self.players[name]
        player.attend(day)


def input_file(file_path, training: BaseballTraining):
    try:
        with open(file_path, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                record = line.strip().split()
                if len(record) == 2:
                    training.process_record(name=record[0], day=record[1])

        for player in training.players.values():
            print(f"NAME : {player.name}, POINT : {player.point}, GRADE : ", end="")
            print(player.grade)

        print("\nRemoved player")
        print("==============")
        for player in training.players.values():
            if player.removable():
                print(player.name)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    b_training = BaseballTraining(NormalPointBridge())
    input_file("attendance_weekday_500.txt", b_training)