import pandas as pd
import re

def clean_text(text):
    """
    Cleans raw text by lowercasing, removing URLs, and stripping punctuation.
    """
    # 1. Convert text to lowercase
    text = text.lower()
    
    # 2. Remove URLs (http/https/www)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # 3. Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def main():
    print("Loading raw datasets...")
    # Adjust the paths if your CSVs are stored inside the 'data/' folder
    fake_df = pd.read_csv('../data/Fake.csv')
    true_df = pd.read_csv('../data/True.csv')

    # Assign labels (1 for Real, 0 for Fake)
    true_df['label'] = 1
    fake_df['label'] = 0

    print("Merging datasets...")
    # Combine both datasets into one main dataframe
    combined_df = pd.concat([true_df, fake_df], ignore_index=True)

    print("Cleaning text data... (This may take a minute or two)")
    # Apply the clean_text function to the 'text' column
    combined_df['cleaned_text'] = combined_df['text'].apply(clean_text)

    # Save the cleaned dataset back to the data folder
    output_path = '../data/cleaned_news_dataset.csv'
    combined_df.to_csv(output_path, index=False)
    
    print(f"Success! Cleaned dataset saved to: {output_path}")
    print(f"Total rows processed: {len(combined_df)}")

if __name__ == "__main__":
    main()Oimport pandas as pd
import re

def clean_text(text):
    """
    Cleans raw text by lowercasing, removing URLs, and stripping punctuation.
    """
    # 1. Convert text to lowercase
    text = text.lower()
    
    # 2. Remove URLs (http/https/www)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # 3. Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def main():
    print("Loading raw datasets...")
    # Adjust the paths if your CSVs are stored inside the 'data/' folder
    fake_df = pd.read_csv('../data/Fake.csv')
    true_df = pd.read_csv('../data/True.csv')

    # Assign labels (1 for Real, 0 for Fake)
    true_df['label'] = 1
    fake_df['label'] = 0

    print("Merging datasets...")
    # Combine both datasets into one main dataframe
    combined_df = pd.concat([true_df, fake_df], ignore_index=True)

    print("Cleaning text data... (This may take a minute or two)")
    # Apply the clean_text function to the 'text' column
    combined_df['cleaned_text'] = combined_df['text'].apply(clean_text)

    # Save the cleaned dataset back to the data folder
    output_path = '../data/cleaned_news_dataset.csv'
    combined_df.to_csv(output_path, index=False)
    
    print(f"Success! Cleaned dataset saved to: {output_path}")
    print(f"Total rows processed: {len(combined_df)}")

if __name__ == "__main__":
    main()
