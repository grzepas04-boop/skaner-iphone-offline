# b113 — wspólna bryła z wielu rzutów

Tryb Rysuj 3D → Wieloosiowo zapisuje kolejne obrysy po zakończeniu gestu. Można obracać widok i dodawać następne rzuty. Zamknij bryłę tworzy jeden obiekt, a kolejne edycje rzutów aktualizują ten sam obiekt. Szkice i ustawienia są zachowywane w projekcie oraz historii.

Obliczenia działają w lokalnym workerze na wspólnym polu objętości, z kontrolą zgodności wszystkich aktywnych rzutów podczas wygładzania. Dostępne są wagi, tolerancje, głębokość pojedynczego widoku, równoległe przekroje oraz jawne detale i otwory. Sprzeczne rzuty mogą dać oznaczony kompromis; źródła nie są usuwane przy nieudanej operacji.

Ograniczenia: skończona rozdzielczość siatki, błędy zgodności są próbkowane, przekroje muszą być równoległe. To model siatkowy, nie dokładny CAD BRep. Nie gwarantuje rekonstrukcji dowolnych sprzecznych szkiców ani zachowania późniejszych ręcznych deformacji przy przebudowie ze źródeł.

Weryfikacja: testy geometrii jednego, dwóch i trzech rzutów, kolejności widoków, przekrojów, otworu i kompromisu; testy UI zapisu jednego obiektu i ponownej edycji; testy historii dokumentu, transformacji grupowych i ochrony tylnej powierzchni pędzla; TypeScript, build oraz kompletność zasobów offline. Bez testu na fizycznym iPhonie.
