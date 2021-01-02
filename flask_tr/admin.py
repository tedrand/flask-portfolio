from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flask_tr.auth import login_required

bp = Blueprint('admin', __name__)

@bp.route('/admin', methods=['GET'])
@login_required
def admin():
    return render_template('admin/index.html')