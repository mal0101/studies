#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

typedef struct Arbre
{
	int Valeur;
	struct Arbre * FG;
	struct Arbre * FD;
} Arbre;

void AfficherArbreCroissant(Arbre * Racine)
{
	if (Racine!=NULL)
	{
		AfficherArbreCroissant(Racine->FG);
		printf("%d ",Racine->Valeur);
		AfficherArbreCroissant(Racine->FD);
	}
}
void AfficherArbreDecroissant(Arbre * Racine)
{
	if (Racine!=NULL)
	{
		AfficherArbreDecroissant(Racine->FD);
		printf("%d ",Racine->Valeur);
		AfficherArbreDecroissant(Racine->FG);
	}
}

void AfficherArbre(Arbre * Racine)
{
	if (Racine!=NULL)
	{
		printf("%d ",Racine->Valeur);
		if (Racine->FD!=NULL || Racine->FG!=NULL)
		{
			AfficherArbre(Racine->FG);
			AfficherArbre(Racine->FD);
		}
	}
}
Arbre * CreerValeur(Arbre * Racine,int valeur)
{
	if (Racine!=NULL)
	{
		if (Racine->Valeur>valeur)
		{
			Racine->FG=CreerValeur(Racine->FG,valeur);
		}
		else
		{
			Racine->FD=CreerValeur(Racine->FD,valeur);
		}
	}
	else
	{
		Racine=(Arbre *)malloc(sizeof(Arbre));
		Racine->Valeur=valeur;
		Racine->FD=NULL;
		Racine->FG=NULL;
	}
return Racine;
}
void EnregArbre(Arbre * Racine,char * NomFic)
{
	int nb;
	FILE * fic;
	fic=fopen(NomFic,"at");
	if (Racine!=NULL)
	{
		nb=Racine->Valeur;
		fwrite(&nb,sizeof(int),1,fic);
		fclose(fic);
		if (Racine->FD!=NULL || Racine->FG!=NULL)
		{
			EnregArbre(Racine->FG,NomFic);
			EnregArbre(Racine->FD,NomFic);
		}
	}
}

Arbre * ChargerArbre(Arbre * Racine,char * NomFic)
{
	int nb;
	FILE * fic;
	fic=fopen(NomFic,"rt");
	fread(&nb,sizeof(int),1,fic);
	while (!feof(fic))
	{
		Racine = CreerValeur(Racine,nb);
		fread(&nb,sizeof(int),1,fic);
	}
	fclose(fic);
	return Racine;
}

int Somme(Arbre * Racine)
{
	int total=0;
	if (Racine!=NULL)
	{
		total=Somme(Racine->FG);
		total+=Racine->Valeur;
		total+=Somme(Racine->FD);
	}
	return total;
}

int CompteValeur(Arbre * Racine)
{
	int total=0;
	if (Racine!=NULL)
	{
		total=CompteValeur(Racine->FG);
		total++;
		total+=CompteValeur(Racine->FD);
	}
	return total;
}

Arbre * RechercheValeur(Arbre * Racine,  int valeur)
{
	if (Racine!=NULL)
	{
		if (Racine->Valeur>valeur)
		{
			Racine=RechercheValeur(Racine->FG,valeur);
		}
		else
		{
			if (Racine->Valeur<valeur)
			{
				Racine=RechercheValeur(Racine->FD,valeur);
			}
		}
		return Racine;
	}
	return Racine;
}

Arbre * SuppValeur(Arbre * Racine, int valeur)
{
	Arbre * ValeurASupprimer;
	if (Racine->Valeur==valeur) // on a trouvé l'élément à supprimer
	{
		ValeurASupprimer=Racine;
		if (ValeurASupprimer->FG==NULL) //si ya pa de FG, on retourne FD
			return ValeurASupprimer->FD;
		else
		{
			Racine=ValeurASupprimer->FG; //sinon on recherche dans FG l'endroit pour insérer le FD
				while (Racine->FD!=NULL)
				{
					Racine=Racine->FD;
				}
				Racine->FD=ValeurASupprimer->FD;
			return ValeurASupprimer->FG;
		}
		free(ValeurASupprimer);
	}
	else
	{
		if (Racine->Valeur>valeur)
		{
			Racine->FG=SuppValeur(Racine->FG,valeur);
		}
		else
		{
			Racine->FD=SuppValeur(Racine->FD,valeur);
		}
	}
	return Racine;
}

