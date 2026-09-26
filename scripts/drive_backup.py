import os
import zipfile
import json
import time

def backup_mmmx():
    print("==================================================")
    print("      MMMX: GOOGLE DRIVE BACKUP & ARCHIVE        ")
    print("==================================================")
    
    base_dir = os.path.expanduser("~/mmmx_worldwide")
    dist_dir = os.path.join(base_dir, "dist")
    drive_dest = os.path.expanduser("~/storage/shared/Download") # Termux shared storage pathway
    
    os.makedirs(dist_dir, exist_ok=True)
    
    # 1. Create ZIP archive of the entire MMMX workspace
    zip_filename = f"mmmx_engine_release_{int(time.time())}.zip"
    zip_path = os.path.join(dist_dir, zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            if "dist" in root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, arcname)
                
    print(f"[SUCCESS] MMMX archive created at: {zip_path}")
    
    # 2. Mirror to Google Drive shared storage path (if available on device)
    if os.path.exists(drive_dest):
        target_path = os.path.join(drive_dest, zip_filename)
        import shutil
        shutil.copy(zip_path, target_path)
        print(f"[SUCCESS] Mirrored to Google Drive sync folder: {target_path}")
    else:
        print("[INFO] Shared storage directory not mounted. Run 'termux-setup-storage' if you want direct local Google Drive folder syncing.")

if __name__ == "__main__":
    backup_mmmx()
