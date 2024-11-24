import sqlite3
from flask import Flask, Blueprint, render_template, request, redirect, url_for
import models.tests.test_eval
from models.tests.test_eval.L2_ADULT.ANGER import evaluate_test as L2_ADULT_ANGER
from models.tests.test_eval.L2_ADULT.ANXIETY import evaluate_test as L2_ADULT_ANXIETY
# from models.tests.test_eval.L2_ADULT.DEPRESSION import evaluate_test as L2_ADULT_DEPRESSION
# from models.tests.test_eval.L2_ADULT.MANIA import evaluate_test as L2_ADULT_MANIA
# from models.tests.test_eval.L2_ADULT.RT_B import evaluate_test as L2_ADULT_RT_B
# from models.tests.test_eval.L2_ADULT.SD import evaluate_test as L2_ADULT_SD
# from models.tests.test_eval.L2_ADULT.SU import evaluate_test as L2_ADULT_SU
# from models.tests.test_eval.L2_ADULT.SS import evaluate_test as L2_ADULT_SS

# from models.tests.test_eval.L2_CHILD.ANGER import evaluate_test as L2_CHILD_ANGER
# from models.tests.test_eval.L2_CHILD.ANXIETY import evaluate_test as L2_CHILD_ANXIETY
# from models.tests.test_eval.L2_CHILD.DEPRESSION import evaluate_test as L2_CHILD_DE
# from models.tests.test_eval.L2_CHILD.MANIA import evaluate_test as L2_CHILD_MANIA
# from models.tests.test_eval.L2_CHILD.RT_B import evaluate_test as L2_CHILD_RT_B
# from models.tests.test_eval.L2_CHILD.SD import evaluate_test as L2_CHILD_SD
# from models.tests.test_eval.L2_CHILD.SU import evaluate_test as L2_CHILD_SU
# from models.tests.test_eval.L2_CHILD.SS import evaluate_test as L2_CHILD_SS


# from models.tests.test_eval.L2_PARENT.ANGER import evaluate_test as L2_PARENT_ANGER
# from models.tests.test_eval.L2_PARENT.ANXIETY import evaluate_test as L2_PARENT_ANXIETY
# from models.tests.test_eval.L2_PARENT.DEPRESSION import evaluate_test as L2_PARENT_DE
# from models.tests.test_eval.L2_PARENT.MANIA import evaluate_test as L2_PARENT_MANIA
# from models.tests.test_eval.L2_PARENT.RT_B import evaluate_test as L2_PARENT_RT_B   
# from models.tests.test_eval.L2_PARENT.SD import evaluate_test as L2_PARENT_SD
# from models.tests.test_eval.L2_PARENT.SU import evaluate_test as L2_PARENT_SU
# from models.tests.test_eval.L2_PARENT.SS import evaluate_test as L2_PARENT_SS



test_routes = Blueprint('test_routes', __name__, template_folder='templates')

@test_routes.route('/PID', methods=['GET', 'POST'])
def test_pid():
    if request.method == 'POST':
        responses = []
        for i in range(1, 221):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT Qno, Question FROM PID_FULL")
        data = c.fetchall()
        conn.close()
        return render_template('test_pid.html', data=data)
    

@test_routes.route('/L1/<category>', methods=['GET', 'POST'])
def level_1(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT Qno, Question FROM L1_{category}")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_1.html', data=data, category=category)
    

@test_routes.route('/L2/<category>/<test_exam>', methods=['GET', 'POST'])
def level_2(category, test_exam):
    responses = []  # Initialize responses at function start
    try:
        if request.method == 'POST':
            # Collect responses
            for i in range(1, 6):  # Assuming 5 questions
                answer = request.form.get(f'q{i}')
                if answer is not None:
                    responses.append(int(answer))

            # Process responses based on category and test_exam
            result = None
            if category == 'ADULT':
                if test_exam == 'ANGER':
                    result = L2_ADULT_ANGER(responses)
                elif test_exam == 'ANXIETY':
                    result = L2_ADULT_ANXIETY(responses)
                # ...other conditions...

            # Return result template
            if result:
                return render_template('test_result.html', 
                                    result=result,
                                    category=category,
                                    test_exam=test_exam)
            
        # Handle GET request
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT Qno, Question FROM L2_{category}_{test_exam}")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_2.html', 
                             data=data,
                             category=category,
                             test_exam=test_exam)
                             
    except Exception as e:
        print(f"Error in level_2: {str(e)}")
        return redirect(url_for('index'))
    

@test_routes.route('/L2/<category>/MANIA', methods=['GET', 'POST'])
def level_2_mania(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM L2_{category}_MANIA")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_2_mania.html', data=data, category=category)
    
@test_routes.route('/L2/<category>/RT_B', methods=['GET', 'POST'])
def level_2_rt_b(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM L2_{category}_RT_B")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_2_rt_b.html', data=data, category=category)
    
@test_routes.route('/L2/<category>/SD', methods=['GET', 'POST'])
def level_2_sd(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM L2_{category}_SD")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_2_sd.html', data=data, category=category)
    
@test_routes.route('/L2/<category>/SU', methods=['GET', 'POST'])
def level_2_su(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM L2_{category}_SU")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_2_su.html', data=data, category=category)
    
@test_routes.route('/L2/<category>/SS', methods=['GET', 'POST'])
def level_2_ss(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM L2_{category}_SS")
        data = c.fetchall()
        conn.close()
        return render_template('test_level_2_ss.html', data=data, category=category)
    
@test_routes.route('/SMD5/<category>', methods=['GET', 'POST'])
def smd5(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM SMD_{category}")
        data = c.fetchall()
        conn.close()
        return render_template('smd_1.html', data=data, category=category)
    

@test_routes.route('/SMD4/<category>', methods=['GET', 'POST'])
def smd4(category):
    if request.method == 'POST':
        responses = []
        for i in range(1, 26):
            answer = request.form.get(f'q{i}')
            if answer is not None:
                responses.append(int(answer))
        # ...process responses...
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('wellnest01.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(f"SELECT * FROM SMD_{category}")
        data = c.fetchall()
        conn.close()
        return render_template('smd_1.html', data=data, category=category)

