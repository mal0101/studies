## Exercice 2 tp 2:
# création de la base de donnée:
data = data.frame(cbind(c(rep("homme", 4), rep("femme", 5)), c(1:4, 3:7)))
names(data) = c("genre", "score")
data$score = as.numeric(data$score)
data
# calcul du score moyen des hommes d'une part puis celui des femmes d'une autre part
attach(data)
ave(score, genre)
cbind(data, MoyCondi=ave(score,genre))
# calcul de la moyenne conditionelle en utilisant la fonction aggregate()
aggregate(score, by=list(genre), FUN=mean)
prop.table(table(genre))
head(data, 3)

