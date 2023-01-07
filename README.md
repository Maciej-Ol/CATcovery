# CATcovery
Web app to better discover your cat origin

by: Dominik Misior, Maciej Oldakowski, Gustaw Ignut, Michał Sadownik 

Description:
Predykcja (co aplikacje będzie przewidywać?): Rasę kota, kolor oczu, umaszczenie
Krótkie uzasadnienie funkcjonalności aplikacji: Aplikacja będzie rozpoznawać rasę kota ze zdjęcia i przekierowywać użytkownika na stronę z informacjami na temat tej rasy. 
Model ML (sieci neuronowe czy inny? czy zostanie wytrenowany na potrzeby aplikacji czy ściągnięty?):  Sieci neuronowe. 

Co dodać:
1. Sieć rozpoznawającą rasę kota i otoczkę do tego
2. Naprawić to, że zdjęcie znika, przy wpisaniu imieniu kotu lub zmianie jego wieku
3. Dodanie generatora imion
4. Dodanie sieci wykrywającej kolor oczu
5. Dodanie tego wszystkiego do pobieranego obrazka
6. Dodanie przewidywanej długości życia na podstawie wieku i rasy

To run:

1. pip install requirements.txt
2. streamlit run main.py

Potential cat-breed-classifiers:
- https://github.com/batogov/cat-breeds-classifier
- https://github.com/tinalulu1327/Cat_Recognition
- https://github.com/samarjit98/Cat-Breeds
