from pyspark.sql import SparkSession
from pyspark import SparkContext
from time import time
from random import random
from operator import add
from math import pi
import numpy as np


def pi_estimator_numpy(n):
    count = 0
    start = time()
    for i in range(n):
        x, y = random(), random()  #on genere des nb aleatoires
        if x**2 + y**2 < 1:
            count += 1  #on rajoute 1 quand le point est dans le cercle

    end = time()
    estimation_py = (4.0 * count / n)
    print(" ---------------------------------------------------------- ")
    print(end-start, " secondes pour faire le calcul avec Numpy avec n= ", n,)
    print("Pi est environ égal à ", estimation_py)
    erreur =  abs(pi - estimation_py)
    print("L'erreur de l'estimation avec pi est de :", erreur)




def pi_estimator_spark(n):
    
    def is_point_inside_unit_circle(p):
        x, y = random(), random()   #simuler deux points  x et y
        return 1 if x*x + y*y < 1 else 0 #vérifier si ces deux points sont dans la cercle

    start = time() #on calcul le temps 
    count = sc.parallelize(range(0, n)).map(is_point_inside_unit_circle).reduce(add) #on compte le nombre de points dans le cercle à partir d'une rdd
    end = time()
    print(" ---------------------------------------------------------- ")
    print((end-start), "secondes pour faire le calcul en spark avec n=", n)
    estimation_py = (4.0 * count / n)
    print("Pi est environ égal à ", estimation_py)
    erreur =  abs(pi - estimation_py)
    print("L'erreur de l'estimation avec pi est de :", erreur)
    

if __name__=="__main__":


    # --- on ouvre une session Spark --- 
    spark = SparkSession.builder.master('local').appName("projet_py").getOrCreate()
    sc = spark.sparkContext
    n= 1000000
    #pi_estimator_spark(n)
    pi_estimator_numpy(n)
    spark.stop()