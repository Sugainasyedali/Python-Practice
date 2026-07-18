def grade(marks):
 if marks >=90 and marks <=100:
    return "A"
 elif marks >=80 and marks <=89:
    return "B"
 elif marks >=70 and marks<=79:
    return "C"
 elif marks>=50 and marks<=69:
    return "D"
 elif marks >100:
    return "Out of range"
 else:
    return "F"