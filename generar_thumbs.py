from PIL import Image
from pathlib import Path

ORIG = Path("media")
THUMBS = Path("media/thumbs")

MAX_SIZE = (400, 400)   # 👈 TU TAMAÑO IDEAL
QUALITY = 80            # 👌 buena calidad / poco peso

for img_path in ORIG.rglob("*.webp"):
    # Saltar miniaturas ya generadas
    if "thumbs" in img_path.parts:
        continue

    # Crear ruta de miniatura equivalente
    thumb_path = THUMBS / img_path.relative_to(ORIG)
    thumb_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            img.thumbnail(MAX_SIZE)
            img.save(thumb_path, "WEBP", quality=QUALITY, method=6)
            print(f"✓ {thumb_path}")
    except Exception as e:
        print(f"✗ Error con {img_path}: {e}")

print("\n✅ Miniaturas generadas")
