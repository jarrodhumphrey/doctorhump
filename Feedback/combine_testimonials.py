#!/usr/bin/env python3
"""
Script to programmatically combine all EXTRACTED-TESTIMONIALS.md files
from the six feedback folders into a single master document.
"""

import os
from pathlib import Path

# Define the base feedback directory
base_dir = Path(__file__).parent

# Define the six folders in order
folders = [
    "01-Screenshots",
    "02-Single-Emails",
    "03-Multi-Page-Reflections",
    "04-Survey-Results",
    "05-Manuscripts",
    "06-Panel-Photos"
]

# Output file
output_file = base_dir / "MASTER-TESTIMONIALS.md"

# Header for the master document
header = """# Master Testimonials Document

**Combined from:** 6 feedback folders
**Generated:** Programmatically combined from individual EXTRACTED-TESTIMONIALS.md files
**Purpose:** Consolidated view of all extracted testimonials and feedback

---

"""

# Create/overwrite the output file
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Write header
    outfile.write(header)

    # Process each folder
    for folder in folders:
        testimonial_file = base_dir / folder / "EXTRACTED-TESTIMONIALS.md"

        # Check if file exists
        if testimonial_file.exists():
            # Add folder separator
            outfile.write(f"\n\n{'='*80}\n")
            outfile.write(f"# FOLDER: {folder}\n")
            outfile.write(f"{'='*80}\n\n")

            # Read and append the content
            with open(testimonial_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
        else:
            # Note missing file
            outfile.write(f"\n\n{'='*80}\n")
            outfile.write(f"# FOLDER: {folder}\n")
            outfile.write(f"{'='*80}\n\n")
            outfile.write(f"**Note:** EXTRACTED-TESTIMONIALS.md not found in {folder}\n")

print(f"[SUCCESS] Master document created: {output_file}")
print(f"[SUCCESS] Combined {len(folders)} folders")
print(f"[SUCCESS] Output: MASTER-TESTIMONIALS.md")
