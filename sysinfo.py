# System Information Script 07/2026

import platform
import os
import shutil

def get_system_info():
    print("=" * 40)
    print("SYSTEM INFORMATION")
    print("=" * 40)
    
    print(f"OS:          {platform.system()} {platform.release()}")
    print(f"Machine:     {platform.machine()}")
    print(f"Processor:   {platform.processor()}")
    print(f"Hostname:    {platform.node()}")
    
    # Disk usage
    total, used, free = shutil.disk_usage("/")
    print(f"Disk Total:  {total // (2**30)} GB")
    print(f"Disk Used:   {used // (2**30)} GB")
    print(f"Disk Free:   {free // (2**30)} GB")
    
    print("=" * 40)

if __name__ == "__main__":
    get_system_info()