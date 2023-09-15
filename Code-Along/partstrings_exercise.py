user_input = "Please write a string"

numbers = "0123456789"
initial_char = ""
char_index_1 = 0

for char_1 in numbers:
    initial_char = char_1
    substring_index = char_index_1 +1
    char_index_2 = substring_index
    for char_2 in user_input[substring_index]:
        if char_2 not in numbers:
            break
        else:   
            if char_2 == char_1:
                print(f"from{char_index_1} to {char_index_2}")
                break
            else:
                char_index_2 += 1
    char_index_1 +=1