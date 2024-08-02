# Write a class Report that takes a comma-separated string of colours ("Green", "Amber" and "Red") as input 
#   and generates count of occurrences of each colour. 
#   print counts in format: "Green: X, Amber: Y, Red: Z".

# Build report that takes results and generates report for each student

# Func takes in colours as arguments. Counts the occurances of that colour
# outputs a string with that number

# FUNCTIONS
    #   report()
    # .count()
# ARUGMENTS
    #    colours
# OUTPUTS 
    #   string connecting colour with num repre. colour count respectively 

class Report():
    def __init__(self, str):
        self.str = str

    def generate(self):
        new_str = self.str.split(", ")

        green_count = 0
        amber_count = 0
        red_count = 0

        for word in new_str:
            if word == "Green":
                green_count += 1
            elif word == "Amber":
                amber_count += 1
            elif word == "Red":
                red_count += 1
        print(f"Green: {green_count}, Amber: {amber_count}, Red: {red_count}" )


report = Report("Green, Green, Amber, Red, Green")
report.generate()
