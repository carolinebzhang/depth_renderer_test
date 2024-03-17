#!/bin/bash

# Source directory
source_dir="/users/czhan157/Downloads/depth_renderer_test/rgba_6_renders"

# Destination directory
dest_dir="/users/czhan157/Downloads/depth_renderer_test/distinct_angles"

# Create destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Function to copy images to distinct folders
copy_images() {
    local source_folder="$1"
    #local dest_folder="$dest_dir/$num"
    mkdir -p "$dest_folder/001"
    mkdir -p "$dest_folder/002"
    mkdir -p "$dest_folder/003"
    mkdir -p "$dest_folder/004"
    mkdir -p "$dest_folder/005"
    mkdir -p "$dest_folder/006"
    for image in "$source_folder"/*.png; do
        if [[ -f "$image" ]]; then
            # Extract the number part of the filename
            num=$(basename "$image" | grep -oE '[0-9]+')
            

            # Copy the image to the corresponding destination folder
            cp "$image" "$dest_folder/$num"
        fi
    done
}

# Loop through each folder in the source directory
for folder in "$source_dir"/*/; do
    if [[ -d "$folder" ]]; then
        # Loop through each subfolder in the current folder
        for subfolder in "$folder"/*/; do
            if [[ -d "$subfolder" ]]; then
                # Extract the last part of the subfolder name
                subfolder_name=$(basename "$subfolder")

                # Copy images to distinct folders based on subfolder name
                copy_images "$subfolder" "$subfolder_name"
            fi
        done
    fi
done