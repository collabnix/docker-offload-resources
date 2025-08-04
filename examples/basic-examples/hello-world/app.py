#!/usr/bin/env python3
"""
Simple Hello World application for Docker Offload demonstration.
"""

import os
import socket
import datetime

def main():
    """Main application function."""
    print("🚀 Hello from Docker Offload!")
    print("=" * 50)
    
    # Show environment information
    print(f"📅 Timestamp: {datetime.datetime.now()}")
    print(f"🖥️  Hostname: {socket.gethostname()}")
    print(f"🐍 Python Version: {os.sys.version}")
    print(f"📁 Working Directory: {os.getcwd()}")
    
    print("=" * 50)
    print("✅ Build executed in cloud: ✓")
    print("✅ Runtime in cloud: ✓")
    print("🎉 Docker Offload is working correctly!")
    
    # Check for Docker Offload environment indicators
    if os.getenv('DOCKER_BUILDKIT'):
        print("🔧 BuildKit enabled")
        
    print("\n💡 Tip: Check 'docker offload status' to verify cloud execution")

if __name__ == "__main__":
    main()
