import sys

if __name__ == '__main__':
    print("#(argument) = ", len(sys.argv))
    print("Arguments: ", sys.argv)
    print("Real Arguments: ", sys.argv[1:])
