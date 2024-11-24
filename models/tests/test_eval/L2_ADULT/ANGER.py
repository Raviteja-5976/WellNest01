import sqlite3
from flask import session
import datetime

def evaluate_test(answers):
    conn = sqlite3.connect('wellnest01.db')
    cursor = conn.cursor()
    
    # Calculate scores
    scoring = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    total_raw_score = sum(scoring[answer] for answer in answers)
    t_score = calculate_t_score(total_raw_score)
    
    # Determine result category
    if t_score < 55:
        result = 'None'
    elif 55 <= t_score < 60:
        result = 'Mild'
    elif 60 <= t_score < 70:
        result = 'Moderate'
    else:
        result = 'Severe'

    # Store results in database
    try:
        username = session.get('user')
        test_id = 'L2_ADULT_ANGER'
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(f'''INSERT INTO {username}_test_result 
                         (test_id, test_result, date)
                         VALUES (?, ?, ?)''',
                      (test_id,result, date))
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
        conn.rollback()
    finally:
        conn.close()
    
    return total_raw_score, t_score, result

# Function to calculate T-score based on raw score
def calculate_t_score(raw_score):
    t_score_table = {
        5: 32.9,
        6: 38.1,
        7: 41.3,
        8: 44.0,
        9: 46.3,
        10: 48.4,
        11: 50.5,
        12: 52.6,
        13: 54.7,
        14: 56.7,
        15: 58.8,
        16: 60.8,
        17: 62.9,
        18: 65.0,
        19: 67.2,
        20: 69.4,
        21: 71.7,
        22: 74.1,
        23: 76.8,
        24: 79.7,
        25: 83.3
    }

    
    return t_score_table.get(raw_score, "Score out of range")

# # Example answers array
# answers = [1,2,5,3,4]

# # Evaluate the test and print results
# total_raw, t_score = evaluate_test(answers)
# print(f"Total Raw Score: {total_raw}")
# print(f"T-Score: {t_score}")