import csv
import pandas as pd

with open('filmes_disney.csv', mode='r', newline='') as arquivo:
    filmes = csv.reader(arquivo)