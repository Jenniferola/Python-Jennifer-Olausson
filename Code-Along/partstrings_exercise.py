def divided_pikachu_and_pichu(list):
    # The values of pichu and pikachu are seperated to two new lists. 

    pichu_datapoints = [item for item in pokemons if item["label"] == 0]
    pikachu_datapoints = [item for item in pokemons if item["label"] == 1]

    for row in pichu_datapoints:
        pichu_x_values_width.append(row["width"])

    for row in pichu_datapoints:
        pichu_y_values_height.append(row["height"])


    for row in pikachu_datapoints:
        pikachu_x_values_width.append(row["width"])

    for row in pikachu_datapoints:
        pikachu_y_values_height.append(row["height"])