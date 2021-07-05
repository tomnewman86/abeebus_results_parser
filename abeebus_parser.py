import csv
import argparse
import os
import sys
import time

__author__ = 'Tom Newman'
__description__ = 'Python script to parse the results of an Abeebus scan from a txt file to a csv. All credit for Abeebus goes to 13Cubed and can be download from here: https://github.com/13Cubed/Abeebus'


def main(input_file, output_file):
    if os.path.isfile(input_file):
        print('='*22)
        print('Abeebus results parser')
        print(__description__ + '\n')
        print(
            f"Built by {__author__}. Version 1.0. All credit for Abeebus goes to 13cubed.")
        print('='*22)
        print('[*] Parsing log file...')
        results_list = parse_data(input_file)
        time.sleep(1)
        print('[*] Copying output to CSV')
        print_to_csv(output_file, results_list)
        time.sleep(1)
        print('[+] Complete! Please check your output location...')
    else:
        print(
            '[-] Input file is not the expected filetype, please select a valid file and try again')
        sys.exit(1)


def parse_data(input_file):
    abeebus_list = []

    with open(input_file) as in_file:

        for lines in in_file:
            split_lines = lines.split('|')
            abeebus_list.append(split_lines)

        return abeebus_list


def print_to_csv(output_file, results_list):
    with open(output_file, 'w') as file:
        tsv_writer = csv.writer(file, delimiter='\t')
        for groupings in results_list:
            tsv_writer.writerow(groupings)

        return output_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__description__,
        epilog='Built by {}. Version 1.0'.format(__author__),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input_file', help='path to Abeebus txt file', required=True, action="store")
    parser.add_argument(
        '-o', '--output_file', help='path to outfile to record parsed data', required=True, action="store")
    args = parser.parse_args()
    main(args.input_file, args.output_file)
