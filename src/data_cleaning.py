import os
import pandas as pd
def get_distinct_prefixes(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Extract the distinct prefixes
    prefixes = set()
    for file in files:
        # Remove the file extension
        file_name = os.path.splitext(file)[0]
        # Split the file name at the first digit
        prefix = ''.join(filter(str.isalpha, file_name))
        prefixes.add(prefix)
    
    return sorted(prefixes)

def merge_files_with_same_prefix(directory, prefix):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter files by the specified prefix
    matching_files = [file for file in files if file.startswith(prefix) and file.endswith('.xlsx')]
    
    # Initialize an empty list to store dataframes
    dfs = []
    
    for file in matching_files:
        # Read each file and extract the first column
        df = pd.read_excel(os.path.join(directory, file), usecols=[0])
        dfs.append(df)
    
    # Concatenate all the dataframes along columns
    aggregated_df = pd.concat(dfs, axis=1)
    
    # Save the aggregated dataframe to a new file
    output_file = os.path.join('../aggregated_output', f'{prefix}_aggregated.xlsx')
    aggregated_df.to_excel(output_file, index=False)
    
    return output_file

# Example usage
directory_path = '../outputs'
distinct_prefixes = get_distinct_prefixes(directory_path)
print(distinct_prefixes)
for prefix in distinct_prefixes:
    merge_files_with_same_prefix(directory_path, prefix)
