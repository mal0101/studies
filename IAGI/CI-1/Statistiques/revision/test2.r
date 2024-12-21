## Exercice 1 tp 2:
taille_eleve = c(138,164,150,132,144,125,149,157,146,158,140,147,136,148,152,144,168,126,138,176,163,119,154,165,146,173,142,147,135,161,145,135,142,150,156,145,128)
taille_eleve

#moyenne des tailles
mean(taille_eleve)

# Regrouppement des données en 5 classes puis 10 classes puis représentation graphique

# regroupement en 5 classes:
hist(taille_eleve, breaks = seq(from = min(taille_eleve), to = max(taille_eleve), length = 6), col = grey(0.8), labels = TRUE, las = 1, xlab = "Taille (cm)", ylab = "Nombre d'élèves", main = "Avec un découpage en 5 classes") -> avec5
# regroupement en 10 classes:
hist(taille_eleve, breaks = seq(from = min(taille_eleve), to = max(taille_eleve), length = 11), col = grey(0.8), labels = TRUE, las = 1, xlab = "Taille (cm)", ylab = "Nombre d'élèves", main = "Avec un découpage en 10 classes") -> avec10
# moyenne dans les deux cas
# dans le cas du regroupement en 5 classes
moy5 <- weighted.mean(avec5$mids, avec5$counts)
moy5
# dans le cas du regroupement en 10 classes
moy10 <- weighted.mean(avec10$mids, avec10$counts)
moy10
boxplot(taille_eleve, horizontal=T, xlab = "Taille (cm)", main = "Taille de 40 élèves")
rug(taille_eleve, 0.1)

