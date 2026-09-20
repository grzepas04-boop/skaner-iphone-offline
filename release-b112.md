# b112 — Napraw siatkę

Projekt → Napraw siatkę: wybierz obiekt lub plik OBJ/STL/GLB, sprawdź raport i podgląd, następnie Zastosuj albo Anuluj.

Naprawa usuwa powielone i zerowe trójkąty oraz poprawia orientację ścian. Opcjonalne łączenie identycznych współrzędnych jest domyślnie wyłączone. Nie zakleja otworów. STL nie przechowuje indeksowanej topologii, więc wspólne punkty odtwarzane są przy odczycie.

To konserwatywna naprawa, nie pełna przebudowa siatki jak w slicerze. Pozostałe otwarte i niemanifoldowe krawędzie blokują zatwierdzenie. GLB do naprawy może zawierać jeden obiekt; zwykły import GLB nadal obsługuje wiele obiektów.

Sprawdzone: algorytm naprawy, rzeczywisty silnik geometrii, podgląd/anulowanie/zatwierdzenie w testach DOM, import GLB, zamykanie eksportu, routing desktopowy, TypeScript, manifest i service worker offline. Bez testu wizualnego na fizycznym iPhonie.
