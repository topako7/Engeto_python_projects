Vyber si projekt

Co ti vyhovuje víc

Máš na výběr za dvou projektů, které jsme pro tebe připravili. Na všech si otestuješ své schopnosti a to, co jsme se v tomto kurzu naučili. Vyber si ten, který se ti zamlouvá nejvíc:

Bull & Cows - hra postavená na hádání 4 ciferného čísla
Tic-tac-toe - na hracím poli 3x3 umístǔjí dva hráči střídavě X a O
Každý projekt je jiný. Samozřejmě ti nebudeme bránit, pokud budeš chtít vyzkoušet oba projekty, právě naopak! Podrobné zadání obou úloh najdeš níže na této stránce. Hodně štěstí!


Varinta 1:

Bulls & Cows

Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.

Program musí splňovat tyto požadavky:
Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import ...

program pozdraví užitele a vypíše úvodní text,
program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky,
program vyhodnotí tip uživatele,
program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows),
zápis organizovaný do krátkých a přehledných funkcí.

Úvodní text:

Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------


Příklad hry s číslem 2017:

Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's {amazing, average, not so good, ...}
Program toho může umět víc. Můžeš přidat například:

počítání času, za jak dlouho uživatel uhádne tajné číslo
uchovávat statistiky počtu odhadů jednotlivých her



Varinata 2

Tic-tac-toe

Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. Jde o hru pro dva hráče (příp. počítač).

Program musí splňovat tyto požadavky:
Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import ...
program pozdraví uživatele,
vypíše v krátkosti pravidla hry,
zobrazí hrací plochu,
vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene,
pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní,
pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní,
pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy,
program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří,
pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu,
zápis organizovaný do krátkých a přehledných funkcí.
Úvodní text:

Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game

Příklad fungujícího kódu:

Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
--------------------------------------------
+---+---+---+
| | | |
+---+---+---+
| | | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player o | Please enter your move number: 5
============================================
+---+---+---+
| | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player x | Please enter your move number: 1
============================================
+---+---+---+
| X | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player x | Please enter your move number:
...
============================================
Player o | Please enter your move number:
============================================
+---+---+---+
| X | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Congratulations, the player o WON!
============================================