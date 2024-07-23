#!/bin/bash

files=(
    "0-gather_data_from_an_API.py"
    "1-export_to_CSV.py"
    "2-export_to_JSON.py"
    "3-dictionary_of_list_of_dictionaries.py"
)

for file in "${files[@]}"; do
    touch "$file"
    echo "#!/usr/bin/python3" > "$file"
    chmod +x "$file"
    git add "$file"
    git commit -m "Added $file"
done

git push

