import csv


def convert_csv(
    source_file_name, output_file_name, delimiter="|", auto_detecting_delimiter=False
):
    with open(source_file_name, newline="") as source_file:
        final_delimiter = delimiter
        if auto_detecting_delimiter == True:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(source_file.read(2048))
            final_delimiter = dialect.delimiter
        with open(output_file_name, mode="w", newline="") as output_file:
            reader = csv.reader(source_file, delimiter=final_delimiter)
            writer = csv.writer(
                output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows(reader)


if __name__ == "__main__":
    source_file_name = (
        input("Please input source file name (default value is original.csv): ")
        or "original.csv"
    )
    output_file_name = (
        input("Please input output file name (default value is output.csv): ")
        or "output.csv"
    )
    delimiter = input("Please input delimiter(optional): ")

    auto_detecting_delimiter = False
    if delimiter == "":
        auto_detecting_delimiter = input("Auto detecting delimiter(y/n): ") == "y"
        if auto_detecting_delimiter:
            print("Delimiter will be detected automatically.")
        else:
            print("Delimiter will be |.")

    convert_csv(
        source_file_name,
        output_file_name,
        "|" if delimiter == "" else delimiter,
        auto_detecting_delimiter,
    )

    print(source_file_name + " was converted to " + output_file_name + " successfully.")
