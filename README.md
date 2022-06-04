# PakWheels Latest Ads Crawler

A scrapy crawler that retrieves the used vehicles ads from first 10 pages of [PakWheels](https://www.pakwheels.com).

## Build

```
pip install -r requirements.txt
```

## Run locally

```
scrapy crawler latest_ads
```

## Deploy to AWS Lambda

```
invoke deploy
```

### OR

```
cd venv/lib/python3.9/site-packages
zip -r ../../../../deployment-package.zip .
cd ../../../../
zip -g deployment-package.zip lambda_function.py
zip -r deployment-package.zip pakwheels
aws lambda update-function-code --function-name PakwheelsLatestAds --zip-file fileb://deployment-package.zip
```

## Check Type Errors (mypy)

```
mypy .
```
