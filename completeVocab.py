import sys

def word_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as archivo:
            return sum(1 for _ in archivo)
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
        return -1

def ensure_newline_at_end(file_path):
    try:
        with open(file_path, 'rb+') as archivo:
            archivo.seek(-1, 2)  # Mover el puntero al último byte
            ultimo_byte = archivo.read(1)
            if ultimo_byte != b'\n':
                archivo.write(b'\n')  # Añadir el salto de línea
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
vocab_file=sys.argv[1]
target_size=int(sys.argv[2])

ensure_newline_at_end(vocab_file)

vocab_size = word_count(vocab_file)
print("Completing ",vocab_file,"with size",vocab_size,"lines to",target_size,"lines.")
with open(vocab_file, "a") as f:
    for i in range(vocab_size, target_size):
        f.write(f'"<extra_token_{i - vocab_size + 1}>": {i}\n')
