# CapSolver.com Python Package
[CapSolver.com](https://capsolver.com) Package for Python

Register For an Account here: [You Get Free Balance!](https://dashboard.capsolver.com/passport/register?inviteCode=RDIXzCKSntoQ)

# Installation
```bash
pip install CapSolverPy
```

# Supported Tasks
* hCaptcha - HCaptchaTask, HCaptchaTaskProxyLess, HCaptchaEnterpriseTask, HCaptchaEnterpriseTaskProxyLess, HCaptchaTurboTask
* reCaptchaV2 - ReCaptchaV2Task, ReCaptchaV2TaskProxyLess, ReCaptchaV2EnterpriseTask, ReCaptchaV2EnterpriseTaskProxyLess
* reCaptchaV3 - ReCaptchaV3Task, ReCaptchaV3TaskProxyLess, ReCaptchaV3EnterpriseTask, ReCaptchaV3EnterpriseTaskProxyLess
* FunCaptcha - FunCaptchaTask, FunCaptchaTaskProxyless
* MtCaptcha - MtCaptchaTask, MtCaptchaTaskProxyless
* Cloudflare - Turnstile
* Cloudflare - IUAM/UAM Challenge 

# Usage Examples
**hCaptcha - HCaptchaTaskProxyless**
```bash
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "HcaptchaTaskProxyless", "websiteKey": "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2","websiteURL": "https://accounts.hcaptcha.com/demo"}})
print(Captcha)
```
