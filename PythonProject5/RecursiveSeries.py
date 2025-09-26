cnt = 0
def foobar(i):
    """
        - returns the nth value in the series foobar():
        - foobar(0) = 0
        - foobar(1) = 2
        - foobar(n) = (3 * foobar(n-1)) - 1  when n > 1
        """
    global cnt
    cnt = cnt + 1
    if i == 0: return 0
    elif i == 1: return 2
    else: return ((foobar(i - 1)) * 3) - 1

def main():
    print(foobar(int(input("Enter the number: "))))
    print("Number of recursive calls:", cnt)

main()