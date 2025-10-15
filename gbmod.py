# vram_unique_per_frame.py
# Reads VRAM each frame, extracts only new unique tiles per frame (skip duplicates)
# Keeps offset structure and writes all to graphics_newtiles.bin

import os
from pyboy import PyBoy

# --- CONFIGURATION ---
VRAM_START = 0x8000
VRAM_END   = 0xA000
TILE_SIZE  = 16
FRAMES_TO_CAPTURE = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
OUTPUT_FILE = "graphics_newtiles.bin"
WHITE_VALUES = {0x00, 0xFF}

def is_white_tile(tile: bytes) -> bool:
    """Return True if all bytes in tile are white (00 or FF)."""
    return all(b in WHITE_VALUES for b in tile)

def run_pyboy_extract(rom_path):
    print(f"🎮 Running ROM: {rom_path}")
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    pyboy = PyBoy(rom_path, window="SDL2", scale=2)
    pyboy.set_emulation_speed(1)

    seen_tiles = set()
    frame_counter = 0
    total_saved = 0
    total_tiles = 0

    with open(OUTPUT_FILE, "ab") as out:
        while frame_counter < FRAMES_TO_CAPTURE:
            pyboy.tick()
            vram = bytearray(pyboy.memory[VRAM_START:VRAM_END])

            frame_new_tiles = bytearray()
            for offset in range(0, len(vram), TILE_SIZE):
                tile = bytes(vram[offset:offset+TILE_SIZE])
                total_tiles += 1

                if is_white_tile(tile):
                    continue  # skip white tile entirely

                if tile not in seen_tiles:
                    seen_tiles.add(tile)
                    frame_new_tiles.extend(tile)

            if frame_new_tiles:
                out.write(frame_new_tiles)
                total_saved += len(frame_new_tiles) // TILE_SIZE
                print(f"✅ Frame {frame_counter:03}: {len(frame_new_tiles)//TILE_SIZE} new tiles")

            frame_counter += 1

    pyboy.stop()
    print("\n🎨 Finished extracting new tiles per frame")
    print(f"🧩 Frames processed: {frame_counter}")
    print(f"💾 Unique tiles saved: {total_saved}")
    print(f"📂 Output file: {OUTPUT_FILE}")
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    print("🎨 Game Boy VRAM Analyzer — Unique Per Frame Tile Reader")
    print("--------------------------------------------------------")
    rom_file = input("Enter ROM filename (.gb): ").strip()
    if not os.path.exists(rom_file):
        print(f"❌ ROM not found: {rom_file}")
    else:
        run_pyboy_extract(rom_file)
