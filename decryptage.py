from pathlib import Path
from string import ascii_uppercase

#J'importe mon texte avec les mots de remplissage
file_ancien_message = Path("ancien-message.txt")
text = file_ancien_message.read_text(encoding='utf-8')
cleanTextAncien = text.lower().replace('\n', ' ')
splittedTextAcien = cleanTextAncien.split()

#j'importe les mots de remplissage et je clean le text
file_mot_remplissance = Path("mot-remplissage.txt")
mot_remplissage = file_mot_remplissance.read_text(encoding="utf-8")
clean_text_mot_remplissage = mot_remplissage.replace("{", '').replace('}', '').replace(',', '').replace("'", '').lower()
set_mot_remplissage = set(clean_text_mot_remplissage.split())

#Je compare les deux fichiers et enleve les mots de remplissage
text_sans_remplissage = [mot for mot in splittedTextAcien if mot not in set_mot_remplissage]

#Je trie par ordre alphabétique
mot_trie = sorted(text_sans_remplissage)


#Generation de la liste de lettre majuscule
cle_alphabet = list(ascii_uppercase)
#Ajout des 10 premiers entiers à la liste
cle_alphabet += [str(i) for i in range(10)]

#J'associe les mots triés et les clés grâce à une liste de compréhension
def associationMotClef():
    association = [(mot_trie[i], cle_alphabet[i]) for i in range(len(mot_trie))]
    return association

