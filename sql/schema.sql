CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    signup_date TEXT,
    user_segment TEXT,
    device_type TEXT,
    acquisition_channel TEXT
);

CREATE TABLE experiment_assignments (
    user_id INTEGER,
    experiment_name TEXT,
    variant TEXT,  -- 'control' or 'treatment'
    assignment_time TEXT
);

CREATE TABLE bank_links (
    user_id INTEGER,
    link_date TEXT,
    link_success INTEGER  -- 1 = success, 0 = failure
);

CREATE TABLE deposits (
    user_id INTEGER,
    deposit_date TEXT,
    amount REAL,
    deposit_success INTEGER  -- 1 = success, 0 = failure
);

