SECRET_KEY = "secret!"

ROOT_URLCONF='acme_challenge.urls'

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS=(
    'acme_challenge',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]
    