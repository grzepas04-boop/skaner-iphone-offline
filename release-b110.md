# b110 — zamykanie eksportu

Dodano przycisk × (44 × 44 px) w przyklejonym pasku eksportu. Panel przewija się na małych ekranach. Zamknięcie przywraca poprzednią zakładkę, zachowując aktywne narzędzie i niedokończony rysunek. Escape zamyka eksport bez przekazywania klawisza do anulowania gestu modelowania.

Przeszły testy rzeczywistych handlerów (powrót do każdej zakładki, ponowne otwarcie, fokus, Escape, brak resetowania narzędzia), test struktury interfejsu desktop/mobile, TypeScript, build i kompletność 16 zasobów offline. Bez wizualnego testu na fizycznym iPhonie.
