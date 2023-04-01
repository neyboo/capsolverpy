from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "ReCaptchaV3TaskProxyLess", "websiteKey": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-","websiteURL": "https://www.google.com/recaptcha/api2/demo", "pageAction": "login", "minScore": 0.7}})
print(Captcha)