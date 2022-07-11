from os import system as s
from random import randint as rint
UNDERLINE = "\033[4m"
END = "\033[0m"

def buf_count_newlines_gen(fname):
    def _make_gen(reader):
        while True:
            b = reader(2 ** 16)
            if not b: break
            yield b
    with open(fname, "rb") as f:
        count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
    return count

def select_random():
    route = './archivos/data.txt'
    lines = buf_count_newlines_gen(route)
    random_number = rint(1,lines)
    random_word = [line for i, line in enumerate(open(route)) if i==random_number]
    random_word=random_word[0]
    random_word = random_word.lower().replace('\n','')
    word_list = [letter for letter in random_word]
    word_guess = ['_' for i in range(len(word_list))]
    return word_list, word_guess

def draw_hangman(n):
    with open('./archivos/hangman_'+str(n)+'.txt','r') as f:
        for line in f:
            print(line)
    

def draw_screen(word_list, word_guess, n):
    s('clear')
    draw_hangman(n)
    for letter in word_guess:
        print(UNDERLINE + letter + END, end='')
    print('')

def guess_word(word_list, word_guess,n):
    letter = input('\n\t Qué letra está en la palabra? \t')
    letter = letter.lower()
    guessed=True
    l_guess=False
    for i in range(len(word_list)):
        if word_list[i]==letter:
            word_guess[i]=letter
            l_guess=True
        if word_guess[i]=='_':
            guessed=False
    if l_guess==False:
        n+=1
    return word_guess,guessed, n



def main():
  word_list, word_guess = select_random()
  guessed = False
  n=0
  draw_screen(word_list, word_guess,n)
  
  while (not guessed and n<6):
    word_guess, guessed, n = guess_word(word_list, word_guess,n)
    draw_screen(word_list, word_guess, n)

  if n==6:
    print('\n\t\t YOU LOOSE!!!')
  else:
    print('\n\t\t YOU WON!!!')

if __name__ == '__main__':
  main()