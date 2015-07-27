# Scraper to collect details of UK cooperative businesses

## License

Copyright 2015 Mark brough

Licensed under the MIT License

## How to run

1. Create a virtualenv

    ```
    cd uk-cooperatives
    virtualenv ./pyenv
    source ./pyenv/bin/activate
    ```

2. Install dependencies


    ```
    pip install -r requirements.txt
    ```

3. Run the scraper!

    ```
    python scrape.py
    ```

## Issues

The scraper tries to save everything to a single CSV file in one go. The API sometimes times out. It would be better to proceed in chunks or have a way of resuming from the last known `store_id`
