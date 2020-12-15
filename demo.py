

import pylev



while True:
    string1 = input("Enter String 1: ")
    string2 = input("Enter String 2: ")

    distance_dl = pylev.damerau_levenshtein(string1,string2)

    print("Damerau Levenshtein Distance ",distance_dl)

    distance_cl = pylev.classic_levenshtein(string1,string2)

    print("Classic Levenshtein Distance ",distance_cl)


    distance_re = pylev.recursive_levenshtein(string1,string2)

    print("Recursive Levenshtein Distance: ",distance_re)

    
