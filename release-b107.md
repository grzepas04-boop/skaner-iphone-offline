# b107 — uporządkowany interfejs

- Grafitowy/jasny motyw z jednolitą typografią, liniowymi ikonami i spokojnym akcentem.
- Pionowy panel parametrów zamiast szerokiej nakładki nad modelem.
- Menu Projekt; zwijane ustawienia wyświetlania i rzuty kamery.
- Drugorzędne ustawienia w nazwanych sekcjach; instrukcje pod Jak używać.
- Historia, materiał i diagnostyka w zwijanych sekcjach listy obiektów.
- Wyszukiwarka poleceń Ctrl+K, dostępna również w menu mobilnym.
- Układ mobilny: pasek narzędzi na dole, parametry nad nim, osobny panel obiektów.

Geometria i operacje modelowania nie były zmieniane. Przenoszone kontrolki zachowują oryginalne elementy DOM, ID, wartości i zdarzenia.

Weryfikacja: TypeScript, build produkcyjny, testy struktury desktop/mobile w jsdom (identyfikatory, wartości, zdarzenia, menu, wyszukiwanie), regresje rysowania, pędzla na powierzchni i ponownego użycia renderów sceny; 16 plików offline.

Ograniczenie weryfikacji: połączenie podglądu przeglądarki i Edge nie było dostępne. Nie wykonano testu wizualnego na ekranie ani na fizycznym iPhone.
