def print_file_lines():
    with open('4.txt', 'r') as f:
        while True:
            lines = f.readlines()
            if not lines:
                break
            for line in lines:
                print(line.strip())

# Direct usage without path variable
print_file_lines()

# f=open('write.txt', 'w')
# lines=['Apple\n','mango\n','kiwi\n','orange\n']
# f.writelines(lines)
# f.close()