import csv
DATA_FILE = "data.csv"
def search(keyword, data):
    pass

def file_writer():
    pass

def file_loader(fname):
    try:
        rows = []
        with open(fname,"rt") as fh:
            data_reader = csv.reader(fh)
            for row in data_reader:
                print(f"Name: {row[0]}")
                rows.append((row[0],row[1]))

    except FileNotFoundError:
        print("The data file is not found")

    return rows

def setup():
    data_rows = file_loader(DATA_FILE)
    # print(f"The number of rows in data: {len(data_rows)}")
    for k,v in data_rows:
        print(f"Name: {k},Email: {v}")

def cli_interface():
    pass

if __name__ == '__main__':
    setup()