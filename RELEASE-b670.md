# Skaner Studio — wersja na telefon b670 (2026-11-19)

Adres: https://grzepas04-boop.github.io/skaner-iphone-offline/?offline=1&v=670

Poprawki znalezione przy modelowaniu czaszki otwieranej pokrętłem (model testowy całej aplikacji)
- **Połącz** z bryłami i otworami naraz: najpierw dokłada bryły, potem wycina otwory. Wcześniej jeden „Otwór” w zaznaczeniu sprawiał, że dokładane bryły (osie, uszy zawiasu) znikały zamiast się dołączyć.
- **Cofnij** po „Połącz” przywraca części razem z rolą „Otwór” (wcześniej otwory wracały jako zwykłe bryły).
- **Lasso**: obrys zaczęty w pustym miejscu obok bryły już jej nie odznacza — cięcie (Przytnij, Zostaw, Podziel) działa od pierwszego kliknięcia.
- **Forma z kul**: skóra zawsze wychodzi szczelna, także przy kulach przechodzących blisko siebie (np. żuchwa przy policzku); zbyt duża rozdzielczość nie kończy się błędem, tylko lekko rzadszą siatką.
- **Kopia odzyskiwania** działa także dla dużych projektów (ponad 130 MB — np. rzeźba z grupami); wcześniej przestawała się zapisywać.
- Sprawdzanie części wspólnej dwóch brył, które tylko się stykają (np. pokrywa na podstawie), mówi wprost „nie mają wspólnej objętości” zamiast błędu silnika.

Sprawdzone: czaszka z mechanizmem (pokrętło → koła 18/30 → sektor 36 na osi zawiasu) zbudowana w samym programie: forma z kul, oczodoły, nos, płaska podstawa lassem, wydrążenie, podział pokrywy, para kół i dopasowane trzecie koło, osie, zawias, połączenia — pokrywa otwiera się o 70° bez kolizji (sprawdzone częścią wspólną brył).
