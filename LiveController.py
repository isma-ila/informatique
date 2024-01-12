#import random
from LiveModel import LiveModel
from LiveView import LiveView


class LiveController:

    def __init__(self):
        self.model = LiveModel()
        self.view = LiveView(self)
        self.get_canvas = self.view.get_canvas()


        # Getter __dico_case
        self.get_dico_case = self.model.get_dico_case()
        i = 0

        # assigne une valeur 0(morte) a chaque coordonnées(cellules)
        # (valeur par défault en quelque sorte ^^)
        while i != self.model.get_width() / self.model.get_c():
            j = 0
            while j != self.model.get_height() / self.model.get_c():
                x = i * self.model.get_c()
                y = j * self.model.get_c()
                self.get_dico_case[x, y] = 0
                j += 1
            i += 1

        #
        self.view.mainloop()


    """
        def gui_change_vit(self, new_speed):
        #fonction pour changer la vitesse(l'attente entre chaque étape)
        # global vitesse
        # vitesse = int(eval(entree.get()))
        print(new_speed)
    
        def gui_go(self):
        print("button go pressed")
     def gui_display(self):
		#1) Récupère le contenu de Model
		#2) L'envoie à  View pour affichage
	
        word_l = self.model.get_word()
        # print(word_l)
        self.view.display_word(word_l)

    def gui_modify(self):
        word_l = self.model.get_word()
        i_alea = random.randrange(len(word_l))
        self.model.modify_word(i_alea)
        print("mot modifié")

    def gui_reset(self):
        self.model.reset_word()
        print("mot resetté")
    """

    # fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au __dico_case
    def click_gauche(self, event):
        x = event.x - (event.x % self.model.get_c())
        y = event.y - (event.y % self.model.get_c())
        self.get_canvas.create_rectangle(x, y, x + self.model.get_c(), y + self.model.get_c(), fill='black')
        self.get_dico_case[x, y] = 1

    # fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au __dico_case
    def click_droit(self, event):
        x = event.x - (event.x % self.model.get_c())
        y = event.y - (event.y % self.model.get_c())
        self.get_canvas.create_rectangle(x, y, x + self.model.get_c(), y + self.model.get_c(), fill='white')
        self.get_dico_case[x, y] = 0

    # "démarrage de l'animation"
    def go(self):
        #
        if self.model.get_flag() == 0:
            self.model.set_flag(1)
            self.view.play()

    # "arrêt de l'animation"
    def stop(self):
        self.model.set_flag(0)

    # fonction pour changer la vitesse(l'attente entre chaque étape)
    def change_vit(self):
        self.model.set_vitesse(self.view.get_entree())
        print(self.model.get_vitesse())


    # Getter height
    def get_height(self):
        return self.model.get_height()

    # Getter width
    def get_width(self):
        return self.model.get_width()

    # Getter cellules
    def get_c(self):
        return self.model.get_c()

    def get_dico_case(self):
        return self.model.get_dico_case()

    def get_dico_etat(self):
        return self.model.get_dico_etat()

    def get_flag(self):
        return self.model.get_flag()

    def get_vitesse(self):
        return self.model.get_vitesse()

    def set_flag(self, flag):
        self.model.set_flag(flag)

    def set_vitesse(self, vitesse):
        self.model.set_vitesse(vitesse)

