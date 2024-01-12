from tkinter import *


class LiveView:
    # Instantiation de classes
    __fen1 = Tk()
    __liveModel_o = ""
    __can1 = ""
    __entree = ""

    def __init__(self, liveModel):
        self.__liveModel_o = liveModel
        self.get_dico_case = self.__liveModel_o.get_dico_case()
        self.get_dico_etat = self.__liveModel_o.get_dico_etat()
        self.__get_c = self.__liveModel_o.get_c()

        # Canvas
        self.__can1 = Canvas(self.__fen1, width=self.__liveModel_o.get_width(), height=self.__liveModel_o.get_height(), bg='white')
        self.__can1.bind("<Button-1>", self.click_gauche)
        self.__can1.bind("<Button-3>", self.click_droit)
        self.__can1.pack(side=TOP, padx=5, pady=5)

        # __
        self.damier()

        b1 = Button(self.__fen1, text='Go!', command = self.go)
        b2 = Button(self.__fen1, text='Stop', command = self.stop)
        b1.pack(side=LEFT, padx=3, pady=3)
        b2.pack(side=LEFT, padx=3, pady=3)
        b3 = Button(self.__fen1, text='Canon planeur', command=self.canon)
        b3.pack(side=LEFT, padx=3, pady=3)

        self.__entree = Entry(self.__fen1)
        self.__entree.bind("<Return>", self.change_vit)
        self.__entree.pack(side=RIGHT)
        chaine = Label(self.__fen1)
        chaine.configure(text="Attente entre chaque étape (ms) :")
        chaine.pack(side=RIGHT)

        self.__fen1.mainloop()



    # Getter canvas
    def get_canvas(self):
        return self.__can1

    # Getter __entree
    def get_entree(self):
        return int(eval(self.__entree.get()))

    def damier(self):  # fonction dessinant le tableau
        self.ligne_vert()
        self.ligne_hor()

    def ligne_vert(self):
        c_x = 0
        while c_x != self.__liveModel_o.get_width():
            self.__can1.create_line(c_x, 0, c_x, self.__liveModel_o.get_height(), width=1, fill='black')
            c_x += self.__liveModel_o.get_c()

    def ligne_hor(self):
        c_y = 0
        while c_y != self.__liveModel_o.get_height():
            self.__can1.create_line(0, c_y, self.__liveModel_o.get_width(), c_y, width=1, fill='black')
            c_y += self.__liveModel_o.get_c()


    # fonction dessinant le célèbre canon à planeur de Bill Gosper
    def canon(self):
        self.get_dico_case[0 * self.__get_c, 5 * self.__get_c] = 1
        self.get_dico_case[0 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[1 * self.__get_c, 5 * self.__get_c] = 1
        self.get_dico_case[1 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[10 * self.__get_c, 5 * self.__get_c] = 1
        self.get_dico_case[10 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[10 * self.__get_c, 7 * self.__get_c] = 1
        self.get_dico_case[11 * self.__get_c, 4 * self.__get_c] = 1
        self.get_dico_case[11 * self.__get_c, 8 * self.__get_c] = 1
        self.get_dico_case[12 * self.__get_c, 3 * self.__get_c] = 1
        self.get_dico_case[12 * self.__get_c, 9 * self.__get_c] = 1
        self.get_dico_case[13 * self.__get_c, 3 * self.__get_c] = 1
        self.get_dico_case[13 * self.__get_c, 9 * self.__get_c] = 1
        self.get_dico_case[14 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[15 * self.__get_c, 4 * self.__get_c] = 1
        self.get_dico_case[15 * self.__get_c, 8 * self.__get_c] = 1
        self.get_dico_case[16 * self.__get_c, 5 * self.__get_c] = 1
        self.get_dico_case[16 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[16 * self.__get_c, 7 * self.__get_c] = 1
        self.get_dico_case[17 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[20 * self.__get_c, 3 * self.__get_c] = 1
        self.get_dico_case[20 * self.__get_c, 4 * self.__get_c] = 1
        self.get_dico_case[20 * self.__get_c, 5 * self.__get_c] = 1
        self.get_dico_case[21 * self.__get_c, 3 * self.__get_c] = 1
        self.get_dico_case[21 * self.__get_c, 4 * self.__get_c] = 1
        self.get_dico_case[21 * self.__get_c, 5 * self.__get_c] = 1
        self.get_dico_case[22 * self.__get_c, 2 * self.__get_c] = 1
        self.get_dico_case[22 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[24 * self.__get_c, 1 * self.__get_c] = 1
        self.get_dico_case[24 * self.__get_c, 2 * self.__get_c] = 1
        self.get_dico_case[24 * self.__get_c, 6 * self.__get_c] = 1
        self.get_dico_case[24 * self.__get_c, 7 * self.__get_c] = 1
        self.get_dico_case[34 * self.__get_c, 3 * self.__get_c] = 1
        self.get_dico_case[34 * self.__get_c, 4 * self.__get_c] = 1
        self.get_dico_case[35 * self.__get_c, 3 * self.__get_c] = 1
        self.get_dico_case[35 * self.__get_c, 4 * self.__get_c] = 1

        # Appel the méthode
        self.go()

        # fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au __dico_case

    def click_gauche(self, event):
        x = event.x - (event.x % self.__liveModel_o.get_c())
        y = event.y - (event.y % self.__liveModel_o.get_c())
        self.get_canvas().create_rectangle(x, y, x + self.__liveModel_o.get_c(), y + self.__liveModel_o.get_c(), fill='black')
        self.get_dico_case[x, y] = 1

        # fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au __dico_case

    def click_droit(self, event):
        x = event.x - (event.x % self.__liveModel_o.get_c())
        y = event.y - (event.y % self.__liveModel_o.get_c())
        self.get_canvas().create_rectangle(x, y, x + self.__liveModel_o.get_c(), y + self.__liveModel_o.get_c(), fill='white')
        self.get_dico_case[x, y] = 0

        # "démarrage de l'animation"

    def go(self):
        #
        if self.__liveModel_o.get_flag() == 0:
            self.__liveModel_o.set_flag(1)
            self.__liveModel_o.play()

        # "arrêt de l'animation"

    def stop(self):
        self.__liveModel_o.set_flag(0)

        # fonction pour changer la vitesse(l'attente entre chaque étape)

    def change_vit(self):
        self.__liveModel_o.set_vitesse(self.get_entree())
        return self.__liveModel_o.get_vitesse()

    def mainloop(self):
        self.__fen1.mainloop()
