import re
import uuid
import secrets
import string
import random
import hashlib
import sys


def validate_uuid4(uuid_string):
    try:
        val = uuid.UUID(str(uuid_string))
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False

    return True


def camel_to_snake(x):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', x)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '_', s)

    return s.lower()


def generate_password(password_size=20):
    alphabet = string.ascii_letters + string.digits

    return ''.join(secrets.choice(alphabet) for i in range(password_size))


def get_user_ip(req):
    if req.headers.getlist("X-Forwarded-For"):
        ip_addr = req.headers.getlist("X-Forwarded-For")[0]
    else:
        ip_addr = req.remote_addr

    return ip_addr


def get_random_id():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))


def sha1(email):
    hash_object = hashlib.sha1(email.encode('utf-8'))
    hex_dig = hash_object.hexdigest()

    return hex_dig


def print_progress_bar(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def list_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_month_name(month_number):
    month_number = int(month_number)

    if month_number == 1: return "January"
    if month_number == 2: return "February"
    if month_number == 3: return "March"
    if month_number == 4: return "April"
    if month_number == 5: return "May"
    if month_number == 6: return "June"
    if month_number == 7: return "July"
    if month_number == 8: return "August"
    if month_number == 9: return "September"
    if month_number == 10: return "October"
    if month_number == 11: return "November"
    if month_number == 12: return "December"


def to_human_date(input_date):
    date_splitted = str(input_date).split("-")

    return "%s %s, %s" % (
        get_month_name(date_splitted[1]),
        date_splitted[2],
        date_splitted[0]
    )
