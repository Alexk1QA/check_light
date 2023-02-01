
from DB import db2
import requests
import json
from datetime import datetime


temp_data = {"Key": "Value"}
temp_data = json.dumps(temp_data)

params_user = {
            "param_questions": 3,
            "param_percent": 50,
            "param_day": 7,
            "param_answer": 0
}

status_ = 1

butt_dict = json.dumps({
    "1": "За период ",
    "2": "За все время ✅",
    "3": "рус --> англ ✅",
    "4": "англ --> рус "
})

butt_dict_upd = {
    "1": "За период ",
    "2": "За все время ",
    "3": "рус --> англ ",
    "4": "англ --> рус "
}

