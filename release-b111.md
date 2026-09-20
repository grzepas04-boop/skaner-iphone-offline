# b111 — import i otwieranie GLB

Importuj dodaje obiekty GLB do sceny. Otwórz przyjmuje też GLB i zastępuje istniejącą scenę po potwierdzeniu. Wszystkie siatki są walidowane przed zmianą sceny. Zachowane zostają nazwy, światowe transformacje oraz podstawowy kolor, chropowatość i metaliczność pierwszego materiału każdej siatki. Jeden krok Cofnij obejmuje cały import.

Zakres: statyczne GLB 2.0 z zasobami w pliku, do 64 MB, 256 obiektów i 2 mln wierzchołków. Jednostki współrzędnych są zachowywane jako mm, zgodnie z dotychczasowym eksportem Skanera. Tekstury, animacje i wielomateriałowe powierzchnie nie są odtwarzane. Zewnętrzne odnośniki, szkielety i aktywne deformacje są odrzucane. Siatka musi przejść dotychczasową walidację importu brył.

Testy: prawdziwy binarny GLB z dwoma obiektami, zagnieżdżonymi transformacjami, ujemną skalą, kolorami, instancjami; import geometrii do rzeczywistego silnika z potwierdzeniem zamknięcia i dodatniej objętości. TypeScript, build i komplet 16 zasobów offline. Bez testu na fizycznym iPhonie.
