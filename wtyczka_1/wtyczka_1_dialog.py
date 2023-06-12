# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka1Dialog
                                 A QGIS plugin
 Wtyczka oblicza przewyższenie i pole powierzchni.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-12
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Żaneta Janiszek
        email                : zanetajaniszek2@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface 
import numpy as np

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_1_dialog_base.ui'))


class wtyczka1Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(wtyczka1Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_roznicawys.clicked.connect(self.roznica_wys)
        self.pushButton_polepow.clicked.connect(self.pole)

    def roznica_wys(self):
        wybrana_warstwa = self.mMapLayerComboBox_warstwa.currentLayer()
        liczba_punktow = len(wybrana_warstwa.selectedFeatures())
    
        if liczba_punktow == 2:
            punkty = wybrana_warstwa.selectedFeatures()
            wysokosci = []
            numery = []
        
            for punkt in punkty:
                numer = punkt["Nr"]
                wysokosc = float(punkt["Z"])
                wysokosci.append(wysokosc)
                numery.append(numer)
        
            przewyzszenie = wysokosci[1] - wysokosci[0]
            self.label_wynik.setText(f'Różnica wysokosci między punktami:\n {numery[0]} i {numery[1]} wynosi\n {przewyzszenie:.3f} m')
        else:
            self.label_wynik.setText('Błąd: Niewłaściwa liczba punktów.')

    def pole(self):
        wybrana_warstwa = self.mMapLayerComboBox_warstwa.currentLayer()
        liczba_punktow = wybrana_warstwa.featureCount()
    
        if liczba_punktow >= 3:
            punkty = wybrana_warstwa.selectedFeatures()
        
            if len(punkty) >= 3:
                numery = []
                wspolrzedne = []
            
                for punkt in punkty:
                    numer = punkt["Nr"]
                    x = float(punkt["X"])
                    y = float(punkt["Y"])
                    wspolrzedne.append((x, y))
                    numery.append(numer)
            
                wspolrzedne = np.array(wspolrzedne)
                X = wspolrzedne[:, 0]
                Y = wspolrzedne[:, 1]
                posortowane = sorted(zip(X, Y), key=lambda punkt: punkt[0])
                X, Y = zip(*posortowane)
            
                if Y[-2] > Y[-1]:
                    X = list(X)[::-1]
                    Y = list(Y)[::-1]
            
                pole = 0.5 * np.abs(np.dot(X, np.roll(Y, 1)) - np.dot(Y, np.roll(X, 1)))
                numery_punktow = ' '.join(str(nr) for nr in numery)
                self.label_wynik.setText(f'Pole powierzchni między punktami\n {numery_punktow} wynosi:\n {pole:.3f} m^2')
            else:
                self.label_wynik.setText('Błąd: Nie wybrano wystarczającej liczby punktów.')
