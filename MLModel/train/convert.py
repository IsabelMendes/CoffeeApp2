#
//  convert.py
//  CoffeeApp
// Convert Pytorch Model to Core ML
//
//  Created by isabelmendes on 21/03/25.
//
import coremltools as ct
import torch

# Load model
model = torch.jit.load("coffee_classifier.pt")
model.eval()

# Convert to Core ML
example_input = torch.rand(1, 3, 224, 224)  # Example image input
mlmodel = ct.convert(model, inputs=[ct.TensorType(shape=example_input.shape)])

# Save Core ML model
mlmodel.save("CoffeeClassifier.mlmodel")
print("Model converted to Core ML!")

