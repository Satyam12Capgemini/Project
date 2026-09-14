import json
import re


def parse_json_response(text: str):
    try:
        return json.loads(text)

    except Exception:

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if match:
            try:
                return json.loads(match.group())
            except Exception:
                pass

    return {
        "raw_response": text
    }