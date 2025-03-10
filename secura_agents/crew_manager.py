from crewai import Task, Crew
from secura_agents.contract_analyzer import contract_analyzer
from secura_agents.finding_proposal import finding_proposal
from secura_agents.critic import critic

analyze_task = Task(
    agent=contract_analyzer,
    description="Analyze a Solidity contract using Slither.",
    expected_output="A comprehensive security analysis of the Solidity contract using Slither"
)

finding_task = Task(
    agent=finding_proposal,
    description="Suggest potential vulnerability fixes.",
    expected_output="A list of proposed fixes for the vulnerabilities identified in the contract"
)

critique_task = Task(
    agent=critic,
    description="Review and critique the proposed fixes.",
    expected_output="A detailed review of the proposed fixes with recommendations for improvements"
)

crew = Crew(
    agents=[contract_analyzer, finding_proposal, critic],
    tasks=[analyze_task, finding_task, critique_task]
)

def run_audit():
    print("🔍 Running smart contract audit...")
    crew.kickoff()