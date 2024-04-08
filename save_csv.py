import pandas as pd

def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(f'csv/{filename}.csv', index=False)
    print(f'csv saved as {filename}.csv')

