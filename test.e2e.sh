set -e

echo '__________'
echo 'txt'
echo xpatho.py testData/xpaths-complex-10.txt
python3 xpatho.py testData/xpaths-complex-10.txt

echo '__________'
echo 'csv'
echo python3 xpatho_csv.py testData/xpaths-complex-10.csv temp/obfuscated.csv  --csv_column 1
python3 xpatho_csv.py testData/xpaths-complex-10.csv temp/obfuscated.csv  --csv_column 1

cat temp/obfuscated.csv

echo '__________'
echo 'json'
echo xpatho_json.py testData/xpaths-complex-10.json
python3 xpatho_json.py testData/xpaths-complex-10.json
