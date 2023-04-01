from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
SolvedToken = SolveCaptcha.solve({"task": {"type": "AntiCloudflareTask", "websiteURL": "https://peet.ws/turnstile-test/non-interactive.html","websiteKey": "0x4AAAAAAABS7vwvV6VFfMcD", "metadata": {"type": "turnstile"}, "proxy": "user:pass@ip:port"}})
print(SolvedToken)