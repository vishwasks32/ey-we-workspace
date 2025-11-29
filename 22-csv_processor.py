DATA_FILE = "data.csv"
def search(keyword, data):
    pass

def file_writer():
    pass

def file_loader(fname):
    try:
        rows = []
        with open(fname,"rb") as fh:
            rows = fh.readlines()
    except FileNotFoundError:
        print("The data file is not found")

    return rows

def setup():
    data_rows = file_loader(DATA_FILE)
    print(f"The number of rows in data: {len(data_rows)}")

def cli_interface():
    pass

if __name__ == '__main__':
    setup()