import sys

def parse_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError('Los dos argumentoss han de ser números enteros')

if len(sys.argv) != 3:
    print('El formato correcto es con dos argumentos')

else:
    print(f'La suma de los valores es: {parse_to_int(sys.argv[1]) + parse_to_int(sys.argv[2])}')
    