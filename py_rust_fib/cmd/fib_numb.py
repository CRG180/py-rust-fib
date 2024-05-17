import argparse
from py_rust_fib.fib_calcs.fib_number import recurring_fibonacci_number

def fib_numb() -> None:
    parser = argparse.ArgumentParser(
        description = 'Calculate Fibonacci numbers')
    parser.add_argument('--number', action='store', type = int,
                        required=True, help = "Fibonaccis number to be \
                            calculated")
    args = parser.parse_args()
    print(f"Your Fibonacci number is: " \
    f"{recurring_fibonacci_number(number=args.number)}")
    
    enty_points = { 'console_scripts': [
        'fib-number = py_rust_fib.com.fib_numb:fib_numb']}