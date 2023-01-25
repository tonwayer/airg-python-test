import os
import threading
import csv
from faker import Faker
import numpy as np

fake = Faker()


def generate_csv(number_of_rows: int, file_name: str):
    fixed_file_name = file_name
    if file_name[4:] != ".csv" and "." not in file_name:
        fixed_file_name = fixed_file_name + ".csv"
    with open(fixed_file_name, mode="w", newline="") as file:
        file_writer = csv.writer(
            file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for _ in range(number_of_rows):
            file_writer.writerow([fake.random_number(), fake.word()])


def random_string_generator(number_of_string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    np_alphabet = [x for x in alphabet]
    np_codes = np.random.choice(np_alphabet, [number_of_string, 10])
    strings = ["".join(np_codes[i]) for i in range(len(np_codes))]
    return strings


def generate_big_csv_with_numpy(number_of_rows: int, file_name: str):
    fixed_file_name = file_name
    if file_name[4:] != ".csv" and "." not in file_name:
        fixed_file_name = fixed_file_name + ".csv"
    data = [
        np.random.randint(1000, 9999, size=number_of_rows),
        random_string_generator(number_of_rows),
    ]
    rows = ["%s, %s\n" % row for row in zip(*data)]
    with open(fixed_file_name, mode="w", newline="") as file:
        file.writelines(rows)


def generate_big_csv_with_multi_threading(number_of_rows: int, output_file_name: str):
    NUMBER_OF_THREADS = 8
    file_names = ["result%s.csv" % x for x in range(NUMBER_OF_THREADS)]
    threads = [
        threading.Thread(
            target=generate_big_csv_with_numpy,
            args=(int(number_of_rows / NUMBER_OF_THREADS), file_names[x]),
            name="n1",
        )
        for x in range(NUMBER_OF_THREADS)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    with open(output_file_name, mode="w") as result_file:
        for file_name in file_names:
            with open(file_name) as file:
                result_file.write(file.read())
    for file_name in file_names:
        os.remove(file_name)


BIG_NUMBER_OF_FILE = 1000000
BIG_NUMBER_OF_FILE2 = 10000000

if __name__ == "__main__":
    while True:
        try:
            number_of_rows = int(input("Please input number of rows: ") or "10")
            break
        except ValueError:
            print("Please input integer only...")
            continue

    output_file_name = (
        input("Please input the name of result file (default value is random.csv): ")
        or "random.csv"
    )

    if number_of_rows < BIG_NUMBER_OF_FILE:
        generate_csv(number_of_rows, output_file_name)
    elif BIG_NUMBER_OF_FILE2 > number_of_rows > BIG_NUMBER_OF_FILE:
        generate_big_csv_with_numpy(number_of_rows, output_file_name)
    else:
        generate_big_csv_with_multi_threading(number_of_rows, output_file_name)
