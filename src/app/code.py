from src.utility.utils import addition
from src.config.conf import num1, num2

def main():
    result = addition(a = num1, b=num2)
    print(f'result = {result}')
    
if __name__ == '__main__':
    main()