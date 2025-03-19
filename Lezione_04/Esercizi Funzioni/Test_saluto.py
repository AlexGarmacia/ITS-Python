#import modulo importa tutto il saluto
import Saluto #richiama un file

Saluto.greet("Alex")

import Saluto as s #soprannome al modulo importato
s.greet("Eleonora")


'''Se voglio importare la funzione greet dal modulo saluto
ed ignorare il resto del moulo farò: '''
from Saluto import greet
greet ("Daniele")

from Saluto import greet as g
g("Federico")


