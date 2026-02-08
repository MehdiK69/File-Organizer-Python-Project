from pathlib import Path

def main():
    source = Path("sandbox")  # dossier courant
   
    if(source.exists()):
        print(f"Dossier source: {source.resolve()}")

    files = [p for p in source.iterdir() if p.is_file()]
    extensions = {
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".gif": "images",
        ".pdf": "documents",
        ".docx": "documents",
        ".txt": "documents",
        ".md": "documents",
        ".mp4": "videos",
        ".mov": "videos",
        ".avi": "videos",
    }

    counts = {"images": 0, "documents": 0, "videos": 0, "autres": 0}
    images_dir = source / "images"
    images_dir.mkdir(exist_ok=True)
    doc_dir = source / "documents"
    doc_dir.mkdir(exist_ok=True)
    videos_dir = source / "videos"
    videos_dir.mkdir(exist_ok=True)
    other_dir = source / "autres"
    other_dir.mkdir(exist_ok=True)



    for f in files:
        ext = f.suffix.lower()
        category = extensions.get(ext, "autres")
        print(category)
        target_path=source/category/f.name
        f.rename(target_path)
        counts[category] += 1
        print("-", f.name)

    print(counts)

if __name__ == "__main__":
    main()
