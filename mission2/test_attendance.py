from attendance import BaseballTraining, NormalPointBridge, input_file
import os


def test_attendance(capsys):
    b_training = BaseballTraining(NormalPointBridge())
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'attendance_weekday_500.txt')
    input_file(file_path, b_training)
    captured = capsys.readouterr()
    expected=f"NAME : Umar, POINT : 48, GRADE : SILVER\n\
NAME : Daisy, POINT : 45, GRADE : SILVER\n\
NAME : Alice, POINT : 61, GRADE : GOLD\n\
NAME : Xena, POINT : 91, GRADE : GOLD\n\
NAME : Ian, POINT : 23, GRADE : NORMAL\n\
NAME : Hannah, POINT : 127, GRADE : GOLD\n\
NAME : Ethan, POINT : 44, GRADE : SILVER\n\
NAME : Vera, POINT : 22, GRADE : NORMAL\n\
NAME : Rachel, POINT : 54, GRADE : GOLD\n\
NAME : Charlie, POINT : 58, GRADE : GOLD\n\
NAME : Steve, POINT : 38, GRADE : SILVER\n\
NAME : Nina, POINT : 79, GRADE : GOLD\n\
NAME : Bob, POINT : 8, GRADE : NORMAL\n\
NAME : George, POINT : 42, GRADE : SILVER\n\
NAME : Quinn, POINT : 6, GRADE : NORMAL\n\
NAME : Tina, POINT : 24, GRADE : NORMAL\n\
NAME : Will, POINT : 36, GRADE : SILVER\n\
NAME : Oscar, POINT : 13, GRADE : NORMAL\n\
NAME : Zane, POINT : 1, GRADE : NORMAL\n\
\n\
Removed player\n\
==============\n\
Bob\n\
Zane\n"
    assert captured.out == expected
