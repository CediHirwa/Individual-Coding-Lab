#!/bin/bash

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

echo "Starting Organizer Script..."

if [ ! -d "$ARCHIVE_DIR" ]; then
    echo "Directory '$ARCHIVE_DIR' not found. Creating it..."
    mkdir "$ARCHIVE_DIR"
else
    echo "Directory '$ARCHIVE_DIR' already exists."
fi

count=$(ls *.csv 2>/dev/null | wc -l)

if [ "$count" != "0" ]; then
    for file in *.csv; do
        TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
        
        BASENAME="${file%.*}"
        EXTENSION="${file##*.}"
        NEW_NAME="${BASENAME}-${TIMESTAMP}.${EXTENSION}"
        
        echo "Processing: $file -> $NEW_NAME"
        
        echo "------------------------------------------------" >> "$LOG_FILE"
        echo "Date: $(date)" >> "$LOG_FILE"
        echo "Operation: Archived $file to $ARCHIVE_DIR/$NEW_NAME" >> "$LOG_FILE"
        echo "--- File Content Dump ---" >> "$LOG_FILE"
        cat "$file" >> "$LOG_FILE"
        echo "------------------------------------------------" >> "$LOG_FILE"
        
        mv "$file" "$ARCHIVE_DIR/$NEW_NAME"
        
        echo "Move Complete."
    done
    echo "All CSV files have been archived."
else
    echo "No .csv files found in the current directory."
fi
