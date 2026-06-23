import csv
#lectura CSV
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      #La función integrada zip() en Python permite combinar elementos de dos o más objetos iterables 
      # (como listas o tuplas) en un solo iterador de tuplas.
      #  Cada tupla agrupa los elementos que comparten la misma posición en los iterables originales, 
      # deteniéndose al llegar al final del iterable más corto
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data


"""{'Rank': '36', 
'CCA3': 'AFG', 
'Country/Territory': 'Afghanistan', 
'Capital': 'Kabul', 
'Continent': 'Asia', 
'2022 Population': '41128771', 
'2020 Population': '38972230', 
'2015 Population': '33753499', 
'2010 Population': '28189672', 
'2000 Population': '19542982', 
'1990 Population': '10694796', 
'1980 Population': '12486631', 
'1970 Population': '10752971', 
'Area (kmÂ²)': '652230', 
'Density (per kmÂ²)': 
'63.0587', 'Growth Rate': '1.0257', 
'World Population Percentage': '0.52'}"""
if __name__ == '__main__':
  data = read_csv('c:/python Workspace/Curso Python/Comprenhensions_Funciones_manejo_de_errores/Clases/app/data.csv')
  print(data[0])

