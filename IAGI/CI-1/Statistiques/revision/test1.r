nbEnfant = c(1,4,4,3,1,5,2,3,2,2,2,3,2,6,4,1,3,1,6,2,1,4,1,1,6,4,1,5,5,1,3,3,7,2,4,3,2,3,3,5,2,3,6,4,4,3,2,2,1,5,3,6,2,0,5,1,7,4,3,5,4,3,6,5,2,7,7,3,3,1,2,0,2,3,5,3,3,7,6,7,2,3,1,3,3,3,5,3,2,5,6,4,1,0,2,6,5,1,0,1)
length(nbEnfant)
mode(nbEnfant)
# structure de la modalité
str(nbEnfant)
# liste des modalité, equivalent of DISTINCT in sql
unique(nbEnfant)
# Effectif d'une modalité
length(nbEnfant[nbEnfant==0])
length(nbEnfant[nbEnfant==4])
# Fréquence d'une modalité
length(nbEnfant[nbEnfant==0])/length(nbEnfant)
# Effectif cumulé croissant
length(nbEnfant[nbEnfant<=6])
# Fréquence cumulée croissant
length(nbEnfant[nbEnfant<=6])/length(nbEnfant)
# table des effectifs
table(nbEnfant) #it shows a table where the first row represents les modalités and the second one les effectifs de chaque modalité
# table des effectifs cumulés
cumsum(table(nbEnfant))
# table des fréquences cumulées
cumsum(table(nbEnfant))/length(nbEnfant)

## Mesure de la tendance centrale
# on calcule le mode en utilisant la commande suivante
as.numeric(names(sort(table(nbEnfant), decreasing = TRUE) [1]))
# la moyenne
mean(nbEnfant)
# la mediane
median(nbEnfant)

## Mesure de dispersion
# l'étendue
range(nbEnfant)
# les quartiles
quantile(nbEnfant)
# calcule de la médiane en utilisant la fonction quantile
quantile(nbEnfant, 0.5)
# les déciles
quantile(nbEnfant, 0:10/10)
# la variance
# la variance théorique
mean(nbEnfant^2) - mean(nbEnfant)^2
# la variance corrigée
var(nbEnfant)
# la variance théorique à partir de la variance corrigée
var(nbEnfant) * (length(nbEnfant)-1)/length(nbEnfant)
# l'écart type
sd(nbEnfant)
# l'écart type en utilisant la variance corrigée
var(nbEnfant) ^ 0.5
# l'écart type en utilisant la variance théorique
(mean(nbEnfant^2) - mean(nbEnfant)^2) ^ 0.5

## Représentation graphique
# Histogramme
barplot(table(nbEnfant))

# boite à moustache
boxplot

