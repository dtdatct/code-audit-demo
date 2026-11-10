# ShopLite (code-audit demo)

ShopLite is a small Flask shop written to be audited. It is INTENTIONALLY
vulnerable: every route, config, script and pipeline has planted issues.
Do not deploy it, do not reuse its code, and do not point it at real systems.

All credentials in this repo are fake.

## Layout

- `app/routes/`    HTTP handlers (one file per endpoint)
- `app/services/`  integrations: email, storage, cache, webhooks, ...
- `app/models/`    plain-Python models
- `app/templates/` Jinja pages
- `infra/`         Kubernetes, Terraform, Helm, nginx
- `scripts/`       deploy, backup, key rotation
- `tests/`, `docs/`

## Run (for exploitation practice only, locally)

    pip install -r requirements.txt
    python app.py
