#!/usr/bin/env python3
"""
Test Case Catalogue Validator for Smart Travel Planner.

Verifies:
1. Selenium = exactly 300 test cases (SEL-001 to SEL-300)
2. Appium = exactly 300 test cases (APP-001 to APP-300)
3. Load = exactly 300 test cases (LOAD-001 to LOAD-300)
4. Security = exactly 300 test cases (SEC-001 to SEC-300)
5. Total catalogue = 1,200 test definitions
6. No duplicate IDs across or within suites
7. No missing IDs in the sequence
8. Correct ID prefixes and formatting
9. All required fields present and non-empty:
   - id
   - category
   - name
   - description
   - priority
   - expected_result
10. Valid YAML syntax
"""

import sys
import os
import re

REQUIRED_FIELDS = ["id", "category", "name", "description", "priority", "expected_result"]

SUITES = {
    "Selenium": {
        "file": os.path.join("tests", "selenium", "test_cases", "test_cases.yml"),
        "prefix": "SEL-",
        "expected_count": 300
    },
    "Appium": {
        "file": os.path.join("tests", "appium", "test_cases", "test_cases.yml"),
        "prefix": "APP-",
        "expected_count": 300
    },
    "Load": {
        "file": os.path.join("tests", "load", "test_cases", "test_cases.yml"),
        "prefix": "LOAD-",
        "expected_count": 300
    },
    "Security": {
        "file": os.path.join("tests", "security", "test_cases", "test_cases.yml"),
        "prefix": "SEC-",
        "expected_count": 300
    }
}

def parse_yaml_file(filepath):
    """
    Parses YAML using PyYAML if installed, otherwise uses robust regex/line parser.
    """
    try:
        import yaml
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and "test_cases" in data:
                return data["test_cases"]
            return data
    except ImportError:
        pass

    # Built-in robust parser for test case YAML structures
    items = []
    current_item = None
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped == "test_cases:":
                continue
            
            # Match '- id: "SEL-001"' or '- id: SEL-001'
            id_match = re.match(r"^-\s*id:\s*[\"']?([^\"'\n]+)[\"']?", stripped)
            if id_match:
                if current_item:
                    items.append(current_item)
                current_item = {"id": id_match.group(1).strip()}
                continue

            # Match field: "value"
            field_match = re.match(r"^(\w+):\s*[\"']?(.*?)[\"']?$", stripped)
            if field_match and current_item is not None:
                key, val = field_match.group(1), field_match.group(2)
                # Clean trailing quotes if present
                if val.endswith('"') or val.endswith("'"):
                    val = val[:-1]
                current_item[key] = val.strip()

    if current_item:
        items.append(current_item)

    return items

def validate_suite(suite_name, config, global_ids):
    filepath = config["file"]
    prefix = config["prefix"]
    expected_count = config["expected_count"]

    errors = []

    if not os.path.exists(filepath):
        return [f"File not found: {filepath}"]

    try:
        cases = parse_yaml_file(filepath)
    except Exception as e:
        return [f"YAML parsing error in {filepath}: {str(e)}"]

    if not isinstance(cases, list):
        return [f"Expected a list of test cases in {filepath}, got {type(cases).__name__}"]

    actual_count = len(cases)
    if actual_count != expected_count:
        errors.append(f"{suite_name}: Expected {expected_count} test cases, found {actual_count}")

    seen_suite_ids = set()

    for idx, item in enumerate(cases, 1):
        if not isinstance(item, dict):
            errors.append(f"{suite_name} Item #{idx}: Item is not a dictionary mapping")
            continue

        item_id = item.get("id")
        if not item_id:
            errors.append(f"{suite_name} Item #{idx}: Missing 'id' field")
            continue

        # Check expected sequence format, e.g. SEL-001
        expected_id = f"{prefix}{idx:03d}"
        if item_id != expected_id:
            errors.append(f"{suite_name} Item #{idx}: Sequence mismatch. Expected '{expected_id}', got '{item_id}'")

        # Check duplicate within suite
        if item_id in seen_suite_ids:
            errors.append(f"{suite_name}: Duplicate ID found within suite: '{item_id}'")
        seen_suite_ids.add(item_id)

        # Check duplicate globally
        if item_id in global_ids:
            errors.append(f"Global duplicate ID detected: '{item_id}'")
        global_ids.add(item_id)

        # Check required fields
        for field in REQUIRED_FIELDS:
            val = item.get(field)
            if val is None or str(val).strip() == "":
                errors.append(f"{suite_name} [{item_id}]: Required field '{field}' is missing or empty")

    return errors

def main():
    print("=" * 70)
    print("  SMART TRAVEL PLANNER - TEST CASE CATALOGUE VALIDATION")
    print("=" * 70)

    # Resolve base dir if running from root or scripts dir
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(base_dir)

    all_errors = []
    global_ids = set()
    total_valid_cases = 0

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    for suite_name, config in SUITES.items():
        print(f"\nValidating {suite_name} suite [{config['file']}]...")
        errors = validate_suite(suite_name, config, global_ids)
        if errors:
            print(f"  [FAIL] with {len(errors)} error(s):")
            for err in errors[:10]:
                print(f"     - {err}")
            if len(errors) > 10:
                print(f"     ... and {len(errors) - 10} more errors")
            all_errors.extend(errors)
        else:
            print(f"  [PASS] exactly {config['expected_count']} valid test definitions")
            total_valid_cases += config["expected_count"]

    print("\n" + "=" * 70)
    print("  VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Total Suites Checked:     {len(SUITES)}")
    print(f"Total Test Definitions:   {total_valid_cases} / 1200")
    print(f"Unique Global IDs:        {len(global_ids)}")
    print(f"Total Errors Detected:    {len(all_errors)}")

    if all_errors:
        print("\n[FAILED] VALIDATION FAILED: Correct the above errors before proceeding.")
        sys.exit(1)
    else:
        print("\n[SUCCESS] VALIDATION SUCCESSFUL: All 1,200 test definitions are strictly valid!")
        sys.exit(0)

if __name__ == "__main__":
    main()
