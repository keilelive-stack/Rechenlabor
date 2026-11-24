# CIQ Operator-Rechenlabor v1.0 · Etappe 19

## Start
`index.html` lokal in einem JavaScript-fähigen Browser öffnen. Kein Server, keine Installation, keine Netzverbindung nötig. Alle Module starten mit vorgegebenen Demonstrationsdaten. Auf **Alle Module berechnen** klicken oder die Eingaben eines Moduls ändern und dessen Rechenknopf benutzen. **JSON exportieren** speichert den zuletzt berechneten Stand einschließlich Eingaben. Nach Änderungen erneut rechnen, bevor exportiert wird.

## Reihenfolge und Rechenvertrag
1. IR und Konstanten: feste 10-µm-Referenz; K_IR = λB/λA = fA/fB = TB/TA = NB/NA. Laborlinie und Empfangslinie in Vakuum. Frequenz- und Energieverschiebung, Doppler, Lorentzfaktor, getrennte Schwarzschild-Inversion.
2. Phase: 3 orthogonale Basen von 4 Empfängern, Δφ in rad, k = Δφ/b. Wellenlänge und Richtung, Position erst mit unabhängiger Tiefe. Messmodus braucht unabhängig bekannte λmin, Basis < λmin/2. Synthetischer Modus ist keine Beobachtung.
3. TOV: für die historische NS-EOS die Zentraldichte eingeben oder das erste Massenmaximum suchen. Der Browser berechnet die dimensionslosen TOV-Gleichungen mit RK4 und linearer Oberflächeninterpolation, nicht mit einer gespeicherten Massentabelle. Zeitmetrik über barotrope Enthalpie; gleiche EOS, Randbedingung und SI-Konstanten wie im Anschluss 18. Mit Oberfläche → IR + 3D wird K synthetisch an die nächsten Module übergeben (keine reale Zentrums-IR-Linie). Für hochpräzise Zahlen den mitgelieferten adaptiven Python-Solver benutzen.
4. Galaktische TOV-Linse: Newton-Massenskala und Newton-Radius des n=1-Polytrops, schwaches Feld (Kompaktheit ≤ 10⁻⁴); W und α sowie finite Differenz -dW/db. Metrik → IR + 3D übergibt den Frequenzquotienten. Kein Fit an SPARC.
5. Wärme, FLRW, Rotation: Stefan-Boltzmann/Wien, Schwarzkörper-Entropiedichte, Hubble- und Teilchenhorizont, flache ΛCDM-Referenz, RAR aus einem eingegebenen Radiuspunkt. Dichten, Emissivität, H0, Ω und a0 sind Eingaben. Die vollständige SPARC-Stichprobe und ihre Originalsimulation sind separat im Paket erhalten.
6. Ising/XY: deterministisches 32×32 Gitter, 100 Sweeps je Klick, periodische Grenzen, Reset für Reproduzierbarkeit. Die Kopplung an reale Gravitation bleibt offen; η=0. Dieses vereinfachte Browser-Modul ersetzt die historische Suite nicht.
7. Alle Selbsttests; JSON exportieren. Das Modul prüft interne Konsistenz, nicht unabhängige empirische Bestätigung. Die historischen Etappen und deren Prüfprogramme sind im ZIP separat erhalten.

## Konstanten: Herkunft beachten
- SI-Definitionen c, h, kB und e; empirischer Referenzwert G = 6.67430e-11 SI. G ist nicht exakt definiert. Aus diesen Eingaben werden ħ, ℓP, tP, mP, EP, Stefan-Boltzmann-Konstante und Wien-Konstante berechnet. Die dimensionslose Vergleichsgröße Ncrit = √(4π) ist keine nachgewiesene physikalische Stabilitätsgrenze.
- c aus unabhängig eingegebenem λ und T bzw. f; h aus unabhängig eingegebener Energie und Frequenz (Energie in eV, Umrechnung über SI-e). Diese Rückrechnungen sind keine unabhängigen Messungen, wenn die Eingaben selbst aus c/h berechnet wurden.
- G aus Kgrav, zwei Radien und unabhängiger Masse. Ohne bekannte Masse nur GM. Schwarzschild-Geometrie, statische Beobachter und getrennte Verschiebungsursachen müssen bestätigt sein. Der Rechner überprüft die Herkunft und Unsicherheiten von Eingaben nicht. Keine scheinbare Messgenauigkeit aus synthetischen Daten ableiten.
- Die Schaltfläche Synthetische G-Kontrolle erzeugt K mit Referenz-G, um den Inversionsweg zu testen. Sie beweist G nicht. Die Planck-Rückrechnung G = c³ℓP²/ħ ist ebenfalls zirkulär, falls ℓP aus G stammt. TOV und FLRW verwenden Referenz-G, nicht das Ergebnis einer optionalen Messinversion.

## Umfang
Das HTML ist eine neue integrierte, begrenzte Referenzanwendung. Nicht alle historischen Teilversuche (z. B. vollständige Hadron-, Regge-, Baryogenese- und 0-K-Modelle) sind in der Browseroberfläche neu implementiert; sie bleiben in den Originalarchiven 01–17. Kein vollständiger Ising-v7.7/RH-Solver. Keine dynamische Kollapsrechnung, keine reale Kernmaterie-EOS, kein abgeleiteter Ising-Energie-Impuls-Tensor, keine unabhängige Herleitung aller Naturkonstanten. Die Browser-EOS-Koeffizienten sind keine gemessenen Entropiewerte. S_BH ist ein hypothetischer Horizontvergleich, keine Sternentropie.

## Hochpräzise Wiederholung (Paketversion)
Im Unterordner `Quellen` sind das nummerierte Operator-ZIP 01–17, der Prüflauf, das Rechen-Startpaket und Anschluss 18 unverändert enthalten. Entpacke das Startpaket und befolge dort README_START_HIER.md; entpacke Anschluss 18 und führe dessen dokumentierte Python-Befehle aus. SciPy-Referenzwerte sind genauer als die Browser-Vorschau. Die ursprüngliche 3D-/SPARC-Offline-Anwendung liegt unter `Historisches_Cross_Labor.html` bei. Der Rechenbericht in `TESTPROTOKOLL.txt` beschreibt den aktuellen Lauf, die alten Prüfberichte beschreiben frühere Läufe.

GitHub: eigener Zweig `ciq/operator-rechenlabor-v1` im Repository `keilelive-stack/Physik`, `CIQ-Rechenlabor/index.html`. Hauptzweig unverändert. Die historischen ZIPs sind nur im lokalen Paket, nicht auf GitHub veröffentlicht.
