# Path to your local text file
file_path = "Q1.txt"

left = []
right = []
total = 0


try:
    # Open the file in read mode
    with open(file_path, "r") as file:
        for line in file:
            # remove next line marker
            line = line.replace("\n", "")
            # remove duplicate spaces
            line = line.replace("  ", " ")
            # split two data into a list
            lineList = line.split()
            # append first data into the left list
            left.append(lineList[0])
            # append second data into the right list
            right.append(lineList[1])
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except IOError as e:
    print(f"Error reading the file: {e}")

# sort the file
left = sorted(left)
right = sorted(right)


# for i in range(len(left)):
#     result = abs(int(left[i]) - int(right[i]))
#     total += result
# print(total)

for i in range(len(left)):
    count = right.count(left[i])
    total += int(left[i]) * count

print(total)