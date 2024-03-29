import sys

def reverse_cipher(text):
    return text[::-1]

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()

        reversed_content = reverse_cipher(content)

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(reversed_content)

            print(f"Successfully encrypted '{input_filename}' and saved the result to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python wp1.py input_filename output_filename")
    else:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        process_file(input_filename, output_filename)