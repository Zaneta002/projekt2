# Wtyczka do QGIS - PyQGIS
Wtyczka gotowa do użycia w programie QGIS oferuje dwie funkcjonalności. Pozwala obliczyć różnicę wysokości między dwoma 
wybranymi punktami oraz pole powierzchni na podstawie współrzędnych minimum trzech wybranych punktów. Do obliczeń 
wykorzystuje metodę Gaussa.

## Wymagania konieczne do prawidłowego działania wtyczki 
System operacyjny i programy:
* system operacyjny Windows 10 
* QGIS 3.22.3

Sposób sformatowana i przekazania danych:
* Aby użyć wtyczki, musisz dostarczyć warstwę wektorową, która zawiera odpowiednie atrybuty wymagane przez kod wtyczki. 
* Może to być warstwa punktowa, liniowa lub poligonowa. 
* Warstwa musi mieć atrybuty "X", "Y", "Z" i "Nr" dla funkcji roznica_wys, lub atrybuty "X", "Y" i "Nr" dla funkcji pole.
* Dane powinny być rozdzielone kropką oraz mieć dokładność minimum 3 miejsc po przecinku

## Działanie wtyczki
Na początku należy zainstalować wtyczkę w programie QGIS oraz zaimportować dane z tabeli atrybutów.

**1. Różnica wysokości** 

W celu obliczenia różnicy wysokości należy:
* wybrać dwa dowolne punkty na jednej warstwie
* otworzyć pobraną wtyczkę
* z rozwijanej listy wybrać aktywną warstwę 
* wybrać przycisk "Różnica wysokości"

Wówczas otrzymujemy wynik obliczeń różnicy wysokości z dokładnością do trzech miejsc po przecinku. 

**2. Pole powierzchni**

W celu obliczenia pola powierzchni należy:
* wybrać przynajmniej trzy dowolne punkty na jednej warstwie
* otworzyć pobraną wtyczkę
* z rozwijanej listy wybrać aktywną warstwę 
* wybrać przycisk "Pole powierzchni"

Wówczas otrzymujemy wynik obliczeń pola powierzchni z dokładnością do trzech miejsc po przecinku. 

## Znane błędy
Jeśli użytkownik poda złą ilość punktów, to program zwróci wiadomość o błędzie: `Nieodpowiednia ilość punktów`
