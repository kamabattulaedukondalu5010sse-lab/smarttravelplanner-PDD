#!/usr/bin/env python3
"""
Full test case definitions generator for Smart Travel Planner.
Produces:
- tests/selenium/test_cases/test_cases.yml (SEL-001 to SEL-300)
- tests/appium/test_cases/test_cases.yml (APP-001 to APP-300)
- tests/load/test_cases/test_cases.yml (LOAD-001 to LOAD-300)
- tests/security/test_cases/test_cases.yml (SEC-001 to SEC-300)
"""

import os
import sys

def format_yaml_entry(item):
    def clean(val):
        s = str(val).replace('"', '\\"')
        return f'"{s}"'
    return (
        f"  - id: {clean(item['id'])}\n"
        f"    category: {clean(item['category'])}\n"
        f"    name: {clean(item['name'])}\n"
        f"    description: {clean(item['description'])}\n"
        f"    priority: {clean(item['priority'])}\n"
        f"    expected_result: {clean(item['expected_result'])}\n"
    )

def write_yaml(filepath, cases):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("test_cases:\n")
        for item in cases:
            f.write(format_yaml_entry(item))
    print(f"Generated {len(cases)} test cases in {filepath}")

# Import selenium cases from script if needed, or build full lists here
import generate_all_test_cases
selenium_cases = generate_all_test_cases.generate_selenium_cases()
assert len(selenium_cases) == 300, f"Expected 300 Selenium cases, got {len(selenium_cases)}"
write_yaml(os.path.join("tests", "selenium", "test_cases", "test_cases.yml"), selenium_cases)
