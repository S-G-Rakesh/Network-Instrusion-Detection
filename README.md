🛡️ Network Intrusion Detection System
Overview
This project is a Network Intrusion Detection System (NIDS) built using machine learning to identify and classify various types of network traffic, including potential security threats. The system leverages a Random Forest Classifier trained on network traffic data to detect anomalies and attacks, ensuring robust and efficient monitoring of network security.

🚀 Features
Real-Time Network Traffic Analysis: Detect potential threats in live network traffic.
Interactive Web Application: A sleek and intuitive user interface built using Streamlit.
Customizable Inputs: Users can input network traffic parameters and get instant classification results.
Visual Results: Displays the type of traffic detected (e.g., Legitimate, DDoS, Protocol Exploitation) with appropriate action recommendations.
📂 Project Structure
bash
Copy code
📦 Network-Intrusion-Detection
├── App.py                          # Streamlit application script
├── Network_Intrusion_Detection.pkl # Machine Learning model (Random Forest Classifier)
├── Network_Intrusion_Detection_Dataset.csv # Dataset used for training and testing
├── logo.webp                       # Project logo
├── requirements.txt                # Python dependencies
└── README.md                       # Project description
🛠️ Tools and Technologies
Python: Programming language used for developing the backend logic.
Random Forest Classifier: Machine learning algorithm for intrusion detection.
Streamlit: Framework for building the web interface.
Pandas and NumPy: For data manipulation and preprocessing.
Matplotlib and Seaborn: For visualizations during model analysis.
Joblib: For saving and loading the trained model.
📊 Dataset
The dataset used for this project contains several network traffic parameters, such as:

Port Number
Received Packets
Sent Packets
Active Flow Entries
Packets Looked Up
Packets Matched
This dataset was preprocessed to remove null values, normalize features, and balance the classes for better training.

🧠 Machine Learning Model
The system uses a Random Forest Classifier, a robust and reliable ensemble learning method, trained on the preprocessed dataset. The model achieved high accuracy in detecting network intrusions, distinguishing between legitimate traffic and various attack types such as:

DDoS Attacks
Protocol Exploitation
Reconnaissance
Traffic Manipulation
Buffer Overflow
💻 How to Run the Project
Prerequisites
Install Python (>= 3.8).
Clone the repository:
bash
Copy code
git clone https://github.com/your_username/network-intrusion-detection.git
cd network-intrusion-detection
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Running the Application
Ensure the dataset (Network_Intrusion_Detection_Dataset.csv) and model (Network_Intrusion_Detection.pkl) are in the project directory.
Run the Streamlit app:
bash
Copy code
streamlit run App.py
Open your browser and go to http://localhost:8501 to interact with the application.
🎨 User Interface
Input Page: Users enter network traffic parameters and submit for classification.
Output Page: Displays the classification result with a summary of the detected traffic type and recommended actions.
👥 Contributors
Abimanyu K A - 23BCE1423
Rakesh S G - 23BAI1181
Yokesh Balaji B - 23BCE1027
📚 References
Enhancing Network Threat Detection with Random Forest-Based NIDS
Random-Forests-Based Network Intrusion Detection Systems
Intrusion Detection System Combined Enhanced Random Forest with SMOTE Algorithm
