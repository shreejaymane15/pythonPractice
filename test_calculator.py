from calculator import square

def main():
    test_square()


def test_square():

    # if square(2) != 4:
    #     print("2 square was not 4")
    # if square(3) != 9:
    #     print("3 square was not 9")
    try:
        assert square(2) == 4
    except:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except:
        print("3 square was not 9")
    
if __name__ == "__main__":
    main()