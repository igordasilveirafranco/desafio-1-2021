import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import time
import multiprocessing


# 1a versao

# def heavy(n, myid):
#     for x in range(1, n):
#         for y in range(1, n):
#             x**y
#     print(myid, "is done")


# def multiproc(n):
#     processes = []
#     for i in range(n):
#         p = multiprocessing.Process(target=heavy, args=(500, i,))
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()


# if __name__ == "__main__":
#     start = time.time()
#     multiproc(80)
#     end = time.time()
#     print("Took: ", end - start)


# 2a versao - melhor

# A CPU heavy calculation, just
# as an example. This can be
# anything you like

# Referencia https://python.land/python-concurrency/python-multiprocessing

def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
            # print(x,y)
    print(myid, "is done")


def doit(n):
    heavy(500, n)


def pooled(n):
    # By default, our pool will have
    # numproc slots
    # Se quiser setar o numero de threads, colocar dentro de Pool, senao deixar Pool() somente
    with multiprocessing.Pool(10) as pool:
        #    pool = Pool(4)
        pool.map(doit, range(n))


if __name__ == "__main__":
    start = time.time()
    pooled(80)
    end = time.time()
    print("Took: ", end - start)

# Resultados de diferentes configuracoes de Pool() com AMD Ryzen 2700:
# Pool(1) - tempo: 38seg
# Pool(2) - tempo: 20seg
# Pool(4) - tempo: 11seg
# Pool(8) - tempo: 8seg
# Pool(12) - tempo: 7.7seg
# Pool(16) - tempo: 7.7seg
# Pool(25) - tempo: 9.5seg
# Pool(32) - tempo: 11.5seg
# Pool() - tempo: 7.7seg
# Pool(11) - tempo: 7.5seg
# Pool(10) - tempo: 7.49seg (melhor)
# Pool(9) - tempo: 7.7seg
