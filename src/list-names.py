import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the names from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    for line in (args.fastq):
        if '@' in line:
            name = line.replace('@', '')
            cleanname = name.strip()
            print(cleanname)
        else:
            continue


if __name__ == '__main__':
    main()
