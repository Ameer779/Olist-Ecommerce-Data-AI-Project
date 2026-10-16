
import sqlite3
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]
DB_PATH = PROJECT_DIR / "database" / "olist_analysis.db"
SQL_PATH = PROJECT_DIR / "src" / "task04" / "queries.sql"
OUTPUT_DIR = PROJECT_DIR / "reports" / "task04"
OUTPUT_FILE = OUTPUT_DIR / "query_results.txt"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sql_text = SQL_PATH.read_text(encoding="utf-8")

with sqlite3.connect(DB_PATH) as connection:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        for number, query in enumerate(sql_text.split(";"), start=1):
            query = query.strip()

            if not query or query.startswith("--"):
                # Skip comment-only sections
                lines = [
                    line for line in query.splitlines()
                    if line.strip() and not line.strip().startswith("--")
                ]
                query = "\n".join(lines).strip()

            if not query:
                continue

            try:
                cursor = connection.execute(query)
                rows = cursor.fetchall()
                columns = [item[0] for item in cursor.description] if cursor.description else []

                output.write(f"\n{'=' * 60}\n")
                output.write(f"Query section {number}\n")
                output.write(f"{'=' * 60}\n")
                output.write(" | ".join(columns) + "\n")

                for row in rows:
                    output.write(" | ".join(str(value) for value in row) + "\n")

                print(f"Query section {number}: {len(rows)} rows returned")

            except sqlite3.Error as error:
                print(f"SQL error in section {number}: {error}")
                raise

print(f"\nResults saved to: {OUTPUT_FILE}")