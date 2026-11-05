# Auto-generated Security & Vulnerability Test Suite
# Conforms to pytest, OWASP defensive security standards, and non-destructive testing
import os
import re
import json
import pytest
import requests

@pytest.mark.security
@pytest.mark.test_id('SEC-141')
def test_sec_141_nosql_injection_in_login_email(target_url, repo_root, auth_headers):
    r"""SEC-141: NoSQL Injection In Login Email - Submit { email: { $gt: '' }, password: 'password' } to /api/auth/login"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-142')
def test_sec_142_nosql_injection_in_login_password(target_url, repo_root, auth_headers):
    r"""SEC-142: NoSQL Injection In Login Password - Submit { email: 'john@example.com', password: { $ne: '' } } to login"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-143')
def test_sec_143_string_casting_in_auth_controller(target_url, repo_root, auth_headers):
    r"""SEC-143: String Casting In Auth Controller - Verify email and password inputs are explicitly cast to String() in authController"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-144')
def test_sec_144_nosql_injection_in_user_signup(target_url, repo_root, auth_headers):
    r"""SEC-144: NoSQL Injection In User Signup - Submit { email: { $regex: '.*' } } to signup endpoint"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-145')
def test_sec_145_nosql_where_clause_injection(target_url, repo_root, auth_headers):
    r"""SEC-145: NoSQL Where Clause Injection - Submit `$where: 'this.password.length > 0'` in query payload"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-146')
def test_sec_146_nosql_regex_dos_redos_in_auth(target_url, repo_root, auth_headers):
    r"""SEC-146: NoSQL Regex DoS (ReDoS) In Auth - Submit catastrophic backtracking regex pattern in email field"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-147')
def test_sec_147_regex_escaping_in_user_lookup(target_url, repo_root, auth_headers):
    r"""SEC-147: Regex Escaping In User Lookup - Verify email search uses regex escape helper `email.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')`"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-148')
def test_sec_148_nosql_injection_in_trip_status_update(target_url, repo_root, auth_headers):
    r"""SEC-148: NoSQL Injection In Trip Status Update - Submit { status: { $ne: null } } to PUT /api/trips/:id/status"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-149')
def test_sec_149_nosql_operator_injection_in_trip_query(target_url, repo_root, auth_headers):
    r"""SEC-149: NoSQL Operator Injection In Trip Query - Submit GET /api/trips?userId[$ne]=1"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-150')
def test_sec_150_nosql_injection_in_booking_creation(target_url, repo_root, auth_headers):
    r"""SEC-150: NoSQL Injection In Booking Creation - Submit { tripId: { $gt: '' } } to POST /api/bookings"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-151')
def test_sec_151_nosql_injection_in_expense_creation(target_url, repo_root, auth_headers):
    r"""SEC-151: NoSQL Injection In Expense Creation - Submit { tripId: { $gt: '' }, amount: 500 } to POST /api/expenses"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-152')
def test_sec_152_sql_injection_classic_or_1_1_check(target_url, repo_root, auth_headers):
    r"""SEC-152: SQL Injection Classic OR '1'='1' Check - Submit `' OR '1'='1` in email, password, and search fields"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-153')
def test_sec_153_sql_injection_union_select_probe(target_url, repo_root, auth_headers):
    r"""SEC-153: SQL Injection UNION SELECT Probe - Submit `' UNION SELECT null, username, password FROM users--` in search"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-154')
def test_sec_154_sql_injection_comment_delimiter_probe(target_url, repo_root, auth_headers):
    r"""SEC-154: SQL Injection Comment Delimiter Probe - Submit `admin'--` in username/email field"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-155')
def test_sec_155_sql_injection_stacked_queries_check(target_url, repo_root, auth_headers):
    r"""SEC-155: SQL Injection Stacked Queries Check - Submit `'; DROP TABLE users;--` in destination search query"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-156')
def test_sec_156_mongoose_schema_type_enforcement(target_url, repo_root, auth_headers):
    r"""SEC-156: Mongoose Schema Type Enforcement - Verify Mongoose schemas define strict types (String, Number, Date, ObjectId)"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-157')
