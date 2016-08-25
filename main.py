def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 5 == 0:
        result = "Buzz"
    elif num % 3 == 0:
        result = "Fizz"
    else:
        result = str(num)

    return result

def main():
    print "\n".join(fizzbuzz(n) for n in xrange(1,100))

if __name__ == '__main__':
	main()
