import copy


class LiveModel:
    __word_original = ["B", "O", "N", "J", "O", "U", "R"]

    # taille de la grille
    __height = 200
    __width = 200

    # taille des cellules
    __c = 10

    # dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
    __dico_case = {}

    # vitesse de l'animation (en réalité __c'est l'attente entre chaque étapes en ms)
    __vitesse = 50

    # dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
    __dico_etat = {}

    #
    __flag = 0


    def __init__(self):
        self.__word = copy.copy(self.__word_original)



    def get_word(self):
        """
		Retourne les données sous forme de liste
		"""
        return self.__word

    # Getter height
    def get_height(self):
        return self.__height

    # Getter width
    def get_width(self):
        return self.__width

    # Getter cellules
    def get_c(self):
        return self.__c

    def get_dico_case(self):
        return self.__dico_case

    def get_dico_etat(self):
        return self.__dico_etat

    def get_flag(self):
        return self.__flag

    def get_vitesse(self):
        return self.__vitesse

    def set_flag(self, flag):
        self.__flag = flag

    def set_vitesse(self, vitesse):
        self.__vitesse = vitesse

    def modify_word(self, index):
        code = ord(self.__word[index])
        new_letter = chr(code + 1)
        self.__word[index] = new_letter

    def reset_word(self):
        self.__word = copy.copy(self.__word_original)