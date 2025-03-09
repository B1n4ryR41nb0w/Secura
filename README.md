# SecurAI: Smart Contract Audit Agent 

**SecurAI** is an AI-powered smart contract auditing tool designed to detect vulnerabilities, classify their severity, explain issues with real-world examples, suggest fixes, and generate comprehensive reports. Built with a multi-agent system using [CrewAI](https://github.com/joaomdmoura/crewAI), SecurAI aims to compete with professional auditors in platforms like Sherlock and Code4rena by May 2025.

## 🌟 Features (Current & Planned)

### Current (as of March 2025)
- **Smart Contract Analysis**: Uses [Slither](https://github.com/crytic/slither) to detect vulnerabilities in Solidity contracts (e.g., reentrancy, unchecked calls).
- **Multi-Agent System**: Leverages CrewAI to orchestrate agents for analysis, classification, explanation, fix proposals, and reporting.
- **Foundation for RAG & Classification**: Preparing to integrate DistilRoBERTa for severity classification and LlamaIndex for Retrieval-Augmented Generation (RAG) explanations.

### Planned (MVP by March 31, 2025)
- **Vulnerability Classification**: Prioritize findings (Critical, High, Medium, Low) using DistilRoBERTa.
- **RAG-Powered Explanations**: Explain vulnerabilities with real-world examples using Llama-70B + LlamaIndex + Weaviate.
- **Audit Reports**: Generate structured reports with GPT-4o Mini.
- **End-to-End Workflow**: Upload a contract → Detect vulnerabilities → Classify → Explain → Report.

### Future (Enhanced MVP by May 26, 2025)
- **Advanced Analysis**: Integrate Mythril (symbolic execution) and Echidna (fuzzing) for deeper vulnerability detection.
- **Fix Proposals**: Suggest secure fixes with DeepSeek-Coder-33B, reviewed by Claude 3.5 Sonnet.
- **Interactive Chatbot**: Answer user queries with Mixtral 8x22B.
- **API & Deployment**: Deploy on AWS/GCP with a FastAPI endpoint for contract uploads.
- **Competition-Ready**: Compete in Sherlock/Code4rena with confidence scoring and exportable reports.

## 📋 Usage

### Run a Basic Audit

Analyze a Contract:
```bash
python scripts/run_audit.py --contract ./ERC20.sol
```
This uses the ContractAnalyzer agent to run Slither and extract functions/vulnerabilities.

**Output**:


## 🗓️ Roadmap

### Month 1: MVP (March 6 – March 31, 2025)
- **Week 1 (Mar 6–10)**: Install Slither, implement ContractAnalyzer, prep DistilRoBERTa and LlamaIndex.
- **Week 2 (Mar 11–17)**: Extend ContractAnalyzer, fine-tune DistilRoBERTa (Bug Classifier), test on 5-10 contracts.
- **Week 3 (Mar 18–24)**: Set up Weaviate + Llama-70B + LlamaIndex (RAG), add GPT-4o Mini (Report Generator).
- **Week 4 (Mar 25–31)**: Integrate agents, test end-to-end, deliver MVP demo.
- **MVP Goal**: Upload contract → Detect vulnerabilities → Classify severity → Explain → Generate report.

### Month 2: Optimization (April 1 – April 28, 2025)
- Add Mythril for deeper analysis.
- Integrate DeepSeek-Coder (Fix Proposal) and Claude 3.5 (Critic).
- Build a FastAPI endpoint and Mixtral 8x22B (Chatbot).
- Benchmark against OpenZeppelin audits.

### Month 3: Deployment (April 29 – May 26, 2025)
- Deploy on AWS/GCP.
- Add Echidna for fuzzing.
- Compete in Sherlock/Code4rena.
- Add confidence scoring and exportable reports.

## 🤝 Contributing

We welcome contributions! To get started:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to your branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

### Current Needs
- Expand `classifier_data.csv` and `rag_data.txt` datasets.
- Implement FindingProposal and Critic agents.
- Write unit tests in `tests/`.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or collaboration, reach out on telegram @murluki_prg
