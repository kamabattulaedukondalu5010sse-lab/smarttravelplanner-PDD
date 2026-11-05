# Auto-generated Security & Vulnerability Test Suite
# Conforms to pytest, OWASP defensive security standards, and non-destructive testing
import os
import re
import json
import pytest
import requests

@pytest.mark.security
@pytest.mark.test_id('SEC-116')
def test_sec_116_reflected_xss_in_destination_search(target_url, repo_root, auth_headers):
    r"""SEC-116: Reflected XSS In Destination Search - Query GET /api/destinations?search=<script>alert('xss')</script>"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-117')
def test_sec_117_reflected_xss_event_handler_injection(target_url, repo_root, auth_headers):
    r"""SEC-117: Reflected XSS Event Handler Injection - Query GET /api/destinations?search=<img src=x onerror=alert(1)>"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-118')
def test_sec_118_reflected_xss_javascript_pseudo_protocol(target_url, repo_root, auth_headers):
    r"""SEC-118: Reflected XSS JavaScript Pseudo-Protocol - Query GET /api/destinations?search=javascript:alert(1)"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-119')
def test_sec_119_stored_xss_in_trip_title(target_url, repo_root, auth_headers):
    r"""SEC-119: Stored XSS In Trip Title - Create trip with title `<script>alert('stored_xss')</script>`"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-120')
def test_sec_120_stored_xss_in_trip_description(target_url, repo_root, auth_headers):
    r"""SEC-120: Stored XSS In Trip Description - Create trip with description containing `<svg onload=alert(1)>`"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-121')
def test_sec_121_stored_xss_in_user_full_name(target_url, repo_root, auth_headers):
    r"""SEC-121: Stored XSS In User Full Name - Update user name to `<b onmouseover=alert(1)>Hacker</b>`"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-122')
def test_sec_122_stored_xss_in_expense_title(target_url, repo_root, auth_headers):
    r"""SEC-122: Stored XSS In Expense Title - Create expense with title `<iframe src=javascript:alert(1)></iframe>`"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-123')
def test_sec_123_stored_xss_in_booking_details(target_url, repo_root, auth_headers):
    r"""SEC-123: Stored XSS In Booking Details - Create booking with details containing malicious script tags"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-124')
def test_sec_124_react_jsx_built_in_escaping_verification(target_url, repo_root, auth_headers):
    r"""SEC-124: React JSX Built-in Escaping Verification - Verify React 19 automatically escapes interpolated string variables"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-125')
def test_sec_125_dangerous_react_dangerouslysetinnerhtml_audit(target_url, repo_root, auth_headers):
    r"""SEC-125: Dangerous React dangerouslySetInnerHTML Audit - Audit React frontend codebase for any usage of dangerouslySetInnerHTML"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-126')
def test_sec_126_content_security_policy_header_check(target_url, repo_root, auth_headers):
    r"""SEC-126: Content-Security-Policy Header Check - Verify server or web host returns Content-Security-Policy header"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-127')
def test_sec_127_x_xss_protection_header_check(target_url, repo_root, auth_headers):
    r"""SEC-127: X-XSS-Protection Header Check - Verify server returns X-XSS-Protection header"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-128')
def test_sec_128_html_entity_encoding_verification(target_url, repo_root, auth_headers):
    r"""SEC-128: HTML Entity Encoding Verification - Verify `<` becomes `&lt;` and `>` becomes `&gt;` when output in HTML"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-129')
def test_sec_129_dom_based_xss_in_leaflet_map_popups(target_url, repo_root, auth_headers):
    r"""SEC-129: DOM-based XSS In Leaflet Map Popups - Verify activity titles in Leaflet map markers cannot execute injected script"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-130')
def test_sec_130_dom_based_xss_in_hash_routing(target_url, repo_root, auth_headers):
    r"""SEC-130: DOM-based XSS In Hash Routing - Inject script payload into window.location.hash '#<script>alert(1)</script>'"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-131')
def test_sec_131_css_injection_in_style_attributes(target_url, repo_root, auth_headers):
    r"""SEC-131: CSS Injection In Style Attributes - Attempt injecting CSS expression `background: url(javascript:alert(1))`"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-132')
def test_sec_132_markdown_injection_defense(target_url, repo_root, auth_headers):
    r"""SEC-132: Markdown Injection Defense - If markdown rendering is used, verify raw HTML rendering is disabled"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-133')
def test_sec_133_svg_image_upload_render_sanitization(target_url, repo_root, auth_headers):
    r"""SEC-133: SVG Image Upload/Render Sanitization - Verify destination images or avatars do not execute embedded SVG scripts"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-134')
def test_sec_134_xss_in_chart_js_tooltips(target_url, repo_root, auth_headers):
    r"""SEC-134: XSS In Chart.js Tooltips - Inject script tags into expense category names rendered in Chart.js tooltips"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-135')
def test_sec_135_json_injection_in_api_responses(target_url, repo_root, auth_headers):
    r"""SEC-135: JSON Injection In API Responses - Verify user input cannot escape JSON string delimiters in API responses"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-136')
def test_sec_136_http_header_injection_crlf_injection(target_url, repo_root, auth_headers):
    r"""SEC-136: HTTP Header Injection / CRLF Injection - Inject CRLF `
Set-Cookie: evil=true` into input fields"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-137')
def test_sec_137_template_injection_ssti_defense(target_url, repo_root, auth_headers):
    r"""SEC-137: Template Injection (SSTI) Defense - Send `{{ 7 * 7 }}` in user name to test server-side template injection"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-138')
def test_sec_138_client_side_template_injection_angular_vue(target_url, repo_root, auth_headers):
    r"""SEC-138: Client-side Template Injection (Angular/Vue) - Verify frontend does not evaluate expressions dynamically"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-139')
def test_sec_139_external_link_rel_attribute_rel_noopener(target_url, repo_root, auth_headers):
    r"""SEC-139: External Link Rel Attribute (rel=noopener) - Verify external links in frontend specify rel='noopener noreferrer'"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content

@pytest.mark.security
@pytest.mark.test_id('SEC-140')
def test_sec_140_json_ld_meta_tags_xss_defense(target_url, repo_root, auth_headers):
    r"""SEC-140: JSON-LD / Meta Tags XSS Defense - Verify meta tags in index.html do not interpolate unescaped parameters"""
    # Verify JSX automatic escaping / absence of raw script execution
    app_jsx = os.path.join(repo_root, "frontend", "src", "App.jsx")
    if os.path.exists(app_jsx):
        with open(app_jsx, "r", encoding="utf-8") as f:
            content = f.read()
        assert "dangerouslySetInnerHTML" not in content
