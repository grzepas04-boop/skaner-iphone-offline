# b109 — łuk i ochrona tylnej strony podczas rzeźbienia

- Łuk: pierwszy gest wyznacza końce, drugi ustawia wygięcie. Mysz zatwierdza kliknięciem; dotyk — puszczeniem drugiego gestu. Bez osobnego przycisku zatwierdzania łuku.
- Lokalny podgląd pędzla na dużych płaskich ścianach i poprawka zatrzymywania długiego gestu po 512 próbkach.
- Ochrona przeciwległej powierzchni w pędzlach budowania. Wypychanie podąża za normalną powierzchni, glina stosuje szerszy płaski profil w kierunku pędzla. Wspólne obliczenia podglądu i silnika.

Testy silnika obejmują powtarzane pociągnięcia inflate/clay po obu stronach ścianki 2 mm: przeciwległa ściana pozostaje nieruchoma, objętość wzrasta i siatka pozostaje zamknięta. Przeszły także regresje rysowanych brył, pozostałych pędzli, boolean, transformacji pędzla oraz OBJ/STL. Zweryfikowano kompilację i kompletność 16 zasobów offline.

Nie przeprowadzono testu wizualnego na fizycznym iPhonie ani na konkretnym modelu użytkownika. Ochrona orientacji nie zastępuje pełnego testu widoczności wielowarstwowych powierzchni. Wcześniejsze deformacje zapisane w modelach nie są automatycznie cofane.
