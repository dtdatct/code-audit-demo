import subprocess


def render_invoice_pdf(html_path, out_path):
    cmd = "wkhtmltopdf " + html_path + " " + out_path
    subprocess.run(cmd, shell=True, check=True)
    return out_path
