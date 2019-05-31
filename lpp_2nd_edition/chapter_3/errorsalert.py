# errorsalert.py
alert_system = "email"  # other value can be email
error_severity = "critical"  # other values: 'medium' or 'low'
error_message = "OMG! Something terrible happened!"


def send_email(email, error_message):
    print(f"Sending email to {email}, with the error message {error_message}")


if alert_system == "console":
    print(error_message)
elif alert_system == "email":
    email = ""
    if error_severity == "critical":
        email = "admin@example.com"
    elif error_severity == "medium":
        email = "support.1@example.com"
    else:
        email = "support.2@example.com"
    send_email(email, error_message)
