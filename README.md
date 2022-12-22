# qa_project

technologies: Python, Selenium, Browserstack

- There are 5 test cases written in Selenium (Python) and all of them are connected to Browserstack
- In each Python file there are 5 configurations that run parallel on Browserstack (2 on windows, 1 on OS X, one on Android and one on iOS)
- Once tests are run, status of each test case shows on browserstack dashboard, where report can be generated

- test were run on the following configurations using browserstack (configurations were chosen depending on the trend found on https://gs.statcounter.com/browser-version-market-share):  

--> Windows 10 - Chrome 107.0  
--> Windows 10 - Edge 107  
--> OS X Ventura - Safari 16  
--> Android 11 - Samsung Galaxy S20 - Chrome  
--> iOS 15.5 - iPhone 13 Pro - Safari  

Links to public Browserstack dashboards:
[TC-1](https://automate.browserstack.com/dashboard/v2/public-build/Y2VHWkZTZG1IUXhldTNiYjA2M2ZqSm1Lc2duMXZ1WktLaFRDVnVKaVBZRlJtcnMzQnIrdGhjc2ZZVVIyQnVRSURZelNhcHQrT0hvc1JNRHQvTmhFalE9PS0tSDNXUHFFdERhdWRCdnBnbmhPQlJsdz09--8c06e1f17b90c08db16b8043b8660d4100c9a83d)
[TC-2](https://automate.browserstack.com/dashboard/v2/public-build/ZGJxWnN2T1VwNW1NNWNUdzRWUm9ZZS85emxZZE9hR1VPNTNpUkpYTWsvWncrbS9kOEFEaFF0aGpGdzJmZ1JDTkNyQzZQZkppYktlQlNTR1VPMmVIOWc9PS0tcjNuREhMWHlDT3ZLSFdSZmgreFY5Zz09--57137bf197ea7ba9103ea66cf37e192ad4ea0371)
[TC-3](https://automate.browserstack.com/dashboard/v2/public-build/Um1vNmpURUJNOG5kOFVmK283TE40eDJaN25tdDRPU3F5RjBMQ0g1cWhTYS96L3hhUG9COG1SNVJrdE8vSTlMbE1jSmhjVXNKVE9EMlR1TDNkeUhWeXc9PS0tVHFzZk5HemtQeFVKR2c4OG11YkJoUT09--f73efabd4e9b3d743904c72231d8f8a3d53b724c)
[TC-4](https://automate.browserstack.com/dashboard/v2/public-build/Y3l0VW10dkN3T2MxU2ZWWjQ0KzRnVXhNK0t5aUR4VWRSU3Ewb0RydjVXVWJiU2ZrbjlvcWtINk43OERKT1hkRTNVOUttbld3YlZMUTBlYUROQ0lYNFE9PS0tS3BleUxneTlGQjBJclg0RERWTUJRdz09--f23b0a0e99ae4b16cb7eede18ea13592267d76e0)
[TC-5](https://automate.browserstack.com/dashboard/v2/public-build/dGViaWVONG9EWU9BaTBReC91czRkQmZxMkZ4UnFlNlRjVzRWMWIyakd5NlU0MUpmbFdlYjFmT2pzbXcrR0RXbG1mZWFkcEp1aEphTUFKMGxtT3g2WEE9PS0tRS84b1BIQnYwTDJuV1pGTVhsbGVFUT09--f586a7adc315d6d1d05263cc0a7265d05a98dd18)
