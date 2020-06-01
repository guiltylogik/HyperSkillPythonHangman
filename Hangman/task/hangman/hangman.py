from random import choice


class Hangman:

    def __init__(self, words):
        self.words = words
        self.hangman = None
        self.hang = None
        self.dash = None
        self.guessed_letters = []
        self.life = 8

    def set_game_pa(self):
        self.hangman = list(choice(self.words))
        self.hang = self.hangman
        self.dash = list('-' * len(self.hangman))

    def main(self):
        self.set_game_pa()

        while self.life != 0:

            print('\n')
            print(''.join(self.dash))

            guess_letter = input('Input a letter: ')

            self.guessed_letters.append(guess_letter)

            if len(guess_letter) > 1:
                print('You should input a single letter')

            elif not guess_letter.islower():
                print('It is not an ASCII lowercase letter')

            elif guess_letter in self.hangman:
                for i in self.hangman:
                    if i == guess_letter:
                        self.dash[self.hangman.index(guess_letter)] = guess_letter
                        self.hangman[self.hangman.index(guess_letter)] = '-'

            else:
                if self.guessed_letters.count(guess_letter) > 1:
                    print('You already typed this letter')

                else:
                    print('No such letter in the word')
                    self.life -= 1

            if self.dash == self.hang:
                print('You guessed the word {}!\nYou survived!'.format(*self.dash))
                break

            if self.life == 0:
                print('You are hanged!')

    def game(self):
        while True:
            print('\n')
            c = input('Type "play" to play the game, "exit" to quit:')

            if c == 'play':
                self.main()
            break


new_game = Hangman(['python', 'java', 'kotlin', 'javascript'])
print("H A N G M A N")
new_game.game()
