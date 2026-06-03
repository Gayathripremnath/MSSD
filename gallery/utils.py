import requests

def verify_captcha(token):
    secret_key = "YOUR_SECRET_KEY"

    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={
            "secret": "6Lf77wYtAAAAAKEVMUPHpiU0x2amLBeNdhvZQ9vF",
            "response": token
        }
    )
   
    return response.json().get("success", False)