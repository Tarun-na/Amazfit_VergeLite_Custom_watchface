# Amazfit Verge Lite Watch Face Tools

A standalone Python project for creating and unpacking Amazfit Verge Lite watch-face files. It uses a 360 × 360 canvas, a 210 × 210 preview, and the Verge Lite `HMDIAL` file header.

## Requirements

- Python 3.7 or newer
- Pillow: `python -m pip install -r requirements.txt`

## Unpack a watch face

```powershell
python main.py path\to\watchface.bin
```

The tool creates a folder beside the input file with the JSON descriptor, extracted image resources, and previews.

Original F1 and Spider-Man binary files are included and unpacked in this project. To unpack them again, run:

```powershell
python main.py watchfaces\F1\F1_original.bin
python main.py watchfaces\SpiderMan\SpiderMan_original.bin
```

## Pack a watch face

Place the JSON descriptor and its numbered PNG resources in the same folder, then run:

```powershell
python main.py path\to\watchface.json
```

The packed file is written beside the JSON with `_packed.bin` appended to its name.

## Included watch faces

- `watchfaces/F1/`: F1 face descriptor, image resources, original binary, and unpacked output folder
- `watchfaces/SpiderMan/`: Spider-Man face descriptor, image resources, original binary, and unpacked output folder

To pack the included editable descriptors:

```powershell
python main.py watchfaces\F1\F1.json
python main.py watchfaces\SpiderMan\SpiderMan.json
```

The project accepts and creates Amazfit Verge Lite watch-face files and rejects files without the Verge Lite file marker. Weather fields are not supported by the documented Verge Lite watch-face format. Some uncommon watch-face elements may not round-trip perfectly.

To install a packed file, use a companion app or transfer method that supports Amazfit Verge Lite.
