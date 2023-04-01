from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "HcaptchaTaskProxyless", "websiteKey": "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2","websiteURL": "https://accounts.hcaptcha.com/demo"}})
print(Captcha)