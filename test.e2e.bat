echo "=== TXT ==="
python xpatho.py testData\xpaths-complex-10.txt

echo "=== CSV ==="
python xpatho_csv.py testData\xpaths-complex-10.csv temp\obfuscated.csv  --csv_column 1
type temp\obfuscated.csv

echo "=== JSON ==="
python xpatho_json.py testData\xpaths-complex-10.json
