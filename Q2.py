# Path to your local text file
file_path = "Q2.txt"
safe_count= 0


def safeCheck(list):
    temp = 0
    increasing = False
    if (int(list[len(list)-1]) - int(list[0]) > 0):
        increasing = True

    for i in range(len(list)):
        if(i > 0 and (abs(int(list[i]) - temp) < 1 or abs(int(list[i]) - temp) >3 )):
            return False
        
        if (i > 0 and increasing and int(list[i]) - temp < 1):
            return False
        
        if (i > 0 and not increasing and int(list[i]) - temp >= 1):
            return False
        temp = int(list[i])
    return True



try:
    # Open the file in read mode
    with open(file_path, "r") as file:
        for line in file:
            # remove next line marker
            line = line.replace("\n", "")
            # split two data into a list
            lineList = line.split(" ")
            if (safeCheck(lineList)):
                safe_count += 1
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except IOError as e:
    print(f"Error reading the file: {e}")

print(safe_count)