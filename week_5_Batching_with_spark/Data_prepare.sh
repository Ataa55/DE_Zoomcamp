#https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
#https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
TAXI_TYPE=$1  #"green"
YEAR=$2         #2020

url_prefix=https://d37ci6vzurychx.cloudfront.net/trip-data/

for  MONTH in $(seq 1 12); do

       
    FMONTH=`printf "%02d" ${MONTH}` 
    
    URL="${url_prefix}${TAXI_TYPE}_tripdata_2021-${FMONTH}.parquet"
    
    FILE_DEST="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"
    FILE_NAME="${TAXI_TYPE}_tripddata_${YEAR}_${FMONTH}.parquet"
    LOCAL_PATH="${FILE_DEST}/${FILE_NAME}"
    
    mkdir -p ${FILE_DEST} 
    echo "Downloading Month ${FMONTH} Data"
    echo "........."
    curl -o ${LOCAL_PATH} ${URL}
 
done