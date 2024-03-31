def get_grade(score: float) -> str:
    if 80 <= score <= 100:
        return "A"  # 4.0
    elif 75 <= score < 80:
        return "B+"  # 3.5
    elif 70 <= score < 75:
        return "B"  # 3.0
    elif 65 <= score < 70:
        return "C+"  # 2.5
    elif 60 <= score < 65:
        return "C"  # 2.0
    elif 55 <= score < 60:
        return "D+"  # 1.5
    elif 50 <= score < 55:
        return "D"  # 1.0
    else:
        return "F"


def get_grade_points(grade: str) -> float:
    if grade == "A":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1.0
    else:
        return 0.0
