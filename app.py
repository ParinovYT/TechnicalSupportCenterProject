import random
import re
import secrets
import string

from flask import Flask, render_template, request

from src.config import load_configurate
from src.core.classes.user import User

cfg = load_configurate('src/config.json')

app = Flask(__name__, static_url_path="/assets", static_folder='assets')


def generate_password():
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W]).{8,64}$'

    while True:
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in
                           range(random.randint(8, 64)))
        if re.match(pattern, password):
            return password


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

#Example Modules Design

@app.route('/advanced-alertify.html', methods=['GET', 'POST'])
def advanced_alertify():
    return render_template('advanced-alertify.html')


@app.route('/advanced-animation.html', methods=['GET', 'POST'])
def advanced_animation():
    return render_template('advanced-animation.html')


@app.route('/advanced-highlight.html', methods=['GET', 'POST'])
def advanced_highlight():
    return render_template('advanced-highlight.html')


@app.route('/advanced-nestable.html', methods=['GET', 'POST'])
def advanced_nestable():
    return render_template('advanced-nestable.html')


@app.route('/advanced-rangeslider.html', methods=['GET', 'POST'])
def advanced_rangeslider():
    return render_template('advanced-rangeslider.html')


@app.route('/advanced-rating.html', methods=['GET', 'POST'])
def advanced_rating():
    return render_template('advanced-rating.html')


@app.route('/advanced-sessiontimeout.html', methods=['GET', 'POST'])
def advanced_sessiontimeout():
    return render_template('advanced-sessiontimeout.html')


@app.route('/calendar.html', methods=['GET', 'POST'])
def calendar():
    return render_template('calendar.html')


@app.route('/charts-c3.html', methods=['GET', 'POST'])
def charts_c3():
    return render_template('charts-c3.html')


@app.route('/charts-chartist.html', methods=['GET', 'POST'])
def charts_chartist():
    return render_template('charts-chartist.html')


@app.route('/charts-chartjs.html', methods=['GET', 'POST'])
def charts_chartjs():
    return render_template('charts-chartjs.html')


@app.route('/charts-flot.html', methods=['GET', 'POST'])
def charts_flot():
    return render_template('charts-flot.html')


@app.route('/charts-morris.html', methods=['GET', 'POST'])
def charts_morris():
    return render_template('charts-morris.html')


@app.route('/charts-other.html', methods=['GET', 'POST'])
def charts_other():
    return render_template('charts-other.html')


@app.route('/form-advanced.html', methods=['GET', 'POST'])
def form_advanced():
    return render_template('form-advanced.html')


@app.route('/form-editors.html', methods=['GET', 'POST'])
def form_editors():
    return render_template('form-editors.html')


@app.route('/form-elements.html', methods=['GET', 'POST'])
def form_elements():
    return render_template('form-elements.html')


@app.route('/form-mask.html', methods=['GET', 'POST'])
def form_mask():
    return render_template('form-mask.html')


@app.route('/form-summernote.html', methods=['GET', 'POST'])
def form_summernote():
    return render_template('form-summernote.html')


@app.route('/form-uploads.html', methods=['GET', 'POST'])
def form_uploads():
    return render_template('form-uploads.html')


@app.route('/form-validation.html', methods=['GET', 'POST'])
def form_validation():
    return render_template('form-validation.html')


@app.route('/form-xeditable.html', methods=['GET', 'POST'])
def form_xeditable():
    return render_template('form-xeditable.html')


@app.route('/icons-dripicons.html', methods=['GET', 'POST'])
def icons_dripicons():
    return render_template('icons-dripicons.html')


@app.route('/icons-fontawesome.html', methods=['GET', 'POST'])
def icons_fontawesome():
    return render_template('icons-fontawesome.html')


@app.route('/icons-ion.html', methods=['GET', 'POST'])
def icons_ion():
    return render_template('icons-ion.html')


@app.route('/icons-material.html', methods=['GET', 'POST'])
def icons_material():
    return render_template('icons-material.html')


@app.route('/icons-themify.html', methods=['GET', 'POST'])
def icons_themify():
    return render_template('icons-themify.html')


@app.route('/icons-typicons.html', methods=['GET', 'POST'])
def icons_typicons():
    return render_template('icons-typicons.html')


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/maps-google.html', methods=['GET', 'POST'])
def maps_google():
    return render_template('maps-google.html')


@app.route('/maps-vector.html', methods=['GET', 'POST'])
def maps_vector():
    return render_template('maps-vector.html')


@app.route('/pages-404.html', methods=['GET', 'POST'])
def pages_404():
    return render_template('pages-404.html')


@app.route('/pages-500.html', methods=['GET', 'POST'])
def pages_500():
    return render_template('pages-500.html')


@app.route('/pages-blank.html', methods=['GET', 'POST'])
def pages_blank():
    return render_template('pages-blank.html')


