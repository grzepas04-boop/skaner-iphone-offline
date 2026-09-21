# b114 — poprawka zapisu kolejnych rzutów

Naprawiono błąd wykryty podczas rzeczywistego rysowania głowy węża: podgląd roboczy mógł zachować identyfikator `live-draft`, przez co kolejne rzuty zastępowały pierwszy. Gotowe kształty nie uruchamiają już roboczego podglądu odręcznego, a finalizowany szkic odręczny otrzymuje osobny stały identyfikator.

Dodano test regresji podglądu roboczego oraz ponownie wykonano test wielokrotnych szkiców, TypeScript, build i kontrolę 16 zasobów offline.
