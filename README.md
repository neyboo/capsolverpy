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
**hCaptcha - HCaptchaTaskProxyLess**
```python
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "HcaptchaTaskProxyless", "websiteKey": "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2","websiteURL": "https://accounts.hcaptcha.com/demo"}})
print(Captcha)
```
**ReCaptchaV2 - ReCaptchaV2TaskProxyLess**
```python
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "ReCaptchaV2TaskProxyLess", "websiteKey": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-","websiteURL": "https://www.google.com/recaptcha/api2/demo"}})
print(Captcha)
```
**ReCaptchaV3 - ReCaptchaV3TaskProxyLess**
```python
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "ReCaptchaV3TaskProxyLess", "websiteKey": "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-","websiteURL": "https://www.google.com/recaptcha/api2/demo", "pageAction": "login", minScore": 0.7}})
print(Captcha)
```
**FunCaptcha - FunCaptchaTaskProxyLess**
```python
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
Captcha = SolveCaptcha.solve({"task": {"type": "FunCaptchaTaskProxyLess", "websitePublicKey": "","websiteURL": ""}})
print(Captcha)
```
**Cloudflare - Turnstile**
```python
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
SolvedToken = SolveCaptcha.solve({"task": {"type": "AntiCloudflareTask", "websiteURL": "https://peet.ws/turnstile-test/non-interactive.html","websiteKey": "0x4AAAAAAABS7vwvV6VFfMcD", "metadata": {"type": "turnstile"}, "proxy": "user:pass@ip:port"}})
print(SolvedToken)
```
**Cloudflare - Challenge**
```python
from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
SolvedToken = SolveCaptcha.solve({"task": {"type": "AntiCloudflareTask", "websiteURL": "https://minecraftpocket-servers.com/login/", "html": "<your challenge html source code>", "metadata": {"type": "challenge"}, "proxy": "user:pass@ip:port"}})
print(SolvedToken)
```

For More Information on these Tasks, please visit [CapSolver docs](https://docs.capsolver.com/guide/getting-started.html). There are a list of tasks you can do with this library
