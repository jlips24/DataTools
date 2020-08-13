import glob
import json
import os


def gather_files():
    """A file to gather all file names in thhe input folder

    Returns:
        [str]: A list of strings representing each file in the input folder
    """
    return glob.glob("input/*.json")


def process_file(filename):
    f = open(filename,)
    data = json.load(f)
    text = json.dumps(data, indent=2, sort_keys=True)
    f.close()
    return text


def save_output(filename, text):
    filename = filename.split('/')[-1]
    with open(os.path.join('output', filename), 'w') as f:
        f.write(text)
    f.close()


def main():
    filenames = gather_files()
    if len(filenames) > 0:
        for filename in filenames:
            text = process_file(filename)
            save_output(filename, text)


if __name__ == "__main__":
    main()
