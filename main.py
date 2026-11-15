import argparse
import logging
import os
import sys
import traceback

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Pack or unpack Amazfit Verge Lite watch-face .bin files."
    )
    parser.add_argument(
        "filename",
        nargs="+",
        help="A Verge Lite .bin file to unpack or a watch-face .json file to pack",
    )
    args = parser.parse_args(argv)

    exit_code = 0
    import program

    for input_file in args.filename:
        if not os.path.isfile(input_file):
            print("File does not exist: %s" % input_file, file=sys.stderr)
            exit_code = 1
            continue

        extension = os.path.splitext(input_file)[1].lower()
        try:
            if extension == ".bin":
                program.Parser.unpackWatchFace(input_file)
            elif extension == ".json":
                program.Parser.packWatchFace(input_file)
            else:
                print("Unsupported file extension: %s" % extension, file=sys.stderr)
                exit_code = 1
                continue
            print("Done: %s" % input_file)
        except Exception as error:
            print("[Fatal] %s: %s" % (input_file, error), file=sys.stderr)
            traceback.print_exc()
            logging.exception(error)
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
