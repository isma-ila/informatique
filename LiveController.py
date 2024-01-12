from tkinter import *


class LiveController:

    def __init__(self, liveModel, liveView):
        self.model = liveModel
        self.view = liveView
        self.get_canvas = self.view.get_canvas()

        #
        self.model.initialisation_cellules()

        self.play()
        #
        self.view.mainloop()



    def play(self):
        v = 0
        while v != self.model.get_width() / self.model.get_c():
            w = 0
            while w != self.model.get_height() / self.model.get_c():
                x = v * self.model.get_c()
                y = w * self.model.get_c()

                # cas spéciaux:
                # les coins
                # coin en haut à gauche
                if x == 0 and y == 0:
                    compt_viv = 0
                    if self.model.get_dico_case[x, y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x + self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv
                # coin en bas à gauche
                elif x == 0 and y == int(self.model.get_height() - self.model.get_c()):
                    compt_viv = 0
                    if self.model.get_dico_case[x, y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x + self.model.get_c(), y] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv
                # coin en haut à droite
                elif x == int(self.model.get_width() - self.model.get_c()) and y == 0:
                    compt_viv = 0
                    if self.model.get_dico_case[x - self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y + self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv
                # coin en bas à droite
                elif x == int(self.model.get_width() - self.model.get_c()) and y == int(
                        self.model.get_height() - self.model.get_c()):
                    compt_viv = 0
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x - self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y - self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv

                # cas spéciaux:
                # les bords du tableau (sans les coins)
                # bord de gauche
                elif x == 0 and 0 < y < int(self.model.get_height() - self.model.get_c()):
                    compt_viv = 0
                    if self.model.get_dico_case[x, y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x + self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv
                # bord de droite
                elif x == int(self.model.get_width() - self.model.get_c()) and 0 < y < int(
                        self.model.get_height() - self.model.get_c()):
                    compt_viv = 0
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x - self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y + self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv
                # bord du haut
                elif 0 < x < int(self.model.get_width() - self.model.get_c()) and y == 0:
                    compt_viv = 0
                    if self.model.get_dico_case[x - self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x + self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv
                # bord du bas
                elif 0 < x < int(self.model.get_width() - self.model.get_c()) and y == int(
                        self.model.get_height() - self.model.get_c()):
                    compt_viv = 0
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x - self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x + self.model.get_c(), y] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv

                # cas généraux
                # les cellules qui ne sont pas dans les bords du tableau
                else:
                    compt_viv = 0
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x - self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x - self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x, y + self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y - self.model.get_c()] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[x + self.model.get_c(), y] == 1:
                        compt_viv += 1
                    if self.model.get_dico_case[
                        x + self.model.get_c(), y + self.model.get_c()] == 1:
                        compt_viv += 1
                    self.model.get_dico_etat[x, y] = compt_viv

                w += 1
            v += 1
        self.redessiner()
        if self.model.get_flag() > 0:
            self.view.__fen1.after(self.model.get_vitesse(), self.play())
        

    # fonction redessinant le tableau à partir de dico_etat
    def redessiner(self):
        self.view.get_canvas.delete(ALL)
        self.view.damier()
        t = 0
        while t != self.model.get_width() / self.model.get_c():
            u = 0
            while u != self.model.get_height() / self.model.get_c():
                x = t * self.model.get_c()
                y = u * self.model.get_c()
                if self.model.get_dico_etat[x, y] == 3:
                    self.model.get_dico_etat[x, y] = 1
                    self.view.__can1.create_rectangle(x, y, x + self.model.get_c(),
                                                 y + self.model.get_c(), fill='black')
                elif self.model.get_dico_etat[x, y] == 2:
                    if self.model.get_dico_etat[x, y] == 1:
                        self.view.__can1.create_rectangle(x, y, x + self.model.get_c(),
                                                     y + self.model.get_c(), fill='black')
                    else:
                        self.view.__can1.create_rectangle(x, y, x + self.model.get_c(),
                                                     y + self.model.get_c(), fill='white')
                elif self.model.get_dico_etat[x, y] < 2 or self.model.get_dico_etat[x, y] > 3:
                    self.model.get_dico_etat[x, y] = 0
                    self.view.__can1.create_rectangle(x, y, x + self.model.get_c(),
                                                 y + self.model.get_c(), fill='white')
                u += 1
            t += 1