@app.route('/pages-directory.html', methods=['GET', 'POST'])
def pages_directory():
    return render_template('pages-directory.html')


@app.route('/pages-invoice.html', methods=['GET', 'POST'])
def pages_invoice():
    return render_template('pages-invoice.html')


@app.route('/pages-lock-screen.html', methods=['GET', 'POST'])
def pages_lock_screen():
    return render_template('pages-lock-screen.html')


@app.route('/pages-login.html', methods=['GET', 'POST'])
def pages_login():
    return render_template('pages-login.html')


@app.route('/pages-recoverpw.html', methods=['GET', 'POST'])
def pages_recoverpw():
    return render_template('pages-recoverpw.html')


@app.route('/pages-register.html', methods=['GET', 'POST'])
def pages_register():
    return render_template('pages-register.html')


@app.route('/pages-timeline.html', methods=['GET', 'POST'])
def pages_timeline():
    return render_template('pages-timeline.html')


@app.route('/tables-basic.html', methods=['GET', 'POST'])
def tables_basic():
    return render_template('tables-basic.html')


@app.route('/tables-datatable.html', methods=['GET', 'POST'])
def tables_datatable():
    return render_template('tables-datatable.html')


@app.route('/tables-editable.html', methods=['GET', 'POST'])
def tables_editable():
    return render_template('tables-editable.html')


@app.route('/tables-responsive.html', methods=['GET', 'POST'])
def tables_responsive():
    return render_template('tables-responsive.html')


@app.route('/ui-alerts.html', methods=['GET', 'POST'])
def ui_alerts():
    return render_template('ui-alerts.html')


@app.route('/ui-badge.html', methods=['GET', 'POST'])
def ui_badge():
    return render_template('ui-badge.html')


@app.route('/ui-buttons.html', methods=['GET', 'POST'])
def ui_buttons():
    return render_template('ui-buttons.html')


@app.route('/ui-cards.html', methods=['GET', 'POST'])
def ui_cards():
    return render_template('ui-cards.html')


@app.route('/ui-carousel.html', methods=['GET', 'POST'])
def ui_carousel():
    return render_template('ui-carousel.html')


@app.route('/ui-dropdowns.html', methods=['GET', 'POST'])
def ui_dropdowns():
    return render_template('ui-dropdowns.html')


@app.route('/ui-grid.html', methods=['GET', 'POST'])
def ui_grid():
    return render_template('ui-grid.html')


@app.route('/ui-images.html', methods=['GET', 'POST'])
def ui_images():
    return render_template('ui-images.html')


@app.route('/ui-lightbox.html', methods=['GET', 'POST'])
def ui_lightbox():
    return render_template('ui-lightbox.html')


@app.route('/ui-modals.html', methods=['GET', 'POST'])
def ui_modals():
    return render_template('ui-modals.html')


@app.route('/ui-navs.html', methods=['GET', 'POST'])
def ui_navs():
    return render_template('ui-navs.html')


@app.route('/ui-pagination.html', methods=['GET', 'POST'])
def ui_pagination():
    return render_template('ui-pagination.html')


@app.route('/ui-popover-tooltips.html', methods=['GET', 'POST'])
def ui_popover_tooltips():
    return render_template('ui-popover-tooltips.html')


@app.route('/ui-progressbars.html', methods=['GET', 'POST'])
def ui_progressbars():
    return render_template('ui-progressbars.html')


@app.route('/ui-sweet-alert.html', methods=['GET', 'POST'])
def ui_sweet_alert():
    return render_template('ui-sweet-alert.html')


@app.route('/ui-tabs-accordions.html', methods=['GET', 'POST'])
def ui_tabs_accordions():
    return render_template('ui-tabs-accordions.html')


@app.route('/ui-typography.html', methods=['GET', 'POST'])
def ui_typography():
    return render_template('ui-typography.html')


@app.route('/ui-video.html', methods=['GET', 'POST'])
def ui_video():
    return render_template('ui-video.html')

#Example Modules DesignEND


@app.route('/login/<password>')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.args.get('passwordGenerate'):
        return render_template('login.html', password=generate_password())

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if request.form['submit_button'] == 'login':
            user_obj = User().sign_in()
            user_obj.execute(username, password, 60)

            statuscode = user_obj.status_code
            token = user_obj.get_token
            print(statuscode)
            if statuscode == 401:
                return 'Пользователь не найден'
            elif statuscode == 400:
                return 'Неверный логин или пароль!'
            elif statuscode == 200:
                return f'Добро пожаловать, {username}, статус {user_obj.status_code}, токен {user_obj.get_token}!'

        if request.form['submit_button'] == 'register':
            user_obj = User().sign_up()
            user_obj.execute(username, password)

            if (user_obj.status_code == 200):
                return f'Учетная запись с именем, {username}, создана!'

        return f'Неверные параметры POST'

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=cfg['server_host'], port=int(cfg['server_port']), debug=bool(cfg['server_debug']))
