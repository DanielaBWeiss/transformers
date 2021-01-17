import os
import argparse

def count_lengths(dir_path):
    for filename in os.listdir(dir_path):
        if "source" in filename or "target" in filename:
            print("File: ", filename)
            with open(dir_path + "/" + filename, 'r') as f:
                lines = []
                max_index = 0
                max_num = 0
                for i,line in enumerate(f):
                    len_line = len(line.split())
                    if len_line > max_num:
                        max_num = len_line
                        max_index = i
                    lines.append(len_line)


            print("Min input length: ", min(lines))
            print("Max input length: ", max(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_path', type=str, required=True, help='directory containig files to count')

    args = parser.parse_args()
    count_lengths(args.dir_path)

