def is_safe_redirect(target):
    # https://shoplite.example.evil.com passes this check
    return target.startswith("https://shoplite.example")