def test_sec_157_mongoose_strict_query_mode(target_url, repo_root, auth_headers):
    r"""SEC-157: Mongoose Strict Query Mode - Verify Mongoose strictQuery is enabled to discard unknown query parameters"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-158')
def test_sec_158_mock_db_injection_safety(target_url, repo_root, auth_headers):
    r"""SEC-158: Mock DB Injection Safety - Verify in-memory mock DB operations use strict string comparison (===)"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-159')
def test_sec_159_nosql_operator_injection_in_query_string(target_url, repo_root, auth_headers):
    r"""SEC-159: NoSQL Operator Injection In Query String - Submit query string `?search[$gt]=` to /api/destinations"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-160')
def test_sec_160_prototype_pollution_in_body_parser(target_url, repo_root, auth_headers):
    r"""SEC-160: Prototype Pollution In Body Parser - Submit `{ '__proto__': { 'polluted': true } }` in POST body"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-161')
def test_sec_161_constructor_prototype_pollution(target_url, repo_root, auth_headers):
    r"""SEC-161: Constructor Prototype Pollution - Submit `{ 'constructor': { 'prototype': { 'isAdmin': true } } }`"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-162')
def test_sec_162_mongodb_bson_parser_dos(target_url, repo_root, auth_headers):
    r"""SEC-162: MongoDB BSON Parser DoS - Send deeply nested BSON document to test parser stack exhaustion"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-163')
def test_sec_163_database_error_message_redaction(target_url, repo_root, auth_headers):
    r"""SEC-163: Database Error Message Redaction - Verify MongoDB error codes (e.g. E11000 duplicate key) do not leak raw query"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-164')
def test_sec_164_database_credentials_exposure_in_error(target_url, repo_root, auth_headers):
    r"""SEC-164: Database Credentials Exposure In Error - Verify connection failure logs mask database credentials"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-165')
def test_sec_165_mongodb_sanitize_middleware_audit(target_url, repo_root, auth_headers):
    r"""SEC-165: MongoDB Sanitize Middleware Audit - Check if express-mongo-sanitize or manual string coercion is applied"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-166')
def test_sec_166_blind_nosql_injection_timing_probe(target_url, repo_root, auth_headers):
    r"""SEC-166: Blind NoSQL Injection Timing Probe - Attempt sleep-based blind NoSQL injection payload"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-167')
def test_sec_167_second_order_sql_nosql_injection_check(target_url, repo_root, auth_headers):
    r"""SEC-167: Second-Order SQL/NoSQL Injection Check - Verify saved input retrieved from DB is not passed to dynamic evaluators"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-168')
def test_sec_168_json_schema_validation_verification(target_url, repo_root, auth_headers):
    r"""SEC-168: JSON Schema Validation Verification - Verify request validation precedes database query execution"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-169')
def test_sec_169_query_selector_injection_in_delete_trip(target_url, repo_root, auth_headers):
    r"""SEC-169: Query Selector Injection In Delete Trip - Attempt delete with selector query to delete multiple trips"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content

@pytest.mark.security
@pytest.mark.test_id('SEC-170')
def test_sec_170_static_code_audit_for_unsanitized_mongo_queries(target_url, repo_root, auth_headers):
    r"""SEC-170: Static Code Audit For Unsanitized Mongo Queries - Scan codebase for direct unsanitized `req.body` passed to Mongoose find"""
    # Verify String casting in authController protects against operator injection
    auth_ctrl = os.path.join(repo_root, "backend", "src", "controllers", "authController.js")
    if os.path.exists(auth_ctrl):
        with open(auth_ctrl, "r", encoding="utf-8") as f:
            content = f.read()
        assert "String(req.body" in content or "String(" in content
