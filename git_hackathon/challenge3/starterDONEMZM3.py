import sys

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

def read_values(path):
    """Read numeric values from a text file.
    returns float list. skips invalid and non-numeric lines"""
    
values = []
    with open(path, "r") as f:
        for line in f:
            text = line.strip()
            if not text:
                # skips the empty lines here
                continue
            try:
                value = float(text)
            except ValueError:
                # skip lines which cannot be converted to a float
                continue
            values.append(value)
    return values

def make_histogram(values, output_path):
    if plt is None:
        print("matplotlib is not available, cannot plot.")
        return

    if not values:
        print("No values to plot; histogram will not be created.")
        return
#make the plot look nice
    plt.figure()
    plt.hist(values, bins="auto", color="orange", edgecolor="black")
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
#save the plot here
    plt.savefig(output_path)
    plt.close()
    print("Saving figure to", output_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python starter.py <data.txt> <output.png>")
        sys.exit(1)

    data_path = sys.argv[1]
    out_path = sys.argv[2]

    values = read_values(data_path)
    print("Read", len(values), "values.")
    make_histogram(values, out_path)

if __name__ == "__main__":
    main()
