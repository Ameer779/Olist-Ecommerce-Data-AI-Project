
import sqlite3
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_DIR / "database" / "olist_analysis.db"
OUTPUT_DIR = PROJECT_DIR / "reports" / "task04"
OUTPUT_FILE = OUTPUT_DIR / "database_tables.md"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with sqlite3.connect(DB_PATH) as connection:
    tables = connection.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
    """).fetchall()

    lines = [
        "# Task 04: Database Tables Report",
        "",
        "Database: Olist Brazilian E-Commerce (SQLite)",
        "",
        "| Table | Rows | Columns |",
        "|---|---:|---:|",
    ]

    for (table_name,) in tables:
        safe_name = table_name.replace('"', '""')

        row_count = connection.execute(
            f'SELECT COUNT(*) FROM "{safe_name}"'
        ).fetchone()[0]

        columns = connection.execute(
            f'PRAGMA table_info("{safe_name}")'
        ).fetchall()

        column_names = ", ".join(column[1] for column in columns)

        lines.append(
            f"| {table_name} | {row_count:,} | {len(columns)} |"
        )
        lines.extend([
            "",
            f"### {table_name}",
            "",
            f"Columns: {column_names}",
        ])

    OUTPUT_FILE.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )

print(f"Tables found: {len(tables)}")
print(f"Report saved to: {OUTPUT_FILE}")
