# scrapy-examples

Examples demonstrating Scrapy skills

## How to deploy

```
cd venv/lib/python3.9/site-packages
zip -r ../../../../deployment-package.zip .
cd ../../../../
zip -g deployment-package.zip lambda_function.py
zip -r deployment-package.zip pakwheels
aws lambda update-function-code --function-name PakwheelsLatestAds --zip-file fileb://deployment-package.zip
```
