
import tkinter as tk

class Morpion:
    def __init__(self):
        self.boutons = []
        self.joueur_actuel = 'X'
        self.partie_gagnee = False
        self.taille_grille = 16
        self.alignement_victoire = 4
        self.label_message = None

    def afficher_message(self, message):
        if self.label_message is not None:
            self.label_message.destroy()
        self.label_message = tk.Label(root, text=message, font=("Arial", 12))
        self.label_message.grid(row=self.taille_grille + 1, columnspan=self.taille_grille)

    def afficher_gagnant(self):
        if not self.partie_gagnee:
            self.partie_gagnee = True
            self.afficher_message(f"Le joueur {self.joueur_actuel} a gagné la partie !")

    def changer_joueur(self):
        self.joueur_actuel = 'O' if self.joueur_actuel == 'X' else 'X'

    def verifier_victoire(self, row, col):
        # Vérification de la victoire horizontale
        if any(all(self.boutons[col + i][row]['text'] == self.joueur_actuel for i in range(self.alignement_victoire))
               for col in range(self.taille_grille - self.alignement_victoire + 1)):
            self.afficher_gagnant()

        # Vérification de la victoire verticale
        if any(all(self.boutons[col][row + i]['text'] == self.joueur_actuel for i in range(self.alignement_victoire))
               for col in range(self.taille_grille)
               for row in range(self.taille_grille - self.alignement_victoire + 1)):
            self.afficher_gagnant()

        # Vérification de la victoire diagonale
        if any(all(self.boutons[col + i][row + i]['text'] == self.joueur_actuel for i in range(self.alignement_victoire))
               for col in range(self.taille_grille - self.alignement_victoire + 1)
               for row in range(self.taille_grille - self.alignement_victoire + 1)):
            self.afficher_gagnant()

        # Vérification de la victoire diagonale inversée
        if any(all(self.boutons[col + i][row - i]['text'] == self.joueur_actuel for i in range(self.alignement_victoire))
               for col in range(self.taille_grille - self.alignement_victoire + 1)
               for row in range(self.alignement_victoire - 1, self.taille_grille)):
            self.afficher_gagnant()

    def placer_symbole(self, row, col):
        bouton = self.boutons[col][row]
        if bouton['text'] == "" and not self.partie_gagnee:
            bouton.config(text=self.joueur_actuel)
            couleur = 'red' if self.joueur_actuel == 'X' else 'blue'
            bouton.config(fg=couleur)
            self.verifier_victoire(row, col)
            self.changer_joueur()

    def creer_grille(self):
        for col in range(self.taille_grille):
            boutons_col = []
            for row in range(self.taille_grille):
                bouton = tk.Button(
                    root, font=("Arial", 10),
                    width=2, height=1,
                    command=lambda r=row, c=col: jeu.placer_symbole(r, c)
                )
                bouton.grid(row=row, column=col)
                boutons_col.append(bouton)
            self.boutons.append(boutons_col)

    def reinitialiser_partie(self):
        for col in self.boutons:
            for bouton in col:
                bouton.destroy()
        if self.label_message is not None:
            self.label_message.destroy()
        self.boutons = []
        self.joueur_actuel = 'X'
        self.partie_gagnee = False
        self.creer_grille()

if __name__ == "__main__":
    jeu = Morpion()

    root = tk.Tk()
    root.title("Morpion")
    root.minsize(400, 400)

    bouton_reset = tk.Button(root, text="Réinitialiser", command=jeu.reinitialiser_partie)
    bouton_reset.grid(row=16, column=0, columnspan=16)

    jeu.creer_grille()

    root.mainloop()