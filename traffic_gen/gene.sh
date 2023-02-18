python traffic_gen.py -c CacheFollower_distribution.txt -n 16 -l 0.7 -b 100G -t 0.01 --incastload 0 -o flowCacheFollowerLoad07Time001_fat16.txt
python traffic_gen.py -c CacheFollower_distribution.txt -n 4096 -l 0.7 -b 100G -t 0.01 --incastload 0 -o flowCacheFollowerLoad07Time001_fat4096.txt
python traffic_gen.py -c CacheFollower_distribution.txt -n 256 -l 0.7 -b 100G -t 0.01 --incastload 0 -o flowCacheFollowerLoad07Time001_fat256.txt
python traffic_gen.py -c CacheFollower_distribution.txt -n 1024 -l 0.7 -b 100G -t 0.01 --incastload 0 -o flowCacheFollowerLoad07Time001_fat1024.txt
