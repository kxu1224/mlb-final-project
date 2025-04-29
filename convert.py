import pandas as pd

# print('hi')

# Load a Parquet file
smiles = pd.read_parquet('drugbank_data/compound_smiles.parquet')
label = pd.read_parquet('drugbank_data/label2text.parquet')
qa = pd.read_parquet('drugbank_data/QA.parquet')
q_idx = pd.read_parquet('drugbank_data/question_idx.parquet')

qa = qa.merge(smiles, on='compound_idx', how='left')
qa = qa.merge(q_idx, on='question_idx', how='left')
qa = qa.merge(label, on='label', how='left')

selected = qa[['smiles', 'question', 'text']]
selected['combine'] = "Question: " + selected['question'] + "\nCompound: " +  selected['smiles']

needed = selected[['combine', 'text']]

needed.to_json('chembl.json', orient='records', lines=True)


# Show the data
print(selected['combine'].head())
