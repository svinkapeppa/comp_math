import argparse

from utils import czt


def transform(input_path, output_path):
    data = []

    with open(input_path) as fd:
        for line in fd:
            data.append(line.strip().split())
    data = [float(item) for row in data for item in row]

    with open(output_path, 'w') as fd:
        for item in czt(data, 3):
            fd.write('{} '.format(item))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', action='store', nargs='?',
                        default='examples/example.txt',
                        help='File containing the input sequence')
    parser.add_argument('-o', '--output', action='store', nargs='?',
                        default='results/result.txt',
                        help='File containing the result of the transformation')
    args = parser.parse_args()

    transform(args.input, args.output)
