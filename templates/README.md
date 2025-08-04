# Docker Offload Templates

This directory contains template files and configurations for common Docker Offload use cases.

## 📁 Available Templates

### Dockerfiles
- `Dockerfile.python-ml` - Machine learning with Python
- `Dockerfile.node-webapp` - Node.js web application
- `Dockerfile.java-spring` - Java Spring Boot application
- `Dockerfile.go-microservice` - Go microservice
- `Dockerfile.multi-stage` - Multi-stage build optimization

### Docker Compose
- `docker-compose.microservices.yml` - Microservices architecture
- `docker-compose.development.yml` - Development environment
- `docker-compose.ml-pipeline.yml` - ML training pipeline

### Configuration Files
- `.dockerignore.template` - Docker ignore patterns
- `docker-offload.env.template` - Environment variables
- `buildkit.toml.template` - BuildKit configuration

### Scripts
- `offload-setup.sh` - Quick setup script
- `performance-test.sh` - Performance benchmarking
- `gpu-check.sh` - GPU availability checker

## 🚀 Usage

1. **Copy the relevant template** to your project directory
2. **Customize** the template for your specific needs
3. **Start Docker Offload** with appropriate settings
4. **Build and run** your application

## 📖 Template Categories

### Performance Optimized
Templates optimized for build speed and resource efficiency with Docker Offload.

### GPU-Enabled
Templates configured for GPU workloads with proper CUDA setup.

### Multi-Architecture
Templates for building cross-platform containers.

### Security-Focused
Templates with security best practices and minimal attack surface.

## 🔧 Customization

Each template includes:
- **Comments** explaining each configuration option
- **Variables** that can be easily customized
- **Best practices** specific to Docker Offload
- **Performance tips** for cloud builds

## 🤝 Contributing

Have a useful template? Please contribute it! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
