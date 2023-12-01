# Text_Generation_For_Short_Stories
 Tensorflow and NLP

The dataset, amalgamated from various sources, serves exclusively for educational or research purposes, emphasizing the non-commercial nature of the project.

This Python script uses the TensorFlow framework for the training of the language model using a compilation of short stories obtained from diverse datasets. The process involves reading the content from the 'short_stories.txt' file, tokenizing the text, and preparing sequences for training. The script meticulously defines a neural network model with embedding and LSTM layers. Subsequently, the model is compiled and trained using the Adam optimizer on the input sequences.

After the completion of training, the model generates text that adheres to grammatical correctness but may lack coherent meaning. Notably, it is observed that approximately 35% of the dataset comprises horror stories, potentially influencing the model's inclination towards generating similar narratives.

The script employs the Gradio library to craft an interface for generating text based on user input. This interface enables users to input a seed text, prompting the model to produce a continuation of the narrative.



https://www.kaggle.com/datasets/linkanjarad/four-sentence-stories-for-text-generation/data?select=stories.csv 
The shoutout from the kaggle dataset.
This subreddit wouldn't be what it is today if it wasn't for the talented writers who have taken time to contribute their unique and interesting stories. I would like to give a special shout out to those creative writers (some have contributed several stories):

u/zsirdagadek  \~  u/LostInThoughtland  \~  u/AvidTendril  \~  u/10percentSinTax  \~  u/MintyPunch u/Realistic_Watch6090  \~   u/KorimLiDano  \~  u/Super_Snakes  \~  u/Ambitious-Meringue14  \~ u/Pupper-Gump


The second source of the stories is from https://fiftywordstories.com/
The writers are Soumya Doralli, Khop, Margie Nairn, Callachan McNulty, Cindy Harum, Rachel Canwell, Cheryl Snell, Fiona H Evans, Charles Gray, Steve Saulsbury, Nelly Shulman, Sam Brown, Carol Reeves, Phyllis Rittner, Michael Theroux, Jennifer Smith, Meg Pokrass, Stephen Tilden, Alastair Millar, Mari Phillips, Rina Palumbo and Anthony Ceschini.

The third source is from https://lithub.com/20-spooky-short-stories-you-can-read-for-free-online/ by Emily Temple and the writers to the story are Ray Bradbury, Karen Russell, Angela Carter, Silvia Moreno-Garcia, John Langan, Richard Matheson, Harlan Ellison, Shirley Jackson, Laird Barron, Carmen Maria Machado, Brian Evenson, Octavia Butler, Kelly Link, Robert Coover, Nalo Hopkinson, Nathaniel Hawthorne, Mariana Enríquez, tr. Megan McDowell, Joyce Carol Oates, Samanta Schweblin, tr. Megan McDowell and Tananarive Due.







