"""
"""
import random
from tkinter import Canvas, TOP, Tk, Entry, ALL, Button, LEFT, RIGHT, Label


class LiveCanvas():

    def __init__(self, liveModel):
        self.running = False
        self.liveModel = liveModel
        self.width = self.liveModel.get_width()
        self.height = self.liveModel.get_height()
        self.c = self.liveModel.get_cell()
        self.fen1 = Tk()
        self.can1 = Canvas(self.fen1, width=self.width, height=self.height, bg='white')
        self.entree = Entry(self.fen1)

        self.init_ui()

    def init_ui(self):
        self.can1 = Canvas(self.fen1, width=self.width, height=self.height, bg='white')
        self.can1.pack(side=TOP, padx=5, pady=5)
        self.damier()

        b1 = Button(self.fen1, text='Go!', command=self.go)
        b2 = Button(self.fen1, text='Stop', command=self.stop)
        b3 = Button(self.fen1, text='Canon planeur', command=self.canon)
        b4 = Button(self.fen1, text='Reset', command=self.reset)

        b1.pack(side=LEFT, padx=3, pady=3)
        b2.pack(side=LEFT, padx=3, pady=3)
        b3.pack(side=LEFT, padx=3, pady=3)
        b4.pack(side=LEFT, padx=3, pady=3)

        self.entree.bind("<Return>", self.change_vit)
        self.entree.pack(side=RIGHT)

        chaine = Label(self.fen1, text="Attente entre chaque étape (ms) :")
        chaine.pack(side=RIGHT)

        self.fen1.after(0, self.mainloop)

    def reset(self):
        self.get_canvas().delete(ALL)
        self.damier()

        col = 0

        while col != self.width / self.c:
            row = 0
            while row != self.height / self.c:
                x = col * self.c
                y = row * self.c

                # Dessiner une cellule
                if self.liveModel.get_dico_case().get((x, y), 0) == 1:
                    self.can1.create_rectangle(x, y, x + self.c, y + self.c, fill='white')
                row += 1
            col += 1


    def go(self):
        self.running = True
        self.liveModel.set_flag(1)

        if self.running:
            self.play()

    def stop(self):
        self.liveModel.set_flag(0)
        self.running = False

    def get_canvas(self):
        return self.can1

    def get_entree(self):
        return int(eval(self.entree.get()))

    def damier(self):
        self.ligne_vert()
        self.ligne_hor()

    def ligne_vert(self):
        c_x = 0
        while c_x != self.width:
            self.can1.create_line(c_x, 0, c_x, self.height, width=1, fill='black')
            c_x += self.c

    def ligne_hor(self):
        c_y = 0
        while c_y != self.height:
            self.can1.create_line(0, c_y, self.width, c_y, width=1, fill='black')
            c_y += self.c

    def canon(self):
        self.liveModel.get_dico_case()[0 * self.c, 5 * self.c] = 1
        self.liveModel.get_dico_case()[0 * self.c, 6 * self.c] = 1

        self.liveModel.get_dico_case()[1 * self.c, 5 * self.c] = 1
        self.liveModel.get_dico_case()[1 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[10 * self.c, 5 * self.c] = 1
        self.liveModel.get_dico_case()[10 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[10 * self.c, 7 * self.c] = 1
        self.liveModel.get_dico_case()[11 * self.c, 4 * self.c] = 1
        self.liveModel.get_dico_case()[11 * self.c, 8 * self.c] = 1
        self.liveModel.get_dico_case()[12 * self.c, 3 * self.c] = 1
        self.liveModel.get_dico_case()[12 * self.c, 9 * self.c] = 1
        self.liveModel.get_dico_case()[13 * self.c, 3 * self.c] = 1
        self.liveModel.get_dico_case()[13 * self.c, 9 * self.c] = 1
        self.liveModel.get_dico_case()[14 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[15 * self.c, 4 * self.c] = 1
        self.liveModel.get_dico_case()[15 * self.c, 8 * self.c] = 1
        self.liveModel.get_dico_case()[16 * self.c, 5 * self.c] = 1
        self.liveModel.get_dico_case()[16 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[16 * self.c, 7 * self.c] = 1
        self.liveModel.get_dico_case()[17 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[20 * self.c, 3 * self.c] = 1
        self.liveModel.get_dico_case()[20 * self.c, 4 * self.c] = 1
        self.liveModel.get_dico_case()[20 * self.c, 5 * self.c] = 1
        self.liveModel.get_dico_case()[21 * self.c, 3 * self.c] = 1
        self.liveModel.get_dico_case()[21 * self.c, 4 * self.c] = 1
        self.liveModel.get_dico_case()[21 * self.c, 5 * self.c] = 1
        self.liveModel.get_dico_case()[22 * self.c, 2 * self.c] = 1
        self.liveModel.get_dico_case()[22 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[24 * self.c, 1 * self.c] = 1
        self.liveModel.get_dico_case()[24 * self.c, 2 * self.c] = 1
        self.liveModel.get_dico_case()[24 * self.c, 6 * self.c] = 1
        self.liveModel.get_dico_case()[24 * self.c, 7 * self.c] = 1
        self.liveModel.get_dico_case()[34 * self.c, 3 * self.c] = 1
        self.liveModel.get_dico_case()[34 * self.c, 4 * self.c] = 1
        self.liveModel.get_dico_case()[35 * self.c, 3 * self.c] = 1
        self.liveModel.get_dico_case()[35 * self.c, 4 * self.c] = 1

        #
        self.redraw()

    def click_gauche(self, event):
        x = event.x - (event.x % self.c)
        y = event.y - (event.y % self.c)
        self.get_canvas().create_rectangle(x, y, x + self.c, y + self.c, fill='black')
        self.liveModel.get_dico_case()[x, y] = 1

    def click_droit(self, event):
        x = event.x - (event.x % self.c)
        y = event.y - (event.y % self.c)
        self.get_canvas().create_rectangle(x, y, x + self.c, y + self.c, fill='white')
        self.liveModel.get_dico_case()[x, y] = 0

    # Redessiner le gui
    def redraw(self):

        self.get_canvas().delete(ALL)
        self.damier()

        col = 0

        while col != self.width / self.c:
            row = 0
            while row != self.height / self.c:
                x = col * self.c
                y = row * self.c

                # Dessiner une cellule
                if self.liveModel.get_dico_case().get((x, y), 0) == 1:
                    self.can1.create_rectangle(x, y, x + self.c, y + self.c, fill='black')
                row += 1
            col += 1

    def mainloop(self):
        self.fen1.mainloop()

    def change_vit(self, event=None):
        self.liveModel.set_interval_time(self.get_entree())

    def play(self):
        if self.running:
            self.update()
            self.redraw()
            if self.liveModel.get_flag() > 0:
                self.fen1.after(self.liveModel.get_interval_time(), self.play)

    def update(self):
        new_dico_etat = {}

        # Réaliser une itération sur le canvas (ligne par colonne)
        for x in range(0, self.liveModel.get_width(), self.liveModel.get_cell()):
            for y in range(0, self.liveModel.get_height(), self.liveModel.get_cell()):
                count_cell_active = 0

                # Iterer
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue  # On ignore la cellule actuelle puisqu'elle n'est pas supposée être voisine à elle-même

                        nx = (x + (i * self.liveModel.get_cell())) % self.liveModel.get_width()
                        ny = (y + (j * self.liveModel.get_cell())) % self.liveModel.get_height()
                        count_cell_active += self.liveModel.get_dico_case().get((nx, ny), 0)

                # Application des règles du jeu de la vie
                if count_cell_active == 3 or count_cell_active == 4:
                    new_dico_etat[x, y] = 1  # Cellule naît ou reste en vie
                elif count_cell_active < 1 or count_cell_active > 4:
                    new_dico_etat[x, y] = 0  # Une cellule qui trépasse
                else:
                    new_dico_etat[x, y] = self.liveModel.get_dico_etat().get((x, y), 0)

        # Mise à jour du modèle une fois tous les nouvels états sont calculés
        self.liveModel.set_dico_etat(new_dico_etat)

        # Actualisation de cellules de manière aléatoire
        for x in range(0, self.liveModel.get_width(), self.liveModel.get_cell()):
            for y in range(0, self.liveModel.get_height(), self.liveModel.get_cell()):
                if random.random() < 0.5:
                    self.liveModel.get_dico_case()[x, y] = new_dico_etat[x, y]
