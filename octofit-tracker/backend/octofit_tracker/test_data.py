from bson import ObjectId

test_users = [
    {"_id": ObjectId(), "username": "ironman", "email": "ironman@octofit.edu", "password": "ironmanpassword"},
    {"_id": ObjectId(), "username": "blackwidow", "email": "blackwidow@octofit.edu", "password": "blackwidowpassword"},
    {"_id": ObjectId(), "username": "hulk", "email": "hulk@octofit.edu", "password": "hulkpassword"},
    {"_id": ObjectId(), "username": "hawkeye", "email": "hawkeye@octofit.edu", "password": "hawkeyepassword"},
    {"_id": ObjectId(), "username": "thor", "email": "thor@octofit.edu", "password": "thorpassword"},
]

test_teams = [
    {"_id": ObjectId(), "name": "Red Team", "members": []},
    {"_id": ObjectId(), "name": "Green Team", "members": []},
]

test_activities = [
    {"_id": ObjectId(), "user": None, "activity_type": "Yoga", "duration": 45, "date": "2025-04-01"},
    {"_id": ObjectId(), "user": None, "activity_type": "Pilates", "duration": 60, "date": "2025-04-02"},
    {"_id": ObjectId(), "user": None, "activity_type": "Running", "duration": 30, "date": "2025-04-03"},
    {"_id": ObjectId(), "user": None, "activity_type": "Weightlifting", "duration": 90, "date": "2025-04-04"},
    {"_id": ObjectId(), "user": None, "activity_type": "Swimming", "duration": 120, "date": "2025-04-05"},
]

test_leaderboard = [
    {"_id": ObjectId(), "team": None, "points": 150},
    {"_id": ObjectId(), "team": None, "points": 120},
]

test_workouts = [
    {"_id": ObjectId(), "name": "Yoga Basics", "description": "Beginner yoga session", "difficulty": "Beginner"},
    {"_id": ObjectId(), "name": "Pilates Core", "description": "Core strengthening pilates", "difficulty": "Intermediate"},
    {"_id": ObjectId(), "name": "Running Endurance", "description": "Endurance training for runners", "difficulty": "Intermediate"},
    {"_id": ObjectId(), "name": "Weightlifting 101", "description": "Introduction to weightlifting", "difficulty": "Beginner"},
    {"_id": ObjectId(), "name": "Swimming Drills", "description": "Advanced swimming techniques", "difficulty": "Advanced"},
]