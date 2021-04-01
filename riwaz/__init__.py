# import pymysql
# pymysql.version_info = (1, 3, 13, "final", 0)
# pymysql.install_as_MySQLdb()

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
# from sentry_sdk.integrations.logging import LoggingIntegration
# import logging
# # All of this is already happening by default!
# sentry_logging = LoggingIntegration(
#     level=logging.INFO,        # Capture info and above as breadcrumbs
#     event_level=logging.ERROR  # Send errors as events
# )

# sentry_sdk.init(
#     dsn="https://d252f4135ae345428c50720adb27bb79@o434518.ingest.sentry.io/5391674",
#     integrations=[DjangoIntegration()],

#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )