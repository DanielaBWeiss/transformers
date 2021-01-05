import os
import argparse

def count_lengths(dir_path):
    for filename in os.listdir(dir_path):
        if "source" in filename or "target" in filename:
            print("File: ", filename)
            with open(dir_path + "/" + filename, 'r') as f:
                data = f.readlines()
                lines = [len(line.split()) for line in data]

            print("Min input length: ", min(lines))
            print("Max input length: ", max(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_path', type=str, required=True, help='directory containig files to count')

    args = parser.parse_args()
    count_lengths(args.dir_path)
