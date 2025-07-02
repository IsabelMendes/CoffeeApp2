#
//  trainML.py
//  CoffeeApp
//
//  Created by isabelmendes on 21/03/25.
//

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader



## 🔹 Hyperparameters
#IMAGE_SIZE = 224
#BATCH_SIZE = 32
#EPOCHS = 10
#LEARNING_RATE = 0.001
#
## 🔹 Image Transformations
#transform = transforms.Compose([
#    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
#    transforms.ToTensor(),
#    transforms.Normalize(mean=[0.5], std=[0.5])
#])
#
## 🔹 Load Dataset
#dataset_path = "/Users/isabelmendes/Documents/CoffeeApp/MLModel/coffe_dataset"
##train_data = datasets.ImageFolder(root=f"{dataset_path}/train", transform=transform)
##val_data = datasets.ImageFolder(root=f"{dataset_path}/val", transform=transform)
#
#
#
##train_loader = DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
##val_loader = DataLoader(dataset=val_data, batch_size=BATCH_SIZE, shuffle=False)
#
## 🔹 CNN Model Definition
#class CoffeeClassifier(nn.Module):
#    def __init__(self):
#        super(CoffeeClassifier, self).__init__()
#        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
#        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
#        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
#        self.pool = nn.MaxPool2d(2, 2)
#        self.fc1 = nn.Linear(128 * (IMAGE_SIZE // 8) * (IMAGE_SIZE // 8), 128)
#        self.fc2 = nn.Linear(128, 2)  # Healthy or Diseased
#
#    def forward(self, x):
#        x = self.pool(torch.relu(self.conv1(x)))
#        x = self.pool(torch.relu(self.conv2(x)))
#        x = self.pool(torch.relu(self.conv3(x)))
#        x = x.view(x.size(0), -1)  # Flatten
#        x = torch.relu(self.fc1(x))
#        x = self.fc2(x)
#        return x
#
## 🔹 Train Model
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#model = CoffeeClassifier().to(device)
#criterion = nn.CrossEntropyLoss()
#optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
#
#for epoch in range(EPOCHS):
#    model.train()
#    for images, labels in train_loader:
#        images, labels = images.to(device), labels.to(device)
#        optimizer.zero_grad()
#        outputs = model(images)
#        loss = criterion(outputs, labels)
#        loss.backward()
#        optimizer.step()
#
## 🔹 Save Model for Swift
#torch.jit.save(torch.jit.script(model), "coffee_classifier.pt")
#print("Model saved as coffee_classifier.pt")
#
