from CapSolver import CapSolver

SolveCaptcha = CapSolver("API-KEY")
SolvedToken = SolveCaptcha.solve({"task": {"type": "AntiCloudflareTask", "websiteURL": "https://minecraftpocket-servers.com/login/", "html": "<your challenge html source code>", "metadata": {"type": "challenge"}, "proxy": "user:pass@ip:port"}})
print(SolvedToken)