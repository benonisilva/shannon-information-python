# Lib responsavel pelos graficos http://python-nvd3.readthedocs.io/en/latest/introduction.html#overview
from nvd3 import multiBarChart
from string import ascii_lowercase
from collections import Counter
import math

# Retorna um contador para cada arquivo de texto passado ver:. from collections import Counter
# https://pymotw.com/2/collections/counter.html
def count_letters_in_file(path):
    with open(path) as f:
        counter = Counter(letter for line in f 
            for letter in line.lower() 
                if letter in ascii_lowercase)
    return counter
# Retorna a distribuicao de todas as letras. para cada letra  letra/total de letras
def array_of_distribution_letters(counter):
    data = []
    sum_all_letters = sum(counter.itervalues())
    for letter in ascii_lowercase:
        freq = counter[letter]/float(sum_all_letters)
        data.append(information_per_simbol(freq))
        #print '%s : %f' % ( letter, counter[letter]/float(sum_all_letters) )
    return data

# https://plus.maths.org/MI/56c09cb543ec31341504b1627e490cb7/images/img-0008.png
# formula.
def information_per_simbol(data):
    return -data * math.log(data, 2)

# Open File to write the D3 Graph
output_file = open('view.html', 'w')
type = 'Calculo: informacao por simbolo'
chart = multiBarChart( color_category = 'category20c', width=900, height=600, x_axis_format=None)
chart.set_containerheader("\n\n<h2>" + type + "\n\n<img src='https://plus.maths.org/MI/56c09cb543ec31341504b1627e490cb7/images/img-0008.png' /> <br> Baseado na frequencia de ocorrencia cada Letra</h2>\n\n")
# Isso cria o html do grafico

#esses sao os dados - letters in lowecase ascii
xdata = ascii_lowercase
# source http://docente.ifrn.edu.br/paulomartins/livros-classicos-de-literatura/dom-casmurro-de-machado-de-assis.-pdf/at_download/file
# to txt
pt_br = count_letters_in_file('machado_pt-br.txt')
# source https://raw.githubusercontent.com/bbejeck/hadoop-algorithms/master/src/shakespeare.txt
en_us = count_letters_in_file('shakespeare_en-us.txt')
ydata_pt_br = array_of_distribution_letters(pt_br)
ydata_en_us = array_of_distribution_letters(en_us)
# end dados

# coloca os dados no grafico - create visualization
extra_serie = {"tooltip": {"y_start": "", "y_end": " total"}}
chart.add_serie(name="informacao por simbolo. Machado", y=ydata_pt_br, x=xdata, extra=extra_serie)
chart.add_serie(name="informacao por simbolo. Shakeaspear", y=ydata_en_us, x=xdata, extra=extra_serie)
chart.buildhtml()
output_file.write(chart.htmlcontent)
# salva tudo
# close Html file
output_file.close()