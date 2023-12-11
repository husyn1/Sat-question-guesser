import pandas as pd

def create_answers_dataframe(txt_files):
    data = {}

    for i, txt_file in enumerate(txt_files):
        with open(txt_file, 'r') as file:
            lines = file.readlines()
            answers = [line.strip().split(' ')[1] for line in lines]

            column_name = f"Reading {i+1}"
            data[column_name] = answers

    df = pd.DataFrame(data, index=range(1, len(answers) + 1))
    return df

# Example usage
txt_files = ['Reading1.txt','Reading2.txt']
answers_df = create_answers_dataframe(txt_files)

# Print the DataFrame
print(answers_df)