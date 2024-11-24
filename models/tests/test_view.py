from flask import Blueprint, render_template

test_view = Blueprint('test_view', __name__, template_folder='templates')

@test_view.route('/test')
def test_main():
    return render_template('test_adult.html')

@test_view.route('/adult/view')
def adult_test():
    return render_template('test_adult.html')

@test_view.route('/child/view')
def child():
    return render_template('test_child_parent.html')


