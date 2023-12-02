#Example Modules Design

from flask import Blueprint, render_template
examples_ui = Blueprint('examples_ui', __name__)

@examples_ui.route('/advanced-alertify.html', methods=['GET', 'POST'])
def advanced_alertify():
    return render_template('example/advanced-alertify.html')


@examples_ui.route('/advanced-animation.html', methods=['GET', 'POST'])
def advanced_animation():
    return render_template('example/advanced-animation.html')


@examples_ui.route('/advanced-highlight.html', methods=['GET', 'POST'])
def advanced_highlight():
    return render_template('example/advanced-highlight.html')


@examples_ui.route('/advanced-nestable.html', methods=['GET', 'POST'])
def advanced_nestable():
    return render_template('example/advanced-nestable.html')


@examples_ui.route('/advanced-rangeslider.html', methods=['GET', 'POST'])
def advanced_rangeslider():
    return render_template('example/advanced-rangeslider.html')


@examples_ui.route('/advanced-rating.html', methods=['GET', 'POST'])
def advanced_rating():
    return render_template('example/advanced-rating.html')


@examples_ui.route('/advanced-sessiontimeout.html', methods=['GET', 'POST'])
def advanced_sessiontimeout():
    return render_template('example/advanced-sessiontimeout.html')


@examples_ui.route('/calendar.html', methods=['GET', 'POST'])
def calendar():
    return render_template('example/calendar.html')


@examples_ui.route('/charts-c3.html', methods=['GET', 'POST'])
def charts_c3():
    return render_template('example/charts-c3.html')


@examples_ui.route('/charts-chartist.html', methods=['GET', 'POST'])
def charts_chartist():
    return render_template('example/charts-chartist.html')


@examples_ui.route('/charts-chartjs.html', methods=['GET', 'POST'])
def charts_chartjs():
    return render_template('example/charts-chartjs.html')


@examples_ui.route('/charts-flot.html', methods=['GET', 'POST'])
def charts_flot():
    return render_template('example/charts-flot.html')


@examples_ui.route('/charts-morris.html', methods=['GET', 'POST'])
def charts_morris():
    return render_template('example/charts-morris.html')


@examples_ui.route('/charts-other.html', methods=['GET', 'POST'])
def charts_other():
    return render_template('example/charts-other.html')


@examples_ui.route('/form-advanced.html', methods=['GET', 'POST'])
def form_advanced():
    return render_template('example/form-advanced.html')


@examples_ui.route('/form-editors.html', methods=['GET', 'POST'])
def form_editors():
    return render_template('example/form-editors.html')


@examples_ui.route('/form-elements.html', methods=['GET', 'POST'])
def form_elements():
    return render_template('example/form-elements.html')


@examples_ui.route('/form-mask.html', methods=['GET', 'POST'])
def form_mask():
    return render_template('example/form-mask.html')


@examples_ui.route('/form-summernote.html', methods=['GET', 'POST'])
def form_summernote():
    return render_template('example/form-summernote.html')


@examples_ui.route('/form-uploads.html', methods=['GET', 'POST'])
def form_uploads():
    return render_template('example/form-uploads.html')


@examples_ui.route('/form-validation.html', methods=['GET', 'POST'])
def form_validation():
    return render_template('example/form-validation.html')


@examples_ui.route('/form-xeditable.html', methods=['GET', 'POST'])
def form_xeditable():
    return render_template('example/form-xeditable.html')


@examples_ui.route('/icons-dripicons.html', methods=['GET', 'POST'])
def icons_dripicons():
    return render_template('example/icons-dripicons.html')


@examples_ui.route('/icons-fontawesome.html', methods=['GET', 'POST'])
def icons_fontawesome():
    return render_template('example/icons-fontawesome.html')


@examples_ui.route('/icons-ion.html', methods=['GET', 'POST'])
def icons_ion():
    return render_template('example/icons-ion.html')


@examples_ui.route('/icons-material.html', methods=['GET', 'POST'])
def icons_material():
    return render_template('example/icons-material.html')


@examples_ui.route('/icons-themify.html', methods=['GET', 'POST'])
def icons_themify():
    return render_template('example/icons-themify.html')


@examples_ui.route('/icons-typicons.html', methods=['GET', 'POST'])
def icons_typicons():
    return render_template('example/icons-typicons.html')


@examples_ui.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('example/index.html')


@examples_ui.route('/maps-google.html', methods=['GET', 'POST'])
def maps_google():
    return render_template('example/maps-google.html')


@examples_ui.route('/maps-vector.html', methods=['GET', 'POST'])
def maps_vector():
    return render_template('example/maps-vector.html')


@examples_ui.route('/pages-404.html', methods=['GET', 'POST'])
def pages_404():
    return render_template('example/pages-404.html')


