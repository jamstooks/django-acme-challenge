# django-acme-challenge

[![Build Status](https://travis-ci.org/jamstooks/django-acme-challenge.svg?branch=master)](https://travis-ci.org/jamstooks/django-acme-challenge)

A quick tool to serve the acme-challenge verification page. When creating an SSL certificate with Let's Encrypt, you need to serve a page that they request to confirm you own the site:

    Make sure your web server displays the following content at
    http://your-domain-name/.well-known/acme-challenge/l9msb_LONG_STRING before continuing:

    l9msb_LONG_STRING.LONG_STRING

This app provides a quick way to serve and update that page from two settings variables.

## Installation

PyPI:

    pip install django-acme-challenge
    
Github:

    pip install https://github.com/jamstooks/django-acme-challenge/archive/v1.2.zip

### Settings

Add `'acme_challenge',` to your installed apps and update your urls.py:

    url(r'^.well-known/acme-challenge/', include('acme_challenge.urls')),

Just set two variables (I like to assign these with env vars, personally):

  - `ACME_CHALLENGE_URL_SLUG`
  - `ACME_CHALLENGE_TEMPLATE_CONTENT`
  
`http://your-domain-name/.well-known/acme-challenge/ACME_CHALLENGE_URL_SLUG`
will then serve the value of `ACME_CHALLENGE_TEMPLATE_CONTENT`
for validation.

### Compatibility

Support Django 1.8 - 2.0 and Python 2 & 3