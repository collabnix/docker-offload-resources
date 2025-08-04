#!/usr/bin/env python3
"""
Simple PyTorch GPU training example for Docker Offload demonstration.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import time
import numpy as np

class SimpleNet(nn.Module):
    """Simple neural network for demonstration."""
    
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, x):
        x = x.view(-1, 784)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return F.log_softmax(x, dim=1)

def create_dummy_data(num_samples=1000):
    """Create dummy data for training."""
    X = torch.randn(num_samples, 1, 28, 28)
    y = torch.randint(0, 10, (num_samples,))
    return TensorDataset(X, y)

def main():
    print("🚀 PyTorch GPU Training with Docker Offload")
    print("=" * 50)
    
    # Check CUDA availability
    cuda_available = torch.cuda.is_available()
    device = torch.device("cuda" if cuda_available else "cpu")
    
    print(f"🔥 PyTorch version: {torch.__version__}")
    print(f"🎯 CUDA available: {cuda_available}")
    
    if cuda_available:
        print(f"🖥️  GPU device: {torch.cuda.get_device_name(0)}")
        print(f"📊 GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
        print(f"💾 GPU memory allocated: {torch.cuda.memory_allocated(0) / 1024**2:.1f} MB")
    else:
        print("⚠️  Running on CPU (GPU not available)")
    
    print("=" * 50)
    
    # Create model and move to device
    model = SimpleNet().to(device)
    print(f"📦 Model created and moved to {device}")
    
    # Create dummy dataset
    dataset = create_dummy_data(1000)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    print("📊 Dummy dataset created (1000 samples)")
    
    # Define loss and optimizer
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training loop
    print("\n🏋️‍♂️ Starting training...")
    start_time = time.time()
    
    for epoch in range(5):
        epoch_loss = 0.0
        for batch_idx, (data, target) in enumerate(dataloader):
            data, target = data.to(device), target.to(device)
            
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(dataloader)
        print(f"📈 Epoch {epoch + 1}/5 - Average Loss: {avg_loss:.4f}")
    
    training_time = time.time() - start_time
    print(f"\n⏱️  Training completed in {training_time:.2f} seconds")
    
    if cuda_available:
        print(f"💾 Final GPU memory allocated: {torch.cuda.memory_allocated(0) / 1024**2:.1f} MB")
        print(f"💾 Max GPU memory allocated: {torch.cuda.max_memory_allocated(0) / 1024**2:.1f} MB")
    
    print("\n✅ Training completed successfully on GPU!" if cuda_available else "\n✅ Training completed on CPU!")
    print("🎉 Docker Offload GPU example finished!")

if __name__ == "__main__":
    main()
