# b103 — elipsy, wyciąganie szkiców i dokładne transformacje

- Elipsa 2D 125 × 40 mm: niezależne osie, płaski podgląd i zapis szkicu; elipsoida 3D zachowuje trzy wymiary. Pole wymiaru włącza dokładny rozmiar.
- Kliknij wnętrze szkicu narzędziem Wybierz lub wybierz szkic z listy i użyj „Przeciągnij szkic w bryłę”. Niebieska strzałka pokazuje wyciągnięcie, puszczenie tworzy bryłę. Grubość dodatnia lub ujemna; otwory zachowane.
- Podczas rysowania bryły można pisać wymiar: Tab przełącza X/Y/Z, Enter tworzy bryłę. Na telefonie pozostają pola wymiarów.
- Pola przesunięcia i obrotu mają krok 0,01 oraz zatwierdzanie Enterem. Liczbowe transformacje grup używają wspólnego środka.
- Wybór ostrych krawędzi pomija przekątne płaskich trójkątów; podgląd edycji ściany porusza także współdzielone kopie wierzchołków renderowania.

Testy: TypeScript, elipsa 125×40 (podgląd i zapis), dodatnie/ujemne wyciąganie z otworem, 12 krawędzi bloku, zaznaczanie pełnych ścian, rzeczywista ścieżka transformacji liczbowej 0,01 mm i obrotu grupy 90°, dotyk, skalowanie równomierne, rzeźbienie, kontury, import/eksport i offline.

Pozostaje do wdrożenia: trwały semantyczny podział zakrzywionych prętów na cztery boki i dwa końce, pełne więzy/dopasowanie powierzchni CAD. To nie jest jeszcze odpowiednik funkcjonalny Shapr3D ani Nomad. Bez weryfikacji interfejsu na fizycznym iPhonie.
