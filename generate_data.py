# generate_data.py

import os
import random
import string

def generate_data():
    data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    with open("temp_data.txt", "w") as file:
        file.write(data)

if __name__ == "__main__":
    generate_data()
    print("Data generated and stored in temp_data.txt.")

