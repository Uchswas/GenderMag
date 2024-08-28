#!/bin/bash

# Define the folder containing your text files
folder_path="../inputs"

# Define the placeholder text to be replaced
placeholder_text="#replace_text_here"

# Backup original main.py
cp subgoals_actions.py subgoals_actions.py.bak

# Iterate through each file in the folder
for file in "$folder_path"/*.txt; do
    echo $file
    if [[ -f "$file" ]]; then
        # Read the content of the text file
        file_content=$(< "$file")

        # Replace the placeholder text in subgoals_actions.py with the file content
        awk -v content="$file_content" -v placeholder="$placeholder_text" \
            '{gsub(placeholder, content)}1' subgoals_actions.py.bak > subgoals_actions.py


        # Run the modified main.py
        python3 main.py

        # Restore the original main.py for the next iteration
        cp subgoals_actions.py.bak subgoals_actions.py
    fi
done

# Clean up: remove the backup file after all iterations are done
rm main.py.bak
