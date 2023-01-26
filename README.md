# CATcovery  
Web app to better discover your cat origin using neural networks and streamlit
  
by: Dominik Misior, Maciej Ołdakowski
  
Description:
You can predict your cat race and get the probability of it, based on a photo. 
What is more you can add a cat name and age. Based on that in the future you will be able to get to know your cat better.

To run:

1. pip install -r requirements.txt
2. streamlit run main.py

Roadmap:
1. A network that recognizes the breed of the cat and the environment for that - Done. 
2. Fix the fact that the photo disappears, when typing the name of the cat or changing its age - Done. 
3. Add name generator, add button to generate name, left text_input for manual entry - Done.
4. Recognizing a cat's coat color
5. Giving a list of information about this cat race
6. Adding it all to the downloaded image
7. Adding life expectancy based on age and race
8. Adding Polish characters in names (warning that they cannot be typed)
9. Adding a network that detects eye color

Potential the (app is using one of this) cat-breeds-classifiers:
- https://github.com/batogov/cat-breeds-classifier
- https://github.com/tinalulu1327/Cat_Recognition
- https://github.com/samarjit98/Cat-Breeds
