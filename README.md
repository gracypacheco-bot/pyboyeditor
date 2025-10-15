# pyboyeditor

Step 1 — Install Python

You need Python 3.10 or newer (3.12–3.13 works fine).

🔹 Download it from:
👉 https://www.python.org/downloads/

✅ During installation:

Check the box: “Add Python to PATH”

Then click Install Now

To verify:

python --version


or

py --version


You should see something like:

Python 3.12.6

🧰 Step 2 — Install PyBoy and dependencies

Open Command Prompt (Windows) or Terminal (macOS/Linux) and run:

pip install pyboy


That installs the emulator core and SDL2 backend automatically.

If you see SDL-related warnings (like “Using SDL2 binaries from pysdl2-dll”), it’s normal.

⚙️ Optional: Install extras for development

If you want better performance or want to modify ROMs:

pip install numpy pillow keyboard


numpy – for faster array processing

pillow – for saving tiles as images later

keyboard – for optional key control

🕹️ Step 3 — Prepare your files

Make a working folder, e.g.:

H:\GameBoyTools\


Copy your Game Boy ROM file into it, e.g. mario.gb

Save the script from above (vram_unique_per_frame.py) into that same folder.

🧩 Step 4 — Run the tool

In your terminal, navigate to the folder:

cd H:\GameBoyTools


Then run:

python vram_unique_per_frame.py


When asked:

Enter ROM filename (.gb):


Type:

mario.gb


✅ It will start PyBoy, run the game for 120 frames, and save the extracted tiles into:

graphics_newtiles.bin

📂 Output files
File	Description
graphics_newtiles.bin	Only unique non-white tiles from all frames
graphics_offsets.bin	Same layout, white tiles zeroed out (if you use that script)
vram_dumps/	(Optional) Raw per-frame VRAM dumps
graphics_unique.bin	Deduplicated set of all unique tiles
graphics_full.bin	Every tile from every frame
🧠 Step 5 — Open or edit the tiles

You can open .bin tile files in:

YY-CHR → https://www.romhacking.net/utilities/119/

Tile Molester

GBTileD
Choose format 2bpp GB mode (Game Boy).

Each 16-byte block = one 8×8 tile.

🚀 (Optional) Step 6 — Build a modded ROM

If you later want to replace tiles into the ROM:

Identify where tile data sits in the ROM (search your unique tile bytes).

Use a small patcher:

python insert_vram_into_rom.py


(I can generate that next if you want.)
