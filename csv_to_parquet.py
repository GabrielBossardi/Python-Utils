import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import glob

def csv_to_parquet(csv_file, parquet_file):
    df = pd.read_csv(csv_file)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_file)

def convert_all_csv_to_parquet(csv_folder, parquet_folder):
    csv_files = glob.glob(csv_folder + '/*.csv')
    for csv_file in csv_files:
        file_name = csv_file.split('/')[-1]
        parquet_file = parquet_folder + '/' + file_name.replace('.csv', '.parquet')
        csv_to_parquet(csv_file, parquet_file)
        print(f"Converted: {csv_file} -> {parquet_file}")

# Example usage:
csv_folder = 'csv_data'
parquet_folder = 'parquet_data'

convert_all_csv_to_parquet(csv_folder, parquet_folder)
