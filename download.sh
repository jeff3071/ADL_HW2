mkdir -p ./cache
mkdir -p ./model/CS
mkdir -p ./model/QA

wget https://www.dropbox.com/s/2td65yuccxpyp4m/cache.zip?dl=1 -O cache.zip
unzip cache
wget https://www.dropbox.com/s/rtkakm1m7xjidak/model.zip?dl=1 -O model.zip
unzip model

rm cache.zip
rm model.zip