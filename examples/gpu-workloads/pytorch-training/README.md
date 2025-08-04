# GPU PyTorch Example with Docker Offload

This example demonstrates running PyTorch with GPU support using Docker Offload.

## Prerequisites

- Docker Desktop 4.43 or later
- Docker Offload beta access with GPU support enabled
- Pro, Team, or Business Docker subscription

## Files

- `Dockerfile` - PyTorch container with CUDA support
- `train.py` - Simple PyTorch training script
- `requirements.txt` - Python dependencies

## Usage

1. **Start Docker Offload with GPU support**
   ```bash
   docker offload start --gpu
   ```

2. **Build the GPU-enabled image**
   ```bash
   docker build -t pytorch-gpu-offload .
   ```

3. **Run with GPU access**
   ```bash
   docker run --rm --gpus all pytorch-gpu-offload
   ```

4. **Check GPU availability**
   ```bash
   docker run --rm --gpus all pytorch-gpu-offload python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU count: {torch.cuda.device_count()}')"
   ```

## Expected Output

```
🚀 PyTorch GPU Training with Docker Offload
============================================
🔥 PyTorch version: 2.1.0
🎯 CUDA available: True
🖥️ GPU device: NVIDIA L4
📊 GPU memory: 22.5 GB
✅ Training completed successfully on GPU!
```

## Performance Notes

- Training should run on NVIDIA L4 GPU in the cloud
- Build time is faster due to cloud compute power
- No local GPU hardware required

## Cost Considerations

- GPU-enabled instances cost more than CPU-only
- Monitor usage through Docker Dashboard
- Stop containers when not needed to optimize costs

## Troubleshooting

```bash
# Verify GPU support is enabled
docker offload status | grep GPU

# Check if CUDA is available in container
docker run --rm --gpus all pytorch-gpu-offload nvidia-smi

# Restart with GPU if needed
docker offload stop
docker offload start --gpu
```
