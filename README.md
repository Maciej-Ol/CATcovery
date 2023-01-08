# CATcovery  
Web app to better discover your cat origin  
  
by: Dominik Misior, Maciej Oldakowski, Gustaw Ignut, Michał Sadownik   
  
Description:
Predykcja (co aplikacje będzie przewidywać?): Rasę kota, kolor oczu, umaszczenie  
Krótkie uzasadnienie funkcjonalności aplikacji: Aplikacja będzie rozpoznawać rasę kota ze zdjęcia i przekierowywać użytkownika na stronę z informacjami na temat tej rasy.   
Model ML (sieci neuronowe czy inny? czy zostanie wytrenowany na potrzeby aplikacji czy ściągnięty?):  Sieci neuronowe, wytrenowane za pomocą:   
https://colab.research.google.com/drive/1pb7sc8zzobUy3jb51aI8IT8qdlwOzu9k?usp=sharing  
https://drive.google.com/drive/folders/1tNFLzgAkrcUNoE_UxpEEbTxQwWlRzgGa?usp=sharing  

Co dodane:
1. Sieć rozpoznawającą rasę kota i otoczkę do tego - Zrobione  
2. Naprawić to, że zdjęcie znika, przy wpisaniu imieniu kotu lub zmianie jego wieku - Zrobione 
3. Dodanie generatora imion - Zrobione, dodano przycisk do generowania imienia, zostawiono text_input do ręcznego wpisania
Jak w przyszłości można rozwinąć:
4. Dodanie sieci wykrywającej kolor oczu
5. Dodanie tego wszystkiego do pobieranego obrazka
6. Dodanie przewidywanej długości życia na podstawie wieku i rasy
7. Dodanie Polskich znaków w imionach (ostrzeganie, że nie można ich wykrywać przy wpisaniu)

To run:

1. pip install -r requirements.txt
2. streamlit run main.py

Potential cat-breed-classifiers:
- https://github.com/batogov/cat-breeds-classifier
- https://github.com/tinalulu1327/Cat_Recognition
- https://github.com/samarjit98/Cat-Breeds
