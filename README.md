# pi-estimator

Projet estimation de Py : Spark constext vs Numpy réalisé par Charlotte Milano et Lisa Grandjean 

Pour lancer le programme : se placer dans le bon répertoire et taper en commande :  spark-submit --master local --deploy-mode client projet_py.py

Les résultats obtenus sont les suivants : 




| n = 100 000   |     spark       |      numpy    |
| :------------ |:---------------:| --------------|
| Temps (s)     |    1.63         |   0.04        |
| valeur de pi  |    3.1404       |   3.1271      |
|ecart % Math.pi|    0.0011       |   0.0145      |

D'après le tableau précédent, on remarque que la méthode numpy s'effectue plus rapidement mais elle est moins précise que la méthode Spark. En effet, l'erreur pour la méthode spark est d'environ 0.0011 en comparant avec la vraie valeur de pi tandis que pour numpy elle est plus grande (environ 0.0145). 

Que se passe t-il avec n = 1 000 000 ? 

| n = 1 000 000 |     spark       |      numpy    |
| :------------ |:---------------:| --------------|
| Temps (s)     | 2.1789          |   0.4         |
| valeur de pi  | 3.14084         | 3.140312      |
|ecart % Math.pi|  0.00075        | 0.001         |

On remarque une fois encore que la version spark est bien plus pécrise que la version numpy. 
