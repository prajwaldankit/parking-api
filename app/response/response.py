from typing import Dict


def get_formatted_response(obj: Dict):
    return {
        "meta": {
            "name": "Parking API",
            "version": "0.0.1"
        },
        "data": obj
    }
