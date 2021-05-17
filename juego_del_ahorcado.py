from unidecode import unidecode
from random import choice
from os import system
from time import sleep
import emojis

#Funcion para leer archivo donde están las palabras a adivinar
def read_words(path = "./files/data.txt"):
    with open( path, "r", encoding = "UTF-8") as f:
        words = [line.strip("\n").upper() for line in f]  #Create a list with the lines from the file and delete the space "\n"  
    return words
  
#Funcion para generar un diccionario con los indices en donde está cada letra de la palabra a adivinar
def generated_dict_selected_word(selected_word_to_list):
    letter_index_dict = {}    
    for index, letter in enumerate(selected_word_to_list):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = [] #Create a new list if there is no one
        letter_index_dict[letter].append(index)    
    return letter_index_dict

#Funcion que escoge una palabra al azar para adivinar y organizar las listas y diccionario necesario para jugar
def game():
    words = read_words(path = "./files/data.txt")
    selected_word = choice(words)
    selected_word_to_list = list(map(lambda letter: unidecode(letter), selected_word))
    selected_word_list_underscores = ["_"] * len(selected_word_to_list)
    letter_index_dict = generated_dict_selected_word(selected_word_to_list)
    return selected_word, selected_word_to_list, selected_word_list_underscores, letter_index_dict

#Funcion principal, se encarga de ejecutar el juego
def run():
    system("clear")
    lifes = 5 # User lifes
    points = 0 # User points
    time = 2 # Waiting time
    selected_word, selected_word_to_list, selected_word_list_underscores, letter_index_dict = game()
    print("----------------------Welcome to the Hangman game------------------------")
    print("You have", lifes, "lifes to win the game. Please wait", time, "seconds to start the game", emojis.encode(':thumbsup:'))
    sleep(time)
    #Start game
    while lifes:
        try:
            system("clear")
            print("Guess the word")
            print("  ".join(selected_word_list_underscores))
        
            letter = input("Enter a letter, please: ").upper()
            if not letter.isalpha():
                raise Exception
        
            if letter in selected_word_to_list:
                for index in letter_index_dict[letter]:
                    selected_word_list_underscores[index] = letter       
            else:
                lifes -= 1
                print("You have", lifes ,"lifes left, please wait", time, "seconds to enter another letter")
                sleep(time)
                if not lifes:
                    print("Sorry, you have no more lifes and you collected:",points, "points", emojis.encode(':sob:'))
                    print("Do you want to play again? \n")
                    play_again = int(input("1: Yes, 0: No \n"))
                    if play_again:
                        run()
                    else:
                        break
            
            #Evalua si el usuario ya logró adivinar la palabra                        
            if "_" not in selected_word_list_underscores:
                system("clear")
                print("Congratulations, you win the game", emojis.encode(':sunglasses:')) 
                points += 1
                print("Good work, the word was:", selected_word, "and you have win", points, "points \n")
                print("Do you want to continue playing? \n")
                continue_playing = int(input("1: Yes, 0: No \n"))
                if continue_playing:
                    selected_word, selected_word_to_list, selected_word_list_underscores, letter_index_dict = game()
                else:
                    break        
        except Exception:
            print("You have to enter a letter, please wait", time, "seconds to try again")
            sleep(time)  
            
        
#Entry point
if __name__ == '__main__':
    run()