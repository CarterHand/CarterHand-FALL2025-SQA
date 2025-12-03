# Software Quality Assurance Project — Fall 2025
Author: Carter Hand

## 1. Project Overview
This project integrates several software quality assurance tasks into the existing MLForensics Python project. The objective was to apply fuzz testing, forensic logging, and continuous integration (CI) to improve the software’s reliability and maintainability.

## 2. Fuzz Testing
A new script named `fuzz.py` was added to the MLForensics project. Five Python methods were selected for fuzzing.  
The fuzzer automatically generated randomized input values, including random numbers, random strings, and values selected from the Big List of Naughty Strings.  
Each selected method was executed repeatedly, and all exceptions raised during execution were recorded in `fuzz-bugs.txt`.  
At least ten distinct errors were captured as required.

Purpose:  
Fuzz testing helps identify unexpected behaviors and edge-case failures that may not surface under normal conditions.

## 3. Logging Instrumentation
Five existing methods were modified to include logging statements.  
Logging additions included parameter tracing, timestamps, warnings for abnormal input values, and execution-flow messages.  
These modifications were applied in modules such as `empirical/report.py`, `mining/mining.py`, and three additional selected files.  
Logged messages help track program execution and support debugging and forensic analysis.

Purpose:  
Logging provides observable system behavior that is useful during debugging and post-incident analysis.

## 4. Continuous Integration
A GitHub Actions workflow file named `.github/workflows/ci.yml` was added.  
The workflow sets up Python, installs dependencies, executes the fuzzer, and verifies that the project runs correctly inside a clean environment.  
This ensures that commits are automatically tested and that the repository remains in a working state. 
LINK: https://github.com/CarterHand/CarterHand-FALL2025-SQA/actions/runs/19879920592

Purpose:  
Continuous integration ensures consistent builds and enables early detection of integration errors.

## 5. Lessons Learned
The project demonstrated how different software quality assurance practices complement one another.  
Fuzz testing identifies hidden errors.  
Logging provides insight into how and why failures occur.  
Continuous integration automates testing to ensure that errors are caught early.  
Together, these practices improve the reliability and maintainability of the software.

