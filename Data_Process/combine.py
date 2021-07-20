# Import the libraries we need
from os import getcwd, listdir
from os.path import abspath, dirname, isfile, join, splitext
import pandas as pd

# Get the output directory for the csv file
output_folder_name = 'q1_most_polluted_state'   # TODO: Update this if needed
output_dir = abspath(join(getcwd(), '..', 'data', output_folder_name))

# Create a list of csv files in the output directory
csv_files = [join(output_dir, f) for f in listdir(output_dir) if isfile(join(output_dir, f)) and 
             splitext(join(output_dir, f))[1] == '.csv']
print("{} csv files found".format(len(csv_files)))

# Create a single csv file from the output csv files
output_file = join(output_dir, 'q1_output.csv')

with open(output_file, 'a') as o_file:
    for num in range(0, len(csv_files)):
        with open(csv_files[num], 'r') as f:
            if num == 0:
                lines = f.readlines()
            else:
                lines = f.readlines()[1:]
            for line in lines:
                 o_file.write(line)

# Create a Pandas DataFrame from the csv file
q1_df = pd.DataFrame.from_csv(output_file)
# Get the row and column counts
rows_cols = q1_df.shape
print("Rows: {}".format(rows_cols[0]))
print("Columns: {}".format(rows_cols[1]))
# Show the first 5 rows
q1_df.head()