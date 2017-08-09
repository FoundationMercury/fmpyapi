# fmpyapi
Foundation Mercury Python API Client

This is a Python package that wraps Foundation Mercury's API.  Foundation Mercury provides API access to curated demographic data sets such as census data and public county records.

The client requires an API key, which can be created after registering at https://www.foundationmercury.com .

The API key is simply a username and password that is used as basic authentication.  You can either pass the username and password into the constructor for the client, or put it in your \~/.netrc file (\~\\_netrc on Windows).  (Note that the username and password you use to log in to the web site won't work here.  It has to be an API key that you create after logging in)

Sample .netrc file:

    machine www.foundationmercury.com
    login myapiusername
    password myapipassword

Installation:

    pip3 install fmapi

Sample usage:

    import fmapi

    client = fmapi.Client()
    


