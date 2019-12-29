with open('p022names.txt', 'r') as f:
    x = str(f.readlines())
bad_ch = ["'", '"', '[', ']']
for bad in bad_ch:
    x = x.replace(bad, "")
names = list(x.split(','))
names = sorted(names)

letters = ['A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def problem_solving(name):
    counter_letter = 0
    counter_name = names.index(name)+1
    for i in range(len(name)):
        counter_letter = counter_letter + int((letters.index(name[i])) + 1)
    score = counter_letter*counter_name
    return score

# call the function with some firstname
print(problem_solving('RICHARD'))
