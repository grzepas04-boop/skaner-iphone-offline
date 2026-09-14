# Skaner Studio — iPhone Offline

Aktualne wydanie: **38** — bezpośrednie chwytanie i wysuwanie wierzchołków, stabilne ciasne łuki prętów przez sumę gładkich kapsuł, dokładny obrys pełnej bryły 1:1 oraz naprawione ekranowe cięcie narzędziem Obszar.

Aktualne wydanie: **release 18**. Bezpośredni adres aplikacji:
`https://grzepas04-boop.github.io/skaner-iphone-offline/release-18/?offline=1`

Wydanie 18 dodaje profesjonalny układ mobilny bez poziomego paska strony,
panel projektu, automatyczne przygotowanie siatki przy pierwszym ruchu dłuta,
adaptacyjną topologię, warstwy rzeźby, stabilne domykanie obrysów, poprawne
płaszczyzny szkicu i pełny eksport OBJ/STL/GLB. Aktualizacja cache 33 dodaje
pełnosiatkowe wygładzanie Loop z podglądem i ochroną ostrych krawędzi,
osobne narzędzia Kopiuj i Lustro X/Y/Z, import OBJ/STL, podświetlanie ścian
i krawędzi pod kursorem, dokładne pełne bryły do 4096 punktów bez wygładzania
ostrych narożników, pręty akceptujące zawracanie o 180° i nakładanie kreski
oraz narzędzie Obszar: ekranowe przecięcie wielu brył na szczelne fragmenty,
które można niezależnie przesuwać, obracać i skalować.
Aktualizacja cache 34 ustawia dla prętów naturalną, gęsto próbkowaną krzywą,
zwiększa okrągły przekrój do 24 segmentów i dodaje widoczne sterowanie
zwężaniem ścian oraz krawędzi. Preset 2% tworzy niemal ostry czubek lub stożek,
natomiast pełne obrysy nadal zachowują dokładne narożniki narysowane przez użytkownika.
Aktualizacja cache 35 dodaje duży, jednoznaczny przełącznik ŚCIANA / KRAWĘDŹ
MIĘDZY ŚCIANKAMI. Na iPhonie krawędź jest chwytana już przy dotknięciu
powierzchni blisko linii, bez konieczności trafiania palcem w cienki piksel.
Aktualizacje cache 36–37 rozdzielają wygląd od topologii: obiekt wygląda gładko,
ale w trybie Ściana / krawędź pokazuje pełną triangulację możliwą do wskazania.
Pręty dostają gęste pierścienie także na prostych odcinkach, a deformacja rozkłada
się na pięciu sąsiednich pierścieniach i automatycznie ogranicza tylko wartość
podglądu, jeśli większa zmiana odwróciłaby trójkąty.
Aktualizacja cache 38 dodaje trzeci tryb edycji WIERZCHOŁEK z podświetleniem
i niebieskim uchwytem ostrego punktu. Pełny obrys nie jest już wygładzany,
natomiast pręt przy ciasnym zagięciu lub nakładaniu odcinków przechodzi przez
stabilną sumę kapsuł. Obszar używa tych samych nazw operacji boolean w wersji
desktopowej i offline, więc prostokąt przecina wszystkie trafione bryły.

Instalowalna aplikacja modelowania 3D działająca lokalnie na iPhonie po pierwszym załadowaniu. Otwórz stronę GitHub Pages w Safari, wybierz **Udostępnij → Dodaj do ekranu początkowego**, a następnie uruchamiaj ją z ikony także bez internetu.

Geometria jest liczona lokalnie przez Manifold WebAssembly. Eksport STL/OBJ korzysta z arkusza udostępniania iOS i opcji **Zachowaj w Plikach**.