int Menu()
{
	int Choix;
	do
	{
		system("cls"); //efface l'écran
		printf("             ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»\n");
		printf("             º                                                      º\n");
		printf("             º                    Menu Principal                    º\n");
		printf("             º                                                      º\n");
		printf("             ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼\n");
		printf("\n                 1- Ajouter un Valeur(s)");
		printf("\n                 2- Afficher l'arbre");
		printf("\n                 3- Afficher l'arbre dans l'ordre croissant");
		printf("\n                 4- Afficher l'arbre dans l'ordre decroissant");
		printf("\n                 5- Somme des Valeurs");
		printf("\n                 6- Nombre de Valeurs");
		printf("\n                 7- Rechercher un Valeur");
		printf("\n                 8- Enlever un Valeur");
		printf("\n                 9- Enregister l'arbre dans un fichier");
		printf("\n                10- Charger l'arbre \205 partir d'un fichier");
		printf("\n                11- Quitter\n");
		printf("\n\n\n\n\n\n\nChoix :");
		scanf("%d",&Choix);
	} while (Choix <1 || Choix >11);
	system("cls");
	return Choix;
}

int main()
{
	int valeur;
	int Choix;
	char * NomFic="Fic.txt";
	Arbre * Racine;
	Arbre * RepRecherche;
	Racine=NULL;
	Choix = Menu();
	while (Choix!=11)
	{
		if (Racine==NULL && Choix>1 && Choix <10)
		{
			printf("Vous devez d'abord saisir un arbre");
			printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
			getch();
		}
		else
		{
			switch (Choix)
			{
				case 1 :	printf("Saisir un entier (0 pour finir la saisie) : ");
							scanf("%d",&valeur);
							while (valeur != 0)
							{
								Racine=CreerValeur(Racine,valeur);
								printf("Saisir un entier (0 pour finir la saisie) : ");
								scanf("%d",&valeur);
							}
							break;
				case 2 :	AfficherArbre(Racine);
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 3 :	AfficherArbreCroissant(Racine);
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 4 :	AfficherArbreDecroissant(Racine);
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 5 :	AfficherArbreCroissant(Racine);
							printf("\nTotal : %d",Somme(Racine));
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 6 :	AfficherArbreCroissant(Racine);
							printf("\nTotal : %d",CompteValeur(Racine));
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 7 :	printf("Saisir la valeur \205 rechercher : ");
							scanf("%d", &valeur);
							RepRecherche=RechercheValeur(Racine,valeur);
							if(RepRecherche!=NULL)
                            {
                                if (RepRecherche->Valeur==valeur)
                                {
                                    printf("%d", RepRecherche->Valeur);
                                }
                                else
                                {
                                    printf("Impossible de trouver la valeur recherch\202e");
                                }
                            }
                            else
                                printf("Impossible de trouver la valeur recherch\202e");
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 8 :	printf("Saisir la valeur du Valeur \205 supprimer : \n");
							scanf("%d",&valeur);
							Racine=SuppValeur(Racine,valeur);
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 9 :	system("del Fic.txt");
							system("cls");
							EnregArbre(Racine,NomFic);
							printf("Arbre enregistr\202\n");
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
				case 10 :	Racine=ChargerArbre(Racine,NomFic);
							printf("Arbre charg\202\n");
							printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAppuyez sur une touche pour retourner au menu principal");
							getch();
							break;
			}
		}
		Choix=Menu();
	}
	 return 0;
}