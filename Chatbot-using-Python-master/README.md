Chatbot Using Python: Deep Learning Techniques

This project aims to build a chatbot using deep learning techniques. The chatbot is trained on a dataset containing categories (intents), patterns, and responses. We utilize a special recurrent neural network (LSTM) to classify which category the user's message belongs to and then provide a random response from the list of corresponding responses.

Getting Started
To get the chatbot up and running, follow these steps:

Download all the necessary files.
Open the command prompt or terminal.
Navigate to the folder where the project files are located.
Ensure that your system has the following modules installed: TensorFlow, Keras, NLTK, and Pickle. If not, install them using the following command: pip install <module_name>

Training the Chatbot Model
To train and create the chatbot model, execute the train_chatbot.py file using the following command:
python train_chatbot.py 
If the training is successful, you will see the message "model created".

Running the Chatbot GUI

To open the graphical user interface (GUI) window and start conversing with the chatbot, execute the chatgui.py file using the following command:
python chatgui.py
This will open the GUI window. Write your text in the section to the right of the "Send" button and click "Send" to receive the chatbot's response.
Error Guide

If you encounter an error like ImportError: cannot import name 'tf_utils' while executing the train_chatbot.py file, follow these steps:

Uninstall Keras using the command: pip uninstall keras
Reinstall Keras using the command: pip install keras==2.2.0

After reinstalling Keras, try executing the train_chatbot.py file again. It should work properly.
Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.