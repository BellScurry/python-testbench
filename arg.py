import sys
import argparse

if __name__ == '__main__':
    print("#(argument) = ", len(sys.argv))
    print(" All Arguments: ", sys.argv)
    print("Real Arguments: ", sys.argv[1:])

    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", metavar="<input file>", help="Input file's path")
    parser.add_argument("rep", metavar="<repetition>", type=int, help="Repetition")
    parser.add_argument("-e", action="store_true", help="Redirect error message to stdout")
    parser.add_argument("-b", metavar="<beep sound file>", dest="beep", help="Beep sound at the end of process")
    parser.add_argument("--silent", action="store_true", help="Execute script without messaging to stdout")
    parser.add_argument("-o", "--outputfile", metavar="<output file>", help="Output file's path")
    args=parser.parse_args()
    print(args.inputfile)
    print(args.rep)
    print(args.e)
    print(args.beep)
    print(args.silent)
    print(args.outputfile)
