import django
from django.conf import settings


def main():
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        ROOT_URLCONF='acme_challenge.urls',
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'acme_challenge',)
    )
    
    django.setup()
    try:
        # Django <= 1.8
        from django.test.simple import DjangoTestSuiteRunner
        test_runner = DjangoTestSuiteRunner(verbosity=1)
    except ImportError:
        # Django >= 1.8
        from django.test.runner import DiscoverRunner
        test_runner = DiscoverRunner(verbosity=1)
        
    failures = test_runner.run_tests(['acme_challenge'])
    if failures:
        sys.exit(failures)

if __name__ == '__main__':
    main()