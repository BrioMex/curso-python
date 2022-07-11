def read():
  with open('./archivos/numbers.txt','r', encoding='utf-8') as f:
    numbers = [int(line) for line in f]
  print(numbers)

def write():
  names = ['Manuel', 'otro_nombre', 'nombre_3']
  with open('./archivos/names.txt','w', encoding='utf-8') as f:
      for name in names:
        f.write(name)
        f.write('\n')

def main():
  read()
  write()


if __name__ == '__main__':
  main()