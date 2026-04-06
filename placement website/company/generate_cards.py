import csv

# Input CSV file
input_file = "companies.csv"
# Output HTML file
output_file = "companies.html"

template = """
<div class="company-box">
  <img src="{logo}" alt="{company} Logo">
  <div class="overlay">
    <h3>{company}</h3>
    <p>Placed: {placed} students</p>
    <p>Departments: {departments}</p>
  </div>
</div>
"""

html_blocks = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        block = template.format(
            logo=row["LogoURL"],
            company=row["Company"],
            placed=row["Placed"],
            departments=row["Departments"]
        )
        html_blocks.append(block)

# Save all blocks into one HTML file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(html_blocks))

print("✅ HTML file generated:", output_file)
