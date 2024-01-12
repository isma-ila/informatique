import copy


class LiveModel:
    #__word_original = ["B", "O", "N", "J", "O", "U", "R"]

    # taille de la grille
    __height = 0
    __width = 0

    # taille des cellules
    __c = 0

    # dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
    __dico_case = {}

    # vitesse de l'animation (en réalité __c'est l'attente entre chaque étapes en ms)
    __vitesse = 0

    # dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
    __dico_etat = {}

    #
    __flag = 0


    def __init__(self):
        #self.__word = copy.copy(self.__word_original)
        self.__height = 200
        self.__width = 200
        self.__c = 10
        self.__dico_case = copy.copy(self.__dico_case)
        self.__dico_etat = copy.copy(self.__dico_etat)
        self.__flag = copy.copy(self.__flag)
        self.__vitesse = 50




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

    def initialisation_cellules(self):
        # assigne une valeur 0(morte) a chaque coordonnées(cellules)
        # (valeur par défault en quelque sorte ^^)
        i = 0
        while i != self.get_width() / self.get_c():
            j = 0
            while j != self.get_height() / self.get_c():
                x = i * self.get_c()
                y = j * self.get_c()
                self.get_dico_case[x, y] = 0
                j += 1
            i += 1