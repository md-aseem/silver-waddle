from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

core_bp = Blueprint("core", __name__)

@core_bp.route("/")
@login_required
def home():
    file_path = os.path.join('/var/www/html/myflaskapp/files', current_user.email.split("@")[0] + "_" + current_user.file_path)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
    except Exception as e:
        file_content = f"Error reading file: {e}"

    # Passing the file content to the template
    return render_template("core/index.html", file_content=file_content)

