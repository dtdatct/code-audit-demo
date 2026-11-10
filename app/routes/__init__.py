from app.routes.search_products import bp as search_products
from app.routes.login_bypass import bp as login_bypass
from app.routes.comment_xss import bp as comment_xss
from app.routes.template_greet import bp as template_greet
from app.routes.ping_host import bp as ping_host
from app.routes.convert_image import bp as convert_image
from app.routes.download_file import bp as download_file
from app.routes.fetch_remote import bp as fetch_remote
from app.routes.go_redirect import bp as go_redirect
from app.routes.invoice_detail import bp as invoice_detail
from app.routes.session_restore import bp as session_restore
from app.routes.import_config import bp as import_config
from app.routes.calc_expr import bp as calc_expr
from app.routes.xml_import import bp as xml_import
from app.routes.transfer_funds import bp as transfer_funds
from app.routes.update_profile import bp as update_profile
from app.routes.reset_password import bp as reset_password
from app.routes.register_user import bp as register_user
from app.routes.token_verify import bp as token_verify
from app.routes.upload_avatar import bp as upload_avatar
from app.routes.render_preview import bp as render_preview
from app.routes.auth_log import bp as auth_log
from app.routes.debug_env import bp as debug_env
from app.routes.admin_users import bp as admin_users
from app.routes.validate_email import bp as validate_email
from app.routes.set_prefs_cookie import bp as set_prefs_cookie
from app.routes.api_me import bp as api_me
from app.routes.admin_login import bp as admin_login

ALL_BLUEPRINTS = [
    search_products,
    login_bypass,
    comment_xss,
    template_greet,
    ping_host,
    convert_image,
    download_file,
    fetch_remote,
    go_redirect,
    invoice_detail,
    session_restore,
    import_config,
    calc_expr,
    xml_import,
    transfer_funds,
    update_profile,
    reset_password,
    register_user,
    token_verify,
    upload_avatar,
    render_preview,
    auth_log,
    debug_env,
    admin_users,
    validate_email,
    set_prefs_cookie,
    api_me,
    admin_login,
]
