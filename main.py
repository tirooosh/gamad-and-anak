import random

def connect_names_in_circle(filename):
    """
    Reads names from a file, connects them randomly in a circle, and writes the connections back to the file.
    """

    with open(filename, "r", encoding="utf-8") as file:  # Assuming UTF-8 encoding
        names = file.read().splitlines()

    random.shuffle(names)  # Shuffle the names randomly

    # Connect the names in a circle
    connections = zip(names, names[1:] + [names[0]])  # Pair each name with the next one in the circle

    with open("changed"+filename, "wb") as file:  # Open in binary mode
        for name1, name2 in connections:
            # Encode the connection string to bytes using the desired encoding
            connection_string = f"{name1} - {name2}\n".encode("utf-8")
            file.write(connection_string)


# Example usage
filename = "names.txt"  # Replace with your actual filename
connect_names_in_circle(filename)
