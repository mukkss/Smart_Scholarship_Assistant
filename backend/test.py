from app.graph.router import run_agent

res1 = run_agent("what is the Eligibility criteria Post-Matric Scholarship Scheme for Minorities")
res2 = run_agent("Tell me about the Fulbright scholarship deadline.")

print("\n=== ANSWER 1 ===")
print(res1)

print("\n=== ANSWER 2 ===")
print(res2)
