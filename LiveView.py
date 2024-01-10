from LiveController import LiveController
from tkinter import *


class LiveView:
    # Instantiation de classes
    __fen1 = Tk()
    __liveController_o = LiveController()

    # Variable entree
    entree = Entry(__fen1)
    entree.bind("<Return>", __liveController_o.change_vit)
    entree.pack(side=RIGHT)

    # Canvas
    __can1 = Canvas(__fen1, width = __liveController_o.get_width(), height = __liveController_o.get_height(), bg='white')
    __can1.bind("<Button-1>", __liveController_o.click_gauche)
    __can1.bind("<Button-3>", __liveController_o.click_droit)
    __can1.pack(side=TOP, padx=5, pady=5)


    def __init__(self, controller):
        self.window = Tk()
        self.get_dico_case = self.__liveController_o.get_dico_case()
        self.get_dico_etat = self.__liveController_o.get_dico_etat()
        self.__get_c = self.__liveController_o.get_c()

        """
        b1 = Button(self.window, text='Go!', command=controller.gui_go)  # référence !
        b1.pack(side=LEFT, padx=3, pady=3)

        # b2 = Button(fen1, text='Display')
        # b2.bind( "<Click>", lambda event: controller.gui_display())
        b2 = Button(self.window, text='Display', command=controller.gui_display)
        b2.pack(side=LEFT, padx=3, pady=3)

        b3 = Button(self.window, text='Modify', command=controller.gui_modify)
        b3.pack(side=LEFT, padx=3, pady=3)

        b4 = Button(self.window, text='Reset', command=controller.gui_reset)
        b4.pack(side=LEFT, padx=3, pady=3)

        entree = Entry(self.window)
        entree.bind("<Return>", lambda event: controller.gui_change_vit(entree.get()))
        entree.pack(side=RIGHT)

        chaine = Label(self.window)
        chaine.configure(text="Attente entre chaque étape (ms) :")
        chaine.pack(side=RIGHT)
        """

        # __
        self.damier()

        b1 = Button(self.__fen1, text='Go!', command = self.__liveController_o.go)
        b2 = Button(self.__fen1, text='Stop', command = self.__liveController_o.stop)
        b1.pack(side=LEFT, padx=3, pady=3)
        b2.pack(side=LEFT, padx=3, pady=3)
        b3 = Button(self.__fen1, text='Canon planeur', command = self.__liveController_o.canon)
        b3.pack(side=LEFT, padx=3, pady=3)

        chaine = Label(self.__fen1)
        chaine.configure(text="Attente entre chaque étape (ms) :")
        chaine.pack(side=RIGHT)

        self.__fen1.mainloop()

    # Getter canvas
    def get_canvas(self):
        return self.__can1

    # Getter entree
    def get_entree(self):
        return int(eval(self.entree))

    def damier(self):  # fonction dessinant le tableau
        self.ligne_vert()
        self.ligne_hor()

    def ligne_vert(self):
        c_x = 0
        while c_x != self.__liveController_o.get_width():
            self.__can1.create_line(c_x, 0, c_x, self.__liveController_o.get_height(), width=1, fill='black')
            c_x += self.__liveController_o.get_c()

    def ligne_hor(self):
        c_y = 0
        while c_y != self.__liveController_o.get_height():
            self.__can1.create_line(0, c_y, self.__liveController_o.get_width(), c_y, width=1, fill='black')
            c_y += self.__liveController_o.get_c()

    def play(self):
        v = 0
        while v != self.__liveController_o.get_width() / self.__liveController_o.get_c():
            w = 0
            while w != self.__liveController_o.get_height() / self.__liveController_o.get_c():
                x = v * self.__liveController_o.get_c()
                y = w * self.__liveController_o.get_c()

                # cas spéciaux:
                # les coins
                if x == 0 and y == 0:  # coin en haut à gauche
                    compt_viv = 0
                    if self.get_dico_case[x, y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv
                elif x == 0 and y == int(self.__liveController_o.get_height() - self.__liveController_o.get_c()):  # coin en bas à gauche
                    compt_viv = 0
                    if self.get_dico_case[x, y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv
                elif x == int(self.__liveController_o.get_width() - self.__liveController_o.get_c()) and y == 0:  # coin en haut à droite
                    compt_viv = 0
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv
                elif x == int(self.__liveController_o.get_width() - self.__liveController_o.get_c()) and y == int(self.__liveController_o.get_height() - self.__liveController_o.get_c()):  # coin en bas à droite
                    compt_viv = 0
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv

                # cas spéciaux:
                # les bords du tableau (sans les coins)
                elif x == 0 and 0 < y < int(self.__liveController_o.get_height() - self.__liveController_o.get_c()):  # bord de gauche
                    compt_viv = 0
                    if self.get_dico_case[x, y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv
                elif x == int(self.__liveController_o.get_width() - self.__liveController_o.get_c()) and 0 < y < int(self.__liveController_o.get_height() - self.__liveController_o.get_c()):  # bord de droite
                    compt_viv = 0
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv
                elif 0 < x < int(self.__liveController_o.get_width() - self.__liveController_o.get_c()) and y == 0:  # bord du haut
                    compt_viv = 0
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv
                elif 0 < x < int(self.__liveController_o.get_width() - self.__liveController_o.get_c()) and y == int(self.__liveController_o.get_height() - self.__liveController_o.get_c()):  # bord du bas
                    compt_viv = 0
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv

                # cas généraux
                # les cellules qui ne sont pas dans les bords du tableau
                else:
                    compt_viv = 0
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x - self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x, y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y - self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y] == 1:
                        compt_viv += 1
                    if self.get_dico_case[x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c()] == 1:
                        compt_viv += 1
                    self.get_dico_etat[x, y] = compt_viv

                w += 1
            v += 1
        self.redessiner()
        if self.__liveController_o.get_flag() > 0:
            self.__fen1.after(self.__liveController_o.get_vitesse(), self.play())

    def redessiner(self):  # fonction redessinant le tableau à partir de dico_etat
        self.__can1.delete(ALL)
        self.damier()
        t = 0
        while t != self.__liveController_o.get_width() / self.__liveController_o.get_c():
            u = 0
            while u != self.__liveController_o.get_height() / self.__liveController_o.get_c():
                x = t * self.__liveController_o.get_c()
                y = u * self.__liveController_o.get_c()
                if self.get_dico_etat[x, y] == 3:
                    self.get_dico_etat[x, y] = 1
                    self.__can1.create_rectangle(x, y, x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c(), fill='black')
                elif self.get_dico_etat[x, y] == 2:
                    if self.get_dico_etat[x, y] == 1:
                        self.__can1.create_rectangle(x, y, x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c(), fill='black')
                    else:
                        self.__can1.create_rectangle(x, y, x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c(), fill='white')
                elif self.get_dico_etat[x, y] < 2 or self.get_dico_etat[x, y] > 3:
                    self.get_dico_etat[x, y] = 0
                    self.__can1.create_rectangle(x, y, x + self.__liveController_o.get_c(), y + self.__liveController_o.get_c(), fill='white')
                u += 1
            t += 1

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
        self.__liveController_o.go()

    def display_word(self, data):
        str = "/".join(data)
        print(str)

    def mainloop(self):
        self.window.mainloop()
