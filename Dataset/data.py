from datasets import load_dataset
import pandas as pd
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
data = load_dataset("zefang-liu/phishing-email-dataset")

df = data['train'].to_pandas()

print(df.head())
