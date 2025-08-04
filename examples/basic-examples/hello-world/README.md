# Hello World Docker Offload Example

A simple example to get started with Docker Offload.

## Prerequisites

- Docker Desktop 4.43 or later
- Docker Offload beta access
- Active Docker subscription

## Files

- `Dockerfile` - Simple container definition
- `app.py` - Basic Python application
- `requirements.txt` - Python dependencies

## Usage

1. **Start Docker Offload**
   ```bash
   docker offload start
   ```

2. **Build the image** (executes in cloud)
   ```bash
   docker build -t hello-offload .
   ```

3. **Run the container** (executes in cloud)
   ```bash
   docker run --rm hello-offload
   ```

4. **Check status**
   ```bash
   docker offload status
   ```

## Expected Output

```
Hello from Docker Offload!
Build executed in cloud: ✓
Runtime in cloud: ✓
```

## Performance Notes

- Build time should be faster than local builds
- Cloud icon (☁️) appears in Docker Desktop when active
- Docker Desktop UI shows purple theme when offloading

## Troubleshooting

If you encounter issues:

```bash
# Check Docker Offload status
docker offload status

# Restart if needed
docker offload stop
docker offload start

# Check logs
docker offload logs
```
