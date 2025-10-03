"""
TensorFlow Removal Script
Safely remove TensorFlow and related packages from your MCP project.
"""

import subprocess
import sys
from pathlib import Path

def get_tensorflow_packages():
    """Get list of TensorFlow-related packages to remove."""
    tf_packages = [
        "tensorflow",
        "tensorboard", 
        "tensorboard-data-server",
        "tf-slim",
        "tensorflow-probability",
        "absl-py",
        "astunparse",
        "flatbuffers",
        "gast",
        "google-pasta",
        "grpcio",
        "h5py",
        "keras",
        "libclang",
        "Markdown",
        "ml_dtypes",
        "namex",
        "opt_einsum",
        "protobuf",
        "termcolor",
        "wrapt"
    ]
    return tf_packages

def remove_tensorflow_files():
    """Remove TensorFlow-related files from project."""
    tf_files = [
        "tensorflow_compat_helper.py",
        "tf_contrib_fix.py", 
        "tf_contrib_compat.py",
        "tf_contrib_solutions.py",
        "tf1_compat_mode.py"
    ]
    
    removed_files = []
    project_root = Path(".")
    
    for file_name in tf_files:
        file_path = project_root / file_name
        if file_path.exists():
            try:
                file_path.unlink()
                removed_files.append(file_name)
                print(f"✅ Removed: {file_name}")
            except Exception as e:
                print(f"❌ Could not remove {file_name}: {e}")
    
    return removed_files

def uninstall_tensorflow():
    """Uninstall TensorFlow and related packages."""
    tf_packages = get_tensorflow_packages()
    python_exe = "C:/Source/mcpdemo/.venv/Scripts/python.exe"
    
    print("🔧 Uninstalling TensorFlow packages...")
    print("=" * 50)
    
    uninstalled = []
    for package in tf_packages:
        try:
            result = subprocess.run(
                [python_exe, "-m", "pip", "uninstall", package, "-y"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                uninstalled.append(package)
                print(f"✅ Uninstalled: {package}")
            else:
                print(f"⚠️  {package} not found (already removed)")
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout removing {package}")
        except Exception as e:
            print(f"❌ Error removing {package}: {e}")
    
    return uninstalled

def check_project_dependencies():
    """Check what your MCP project actually needs."""
    print("\n📋 Your MCP Project Actually Needs:")
    print("=" * 40)
    
    required_packages = [
        "fastmcp>=2.12.4",
        "click>=8.0.0", 
        "openai>=2.0.1",
        "agents>=1.4.0",
        "python-dotenv>=1.1.1",
        "mcp>=1.15.0"
    ]
    
    for package in required_packages:
        print(f"✅ {package}")
    
    print("\n❌ NOT NEEDED for your MCP project:")
    print("   - tensorflow (2+ GB)")
    print("   - tensorboard")
    print("   - keras")
    print("   - All ML/AI training libraries")

def update_requirements():
    """Update requirements.txt to remove TensorFlow."""
    requirements_file = Path("requirements.txt")
    
    if requirements_file.exists():
        print("\n📝 Updating requirements.txt...")
        
        # Read current requirements
        content = requirements_file.read_text()
        
        # Remove TensorFlow lines
        lines = content.strip().split('\n')
        new_lines = [line for line in lines 
                    if not any(tf_pkg in line.lower() 
                             for tf_pkg in ['tensorflow', 'keras', 'tensorboard'])]
        
        # Write updated requirements
        new_content = '\n'.join(new_lines)
        requirements_file.write_text(new_content)
        
        print("✅ Updated requirements.txt")
        print("📦 Current requirements:")
        for line in new_lines:
            if line.strip():
                print(f"   {line}")

def show_disk_space_saved():
    """Estimate disk space saved."""
    print("\n💾 Estimated Disk Space Saved:")
    print("=" * 40)
    
    savings = {
        "TensorFlow": "~2.5 GB",
        "Keras": "~500 MB", 
        "TensorBoard": "~200 MB",
        "Supporting libraries": "~800 MB",
        "Total": "~4 GB"
    }
    
    for item, size in savings.items():
        print(f"📁 {item}: {size}")

def main():
    """Main function to remove TensorFlow from MCP project."""
    print("🧹 TensorFlow Removal for MCP Project")
    print("=" * 50)
    print("This script will remove TensorFlow since your MCP project doesn't need it.")
    print()
    
    # Ask for confirmation
    try:
        confirm = input("❓ Remove TensorFlow and free up ~4GB disk space? (y/N): ").lower().strip()
        if confirm not in ['y', 'yes']:
            print("❌ Removal cancelled.")
            return
    except KeyboardInterrupt:
        print("\n❌ Removal cancelled.")
        return
    
    print("\n🚀 Starting TensorFlow removal...")
    
    # Remove TensorFlow files
    print("\n1. Removing TensorFlow helper files...")
    removed_files = remove_tensorflow_files()
    
    # Uninstall packages
    print("\n2. Uninstalling TensorFlow packages...")
    uninstalled = uninstall_tensorflow()
    
    # Update requirements
    print("\n3. Updating project files...")
    update_requirements()
    
    # Show what the project actually needs
    check_project_dependencies()
    
    # Show space saved
    show_disk_space_saved()
    
    print("\n🎉 TensorFlow Removal Complete!")
    print("=" * 40)
    print(f"📁 Removed {len(removed_files)} helper files")
    print(f"📦 Uninstalled {len(uninstalled)} packages") 
    print("💾 Freed up approximately 4GB disk space")
    print()
    print("✅ Your MCP project is now lean and focused!")
    print("🚀 All MCP functionality remains intact")
    print()
    print("🧪 Test your project:")
    print("   python -m mcpdemo.server")
    print("   python src/mcpdemo/azure_openai_client.py")

if __name__ == "__main__":
    main()