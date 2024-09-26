#!/bin/bash

# Define the folder containing your text files
folder_path="../inputs"

# Define the placeholder text to be replaced
placeholder_text="#replace_text_here"

# Backup original main.py
cp create_ppt.py create_ppt.py.bak

# Iterate through each file in the folder
for file in "$folder_path"/*.txt; do
    echo $file
    if [[ -f "$file" ]]; then
        # Read the content of the text file
        file_content=$(< "$file")

        # Replace the placeholder text in create_ppt.py with the file content
        awk -v content="$file_content" -v placeholder="$placeholder_text" \
            '{gsub(placeholder, content)}1' create_ppt.py.bak > create_ppt.py


        # Run the modified main.py
        python3 create_ppt.py

        # Restore the original main.py for the next iteration
        cp create_ppt.py.bak create_ppt.py
    fi
done

# Clean up: remove the backup file after all iterations are done
rm create_ppt.py.bak
