# Skaner Studio — zasady dla Claude

## Wizja produktu (NADRZĘDNA — stosuj przy każdym zadaniu)

**„CAD” to nie jest tryb. Cała aplikacja ma działać jak CAD.**

Cel: jedna aplikacja, w której narzędzia do rzeźbienia i pełne narzędzia CAD
współistnieją i są dostępne wszędzie, bez przełączania się do osobnego „trybu CAD”.

Zasady wynikające z wizji:

1. **Wymiary wszędzie** — każdy obiekt, krawędź, ściana, szkic, otwór, pręt,
   fragment rzeźby może mieć dokładne wymiary (wpis liczbowy, jednostki, wymiar
   klikany/edytowalny po fakcie).
2. **2D → 3D na każdej powierzchni** — rysowanie w 2D (linie, łuki, obrysy,
   profile) na dowolnej płaszczyźnie lub ścianie dowolnej bryły (także rzeźby /
   skanu), a potem wyciąganie, obrót, loft, sweep do 3D.
3. **Operacje CAD stosowalne do wszystkiego** — boolean, fazka, zaokrąglenie,
   offset, pochylenie, szyk, lustro działają na bryłach dokładnych, siatkach
   rzeźby i skanach, a nie tylko na „częściach CAD”.
4. **Rzeźba i CAD mieszają się swobodnie** — można rzeźbić bryłę CAD i nadawać
   precyzyjne wymiary rzeźbie; brak sztywnej granicy „to jest część CAD”.
5. **Łatwy dostęp** — narzędzia CAD w głównym przepływie (pasek, menu
   kontekstowe, wyszukiwarka), nie schowane w osobnej zakładce/kategorii.

### Stan obecny vs cel (b664)

Bundle `assets/index-*.js` nadal ma osobny tryb/kategorię `cad`
(`{id:'cad',name:'CAD'}`, menu `m-cad`, `#cad-inspector`, narzędzia `cad-*`
z `requirement:'part'|'sketch'`). To **dług względem wizji** — przy każdej
zmianie dotyczącej tych obszarów kieruj się ku:

- rozpuszczeniu kategorii `CAD` w ogólnych kategoriach (Szkic / Bryły / Rzeźba),
- zdjęciu ograniczeń `requirement:'part'` tam, gdzie operacja ma sens na siatce,
- inspektorowi wymiarów/historii dostępnemu dla każdego zaznaczenia.

Nie nazywaj nowych funkcji „trybem CAD”; w UI i release notes opisuj je jako
narzędzia ogólne.

## Konwencje repo

- Język UI, commitów i release notes: polski.
- Każde wydanie: `RELEASE-bNNN.md` + commit `Skaner Studio bNNN: …`.
- Aplikacja offline (PWA): zmiany assetów wymagają aktualizacji
  `service-worker.js` / `offline-assets.json`.
