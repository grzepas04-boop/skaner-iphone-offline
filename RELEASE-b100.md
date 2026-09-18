# b100 — obrysy wieloosiowe, otwory, telefon

- Wieloosiowe zatwierdzenie nie spłaszcza kolejnych profili do pierwszej płaszczyzny.
- Każdy pełny obrys ma własną normalną; podgląd nie łączy osobnych rzutów.
- Tryb wieloosiowy wybiera główną oś kamery, nie przypadkową ścianę istniejącego modelu.
- Dziura — nowy kontur: zachowuje zewnętrzny obrys i rozpoczyna osobny otwór na tej samej płaszczyźnie. Kolejne naciśnięcia pozwalają dodać następne otwory. Otwory pozostają po zmianie grubości.
- Podgląd płaskiego obrysu uwzględnia wewnętrzne pętle.
- Nagłówek mobilny ma osobny wiersz zakładek i safe-area; Zapisz oraz Panele w górnym wierszu. Eksport jest dostępny w zakładkach. Usunięto mobilne nakładające się przyciski i dużą kostkę orientacji.

## Użycie

Pełna bryła → Wieloosiowo: narysuj pełny obrys z przodu jednym gestem, zmień rzut na BOK, narysuj pełny profil boczny, opcjonalnie kolejny z góry. Zakończ kreskę tworzy wspólną część wyciągniętych obrysów. Profile muszą być wyrównane we wspólnej przestrzeni; nie jest to automatyczna rekonstrukcja dowolnego obiektu ze zdjęć.

Pełna bryła na jednej płaszczyźnie: obrys zewnętrzny → Dziura → kontur wewnętrzny → Utwórz bryłę. Otwór musi leżeć wewnątrz obrysu; tryb otworów nie łączy się jeszcze z wieloosiowym.

## Weryfikacja

Przeszły: geometria pierścienia i przebudowa grubości z otworem; torso przód/bok; trzeci profil; rzeczywista funkcja zatwierdzenia wieloosiowego; dotykowy uchwyt ściany; transformacje grupowe i afiniczne; gesty rzeźbienia; rzeźbienie obrysów, Boolean, pinch/expand; kompilacja; instalacja i zasoby offline (16).

Nie wykonano testu gestów ani układu na fizycznym iPhonie. Połączenie z automatycznym podglądem przeglądarki było niedostępne.
