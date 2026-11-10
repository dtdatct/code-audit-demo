import ldap  # python-ldap


def find_user(conn, username):
    query = "(&(objectClass=person)(uid=" + username + "))"
    return conn.search_s("ou=people,dc=shoplite,dc=local", ldap.SCOPE_SUBTREE, query)
