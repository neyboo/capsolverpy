from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "FunCaptchaTaskProxyLess", "websitePublicKey": "","websiteURL": ""}})
print(Captcha)