#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    est_pair = len(string) % 2 == 0
    return est_pair


def remove_third_char(string: str) -> str:
    string = string[:2]+string[3:]
    return string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    for x in range(len(string)):
        if string[x] == old_char:
            string = string[:x] + new_char + string[x+1:]
    return string


def get_number_of_char(string: str, char: str) -> int:
    occurence = 0;
    for lettre in string :
        if lettre == char:
            occurence += 1
    return occurence


def get_number_of_words(sentence: str, word: str) -> int:
    occurence = 0;
    sentence = sentence.split()
    for i in sentence:
        if i == word:
            occurence += 1
    return occurence


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
