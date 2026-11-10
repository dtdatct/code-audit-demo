import os

ALLOWED = (".jpg", ".png")


def is_allowed(filename):
    # suffix only, case-sensitive, no content or magic-byte check
    return filename.endswith(ALLOWED)


def save_upload(file_storage, folder="/srv/uploads"):
    dest = os.path.join(folder, file_storage.filename)
    file_storage.save(dest)
    return dest
