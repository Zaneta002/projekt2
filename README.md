# Wtyczka do QGIS - PyQGIS
Wtyczka gotowa do użycia w programie QGIS oferuje dwie funkcjonalności. Pozwala obliczyć różnicę wysokości między dwoma 
wybranymi punktami oraz pole powierzchni na podstawie współrzędnych minimum trzech wybranych punktów. Do obliczeń 
wykorzystuje metodę Gaussa.

## Wymagania konieczne do prawidłowego działania wtyczki 
System operacyjny i programy:
* oprogramowanie Windows 10 
* QGIS 3.22.3

Sposób sformatowana i przekazania danych:
* W celu wykonania obliczeń należy przekazać programowi plik w formacie .csv zawierający współrzędne punktów 
* Kolejność danych w pliku powinna być następująca: Nr  X  Y  Z
* Dane powinny być być rozdzielone kropką oraz mieć dokładność minimum 3 miejsc po przecinku

## Działanie wtyczki
Na początku należy zainstalować wtyczkę w programie QGIS oraz zaimportować warstwę ze współrzędnymi punktów w rozszerzeniu
shp z pliku "przykładowe_dane".

**1. Różnica wysokości** 

W celu obliczenia różnicy wysokości należy:
* wybierać dwa dowolne punkty na jednej warstwie
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
