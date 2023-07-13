student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
student_count = 0
for height in student_heights:
    total_height += height
    student_count += 1
print(f"Total Height : {total_height}")
print(f"Student Count : {student_count}")

avg_height = round(total_height / student_count)
print(f"Average height is {avg_height}")
