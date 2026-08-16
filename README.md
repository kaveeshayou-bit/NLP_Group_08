# TruthGuard — Automated Fake News Detection

## 👥 Group Members & Contributions
*   **CIT-24-01-0330:** Kaveesha (Team Leader) — Data Preprocessing, Naive Bayes, TextCNN, Web Application
*   **CIT-24-01-0393:** Sehath — Logistic Regression, LSTM
*   **CIT-24-01-0064:** Nevith — Random Forest, DistilBERT

## 🚨 Problem Statement
The rapid spread of fabricated news on digital platforms threatens public trust and democratic systems. Manual fact-checking is impossible given the sheer volume of daily articles. This project provides a scalable, automated NLP pipeline capable of analyzing semantic and contextual cues to flag untrustworthy text instantly.

## 📊 Dataset Information
*   **Source:** Fake and Real News Dataset (Kaggle)
*   **Original Size:** 44,898 records
*   **Cleaned Size:** 39,098 records (after deduplication and null-value removal)
*   **Classes:** 0 (Fake News), 1 (Real News)

## 🛠️ Setup Instructions
To set up this project locally on macOS, it is recommended to use an isolated Python 3.10 virtual environment to ensure compatibility with Apple Silicon and TensorFlow.

1. Clone the repository:
   ```bash
   git clone [https://github.com/kaveeshayou-bit/NLP_Group_08.git](https://github.com/kaveeshayou-bit/NLP_Group_08.git)
   cd NLP_Group_08/web_app
