set -e

echo ''
echo xpatho.py testData/xpaths-complex-10.txt
python3 xpatho.py testData/xpaths-complex-10.txt

echo ''
echo python3 xpatho_csv.py testData/xpaths-complex-10.csv temp/obfuscated.csv  --csv_column 1 
python3 xpatho_csv.py testData/xpaths-complex-10.csv temp/obfuscated.csv  --csv_column 1 

cat temp/obfuscated.csv
