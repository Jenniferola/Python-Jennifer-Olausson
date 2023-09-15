#Empty list
birthday_wishlist = []

#List with a few items in "string"- type
close_family = ["Niklas", "Ulrika", "Mormor"]

#Lists with mixed data-types. Al
my_random_favourite_things = [25, 2, 5, "Jens", True, 9.5, "Lotus", "Hugo", "travel"]

#Lists with nedstled list.
my_nestled_family = ["Niklas" , ["Alice", "Noel"], "Göran", ["Ulrika"]]

#Skriver ut listan med starten av listans namn och = tecken och sedan innehållet. Men med citatecken och hakparanteser. = teckmet efter listnamnet
print(f"{close_family}")

# len() skriver ut antalet i listan. Men även ordet "len" med osv. Alternativet nedan skriver bara ut siffran.
print(f"{len(close_family)}")

#Skriver ut antalet i listan utan f-string.
print(len(close_family))

# Räknar antalet i listan som heter det inom tex "Niklas" med f-string.
print(f"{close_family.count('Niklas')}")

#Som ovan utan f-string. Räknar antalet som heter "Niklas i listan"
print(close_family.count("Niklas"))

#Append/lägg till ny item i en lista. Lägger till Göran.
close_family.append('Göran') 

#Skriver ut close_family listan med "Göran" som lades till ovan.
print(close_family)

#Lägger till sistan listan till den första. Dvs nya namnet är det första.
close_family += my_random_favourite_things

#Skriver ut den nya listan som var två innan.
print(close_family)

#Skriver ut index 0, första index i listan-
print(f"{close_family[0]}")

# Skriver ut sista itemet
print(f"{close_family[-1]}")

#Skriver ut item från start index 3 (dvs fjärde saken) till index 7.
print(f"{close_family[3:7]}")

#Samma som ovan men hoppar två steg. (Start:stop:step)
print(f"{close_family[2:9:2]}")

# Om man vill ha olika placeringar i en list får man addera.
print(f"{close_family[2]} , {close_family[-2]}")

for item in close_family:
    print(close_family)



# List Comprehension = skapa en ny lista av en gammal lista. En fruktlista, skapa en ny lista av fruktlistan med frukterna som innehåller bokstaven "a".
fruits = ["apple", "kiwi", "banana"]
fruits_with_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_a)

fruits_with_b = [fruit for fruit in fruits if not "a" in fruit]