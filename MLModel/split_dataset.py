#
#  split_dataset.py
#  CoffeeApp


import os
import shutil
import random

# Paths
DATASET_PATH = "/Users/isabelmendes/Documents/CoffeeApp/MLModel/coffe_dataset" # Folder where your original images are stored
OUTPUT_PATH = "/Users/isabelmendes/Documents/CoffeeApp/MLModel/dataset_split"  # New folder to store train/val

# Define train/val split ratio
TRAIN_RATIO = 0.8  # 80% for training, 20% for validation

# Create directories
train_path = os.path.join(OUTPUT_PATH, "train")
val_path = os.path.join(OUTPUT_PATH, "val")

os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)

# Get all images
all_images = [f for f in os.listdir(DATASET_PATH) if f.endswith((".jpg", ".png"))]
random.shuffle(all_images)  # Shuffle dataset

# Split dataset
split_index = int(len(all_images) * TRAIN_RATIO)
train_images = all_images[:split_index]
val_images = all_images[split_index:]

# Move images to train/val folders
for img in train_images:
    shutil.move(os.path.join(DATASET_PATH, img), os.path.join(train_path, img))

for img in val_images:
    shutil.move(os.path.join(DATASET_PATH, img), os.path.join(val_path, img))

print(f"Dataset split: {len(train_images)} train images, {len(val_images)} validation images.")


