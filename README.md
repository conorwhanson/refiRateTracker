# Mortgage Refinance Rate Tracker
This repository contains a simple Python script that runs Selenium to vist **four** mortgage lenders, scrape their current 30-year refinance rate, and append those rates to a `csv` file (along with the current date). This data is then used to graph a timeseries of refinance rates.

The four mortgage lenders are:
- [Affinity Plus Credit Union (local to MN)](https://www.affinityplus.org/rates/mortgage-rates)
- [Rocket Mortgage](https://www.rocketmortgage.com/refinance-rates)
- [Blaze Credit Union (local to MN)](https://blazecu.com/personal/borrow/mortgage/mortgage-refinance)
- [Magnifi (local to MN, ND, and WI)](https://mymagnifi.org/rates/rates-mortgages.html)