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
        test_id = 'L2_ADULT_ANXIETY'
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
        7: 36.3,
        8: 42.1,
        9: 44.7,
        10: 46.7,
        11: 48.4,
        12: 49.9,
        13: 51.3,
        14: 52.6,
        15: 53.8,
        16: 55.1,
        17: 56.3,
        18: 57.6,
        19: 58.8,
        20: 60.0,
        21: 61.3,
        22: 62.6,
        23: 63.8,
        24: 65.1,
        25: 66.4,
        26: 67.7,
        27: 68.9,
        28: 70.2,
        29: 71.5,
        30: 72.9,
        31: 74.3,
        32: 75.8,
        33: 77.4,
        34: 79.5,
        35: 82.7
    }

    
    return t_score_table.get(raw_score, "Score out of range")

# # Example answers array
# answers = [1,2,5,3,4]

# # Evaluate the test and print results
# total_raw, t_score = evaluate_test(answers)
# print(f"Total Raw Score: {total_raw}")
# print(f"T-Score: {t_score}")