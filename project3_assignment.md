Zadání projektu
Popis projektu
Závěrečný projekt prověří tvé znalosti nejenom z posledních lekcí, ale z celého kurzu. Tvým úkolem bude vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu.

Napiš takový skript, který vybere jakýkoliv územní celek z tohoto odkazu (https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) Např. X u Benešov odkazuje sem (https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xnumnuts=2101). Z tohoto odkazu chcete vyscrapovat výsledky hlasování pro všechny obce.

Můžeš stahovat výsledky hlasování:

Pomocí odkazů ve sloupci číslo, např. 529303,
pomocí odkazů ve sloupci Výběr okrsku, tedy sloupec se symbolem X.
Je na tobě, který sloupec použiješ, ale dobře si jednotlivé odkazy prohlédni, jestli tě opravdu odkážou na výsledky obce.

Jak postupovat
Na svém počítači si vytvoříte vlastní virtuální prostředí (speciálně pro tento úkol)
Do nově vytvořeného prostředí si přes IDE (nebo příkazový řádek) nainstalujete potřebné knihovny třetích stran
Vygenerujete soubor requirements.txt, který obsahuje soupis všech knihoven a jejich verzí (nevypisovat ručně!)
Výsledný soubor budete spouštět pomocí 2 argumentů (ne pomocí funkce input). První argument obsahuje odkaz, který územní celek chcete scrapovat (př. územní celek Prostějov ), druhý argument obsahuje jméno výstupního souboru (př. vysledky_prostejov.csv)
Pokud uživatel nezadá oba argumenty (ať už nesprávné pořadí, nebo argument, který neobsahuje správný odkaz), program jej upozorní a nepokračuje.
Následně dopište README.md soubor, který uživatele seznámíte se svým projektem. Jak nainstalovat potřebné knihovny ze souboru requirements.txt, jak spustit váš soubor, příp. doplnit ukázku, kde demonstrujete váš kód na konkrétním odkaze s konkrétním výpisem.
Projekt musí splňovat tyto body:
Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit (zejména zaslání zpětné vazby na Discord):

"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import ...

Soubor s programem (..nebo také skript) s příponou .py, který pro správný běh potřebuje 2 argumenty pro spuštění,
soubor se seznamem pouze relevantních knihoven a jejich verzí k projektu (requirements.txt),
stručnou dokumentaci (popis, instalace knihoven, ukázka) (README.md)
soubor s uloženým výstupem (.csv),
zápis organizovaný do krátkých a přehledných funkcí.
Výstup bude obsahovat
Ve výstupu (soubor .csv) každý řádek obsahuje informace pro konkrétní obec. Tedy podobu:

kód obce
název obce
voliči v seznamu
vydané obálky
platné hlasy
kandidující strany (co sloupec, to počet hlasů pro stranu pro všechny strany).