@examples_ui.route('/pages-500.html', methods=['GET', 'POST'])
def pages_500():
    return render_template('example/pages-500.html')


@examples_ui.route('/pages-blank.html', methods=['GET', 'POST'])
def pages_blank():
    return render_template('example/pages-blank.html')


@examples_ui.route('/pages-directory.html', methods=['GET', 'POST'])
def pages_directory():
    return render_template('example/pages-directory.html')


@examples_ui.route('/pages-invoice.html', methods=['GET', 'POST'])
def pages_invoice():
    return render_template('example/pages-invoice.html')


@examples_ui.route('/pages-lock-screen.html', methods=['GET', 'POST'])
def pages_lock_screen():
    return render_template('example/pages-lock-screen.html')


@examples_ui.route('/pages-login.html', methods=['GET', 'POST'])
def pages_login():
    return render_template('example/pages-login.html')


@examples_ui.route('/pages-recoverpw.html', methods=['GET', 'POST'])
def pages_recoverpw():
    return render_template('example/pages-recoverpw.html')


@examples_ui.route('/pages-register.html', methods=['GET', 'POST'])
def pages_register():
    return render_template('example/pages-register.html')


@examples_ui.route('/pages-timeline.html', methods=['GET', 'POST'])
def pages_timeline():
    return render_template('example/pages-timeline.html')


@examples_ui.route('/tables-basic.html', methods=['GET', 'POST'])
def tables_basic():
    return render_template('example/tables-basic.html')


@examples_ui.route('/tables-datatable.html', methods=['GET', 'POST'])
def tables_datatable():
    return render_template('example/tables-datatable.html')


@examples_ui.route('/tables-editable.html', methods=['GET', 'POST'])
def tables_editable():
    return render_template('example/tables-editable.html')


@examples_ui.route('/tables-responsive.html', methods=['GET', 'POST'])
def tables_responsive():
    return render_template('example/tables-responsive.html')


@examples_ui.route('/ui-alerts.html', methods=['GET', 'POST'])
def ui_alerts():
    return render_template('example/ui-alerts.html')


@examples_ui.route('/ui-badge.html', methods=['GET', 'POST'])
def ui_badge():
    return render_template('example/ui-badge.html')


@examples_ui.route('/ui-buttons.html', methods=['GET', 'POST'])
def ui_buttons():
    return render_template('example/ui-buttons.html')


@examples_ui.route('/ui-cards.html', methods=['GET', 'POST'])
def ui_cards():
    return render_template('example/ui-cards.html')


@examples_ui.route('/ui-carousel.html', methods=['GET', 'POST'])
def ui_carousel():
    return render_template('example/ui-carousel.html')


@examples_ui.route('/ui-dropdowns.html', methods=['GET', 'POST'])
def ui_dropdowns():
    return render_template('example/ui-dropdowns.html')


@examples_ui.route('/ui-grid.html', methods=['GET', 'POST'])
def ui_grid():
    return render_template('example/ui-grid.html')


@examples_ui.route('/ui-images.html', methods=['GET', 'POST'])
def ui_images():
    return render_template('example/ui-images.html')


@examples_ui.route('/ui-lightbox.html', methods=['GET', 'POST'])
def ui_lightbox():
    return render_template('example/ui-lightbox.html')


@examples_ui.route('/ui-modals.html', methods=['GET', 'POST'])
def ui_modals():
    return render_template('example/ui-modals.html')


@examples_ui.route('/ui-navs.html', methods=['GET', 'POST'])
def ui_navs():
    return render_template('example/ui-navs.html')


@examples_ui.route('/ui-pagination.html', methods=['GET', 'POST'])
def ui_pagination():
    return render_template('example/ui-pagination.html')


@examples_ui.route('/ui-popover-tooltips.html', methods=['GET', 'POST'])
def ui_popover_tooltips():
    return render_template('example/ui-popover-tooltips.html')


@examples_ui.route('/ui-progressbars.html', methods=['GET', 'POST'])
def ui_progressbars():
    return render_template('example/ui-progressbars.html')


@examples_ui.route('/ui-sweet-alert.html', methods=['GET', 'POST'])
def ui_sweet_alert():
    return render_template('example/ui-sweet-alert.html')


@examples_ui.route('/ui-tabs-accordions.html', methods=['GET', 'POST'])
def ui_tabs_accordions():
    return render_template('example/ui-tabs-accordions.html')


@examples_ui.route('/ui-typography.html', methods=['GET', 'POST'])
def ui_typography():
    return render_template('example/ui-typography.html')


@examples_ui.route('/ui-video.html', methods=['GET', 'POST'])
def ui_video():
    return render_template('example/ui-video.html')

