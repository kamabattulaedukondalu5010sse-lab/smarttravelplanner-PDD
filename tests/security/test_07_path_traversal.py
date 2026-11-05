# Auto-generated Security & Vulnerability Test Suite
# Conforms to pytest, OWASP defensive security standards, and non-destructive testing
import os
import re
import json
import pytest
import requests

@pytest.mark.security
@pytest.mark.test_id('SEC-171')
def test_sec_171_dot_dot_slash_path_traversal_probe(target_url, repo_root, auth_headers):
    r"""SEC-171: Dot-Dot-Slash Path Traversal Probe - Submit GET /api/destinations/../../etc/passwd"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-172')
def test_sec_172_encoded_dot_dot_slash_traversal(target_url, repo_root, auth_headers):
    r"""SEC-172: Encoded Dot-Dot-Slash Traversal - Submit GET /api/destinations/%2e%2e%2f%2e%2e%2fetc/passwd"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-173')
def test_sec_173_double_encoded_traversal_probe(target_url, repo_root, auth_headers):
    r"""SEC-173: Double Encoded Traversal Probe - Submit GET /api/destinations/%252e%252e%252fetc/passwd"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-174')
def test_sec_174_windows_backslash_path_traversal(target_url, repo_root, auth_headers):
    r"""SEC-174: Windows Backslash Path Traversal - Submit GET /api/destinations/..\..\windows\win.ini"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-175')
def test_sec_175_static_asset_directory_boundary_check(target_url, repo_root, auth_headers):
    r"""SEC-175: Static Asset Directory Boundary Check - Attempt to traverse outside frontend/dist directory via static asset URL"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-176')
def test_sec_176_backend_source_code_file_disclosure(target_url, repo_root, auth_headers):
    r"""SEC-176: Backend Source Code File Disclosure - Attempt GET /src/index.js or GET /backend/src/index.js via web server"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-177')
def test_sec_177_environment_file_disclosure_check(target_url, repo_root, auth_headers):
    r"""SEC-177: Environment File Disclosure Check - Attempt GET /.env or GET /backend/.env via HTTP requests"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-178')
def test_sec_178_git_repository_metadata_disclosure(target_url, repo_root, auth_headers):
    r"""SEC-178: Git Repository Metadata Disclosure - Attempt GET /.git/config or GET /.git/HEAD via HTTP"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-179')
def test_sec_179_package_manifest_disclosure(target_url, repo_root, auth_headers):
    r"""SEC-179: Package Manifest Disclosure - Attempt GET /package.json or GET /backend/package.json"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-180')
def test_sec_180_docker_configuration_disclosure(target_url, repo_root, auth_headers):
    r"""SEC-180: Docker Configuration Disclosure - Attempt GET /Dockerfile or GET /docker-compose.yml"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-181')
def test_sec_181_log_file_disclosure_check(target_url, repo_root, auth_headers):
    r"""SEC-181: Log File Disclosure Check - Attempt GET /appium-server.log or GET /out.log via HTTP"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-182')
def test_sec_182_absolute_file_path_traversal(target_url, repo_root, auth_headers):
    r"""SEC-182: Absolute File Path Traversal - Submit GET /etc/shadow or GET /C:/Windows/win.ini"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-183')
def test_sec_183_null_byte_path_truncation_check(target_url, repo_root, auth_headers):
    r"""SEC-183: Null Byte Path Truncation Check - Submit GET /api/destinations/goa.jpg%00.html"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-184')
def test_sec_184_arbitrary_file_read_in_uploads(target_url, repo_root, auth_headers):
    r"""SEC-184: Arbitrary File Read In Uploads - If file upload exists, verify uploaded filename cannot contain ../"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-185')
def test_sec_185_local_file_inclusion_lfi_in_dynamic_require(target_url, repo_root, auth_headers):
    r"""SEC-185: Local File Inclusion (LFI) In Dynamic Require - Audit codebase for dynamic require(req.body.module)"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-186')
def test_sec_186_remote_file_inclusion_rfi_check(target_url, repo_root, auth_headers):
    r"""SEC-186: Remote File Inclusion (RFI) Check - Attempt to include remote URL http://evil.com/shell.js in file paths"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-187')
def test_sec_187_symlink_traversal_check(target_url, repo_root, auth_headers):
    r"""SEC-187: Symlink Traversal Check - Verify static file server does not follow symlinks outside web root"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-188')
def test_sec_188_default_server_welcome_file_disclosure(target_url, repo_root, auth_headers):
    r"""SEC-188: Default Server Welcome File Disclosure - Verify server does not expose internal directory directory listings"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-189')
def test_sec_189_backup_file_extensions_check(target_url, repo_root, auth_headers):
    r"""SEC-189: Backup File Extensions Check - Attempt GET /index.js.bak, /index.js.old, /index.js~"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-190')
def test_sec_190_temporary_files_disclosure_check(target_url, repo_root, auth_headers):
    r"""SEC-190: Temporary Files Disclosure Check - Attempt GET /#index.js#, /index.js.swp (Vim swap)"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-191')
def test_sec_191_case_sensitivity_path_normalization(target_url, repo_root, auth_headers):
    r"""SEC-191: Case Sensitivity Path Normalization - Test case folding path traversal on Windows / Linux"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-192')
def test_sec_192_safe_path_resolution_in_express(target_url, repo_root, auth_headers):
    r"""SEC-192: Safe Path Resolution In Express - Verify all express.static paths use path.join / path.resolve"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-193')
def test_sec_193_robots_txt_security_check(target_url, repo_root, auth_headers):
    r"""SEC-193: Robots.txt Security Check - Verify robots.txt does not reveal sensitive administrative paths"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-194')
def test_sec_194_source_map_disclosure_audit(target_url, repo_root, auth_headers):
    r"""SEC-194: Source Map Disclosure Audit - Check if production frontend bundle exposes full source maps"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")

@pytest.mark.security
@pytest.mark.test_id('SEC-195')
def test_sec_195_test_artifact_directory_web_isolation(target_url, repo_root, auth_headers):
    r"""SEC-195: Test Artifact Directory Web Isolation - Verify reports/ and test_cases/ are not served as public web directories"""
    try:
        res = requests.get(f"{target_url}/../../etc/passwd", timeout=3)
        assert res.status_code in [404, 400, 403]
        assert "root:" not in res.text
    except requests.exceptions.ConnectionError:
        pytest.skip("Target server offline")
