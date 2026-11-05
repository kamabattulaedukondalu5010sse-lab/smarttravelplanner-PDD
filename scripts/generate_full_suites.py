#!/usr/bin/env python3
"""
Complete generator for all 1,200 test cases across:
- tests/selenium/test_cases/test_cases.yml (SEL-001 to SEL-300)
- tests/appium/test_cases/test_cases.yml (APP-001 to APP-300)
- tests/load/test_cases/test_cases.yml (LOAD-001 to LOAD-300)
- tests/security/test_cases/test_cases.yml (SEC-001 to SEC-300)
"""

import os

def format_yaml(cases):
    lines = ["test_cases:"]
    for c in cases:
        lines.append(f"  - id: \"{c['id']}\"")
        lines.append(f"    category: \"{c['category']}\"")
        lines.append(f"    name: \"{c['name']}\"")
        desc = c['description'].replace('"', '\\"')
        lines.append(f"    description: \"{desc}\"")
        lines.append(f"    priority: \"{c['priority']}\"")
        exp = c['expected_result'].replace('"', '\\"')
        lines.append(f"    expected_result: \"{exp}\"")
    return "\n".join(lines) + "\n"

# ----------------- APPIUM (APP-001 to APP-300) -----------------
def get_appium_cases():
    cases = []
    
    # 1. App Launch & Splash Screen (APP-001 to APP-030) - 30
    c1 = [
        ("App Cold Launch", "Perform cold launch of Flutter mobile app on Android emulator", "Critical", "App launches cleanly without crash and displays splash screen"),
        ("Splash Screen Animation", "Verify splash screen logo scaling and opacity animation", "Medium", "Scale transition animates smoothly over 2 seconds"),
        ("Splash Screen Brand Title", "Verify 'Smart Travel Planner' title text appears on splash screen", "High", "Brand title renders with bold white typography"),
        ("Splash Screen Subtitle", "Verify 'AI-Powered Intelligent Travel with Cost Optimization' subtitle", "Medium", "Subtitle renders beneath brand title"),
        ("Splash Screen Auto Navigation", "Verify automatic transition to /login route after 3 second delay", "Critical", "LoginScreen opens automatically without user interaction"),
        ("Splash Screen Background Gradient", "Verify background gradient displays primary to dark blue colors", "Low", "LinearGradient background renders correctly"),
        ("Splash Screen Decorative Circles", "Verify positioned background decorative circular overlays", "Low", "Decorative circle containers render in corners"),
        ("Splash Screen Quick Navigation On Tap", "Tap screen during splash to test tap behavior", "Low", "Tap does not trigger invalid route transition"),
        ("Splash Orientation Change", "Rotate device to landscape during splash screen animation", "Medium", "Splash screen layout preserves aspect ratio without pixel overflow"),
        ("Splash Return To Foreground", "Send app to background during splash and resume immediately", "Medium", "App resumes and navigates to login as expected"),
        ("Splash Memory Footprint", "Measure heap memory usage during initial splash load", "Low", "Memory usage stays within normal Android limits (< 150MB)"),
        ("Splash No Network Tolerance", "Launch app in airplane mode with zero network connectivity", "High", "Splash displays and navigates to login smoothly"),
        ("Splash Back Button Guard", "Press Android hardware back button during splash screen", "Low", "Back button does not cause black screen or uncaught exception"),
        ("Splash Dark Theme Handling", "Launch app while system dark mode is enabled on Android", "Low", "Splash screen applies appropriate theme colors"),
        ("Splash Status Bar Styling", "Verify Android status bar icons are light and transparent", "Low", "Status bar blends seamlessly with splash header"),
        ("Splash App Version Display", "Verify build version or trademark footer if configured", "Low", "Footer information rendered accurately"),
        ("Splash Warm Launch Time", "Perform warm launch and verify transition within 1.5 seconds", "Medium", "Warm start is significantly faster than cold start"),
        ("Splash Multi-tasking Switcher", "Open Android recent apps overview during splash animation", "Low", "App preview card displays splash UI accurately"),
        ("Splash Custom Font Rendering", "Verify custom typography loads without fallback font glitch", "Low", "Headings render in specified font family"),
        ("Splash Device Density Scaling", "Test splash rendering on hdpi, xhdpi, and xxhdpi screen densities", "Medium", "Assets scale crisp without blurring"),
        ("Splash Accessibility Label", "Inspect accessibility semantic tree for splash screen announcement", "Low", "Screen reader announces app title"),
        ("Splash Flutter Engine Startup", "Verify Flutter engine initialization finishes cleanly in logcat", "High", "Flutter Engine reports initialized in logcat"),
        ("Splash Render Frame Callback", "Verify first frame callback fires within 500ms of process start", "Medium", "First frame rendered promptly"),
        ("Splash Native Splash Handover", "Verify seamless transition from Android native launch screen to Flutter splash", "Low", "Zero black frame flash during handover"),
        ("Splash Low Storage Startup", "Launch app on device with low available internal storage", "Low", "App handles low storage startup gracefully"),
        ("Splash Low RAM Startup", "Launch app on low RAM virtual device profile", "Low", "App boots without out-of-memory error"),
        ("Splash Logcat Initialization Log", "Inspect logcat for clean startup without missing asset warnings", "Medium", "No missing resource or asset warnings logged"),
        ("Splash Safe Area Insets", "Verify splash content does not clip under camera notch or display cutout", "Medium", "Safe area insets respected"),
        ("Splash High Refresh Rate (90/120Hz)", "Verify 60+ fps animation fluidity on high refresh emulators", "Low", "Animation runs smoothly without frame drops"),
        ("Splash Screen Route Disposal", "Verify SplashScreen widget state is disposed after navigation to login", "Medium", "Animation controller disposed properly")
    ]
    for idx, (n, d, p, e) in enumerate(c1, 1):
        cases.append({"id": f"APP-{idx:03d}", "category": "App Launch & Splash Screen", "name": n, "description": d, "priority": p, "expected_result": e})

    # 2. Mobile Authentication & Sign In (APP-031 to APP-065) - 35
    c2 = [
        ("Login Screen Header Display", "Verify 'Welcome Back!' heading and subtext on LoginScreen", "High", "Heading and guidance subtitle display cleanly"),
        ("Login Email Field Presence", "Verify Email Address TextField renders with email icon", "High", "Email TextField is visible with mail prefix icon"),
        ("Login Password Field Presence", "Verify Password TextField renders with lock icon", "High", "Password TextField is visible with lock prefix icon"),
        ("Login Password Obscure Text", "Verify password characters are obscured by default", "High", "Characters masked with bullet dots"),
        ("Login Password Visibility Toggle", "Tap eye icon to toggle password visibility to plain text", "Medium", "Password characters become visible in plain text"),
        ("Login Empty Submission Validation", "Tap Login button with empty email and password fields", "Critical", "Snackbar alerts 'Please fill in all fields'"),
        ("Login Empty Email Only", "Enter password but leave email field empty and tap Login", "High", "Validation alerts missing email input"),
        ("Login Empty Password Only", "Enter email but leave password empty and tap Login", "High", "Validation alerts missing password input"),
        ("Login Invalid Email Format", "Enter 'invalidemail' without @ domain and submit login", "High", "Validation alerts invalid email format"),
        ("Login Nonexistent User Credentials", "Enter unregistered email address and submit login", "High", "Snackbar alerts 'Invalid email or password'"),
        ("Login Wrong Password Submission", "Enter valid registered email with incorrect password", "Critical", "Snackbar alerts 'Invalid email or password'"),
        ("Login Standard User Success", "Enter valid credentials (john@example.com) and submit login", "Critical", "Login succeeds, token saved, navigates to DashboardLayout"),
        ("Login Button Loading State", "Verify circular progress indicator appears inside Login button while request is in flight", "Medium", "Button displays spinner and disables interaction"),
        ("Login Keyboard Return Key", "Press soft keyboard action 'Done' on password input to submit", "Medium", "Triggers login authentication request"),
        ("Login Keyboard Dismissal", "Tap background outside text fields to dismiss soft keyboard", "Medium", "Soft keyboard dismisses cleanly"),
        ("Login Email Whitespace Trimming", "Enter email with leading/trailing spaces and verify login", "Medium", "Email trimmed and login succeeds"),
        ("Login Case Insensitive Email", "Enter email in all uppercase letters and verify login", "Medium", "Email normalized and login succeeds"),
        ("Login Navigate To Signup Screen", "Tap 'Sign Up' text button in footer", "High", "Navigates to /signup route"),
        ("Login Social Auth Buttons", "Verify Google and Apple sign in buttons if present", "Low", "Third-party auth buttons render cleanly"),
        ("Login SharedPreferences Token Save", "Verify JWT token is stored securely in app local storage", "High", "SharedPreferences contains non-null auth token"),
        ("Login Offline Mock Fallback", "Submit login when backend API is unreachable", "High", "App falls back gracefully to offline mock session"),
        ("Login Quick Fill Test Credentials", "Tap test credentials chip if debug helper is enabled", "Low", "Form auto-populates with standard test user"),
        ("Login Biometric Prompt Trigger", "Verify biometric authentication option on supported hardware", "Low", "Biometric prompt is invoked if configured"),
        ("Login Rapid Double Tap Submit", "Double tap login button rapidly", "Medium", "Only a single network request is dispatched"),
        ("Login Session Expiration Redirect", "Trigger 401 Unauthorized API error and verify redirect to Login", "High", "App logs out and returns to LoginScreen"),
        ("Login Back Button From Login", "Press hardware back button on LoginScreen", "Medium", "App minimizes or prompts for exit"),
        ("Login Accessibility Focus Order", "Inspect accessibility traversal through login inputs", "Low", "Screen reader navigates Email -> Password -> Login"),
        ("Login Password Min Length Check", "Enter password under 6 characters", "Medium", "Validation requires minimum 6 characters"),
        ("Login Special Characters Support", "Enter complex password containing symbols and punctuation", "High", "Password handled accurately without character corruption"),
        ("Login Font Scale Accessibility", "Increase Android system font size to largest and inspect LoginScreen", "Medium", "Text scales without widget overflow yellow stripes"),
        ("Login Dark Mode Contrast", "Inspect login fields contrast ratio in Android dark theme", "Low", "Text and icons remain clearly legible"),
        ("Login Landscape Scrollability", "Rotate to landscape orientation and verify screen is scrollable", "Medium", "SingleChildScrollView prevents RenderFlex overflow"),
        ("Login Clears Previous Errors", "Verify error snackbar dismisses when user edits inputs", "Low", "Error banner dismisses automatically"),
        ("Login Network Timeout Handling", "Simulate 15 second network timeout during login request", "Medium", "App displays connection timeout notice"),
        ("Login Remember Me Checkbox", "Toggle 'Remember Me' checkbox if present", "Low", "Checkbox state updates and persists")
    ]
    for idx, (n, d, p, e) in enumerate(c2, 31):
        cases.append({"id": f"APP-{idx:03d}", "category": "Mobile Authentication & Sign In", "name": n, "description": d, "priority": p, "expected_result": e})

    # 3. Mobile User Registration & Validation (APP-066 to APP-095) - 30
    c3 = [
        ("Signup Screen Header Display", "Verify 'Create Account' heading and subtext on SignupScreen", "High", "Heading and guidance subtitle render cleanly"),
        ("Signup Full Name Field", "Verify Full Name TextField with person icon", "High", "Full Name TextField is visible"),
        ("Signup Email Address Field", "Verify Email Address TextField with mail icon", "High", "Email TextField is visible"),
        ("Signup Phone Number Field", "Verify Phone Number TextField with phone icon", "Medium", "Phone TextField is visible"),
        ("Signup Password Field", "Verify Password TextField with lock icon", "High", "Password TextField is visible"),
        ("Signup Empty Form Submission", "Tap 'Sign Up' button with all fields blank", "Critical", "Snackbar alerts 'Please fill in all fields'"),
        ("Signup Missing Name Validation", "Fill email, phone, password but leave name blank", "High", "Validation alerts missing name"),
        ("Signup Missing Email Validation", "Fill name, phone, password but leave email blank", "High", "Validation alerts missing email"),
        ("Signup Missing Password Validation", "Fill name, email, phone but leave password blank", "High", "Validation alerts missing password"),
        ("Signup Short Password Validation", "Enter password with fewer than 6 characters", "High", "Validation alerts password must be at least 6 characters"),
        ("Signup Valid New Account", "Fill valid unique credentials and submit registration", "Critical", "Account created, token stored, navigates to Dashboard"),
        ("Signup Duplicate Email Conflict", "Register with already existing email address", "Critical", "Snackbar alerts 'User already exists'"),
        ("Signup Phone Format Handling", "Enter 10-digit phone number and verify format acceptance", "Medium", "Phone number is accepted and stored"),
        ("Signup Password Visibility Toggle", "Tap eye icon on password input in SignupScreen", "Medium", "Password characters toggle between masked and plain text"),
        ("Signup Button Loading Indicator", "Verify spinner appears inside Sign Up button during registration API call", "Medium", "Loading spinner renders and button disables"),
        ("Signup Navigate Back To Login", "Tap 'Log In' text button at bottom of SignupScreen", "High", "Navigates back to /login route"),
        ("Signup Hardware Back Button", "Press Android hardware back button on SignupScreen", "Medium", "Returns cleanly to LoginScreen"),
        ("Signup Terms and Privacy Checkbox", "Verify Terms and Conditions checkbox if required", "Low", "Checkbox must be checked to enable submission"),
        ("Signup Name Whitespace Trimming", "Enter name with excess whitespace and submit", "Low", "Name trimmed before sending to API"),
        ("Signup Email Lowercase Normalization", "Enter mixed-case email during registration", "Medium", "Email converted to lowercase format"),
        ("Signup Unicode Name Support", "Register user with multilingual or accented name (e.g. José Silva)", "Medium", "Name is stored and displayed correctly"),
        ("Signup Soft Keyboard Types", "Verify Email field specifies TextInputType.emailAddress", "Low", "Soft keyboard shows @ and . shortcuts"),
        ("Signup Phone Keyboard Type", "Verify Phone field specifies TextInputType.phone", "Low", "Soft keyboard shows numeric keypad"),
        ("Signup Screen Landscape Scroll", "Rotate to landscape orientation and verify form scrollability", "Medium", "Form scrolls smoothly without RenderFlex overflow"),
        ("Signup Auto-Login Behavior", "Verify successful registration logs user in directly without manual login step", "High", "DashboardLayout opens with active session"),
        ("Signup Duplicate Submit Prevention", "Rapidly tap Sign Up button twice", "Medium", "Only a single user creation request is made"),
        ("Signup Offline Mock User Creation", "Register when API is offline and verify mock user creation", "High", "Offline mock user account initialized successfully"),
        ("Signup Accessibility Traversal", "Inspect screen reader order through all signup fields", "Low", "Screen reader traverses Name -> Email -> Phone -> Password -> Sign Up"),
        ("Signup Form Reset On Return", "Navigate back to login and re-open signup to verify clear state", "Low", "Form inputs are reset"),
        ("Signup High Font Accessibility", "Test signup screen rendering with enlarged system font", "Low", "All labels and inputs adapt without truncation")
    ]
    for idx, (n, d, p, e) in enumerate(c3, 66):
        cases.append({"id": f"APP-{idx:03d}", "category": "Mobile User Registration & Validation", "name": n, "description": d, "priority": p, "expected_result": e})

    # 4. Home Dashboard & Bottom Navigation (APP-096 to APP-130) - 35
    c4 = [
        ("Dashboard Bottom Navigation Render", "Verify BottomNavigationBar displays 5 items: Home, Explore, Trips, Alerts, Profile", "Critical", "All 5 navigation tabs are visible with icons and labels"),
        ("Dashboard Initial Home Tab Active", "Verify Home tab is selected by default on dashboard load", "High", "Home tab has active icon and primary color tint"),
        ("Dashboard User Greeting Banner", "Verify header displays personalized greeting with user name", "High", "Greeting displays 'Hello, [User Name]'"),
        ("Dashboard Notification Bell Icon", "Verify notification bell icon button in top AppBar", "Medium", "Notification bell icon is visible and clickable"),
        ("Dashboard Avatar Action", "Verify user avatar thumbnail in top AppBar", "Medium", "Avatar image displays in header"),
        ("Dashboard Active Trip Card", "Verify active upcoming trip itinerary card is rendered on Home", "High", "Card displays destination name, travel dates, and cost"),
        ("Dashboard Active Trip Cost Badge", "Verify 'Cost Optimized' chip is rendered on active trip card", "Medium", "Cost optimized badge is visible"),
        ("Dashboard Active Trip Timeline Item", "Verify timeline items (e.g. Day 1 activities) on active trip card", "Medium", "Timeline displays activity titles, times, and categories"),
        ("Dashboard Quick Action Plan Trip", "Tap 'Plan Trip' quick action button on Home screen", "High", "Opens Planner/CreateTrip screen"),
        ("Dashboard Quick Action Budget Tool", "Tap 'Budget Tool' quick action button on Home screen", "High", "Opens BudgetToolScreen"),
        ("Dashboard Quick Action Top Destinations", "Tap 'Top Destinations' quick action button on Home screen", "High", "Opens TopDestinationsScreen"),
        ("Dashboard Quick Action AI Suggestions", "Tap 'AI Suggestions' quick action button on Home screen", "High", "Opens AiSuggestionsScreen"),
        ("Dashboard Featured Destinations Carousel", "Verify horizontal list of featured destinations on Home screen", "High", "Destinations scroll horizontally with image cards"),
        ("Dashboard Destination Card Tap", "Tap on 'Goa' destination card in featured list", "High", "Navigates to destination detail or planner screen"),
        ("Dashboard Destination Rating Display", "Verify destination cards display star rating (e.g. 4.8)", "Low", "Star icon and numeric score render"),
        ("Dashboard Destination Category Tag", "Verify destination category pill (Beach, Mountain, etc.)", "Low", "Category pill is visible"),
        ("Dashboard Pull To Refresh", "Perform swipe down gesture on Home screen to trigger refresh", "High", "Refresh indicator spins and re-fetches dashboard data"),
        ("Dashboard Tab Switch To Explore", "Tap 'Explore' tab in bottom navigation bar", "Critical", "View transitions to SearchDestinationScreen"),
        ("Dashboard Tab Switch To Trips", "Tap 'Trips' tab in bottom navigation bar", "Critical", "View transitions to Trips overview screen"),
        ("Dashboard Tab Switch To Alerts", "Tap 'Alerts' tab in bottom navigation bar", "Critical", "View transitions to NotificationsScreen"),
        ("Dashboard Tab Switch To Profile", "Tap 'Profile' tab in bottom navigation bar", "Critical", "View transitions to ProfileScreen"),
        ("Dashboard Tab Return To Home", "Tap 'Home' tab after visiting other tabs", "High", "View transitions back to Home screen without state loss"),
        ("Dashboard Budget Summary Card", "Verify budget statistics overview card on Home screen", "Medium", "Displays Total Budget, Total Spent, and Savings"),
        ("Dashboard Travel Advisory Notice", "Verify advisory or seasonal tip card on Home screen", "Low", "Card displays tip text with informational icon"),
        ("Dashboard Empty Trip State", "Verify helpful prompt when user has zero planned trips", "Medium", "Empty state encourages creating first trip"),
        ("Dashboard View All Destinations Link", "Tap 'View All' link next to Popular Destinations header", "Medium", "Opens full destinations catalogue"),
        ("Dashboard Dark Mode Rendering", "Verify dashboard colors in Android dark mode", "Low", "Card surfaces and text adapt cleanly to dark theme"),
        ("Dashboard Offline Banner", "Verify subtle offline indicator when internet connection drops", "Medium", "Banner informs user of offline cached data"),
        ("Dashboard Hardware Back Button Behavior", "Press back button on Home tab", "Medium", "Prompts user to exit or minimizes application"),
        ("Dashboard Bottom Bar Safe Area Inset", "Verify bottom navigation does not overlap Android navigation bar", "Medium", "Bottom padding respects device safe area insets"),
        ("Dashboard Fast Tab Switching", "Rapidly tap between tabs in bottom navigation bar", "Medium", "No crashes or stuttering during tab switching"),
        ("Dashboard Scroll Position Preservation", "Scroll down Home screen, switch tabs and return", "Low", "Scroll offset remains preserved"),
        ("Dashboard Image Memory Caching", "Verify cached network images load instantly without re-downloading", "Low", "Destination thumbnails load from memory cache"),
        ("Dashboard Currency Symbol Display", "Verify Indian Rupee (₹) symbol renders on all price elements", "Low", "Prices display with ₹ symbol"),
        ("Dashboard Orientation Rotation", "Rotate dashboard to landscape and back to portrait", "Low", "Grid and carousel re-layout responsively")
    ]
    for idx, (n, d, p, e) in enumerate(c4, 96):
        cases.append({"id": f"APP-{idx:03d}", "category": "Home Dashboard & Bottom Navigation", "name": n, "description": d, "priority": p, "expected_result": e})

    # 5. Destination Discovery & Search (APP-131 to APP-160) - 30
    c5 = [
        ("Search Screen Initial Load", "Navigate to SearchDestinationScreen from Explore tab", "High", "Search screen renders with search bar and filter chips"),
        ("Search Input Field Display", "Verify search TextField displays 'Search destinations...' hint", "High", "Search TextField is visible with search prefix icon"),
        ("Search Tune Filter Action Icon", "Verify tune/filter icon button in search bar trailing edge", "Medium", "Filter icon is visible and clickable"),
        ("Search Real-time Query Typing", "Type 'Goa' into search field", "High", "Destination list filters immediately to show Goa"),
        ("Search Case Insensitive Matching", "Type 'mAnAlI' in search field", "Medium", "Search finds Manali regardless of mixed casing"),
        ("Search Partial Substring Matching", "Type 'Ker' in search field", "Medium", "Search finds Kerala matching partial query"),
        ("Search Clear Text Button", "Tap clear (X) icon in search bar", "Medium", "Query clears and full destination list re-appears"),
        ("Search No Results View", "Type nonexistent destination 'XanaduIsland'", "High", "Empty search illustration and 'No destinations found' renders"),
        ("Category Filter Chip All", "Tap 'All' category filter chip", "Medium", "All destinations are displayed"),
        ("Category Filter Chip Beach", "Tap 'Beach' category filter chip", "High", "List filters to beach destinations (e.g. Goa)"),
        ("Category Filter Chip Mountain", "Tap 'Mountain' category filter chip", "High", "List filters to mountain destinations (e.g. Manali, Shimla)"),
        ("Category Filter Chip Nature", "Tap 'Nature' category filter chip", "High", "List filters to nature destinations (e.g. Kerala)"),
        ("Category Filter Chip Luxury", "Tap 'Luxury' category filter chip", "High", "List filters to luxury destinations (e.g. Dubai)"),
        ("Category Filter Chip Heritage", "Tap 'Heritage' category filter chip", "High", "List filters to heritage destinations (e.g. Jaipur)"),
        ("Category Filter Chip Adventure", "Tap 'Adventure' category filter chip", "High", "List filters to adventure destinations (e.g. Leh Ladakh)"),
        ("Destination Card Elements Verification", "Inspect destination card in search results", "High", "Displays image, name, description, rating, and cost factor"),
        ("Destination Bookmark Heart Toggle", "Tap heart icon on destination card", "Medium", "Heart icon fills and destination is bookmarked"),
        ("Destination Card Tap To Detail", "Tap on destination card in search list", "High", "Opens detailed destination view or modal sheet"),
        ("Destination Detail Modal Sheet", "Verify bottom modal sheet opens with full destination information", "High", "Modal displays large image, attractions list, and Plan Trip button"),
        ("Destination Detail Plan Trip Button", "Tap 'Plan Trip to [Destination]' inside detail sheet", "High", "Navigates to planner with destination pre-selected"),
        ("Search Soft Keyboard Dismiss On Scroll", "Scroll search results list with soft keyboard open", "Medium", "Soft keyboard dismisses on list drag"),
        ("Search Special Characters Handling", "Type symbols '@#$%^' into search input", "Low", "Search handles symbols safely without crashing"),
        ("Search Back Navigation", "Tap back arrow button in search AppBar", "Medium", "Returns to previous dashboard screen"),
        ("Search Filter Modal Dialog", "Tap tune icon to open advanced filter dialog", "Medium", "Filter dialog opens with budget and rating sliders"),
        ("Search Filter By Min Rating", "Set minimum rating filter to 4.8 and apply", "Medium", "Results display only destinations with rating >= 4.8"),
        ("Search Reset Filters Action", "Tap 'Reset Filters' in filter dialog", "Low", "All filter selections restore to defaults"),
        ("Search Results Count Indicator", "Verify search displays count of matched destinations", "Low", "Result count text (e.g. '7 destinations found') is visible"),
        ("Search Large Destination Catalogue", "Verify performance with 50+ destination list items", "Low", "ListView.builder scrolls smoothly with item recycling"),
        ("Search Offline Cached Destinations", "Search destinations in airplane mode", "High", "Cached destinations are searchable offline"),
        ("Search Accessibility VoiceOver", "Inspect screen reader labels for destination search items", "Low", "Screen reader announces destination name and rating")
    ]
    for idx, (n, d, p, e) in enumerate(c5, 131):
        cases.append({"id": f"APP-{idx:03d}", "category": "Destination Discovery & Search", "name": n, "description": d, "priority": p, "expected_result": e})

    # 6. Trip Planner & Itinerary Viewer (APP-161 to APP-195) - 35
    c6 = [
        ("Planner Screen Initial Load", "Navigate to CreateTripScreen / Planner", "Critical", "Planner screen renders with all configuration inputs"),
        ("Planner Destination Dropdown", "Verify destination dropdown contains all available locations", "High", "Dropdown contains Goa, Manali, Kerala, Dubai, etc."),
        ("Planner Select Destination", "Select 'Goa' from destination dropdown", "High", "Destination value updates to Goa"),
        ("Planner Date Range Picker Trigger", "Tap travel dates input field to open date picker", "High", "Material date range picker modal opens"),
        ("Planner Select Date Range", "Select start date and end date in calendar picker", "High", "Date fields update with formatted date string"),
        ("Planner Travelers Stepper Increment", "Tap plus (+) button to increment travelers count", "Medium", "Travelers count increments from 1 to 2"),
        ("Planner Travelers Stepper Decrement", "Tap minus (-) button to decrement travelers count", "Medium", "Travelers count decrements but stays >= 1"),
        ("Planner Travelers Minimum Limit", "Attempt to decrement travelers count below 1", "Medium", "Count remains at 1, minus button disabled"),
        ("Planner Total Budget Input", "Enter budget amount '25000' in budget TextField", "High", "Budget TextField updates to 25000"),
        ("Planner Empty Budget Validation", "Attempt optimization with blank budget field", "Medium", "Validation alerts budget is required"),
        ("Planner Zero Budget Validation", "Enter 0 in budget field and submit", "Medium", "Validation requires budget > 0"),
        ("Planner Optimize Button Presence", "Verify 'Optimize Trip' elevated button is rendered", "High", "Optimize button is visible and enabled"),
        ("Planner Optimize Trip Execution", "Tap 'Optimize Trip' with valid inputs", "Critical", "Cost optimization algorithm calculates budget and generates itinerary"),
        ("Planner Optimization Results Card", "Verify optimization breakdown card displays on screen", "Critical", "Displays Total Budget, Optimized Cost, and Total Savings"),
        ("Planner Savings Percentage Badge", "Verify savings badge displays percentage saved", "Medium", "Badge indicates percentage savings achieved"),
        ("Planner Stay Recommendation Card", "Verify hotel/stay cost-saving recommendation note", "Medium", "Recommendation advises on room selection savings"),
        ("Planner Transport Mode Card", "Verify recommended transport option (e.g. Train/Flight)", "Medium", "Transport mode card is displayed with pricing"),
        ("Planner Itinerary Day Expansion", "Tap 'Day 1' expansion tile in generated itinerary", "High", "Day 1 itinerary activities expand"),
        ("Planner Activity Item Schedule", "Verify activity schedule time is displayed (e.g. 09:00 AM)", "Low", "Schedule timestamp is visible on activity tile"),
        ("Planner Activity Title and Cost", "Verify activity displays title and cost with ₹ symbol", "Low", "Activity title and individual cost render"),
        ("Planner Activity Category Icon", "Verify category icon (Food, Stay, Transport, Activities) on activity item", "Low", "Appropriate icon is displayed"),
        ("Planner Day 2 Itinerary Expansion", "Tap 'Day 2' expansion tile to inspect second day schedule", "Medium", "Day 2 activities expand cleanly"),
        ("Planner Save Trip Action", "Tap 'Save Trip' elevated button", "Critical", "Trip is saved via POST /api/trips and confirmation displays"),
        ("Planner Saved Trip Toast", "Verify confirmation snackbar confirms trip has been saved", "High", "Snackbar displays 'Trip planned successfully!'"),
        ("Planner Saved Trip In Dashboard", "Navigate to Home and verify saved trip appears in active trip card", "Critical", "Home dashboard updates with newly saved trip"),
        ("Planner Form Reset After Save", "Verify planner form clears or resets after successful save", "Low", "Planner is ready for next trip creation"),
        ("Planner Budget Slider Control", "Adjust budget using interactive slider if present", "Low", "Numeric text updates to match slider position"),
        ("Planner Destination Switch Recalculation", "Switch destination from Goa to Dubai and re-optimize", "High", "Costs recalculate with Dubai luxury cost factor"),
        ("Planner Reorder Itinerary Activities", "Long press and drag activity item to reorder if supported", "Low", "Activity order updates smoothly"),
        ("Planner Delete Activity From Itinerary", "Swipe activity item to remove from itinerary", "Low", "Activity is removed and total cost updates"),
        ("Planner Offline Itinerary Generation", "Generate trip itinerary while offline", "High", "Local algorithm generates valid mock itinerary"),
        ("Planner Long Duration Trip (7 Days)", "Configure 7-day travel period and verify multi-day itinerary", "Medium", "Generates all 7 days with balanced activities"),
        ("Planner Currency Symbol Consistency", "Verify all cost figures use configured currency symbol", "Low", "Currency formatted consistently as ₹XX,XXX"),
        ("Planner Screen Landscape Scroll", "Verify planner form scrolls cleanly in landscape mode", "Low", "No RenderFlex overflow on rotation"),
        ("Planner Cancel Action", "Tap cancel or back button during trip planning", "Low", "Returns cleanly to previous view")
    ]
    for idx, (n, d, p, e) in enumerate(c6, 161):
        cases.append({"id": f"APP-{idx:03d}", "category": "Trip Planner & Itinerary Viewer", "name": n, "description": d, "priority": p, "expected_result": e})

    # 7. Budget Calculation & Expense Tracking (APP-196 to APP-225) - 30
    c7 = [
        ("Budget Tool Screen Navigation", "Navigate to BudgetToolScreen from dashboard quick actions", "High", "BudgetToolScreen opens with calculation controls"),
        ("Budget Destination Selection", "Select destination in budget tool screen", "Medium", "Destination selected with cost multiplier applied"),
        ("Budget Travelers Count Input", "Enter number of travelers in budget tool", "Medium", "Per-traveler cost updates accurately"),
        ("Budget Calculation Per Person", "Verify cost per person equals total cost divided by travelers count", "High", "Calculated value matches expected mathematical quotient"),
        ("Budget Category Distribution Chart", "Verify fl_chart Pie/Bar chart renders cost allocation", "High", "fl_chart widget paints category slices cleanly"),
        ("Budget Category Slices Breakdown", "Verify categories: Stay (40%), Transport (30%), Food (15%), Activities (15%)", "Medium", "Category breakdown percentages render"),
        ("Budget Savings Tip Chip", "Verify AI budget savings tip chip is displayed", "Low", "Chip displays practical travel savings tip"),
        ("Trip Expenses Screen Navigation", "Navigate to trip expenses view from trip detail", "High", "Expenses view opens with total spend summary"),
        ("Expense Total Spend Card", "Verify Total Spend card calculates sum of recorded expenses", "High", "Total spend card displays accurate numerical total"),
        ("Expense Remaining Budget Metric", "Verify Remaining Budget card reflects trip budget minus spend", "High", "Remaining budget updates accurately"),
        ("Expense Add Floating Action Button", "Verify FloatingActionButton (+) is visible on expenses screen", "High", "FAB button is visible and clickable"),
        ("Expense Add Modal Bottom Sheet", "Tap FAB to open Add Expense bottom sheet", "High", "Modal bottom sheet opens with title, amount, and category fields"),
        ("Expense Title Input", "Enter expense title 'Goan Fish Curry'", "High", "Title field updates with input text"),
        ("Expense Amount Input", "Enter expense amount '850'", "High", "Amount field updates to 850"),
        ("Expense Category Dropdown Selection", "Select 'Food' category from dropdown", "High", "Category select updates to Food"),
        ("Expense Empty Title Validation", "Attempt to submit expense with blank title", "Medium", "Validation requires title input"),
        ("Expense Empty Amount Validation", "Attempt to submit expense with blank amount", "Medium", "Validation requires amount input"),
        ("Expense Negative Amount Validation", "Enter negative value in amount field", "Medium", "Validation rejects negative numbers"),
        ("Expense Submit Execution", "Tap 'Add Expense' button in bottom sheet", "Critical", "Expense is created and added to expense list"),
        ("Expense List Item Render", "Verify new expense item appears in ListView", "Critical", "Item displays title, category badge, and formatted amount"),
        ("Expense List Category Icon", "Verify category icon (restaurant, hotel, etc.) on expense item", "Low", "Appropriate icon is rendered"),
        ("Expense Swipe To Delete", "Swipe expense list item to trigger deletion", "High", "Item is deleted and total spend decreases"),
        ("Expense Delete Undo Snackbar", "Verify 'Expense deleted' snackbar appears with Undo button", "Medium", "Undo button restores deleted expense"),
        ("Over Budget Visual Warning", "Simulate total expenses exceeding allocated budget", "High", "Budget progress bar turns red with warning banner"),
        ("Expense Category Filter Chips", "Filter expenses list by tapping 'Transport' chip", "Medium", "List displays only transport expenses"),
        ("Expense Category Filter Clear", "Tap active filter chip again to clear filter", "Low", "All expenses re-appear in list"),
        ("Expense Date Timestamp Display", "Verify expense list item displays date and time", "Low", "Date string is formatted cleanly"),
        ("Expense Empty State View", "Verify empty state graphic when trip has zero expenses", "Low", "Empty state displays 'No expenses recorded yet'"),
        ("Expense Export Action", "Tap export icon to generate expense report summary", "Low", "Report summary sheet or share sheet opens"),
        ("Expense Offline Persistence", "Add expense while offline and verify local storage persistence", "High", "Expense persists and syncs upon reconnection")
    ]
    for idx, (n, d, p, e) in enumerate(c7, 196):
        cases.append({"id": f"APP-{idx:03d}", "category": "Budget Calculation & Expense Tracking", "name": n, "description": d, "priority": p, "expected_result": e})

    # 8. User Profile & Settings Management (APP-226 to APP-255) - 30
    c8 = [
        ("Profile Screen Navigation", "Tap 'Profile' tab in bottom navigation bar", "Critical", "ProfileScreen opens with user overview"),
        ("Profile User Name Header", "Verify user full name is displayed prominently in header", "High", "User name renders in large typography"),
        ("Profile Email Display", "Verify registered email address is displayed beneath user name", "High", "Email address renders in subtitle styling"),
        ("Profile Avatar Display", "Verify circular avatar image or initial letter fallback", "Medium", "CircleAvatar widget renders without asset error"),
        ("Profile Travel Statistics Row", "Verify statistics row (Trips Planned, Places Visited, Reviews)", "Medium", "Numeric stat counters are visible"),
        ("Profile Menu Personal Info", "Verify 'Personal Information' list tile is present", "High", "List tile renders with user icon"),
        ("Profile Tap Personal Info", "Tap 'Personal Information' list tile", "High", "Navigates to PersonalInformationScreen"),
        ("Personal Info Form Inputs", "Verify Name, Email, and Phone TextFields in PersonalInformationScreen", "High", "All personal info TextFields render"),
        ("Personal Info Edit Name", "Update name in TextField and tap Save", "High", "Name updates via API and reflects on ProfileScreen"),
        ("Personal Info Edit Phone", "Update phone number and tap Save", "Medium", "Phone number updates successfully"),
        ("Personal Info Save Snackbar", "Verify confirmation snackbar confirms profile updated", "Medium", "Snackbar alerts 'Profile updated successfully'"),
        ("Profile Menu Settings Tile", "Verify 'Settings' list tile is present", "High", "List tile renders with settings cog icon"),
        ("Profile Tap Settings", "Tap 'Settings' list tile", "High", "Navigates to SettingsScreen"),
        ("Settings Dark Mode Switch", "Verify 'Dark Mode' SwitchListTile in SettingsScreen", "High", "Switch toggle is visible"),
        ("Settings Toggle Dark Mode", "Toggle Dark Mode switch to on", "High", "App theme updates dynamically to dark theme"),
        ("Settings Toggle Push Notifications", "Toggle 'Push Notifications' switch", "Medium", "Notification switch state updates"),
        ("Settings Toggle Budget Alerts", "Toggle 'Over-Budget Alerts' switch", "Medium", "Budget alert switch state updates"),
        ("Settings Currency Selection", "Tap 'Currency' tile and select 'USD'", "High", "Currency updates to USD across all screens"),
        ("Settings Clear Cache Action", "Tap 'Clear Cache' tile in settings", "Low", "Temporary cached data is cleared with confirmation"),
        ("Settings App Version Tile", "Verify app version (e.g. 1.0.0+1) is displayed in settings footer", "Low", "Version string matches pubspec.yaml version"),
        ("Profile Menu Help and Support", "Tap 'Help & Support' list tile", "Low", "FAQ or support contact sheet opens"),
        ("Profile Menu Privacy Policy", "Tap 'Privacy Policy' list tile", "Low", "Privacy policy webview or text sheet opens"),
        ("Profile Logout Button Presence", "Verify 'Log Out' list tile with red styling and exit icon", "Critical", "Logout tile is visible in red accent"),
        ("Profile Tap Logout Action", "Tap 'Log Out' list tile", "Critical", "Confirmation dialog appears asking user to confirm logout"),
        ("Profile Logout Dialog Cancel", "Tap 'Cancel' inside logout confirmation dialog", "Medium", "Dialog dismisses, user remains on ProfileScreen"),
        ("Profile Logout Dialog Confirm", "Tap 'Log Out' inside confirmation dialog", "Critical", "Session cleared, token deleted, navigates to LoginScreen"),
        ("Profile Unauthenticated Guard", "Verify user cannot navigate back to ProfileScreen after logout", "Critical", "Pressing back on Login does not return to profile"),
        ("Notifications Screen Navigation", "Tap 'Alerts' tab in bottom navigation bar", "High", "NotificationsScreen opens"),
        ("Notifications List View", "Verify list of travel alerts and system notifications", "Medium", "Notification cards display title, time, and icon"),
        ("Notifications Clear All Action", "Tap 'Clear All' icon in notifications header", "Low", "Notifications list clears and displays empty state")
    ]
    for idx, (n, d, p, e) in enumerate(c8, 226):
        cases.append({"id": f"APP-{idx:03d}", "category": "User Profile & Settings Management", "name": n, "description": d, "priority": p, "expected_result": e})

    # 9. Gestures, Scrolling & UI Orientations (APP-256 to APP-280) - 25
    c9 = [
        ("Home Dashboard Vertical Scroll", "Perform fling scroll gesture up and down on HomeDashboard", "High", "ListView scrolls fluidly without jank"),
        ("Featured Destinations Horizontal Swipe", "Swipe horizontally through featured destinations list", "High", "Horizontal carousel scrolls smoothly"),
        ("Destination Image Pinch To Zoom", "Perform pinch zoom gesture on destination photo preview", "Medium", "Photo zooms in and returns smoothly"),
        ("Notification Swipe Dismissal", "Swipe notification card to the left to dismiss", "Medium", "Dismissible widget animates out and deletes item"),
        ("BottomSheet Drag Dismissal", "Drag modal bottom sheet downward to dismiss", "Medium", "Modal sheet follows drag and dismisses at threshold"),
        ("Double Tap Like Destination", "Double tap on destination card image", "Low", "Heart animation triggers and item is liked"),
        ("Long Press Context Menu", "Long press on trip card to open action context menu", "Medium", "Context menu options appear (Share, Edit, Delete)"),
        ("Portrait To Landscape Rotation", "Rotate device 90 degrees to landscape orientation", "High", "Layout recalculates without crashing or UI clipping"),
        ("Landscape To Portrait Rotation", "Rotate device back to portrait orientation", "High", "Layout restores standard portrait layout cleanly"),
        ("Soft Keyboard Input Avoidance", "Focus text field at bottom of screen to trigger keyboard", "High", "View insets adjust so text field remains visible above keyboard"),
        ("Keyboard Next Action Traversal", "Tap 'Next' on soft keyboard action to cycle input fields", "Medium", "Focus advances sequentially to next TextField"),
        ("Multi-touch Simultaneous Taps", "Tap two buttons simultaneously on screen", "Low", "App handles multi-touch gracefully without race condition"),
        ("Overscroll Glow Animation", "Scroll to top/bottom boundary of list and observe stretch/glow", "Low", "Android overscroll glow or stretch effect renders cleanly"),
        ("Pull To Refresh Distance Threshold", "Pull down half distance and release without exceeding threshold", "Low", "Refresh cancels cleanly without triggering API call"),
        ("Pull To Refresh Full Trigger", "Pull down past trigger threshold and release", "Medium", "Triggers onRefresh callback and refreshes data"),
        ("Itinerary Reorder Drag Gesture", "Drag and drop itinerary activity tile up or down", "Low", "Tile snaps into new position in list"),
        ("DatePicker Month Swipe", "Swipe horizontally in date picker to change calendar months", "Medium", "Calendar animates to next month smoothly"),
        ("Slider Drag Precision", "Drag budget slider thumb across track", "Low", "Slider thumb follows finger position precisely"),
        ("Tab Swipe Gesture Transition", "Swipe left/right to change bottom tabs if TabBarView is active", "Medium", "View transitions smoothly with swipe"),
        ("Dialog Backdrop Tap Dismiss", "Tap outside alert dialog on semi-transparent barrier", "Medium", "Barrier dismisses dialog if barrierDismissible is true"),
        ("Edge Swipe Back Gesture", "Perform swipe from left edge on Android 10+ gesture navigation", "High", "Triggers pop route navigation cleanly"),
        ("High DPI Touch Accuracy", "Verify touch target sizes meet minimum 48x48 dp Android guidelines", "Medium", "Buttons are easily tappable without mis-clicks"),
        ("Rapid Tap Debouncing", "Tap action button rapidly 5 times in 1 second", "Medium", "Action debounces and executes once"),
        ("Text Selection and Copy", "Long press on itinerary text to select and copy", "Low", "System text selection toolbar appears"),
        ("Scrollbar Drag Interaction", "Drag scrollbar thumb directly on scrollable views", "Low", "Content scrolls proportionally to scrollbar drag")
    ]
    for idx, (n, d, p, e) in enumerate(c9, 256):
        cases.append({"id": f"APP-{idx:03d}", "category": "Gestures, Scrolling & UI Orientations", "name": n, "description": d, "priority": p, "expected_result": e})

    # 10. Lifecycle, Background/Foreground & Network Resilience (APP-281 to APP-300) - 20
    c10 = [
        ("App Send To Background", "Press Android Home button while viewing HomeDashboard", "High", "App moves to background without crashing"),
        ("App Resume From Background", "Re-open app from recent apps switcher", "High", "App restores exactly to HomeDashboard state"),
        ("Session Kept On Backgrounding", "Verify user remains logged in after app is backgrounded for 5 minutes", "High", "Session token remains valid and active"),
        ("App Process Termination and Restart", "Terminate app process and relaunch from launcher icon", "Critical", "App reads stored token and auto-navigates past login to Dashboard"),
        ("Airplane Mode Disconnection", "Enable airplane mode while navigating app", "High", "App handles network loss gracefully with cached data"),
        ("Airplane Mode Reconnection", "Disable airplane mode to restore network connectivity", "High", "App resumes network calls and updates state"),
        ("API Error 500 Handling", "Simulate 500 Internal Server Error response from backend API", "High", "App displays user-friendly error notice without red screen of death"),
        ("API Error 404 Handling", "Simulate 404 Not Found response for deleted trip", "Medium", "App displays resource not found message"),
        ("Low Memory Trim Notification", "Trigger system low memory trim callback (TRIM_MEMORY_RUNNING_CRITICAL)", "Medium", "App trims image caches without process crash"),
        ("System Permission Camera/Storage", "Request storage or photo permission if receipt upload is triggered", "Low", "Standard Android permission dialog is displayed"),
        ("System Permission Denial Handling", "Deny requested permission in permission dialog", "Low", "App handles denial gracefully without crashing"),
        ("Deep Link URL Handling", "Launch app via deep link URL 'smarttravel://trip/60d000000000000000000201'", "Medium", "App opens directly on specified trip detail view"),
        ("Android Back Hardware Key Navigation", "Press hardware back button through screen stack (Detail -> Home)", "High", "Screen stack pops in accurate reverse order"),
        ("Android Back Hardware Key Exit Prompt", "Press hardware back button on root dashboard screen", "Medium", "App prompts user before closing or minimizes"),
        ("App Update Check Simulation", "Verify app behavior when version check API returns update available", "Low", "Optional update prompt banner displays"),
        ("Device Timezone Change Handling", "Change device timezone from IST to UTC while app is running", "Low", "Date and time calculations adjust accurately"),
        ("Battery Saver Mode Handling", "Enable Android battery saver mode and verify reduced animation load", "Low", "App functions smoothly with power saving enabled"),
        ("Split Screen Multi-window Mode", "Launch app in Android split screen multi-window mode", "Medium", "Layout adapts to half-screen height constraints"),
        ("Logcat Zero Unhandled Exceptions", "Monitor logcat output during complete 30-minute test run", "High", "Zero uncaught Flutter exceptions or fatal crashes"),
        ("Accessibility TalkBack Navigation", "Perform full user journey with Android TalkBack screen reader enabled", "Medium", "All critical actions are fully navigable via screen reader")
    ]
    for idx, (n, d, p, e) in enumerate(c10, 281):
        cases.append({"id": f"APP-{idx:03d}", "category": "Lifecycle & Network Resilience", "name": n, "description": d, "priority": p, "expected_result": e})

    return cases

# ----------------- K6 LOAD (LOAD-001 to LOAD-300) -----------------
def get_load_cases():
    cases = []
    
    # 1. Smoke Profile Scenarios (LOAD-001 to LOAD-040) - 40
    c1 = [
        ("Smoke Root Health Check", "Baseline GET / health probe with 1 VU for 10s", "Critical", "HTTP 200, latency < 50ms, 0% errors"),
        ("Smoke Auth Login Baseline", "Baseline POST /api/auth/login with valid user credentials", "Critical", "HTTP 200, JWT token returned, latency < 150ms"),
        ("Smoke Auth Invalid Login Baseline", "Baseline POST /api/auth/login with wrong credentials", "High", "HTTP 401, error message returned, latency < 150ms"),
        ("Smoke Auth Empty Login Baseline", "Baseline POST /api/auth/login with blank payload", "Medium", "HTTP 400, validation error, latency < 50ms"),
        ("Smoke Get Destinations Baseline", "Baseline GET /api/destinations single request", "Critical", "HTTP 200, JSON array of destinations, latency < 80ms"),
        ("Smoke Search Destinations Goa", "Baseline GET /api/destinations?search=Goa", "High", "HTTP 200, filtered destination returned, latency < 80ms"),
        ("Smoke Search Destinations Manali", "Baseline GET /api/destinations?search=Manali", "High", "HTTP 200, Manali destination returned, latency < 80ms"),
        ("Smoke Search Destinations Kerala", "Baseline GET /api/destinations?search=Kerala", "High", "HTTP 200, Kerala destination returned, latency < 80ms"),
        ("Smoke Search Destinations Dubai", "Baseline GET /api/destinations?search=Dubai", "High", "HTTP 200, Dubai destination returned, latency < 80ms"),
        ("Smoke Search Destinations No Match", "Baseline GET /api/destinations?search=NonexistentPlace", "Medium", "HTTP 200, empty array returned, latency < 80ms"),
        ("Smoke Get User Profile Baseline", "Baseline GET /api/auth/user with valid Bearer token", "Critical", "HTTP 200, user profile object returned, latency < 100ms"),
        ("Smoke Get User Profile Unauthenticated", "Baseline GET /api/auth/user without Authorization header", "High", "HTTP 401, unauthorized response, latency < 50ms"),
        ("Smoke Get User Profile Malformed Token", "Baseline GET /api/auth/user with malformed token", "High", "HTTP 401, invalid token rejection, latency < 50ms"),
        ("Smoke Get Trips Baseline", "Baseline GET /api/trips for authenticated user", "Critical", "HTTP 200, trips array returned, latency < 120ms"),
        ("Smoke Get Single Trip By ID", "Baseline GET /api/trips/:id for known trip ID", "High", "HTTP 200, trip object returned, latency < 100ms"),
        ("Smoke Get Trip Invalid ID", "Baseline GET /api/trips/invalid_id", "Medium", "HTTP 404 or 400 handled gracefully, latency < 50ms"),
        ("Smoke Create Trip Baseline", "Baseline POST /api/trips with valid itinerary payload", "Critical", "HTTP 201, created trip returned with _id, latency < 150ms"),
        ("Smoke Create Trip Missing Fields", "Baseline POST /api/trips with missing budget field", "Medium", "HTTP 400, validation error, latency < 50ms"),
        ("Smoke Update Trip Status Baseline", "Baseline PUT /api/trips/:id/status to 'completed'", "High", "HTTP 200, updated trip status returned, latency < 100ms"),
        ("Smoke Delete Trip Baseline", "Baseline DELETE /api/trips/:id", "High", "HTTP 200, deletion confirmation, latency < 100ms"),
        ("Smoke Get Bookings Baseline", "Baseline GET /api/bookings for authenticated user", "High", "HTTP 200, bookings array returned, latency < 100ms"),
        ("Smoke Create Booking Baseline", "Baseline POST /api/bookings with valid tripId and hotel", "Critical", "HTTP 201, created booking returned, latency < 150ms"),
        ("Smoke Create Booking Invalid Trip", "Baseline POST /api/bookings with nonexistent tripId", "Medium", "HTTP 404, error message returned, latency < 80ms"),
        ("Smoke Get Expenses By Trip Baseline", "Baseline GET /api/expenses/trip/:tripId", "High", "HTTP 200, expense items array returned, latency < 100ms"),
        ("Smoke Get Expense Stats Baseline", "Baseline GET /api/expenses/trip/:tripId/stats", "High", "HTTP 200, category breakdown stats returned, latency < 100ms"),
        ("Smoke Add Expense Baseline", "Baseline POST /api/expenses with valid title and amount", "Critical", "HTTP 201, created expense returned, latency < 120ms"),
        ("Smoke Add Expense Zero Amount", "Baseline POST /api/expenses with amount 0", "Medium", "HTTP 400 or handled gracefully, latency < 50ms"),
        ("Smoke Frontend Static Index HTML", "Baseline GET http://localhost:3000/ web frontend index", "Critical", "HTTP 200, HTML document returned, latency < 50ms"),
        ("Smoke Frontend CSS Asset", "Baseline GET static CSS stylesheet bundle", "High", "HTTP 200, stylesheet content-type text/css, latency < 30ms"),
        ("Smoke Frontend JS Asset", "Baseline GET static JavaScript application bundle", "High", "HTTP 200, script content-type text/javascript, latency < 50ms"),
        ("Smoke Sequential User Flow 1 VU", "Single user performs Login -> View Destinations -> View Trips -> Logout", "Critical", "Complete user journey passes with 100% success"),
        ("Smoke Response Content Type Header", "Verify all API responses return Content-Type application/json", "High", "Content-Type matches application/json"),
        ("Smoke CORS Preflight OPTIONS Check", "Baseline OPTIONS /api/auth/login check", "Medium", "HTTP 204 or 200 with CORS headers, latency < 30ms"),
        ("Smoke HTTP Compression Gzip Check", "Verify server supports gzip or br encoding", "Low", "Content-Encoding indicates compression if supported"),
        ("Smoke HTTP Keep-Alive Connection", "Verify TCP keep-alive header is respected across consecutive requests", "Medium", "Connection re-used across requests"),
        ("Smoke 404 Unknown Route Probe", "Baseline GET /api/nonexistent_route", "Low", "HTTP 404 returned cleanly without stack trace"),
        ("Smoke SSL/TLS Handshake Simulation", "Measure TLS negotiation latency if HTTPS is enabled", "Low", "TLS handshake overhead < 50ms"),
        ("Smoke Payload Size Under 50KB", "Verify destination list payload size is within reasonable bounds", "Medium", "Payload transfer < 50KB"),
        ("Smoke Memory Baseline Pre-Test", "Inspect baseline memory footprint prior to load ramp-up", "Medium", "Backend memory < 120MB RSS"),
        ("Smoke Zero Error Rate Confirmation", "Verify smoke profile achieves 0.00% http_req_failed", "Critical", "Threshold rate < 0.01 satisfied")
    ]
    for idx, (n, d, p, e) in enumerate(c1, 1):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Smoke Profile Scenarios", "name": n, "description": d, "priority": p, "expected_result": e})

    # 2. Normal Load Profile Scenarios (LOAD-041 to LOAD-085) - 45
    c2 = [
        ("Normal Load 10 VUs Destinations", "10 concurrent VUs querying GET /api/destinations for 30s", "High", "p95 < 200ms, error rate < 0.5%"),
        ("Normal Load 10 VUs Search Goa", "10 VUs searching GET /api/destinations?search=Goa", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Search Manali", "10 VUs searching GET /api/destinations?search=Manali", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Search Kerala", "10 VUs searching GET /api/destinations?search=Kerala", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Search Jaipur", "10 VUs searching GET /api/destinations?search=Jaipur", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Search Shimla", "10 VUs searching GET /api/destinations?search=Shimla", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Search Leh Ladakh", "10 VUs searching GET /api/destinations?search=Leh", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Auth Login", "10 VUs authenticating concurrently with valid credentials", "Critical", "p95 < 250ms, 100% login success"),
        ("Normal Load 10 VUs Get Profile", "10 VUs fetching user profile GET /api/auth/user", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Get Trips", "10 VUs fetching trips list GET /api/trips", "High", "p95 < 220ms, 0% errors"),
        ("Normal Load 10 VUs Get Trip Detail", "10 VUs fetching single trip GET /api/trips/:id", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Get Bookings", "10 VUs fetching user bookings GET /api/bookings", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Get Expenses", "10 VUs fetching trip expenses GET /api/expenses/trip/:id", "High", "p95 < 200ms, 0% errors"),
        ("Normal Load 10 VUs Expense Stats", "10 VUs fetching expense stats GET /api/expenses/trip/:id/stats", "High", "p95 < 220ms, 0% errors"),
        ("Normal Load 10 VUs Mixed Browsing", "10 VUs executing mixed destination browse and trip review", "Critical", "p95 < 250ms, error rate < 0.5%"),
        ("Normal Load 15 VUs Sustained Read", "15 VUs sustained read load across all GET endpoints for 45s", "High", "p95 < 300ms, throughput > 50 req/s"),
        ("Normal Load 15 VUs Destination Search Variations", "15 VUs querying varying destination keywords randomly", "High", "p95 < 250ms, zero dropped requests"),
        ("Normal Load 15 VUs Authenticated Session Simulation", "15 VUs holding authenticated sessions and querying trips", "High", "p95 < 280ms, 0% auth failures"),
        ("Normal Load 15 VUs Concurrent Booking Queries", "15 VUs querying trip bookings concurrently", "Medium", "p95 < 250ms, 0% errors"),
        ("Normal Load 20 VUs Peak Normal Traffic", "20 VUs simulating peak normal business hours traffic for 1 minute", "Critical", "p95 < 350ms, error rate < 1.0%"),
        ("Normal Load 20 VUs Login and Dashboard Flow", "20 VUs logging in and loading dashboard metrics simultaneously", "Critical", "p95 < 400ms, 100% successful flows"),
        ("Normal Load 20 VUs Itinerary Retrieval", "20 VUs requesting multi-day trip itineraries", "High", "p95 < 320ms, 0% errors"),
        ("Normal Load 20 VUs Expense Logging Simulation", "20 VUs recording expenses periodically (1 req every 3s)", "High", "p95 < 300ms, data accurately recorded"),
        ("Normal Load 20 VUs Frontend Static Assets Delivery", "20 VUs requesting Vite static assets bundle concurrently", "Medium", "p95 < 100ms, static assets served rapidly"),
        ("Normal Load Ramp Up 0 to 15 VUs", "Ramp up linearly from 0 to 15 VUs over 20 seconds", "Medium", "Smooth latency curve without initial spikes"),
        ("Normal Load Steady State 15 VUs", "Hold steady at 15 VUs for 30 seconds", "Medium", "Latency variance < 50ms across window"),
        ("Normal Load Ramp Down 15 to 0 VUs", "Ramp down linearly from 15 to 0 VUs over 10 seconds", "Low", "Server releases connection pool cleanly"),
        ("Normal Load Throughput Measurement", "Measure requests per second achieved at 20 VUs", "Medium", "Throughput exceeds 75 req/s"),
        ("Normal Load Connection Reuse Rate", "Verify HTTP connection reuse > 95% across iterations", "Medium", "TCP connections re-used efficiently"),
        ("Normal Load CPU Utilization Monitoring", "Monitor server CPU during 20 VUs normal load", "Medium", "CPU usage remains < 60%"),
        ("Normal Load Memory Stability Check", "Verify server memory remains bounded during 20 VUs test", "Medium", "Memory growth < 25MB without leak"),
        ("Normal Load DNS Resolution Caching", "Verify DNS lookup overhead is negligible on repeated calls", "Low", "DNS resolution time < 2ms"),
        ("Normal Load Random Think Time Simulation", "Include 1s to 2s random think time between user actions", "Medium", "Simulates realistic human interaction rhythms"),
        ("Normal Load Mixed Read/Write 80/20", "80% reads (search, get trips) and 20% writes (create trip, add expense)", "High", "p95 < 350ms, writes process cleanly"),
        ("Normal Load Profile Update Concurrency", "5 VUs updating user profile settings concurrently", "Medium", "p95 < 250ms, updates persist accurately"),
        ("Normal Load Status Transition Concurrency", "5 VUs updating trip status from upcoming to completed", "Medium", "p95 < 250ms, status transitions succeed"),
        ("Normal Load Booking Confirmation Concurrency", "5 VUs confirming hotel bookings simultaneously", "High", "p95 < 300ms, bookings created without collision"),
        ("Normal Load Concurrent Itinerary Optimization", "5 VUs requesting trip cost optimization calculations", "High", "p95 < 350ms, algorithm computes reliably"),
        ("Normal Load Response Body Checksum Verification", "Verify response JSON payloads remain intact and uncorrupted", "Medium", "100% valid JSON responses"),
        ("Normal Load Error Rate Threshold Validation", "Validate http_req_failed stays strictly below 0.01", "Critical", "Error rate threshold confirmed satisfied"),
        ("Normal Load Latency p95 Threshold Validation", "Validate http_req_duration p(95) remains below 500ms", "Critical", "Latency threshold confirmed satisfied"),
        ("Normal Load Latency p99 Measurement", "Record p99 latency tail metric under 20 VUs", "Medium", "p99 < 650ms"),
        ("Normal Load Median Latency Measurement", "Record p50 (median) latency metric under 20 VUs", "Medium", "p50 < 120ms"),
        ("Normal Load Iteration Duration Distribution", "Measure full iteration loop time across virtual users", "Medium", "Iteration duration reflects expected pacing"),
        ("Normal Load Graceful Finish Verification", "Verify k6 reports clean teardown without unhandled rejections", "High", "Test finishes with exit code 0")
    ]
    for idx, (n, d, p, e) in enumerate(c2, 41):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Normal Load Profile Scenarios", "name": n, "description": d, "priority": p, "expected_result": e})

    # 3. Stress Profile Scenarios (LOAD-086 to LOAD-130) - 45
    c3 = [
        ("Stress Ramp To 30 VUs", "Ramp concurrency to 30 VUs over 30s to observe degradation boundary", "High", "p95 < 450ms, error rate < 1%"),
        ("Stress Ramp To 50 VUs", "Ramp concurrency to 50 VUs over 45s", "Critical", "Server maintains availability, p95 < 600ms"),
        ("Stress Ramp To 75 VUs", "Ramp concurrency to 75 VUs over 1 minute", "High", "System handles high concurrency with graceful queuing"),
        ("Stress Peak 100 VUs Hold", "Hold 100 VUs concurrency for 30s to determine saturation limit", "Critical", "Server does not crash, errors stay below 5%"),
        ("Stress 50 VUs Concurrent Logins", "50 VUs submitting login requests simultaneously (bcrypt CPU load)", "Critical", "Bcrypt hashing queues and processes without dropping TCP sockets"),
        ("Stress 50 VUs Destination Search Regex", "50 VUs executing regex search across destination catalogue", "High", "Regex queries execute within timeout limits"),
        ("Stress 50 VUs Trip Creation Bursts", "50 VUs posting new trip itineraries concurrently", "High", "Database writes commit without lock deadlock"),
        ("Stress 50 VUs Expense Aggregation Bursts", "50 VUs requesting expense statistics aggregation concurrently", "High", "Aggregation pipelines complete within 500ms"),
        ("Stress 50 VUs Booking Transaction Bursts", "50 VUs booking hotel rooms concurrently", "High", "Bookings created with unique IDs"),
        ("Stress Connection Pool Saturation Test", "Test behavior when concurrent requests exceed MongoDB connection pool size", "High", "Mongoose queues requests without dropping connections"),
        ("Stress Socket Descriptor Exhaustion Test", "Open high number of concurrent HTTP connections", "Medium", "Node.js event loop manages sockets without EMFILE errors"),
        ("Stress Event Loop Lag Measurement", "Measure Node.js event loop lag under 75 VUs", "Medium", "Event loop delay remains < 100ms"),
        ("Stress Garbage Collection Pressure", "Monitor V8 garbage collection pauses during heavy allocation load", "Medium", "GC pauses do not exceed 200ms"),
        ("Stress Memory Consumption Growth", "Observe Node.js resident set size (RSS) under 100 VUs", "High", "RSS stays within 512MB container limit"),
        ("Stress Recovery Post 100 VUs", "Drop from 100 VUs back to 5 VUs and measure recovery time", "Critical", "Latencies return to baseline (< 100ms) within 10s"),
        ("Stress Zero 502 Bad Gateway Errors", "Verify reverse proxy or server does not emit 502 Bad Gateway under stress", "High", "Zero 502 responses emitted"),
        ("Stress Zero 503 Service Unavailable", "Verify server does not drop connections with 503", "High", "Zero 503 responses emitted"),
        ("Stress Zero 504 Gateway Timeout", "Verify all requests complete before 30s gateway timeout", "High", "Zero 504 timeouts occur"),
        ("Stress Rapid Sequential Requests No Think Time", "VUs execute back-to-back requests with 0ms sleep delay", "Medium", "Maximum requests per second throughput identified"),
        ("Stress High Request Rate 150 RPS", "Drive request rate to 150 requests per second", "High", "System sustains throughput without crashing"),
        ("Stress Large Payload Processing", "Post 50 multi-day trip itineraries with 30+ activities each", "Medium", "JSON body parser handles large payloads without memory spike"),
        ("Stress Concurrent Profile Updates", "30 VUs updating user profiles simultaneously", "Medium", "No data race conditions or document version conflicts"),
        ("Stress Mixed CRUD Under Heavy Load", "Concurrent mix: 40% read, 30% create, 20% update, 10% delete", "High", "All CRUD operations maintain data integrity"),
        ("Stress Cache Invalidation Under Load", "Frequent updates trigger cache invalidations while reads are active", "Low", "Cache coherence preserved"),
        ("Stress Frontend Static File Load Under 100 VUs", "100 VUs fetching static assets simultaneously", "Medium", "Static assets served efficiently"),
        ("Stress HTTP 429 Rate Limiter Trigger", "Verify rate limiting activates if threshold is exceeded under stress", "High", "429 Too Many Requests returned gracefully if configured"),
        ("Stress Token Verification Saturation", "100 VUs submitting requests with Bearer JWT tokens to test jwt.verify throughput", "High", "JWT verification processes at > 500 req/s"),
        ("Stress Database Write Queue Depth", "Monitor write queue depth during 50 concurrent trip creations", "Medium", "Queue drains cleanly without connection timeout"),
        ("Stress Slow Client Simulation", "Simulate slow client connections during high server load", "Low", "Server does not block other clients on slow write sockets"),
        ("Stress CPU Saturation Point Identification", "Identify VU count where CPU reaches 90%", "Medium", "Threshold recorded for capacity planning"),
        ("Stress Memory Saturation Point Identification", "Identify VU count where memory climbs steeply", "Medium", "Threshold recorded for auto-scaling triggers"),
        ("Stress Graceful Degradation Check", "Verify server responds with appropriate error rather than silent hanging", "High", "Clean HTTP status codes maintained"),
        ("Stress Worker Thread Utilization", "Verify Node.js libuv threadpool behavior under crypto/bcrypt load", "Medium", "Threadpool does not starve asynchronous I/O"),
        ("Stress Database Connection Reconnection", "Simulate transient database glitch during stress and verify recovery", "High", "Backend reconnects and resumes service"),
        ("Stress Latency Percentile p99.9 Observation", "Record ultra-tail latency under stress profile", "Low", "p99.9 latency recorded"),
        ("Stress Sustained 3-Minute Stress Run", "Execute 50 VUs sustained load for 3 minutes", "High", "System maintains stability over multi-minute stress duration"),
        ("Stress Post-Test Log Inspection", "Inspect server error logs post-stress test for unhandled promise rejections", "High", "Zero unhandled promise rejections logged"),
        ("Stress Port Exhaustion Prevention", "Verify ephemeral port exhaustion does not occur on test runner", "Low", "TCP connections closed or recycled cleanly"),
        ("Stress Peak Concurrency Threshold Evaluation", "Evaluate k6 threshold results for stress execution", "High", "Stress metrics captured in report"),
        ("Stress Report Generation Verification", "Verify JSON and HTML summaries output valid stress test data", "High", "Summary files generated"),
        ("Stress Failure Rate Logging", "Log any failed requests with HTTP status code and response body snippet", "Medium", "Detailed failure diagnostic output"),
        ("Stress Network Bandwidth Utilization", "Measure network megabits per second transferred during stress", "Low", "Bandwidth consumption recorded"),
        ("Stress Server Process Survivability", "Verify Node.js process PID remains unchanged throughout stress run", "Critical", "Process did not restart or crash"),
        ("Stress Heap Snapshot Comparison", "Compare heap size before and after stress profile", "Medium", "Heap returns to baseline after GC"),
        ("Stress Test Completion Clean Teardown", "Teardown k6 stress execution without zombie connections", "High", "Clean test exit")
    ]
    for idx, (n, d, p, e) in enumerate(c3, 86):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Stress Profile Scenarios", "name": n, "description": d, "priority": p, "expected_result": e})

    # 4. Spike Profile Scenarios (LOAD-131 to LOAD-170) - 40
    c4 = [
        ("Spike Traffic Surge 2 to 50 VUs in 5s", "Instantly surge concurrency from 2 to 50 VUs within 5 seconds", "Critical", "Server absorbs traffic spike without dropping connections"),
        ("Spike Flash Sale Destination Search", "50 VUs hit GET /api/destinations within 2-second burst window", "High", "All requests complete, p95 < 400ms"),
        ("Spike Flash Sale Booking Submission", "30 VUs submit POST /api/bookings within 3-second burst window", "Critical", "Bookings created, zero 500 server crashes"),
        ("Spike Login Surge Post-Notification", "40 VUs submit POST /api/auth/login simultaneously", "High", "Logins processed sequentially or concurrently without connection drop"),
        ("Spike Recovery Within 10 Seconds", "Measure time for response latency to normalize after spike drops", "High", "Latencies normalize back to < 100ms within 10s"),
        ("Spike Micro-Burst 100 Requests in 1s", "Inject 100 requests in a 1-second burst window", "High", "Server absorbs micro-burst smoothly"),
        ("Spike Dual Wave Double Spike", "First spike to 40 VUs, drop to 5 VUs, second spike to 60 VUs", "High", "Server survives consecutive shock waves"),
        ("Spike Database Connection Spike Handling", "Observe MongoDB connection count during sudden traffic spike", "Medium", "Pool handles connection burst without exhausting limit"),
        ("Spike Memory Surge Observation", "Verify heap memory does not spike dangerously during sudden allocation surge", "Medium", "V8 heap manages burst allocations cleanly"),
        ("Spike Event Loop Surge Delay", "Verify event loop delay during spike remains < 250ms", "Medium", "Event loop does not freeze"),
        ("Spike Zero Connection Reset By Peer", "Verify client does not encounter ECONNRESET during spike", "High", "Zero connection reset errors observed"),
        ("Spike Zero Connection Refused", "Verify client does not encounter ECONNREFUSED during spike", "High", "Zero connection refused errors observed"),
        ("Spike Frontend Asset Spike", "50 VUs requesting frontend index.html and assets in 2s burst", "Medium", "Static assets delivered without latency spike"),
        ("Spike Expense Logging Wave", "30 VUs logging expenses in burst fashion", "Medium", "Expenses committed accurately"),
        ("Spike Search Autocomplete Burst", "50 VUs sending rapid 3-character search queries in burst", "Medium", "Search endpoint responds within acceptable limits"),
        ("Spike Itinerary Optimization Burst", "20 VUs requesting trip cost optimization calculations simultaneously", "High", "Optimization CPU calculations complete cleanly"),
        ("Spike Token Validation Wave", "50 VUs requesting protected routes simultaneously", "High", "JWT authentication validates every request"),
        ("Spike Profile View Wave", "40 VUs requesting GET /api/auth/user concurrently", "Medium", "User profiles delivered with 0% error rate"),
        ("Spike Trip List Fetch Wave", "40 VUs requesting GET /api/trips concurrently", "Medium", "Trip lists delivered with 0% error rate"),
        ("Spike Booking List Fetch Wave", "40 VUs requesting GET /api/bookings concurrently", "Medium", "Booking lists delivered with 0% error rate"),
        ("Spike Expense Stats Calculation Wave", "30 VUs requesting expense statistics in burst", "Medium", "Calculations complete within 400ms"),
        ("Spike Server Backpressure Management", "Verify server applies natural backpressure without crashing", "High", "Sockets queued and handled gracefully"),
        ("Spike Threshold Evaluation", "Evaluate k6 threshold satisfaction under spike profile", "High", "Thresholds evaluated accurately"),
        ("Spike Latency p95 Surge Ceiling", "Ensure p95 latency during peak spike does not exceed 1000ms", "High", "p95 ceiling respected"),
        ("Spike Latency p99 Surge Ceiling", "Ensure p99 latency during peak spike does not exceed 1500ms", "Medium", "p99 ceiling respected"),
        ("Spike Error Rate Ceiling Under 2%", "Ensure error rate during peak spike does not exceed 2%", "High", "Error rate stays < 2%"),
        ("Spike Recovery Latency Verification", "Verify 5 consecutive requests immediately after spike have latency < 80ms", "High", "System fully recovered"),
        ("Spike System Load Average Peak", "Record OS load average during spike execution", "Low", "Load average recorded"),
        ("Spike Network Throughput Peak", "Record peak network transfer rate during spike", "Low", "Peak throughput captured"),
        ("Spike Socket Keep-Alive Resiliency", "Verify keep-alive sockets remain functional across spike burst", "Medium", "Keep-alive connections maintained"),
        ("Spike Zero Orphaned Sockets", "Verify all sockets close or return to pool after spike", "Medium", "Zero dangling sockets detected"),
        ("Spike Logcat/Console Cleanliness", "Inspect server console for uncaught exception traces during spike", "High", "Zero crash stack traces in console"),
        ("Spike Fast Ramp Down 50 to 0 VUs in 2s", "Abruptly drop concurrency from 50 to 0 VUs", "Medium", "Server settles to idle immediately"),
        ("Spike Multi-Tenant Concurrency Burst", "Multiple distinct user accounts making concurrent requests", "High", "Tenant data isolation maintained under spike"),
        ("Spike Unauthenticated vs Authenticated Mix", "Spike containing 50% public queries and 50% authenticated queries", "High", "Both public and protected routes handle burst"),
        ("Spike Payload Deserialization Burst", "Bursts of large JSON requests hitting API", "Medium", "Payloads parsed without V8 buffer exhaustion"),
        ("Spike HTTP Method Mix Burst", "Bursts mixing GET, POST, PUT, DELETE concurrently", "High", "All HTTP methods process reliably"),
        ("Spike Asynchronous File Write Impact", "Verify logging or report writing does not block main thread during spike", "Low", "Asynchronous I/O operates smoothly"),
        ("Spike Summary HTML Generation", "Verify k6 HTML reporter generates spike performance visualization", "High", "HTML report generated"),
        ("Spike Test Execution Completion", "Complete spike test run within allocated CI test window", "High", "Test finishes with valid summary")
    ]
    for idx, (n, d, p, e) in enumerate(c4, 131):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Spike Profile Scenarios", "name": n, "description": d, "priority": p, "expected_result": e})

    # 5. Soak & Endurance Profile Scenarios (LOAD-171 to LOAD-205) - 35
    c5 = [
        ("Soak Extended Baseline 5 VUs", "Run sustained 5 VUs load for extended duration to monitor stability", "High", "Zero memory leak, stable latency over time"),
        ("Soak Memory Leak Detection", "Compare RSS memory at minute 1 vs minute 5 of continuous load", "Critical", "RSS delta < 20MB after initial warmup"),
        ("Soak Database Connection Pool Leak Detection", "Verify active Mongoose connection count does not grow monotonically", "Critical", "Connection pool remains stable at configured pool size"),
        ("Soak Event Listener Leak Detection", "Monitor EventEmitter listener counts on server process", "High", "No MaxListenersExceededWarning emitted"),
        ("Soak File Descriptor Leak Detection", "Monitor open file descriptors on server process over time", "High", "File descriptors close properly after request completion"),
        ("Soak Socket Leak Detection", "Verify closed client sockets do not remain in CLOSE_WAIT state indefinitely", "High", "Sockets cleaned up cleanly by OS TCP stack"),
        ("Soak V8 Heap Growth Rate", "Track heapUsed metric across 500 consecutive test iterations", "Medium", "Heap stabilizes at steady state"),
        ("Soak Sustained Latency Consistency", "Verify p95 latency does not drift upwards over prolonged test duration", "High", "Latency remains flat throughout test run"),
        ("Soak Continuous User Journey Cycles", "VUs continuously perform: Login -> Browse -> Plan -> Add Expense -> Logout", "Critical", "100% of journey iterations complete successfully"),
        ("Soak Continuous Destination Searches", "VUs continuously query destination catalogue with random filters", "Medium", "Search throughput remains constant"),
        ("Soak Continuous Trip Creations and Deletions", "VUs continuously create and delete temporary trips to test DB churn", "High", "Database handles continuous churn without slowdown"),
        ("Soak Continuous Booking Operations", "VUs continuously create bookings to test collection growth handling", "Medium", "Bookings insert reliably"),
        ("Soak Continuous Expense Tracking", "VUs continuously add and remove expenses", "Medium", "Expense calculations remain accurate"),
        ("Soak Continuous Profile Updates", "VUs continuously update profile names and avatars", "Low", "Profile updates persist cleanly"),
        ("Soak Error Rate Long-Term Stability", "Ensure cumulative error rate remains < 0.1% across full soak run", "Critical", "Error rate stays well below threshold"),
        ("Soak Garbage Collection Frequency", "Monitor minor and major GC cycle intervals under steady load", "Medium", "GC cycles occur at regular healthy intervals"),
        ("Soak CPU Temperature / Throttling", "Ensure server runner does not thermal throttle during soak run", "Low", "CPU performance remains consistent"),
        ("Soak Disk Space Consumption", "Verify application log file growth does not exhaust disk storage", "Low", "Log file growth rate is manageable"),
        ("Soak Network Packet Loss Rate", "Monitor for TCP retransmissions or dropped packets over soak duration", "Low", "Packet loss rate < 0.05%"),
        ("Soak HTTP Keep-Alive Session Longevity", "Verify clients can maintain long-lived keep-alive connections", "Medium", "Keep-alive connections handle multiple requests"),
        ("Soak Periodic Background Jobs Impact", "Verify background tasks (e.g. seeding, cleanup) do not cause latency spikes", "Low", "Latency remains unaffected by background tasks"),
        ("Soak Repeated JWT Token Generation", "Issue 500+ tokens over time to verify signing performance and entropy", "Medium", "Token generation throughput remains consistent"),
        ("Soak Token Verification Throughput", "Verify 10,000+ token verifications complete without crypto memory leak", "Medium", "Crypto memory remains bounded"),
        ("Soak Continuous 404 Route Requests", "Periodically send 404 requests to verify error handlers do not leak memory", "Low", "Error handler cleans up request/response objects"),
        ("Soak Continuous 401 Route Requests", "Periodically send unauthenticated requests to verify auth guard cleanup", "Low", "Auth guards release resources cleanly"),
        ("Soak Asynchronous Callback Stack Depth", "Verify async callback chains do not grow unbounded", "Medium", "Call stack depth remains normal"),
        ("Soak Server Health Probe Consistency", "Probe GET / every 10 seconds during soak test", "High", "Health check always returns 200 OK within 30ms"),
        ("Soak Mock DB Fallback Endurance", "Run soak test against in-memory mock DB mode to verify mock stability", "High", "Mock DB handles continuous access without memory explosion"),
        ("Soak MongoDB Mode Endurance", "Run soak test against MongoDB container to verify driver connection longevity", "High", "Mongo driver maintains healthy connection state"),
        ("Soak Test Progress Reporting", "Verify k6 logs periodic progress metrics every 30s", "Low", "Progress logs output cleanly"),
        ("Soak Metric Percentiles Stability", "Verify p50, p90, p95, p99 ratios remain constant over time", "Medium", "Distribution shape remains consistent"),
        ("Soak Runner Process Stability", "Verify k6 runner process itself does not leak memory on prolonged runs", "Medium", "Runner memory remains bounded"),
        ("Soak Graceful Termination On Interrupt", "Send SIGINT to k6 and verify graceful report generation", "Low", "Runner handles interrupt cleanly"),
        ("Soak HTML Report Rendering of Long Series", "Verify HTML reporter renders long-duration timeseries graphs", "Low", "Report renders cleanly"),
        ("Soak Test Completion Success", "Endurance test completes full duration and satisfies all criteria", "High", "Endurance test marked successful")
    ]
    for idx, (n, d, p, e) in enumerate(c5, 171):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Soak & Endurance Profile Scenarios", "name": n, "description": d, "priority": p, "expected_result": e})

    # 6. API Performance & Endpoint Benchmarks (LOAD-206 to LOAD-240) - 35
    c6 = [
        ("Benchmark GET / Latency TTFB", "Measure Time To First Byte for root health endpoint", "High", "TTFB < 20ms"),
        ("Benchmark GET /api/destinations TTFB", "Measure TTFB for full destinations catalogue", "High", "TTFB < 40ms"),
        ("Benchmark GET /api/destinations?search=Goa TTFB", "Measure TTFB for filtered destination query", "High", "TTFB < 40ms"),
        ("Benchmark POST /api/auth/login TTFB", "Measure TTFB for authentication login request", "Critical", "TTFB < 120ms (including bcrypt compare)"),
        ("Benchmark POST /api/auth/signup TTFB", "Measure TTFB for user registration request", "Critical", "TTFB < 150ms (including bcrypt salt & hash)"),
        ("Benchmark GET /api/auth/user TTFB", "Measure TTFB for authenticated user profile retrieval", "High", "TTFB < 50ms"),
        ("Benchmark PUT /api/auth/user TTFB", "Measure TTFB for user profile update", "Medium", "TTFB < 60ms"),
        ("Benchmark GET /api/trips TTFB", "Measure TTFB for user trips list retrieval", "High", "TTFB < 50ms"),
        ("Benchmark GET /api/trips/:id TTFB", "Measure TTFB for single trip retrieval", "High", "TTFB < 40ms"),
        ("Benchmark POST /api/trips TTFB", "Measure TTFB for trip creation and cost optimization", "Critical", "TTFB < 100ms"),
        ("Benchmark PUT /api/trips/:id/status TTFB", "Measure TTFB for trip status update", "Medium", "TTFB < 50ms"),
        ("Benchmark DELETE /api/trips/:id TTFB", "Measure TTFB for trip deletion", "Medium", "TTFB < 50ms"),
        ("Benchmark GET /api/bookings TTFB", "Measure TTFB for user bookings list retrieval", "High", "TTFB < 50ms"),
        ("Benchmark POST /api/bookings TTFB", "Measure TTFB for booking creation", "Critical", "TTFB < 80ms"),
        ("Benchmark GET /api/expenses/trip/:id TTFB", "Measure TTFB for trip expenses list", "High", "TTFB < 40ms"),
        ("Benchmark GET /api/expenses/trip/:id/stats TTFB", "Measure TTFB for expense aggregation statistics", "High", "TTFB < 60ms"),
        ("Benchmark POST /api/expenses TTFB", "Measure TTFB for expense creation", "Critical", "TTFB < 70ms"),
        ("Benchmark Frontend Index HTML Download Time", "Measure content download time for frontend index.html", "Medium", "Download time < 20ms"),
        ("Benchmark Frontend JS Bundle Download Time", "Measure content download time for 400KB+ JS bundle", "Medium", "Download time < 80ms"),
        ("Benchmark Frontend CSS Bundle Download Time", "Measure content download time for CSS stylesheet", "Low", "Download time < 15ms"),
        ("Benchmark DNS Resolution Duration", "Measure DNS resolution time across endpoints", "Low", "DNS duration < 5ms"),
        ("Benchmark TCP Connection Handshake Duration", "Measure TCP SYN/ACK handshake duration", "Medium", "TCP handshake < 15ms"),
        ("Benchmark HTTP Header Parsing Overhead", "Measure server overhead to parse incoming HTTP request headers", "Low", "Parsing overhead < 2ms"),
        ("Benchmark JSON Deserialization Overhead", "Measure server time to deserialize 20KB trip payload", "Low", "Deserialization time < 5ms"),
        ("Benchmark JSON Serialization Overhead", "Measure server time to serialize destination catalogue response", "Low", "Serialization time < 5ms"),
        ("Benchmark Single VU Maximum Throughput", "Measure maximum RPS achievable with 1 VU (zero think time)", "Medium", "Single VU achieves > 80 req/s"),
        ("Benchmark 5 VUs Maximum Throughput", "Measure maximum RPS achievable with 5 VUs", "Medium", "5 VUs achieve > 250 req/s"),
        ("Benchmark 10 VUs Maximum Throughput", "Measure maximum RPS achievable with 10 VUs", "Medium", "10 VUs achieve > 400 req/s"),
        ("Benchmark Compression Ratio Savings", "Measure bandwidth savings from gzip/deflate compression", "Low", "Compression reduces payload size by > 60%"),
        ("Benchmark HTTP Pipeline Response Pacing", "Measure latency consistency across 100 sequential requests", "Low", "Standard deviation < 15ms"),
        ("Benchmark CORS Overhead", "Measure latency difference between requests with and without CORS headers", "Low", "CORS overhead < 2ms"),
        ("Benchmark Route Matching Overhead", "Measure Express router match time across routes", "Low", "Router overhead < 1ms"),
        ("Benchmark Middleware Chain Overhead", "Measure time spent in Express middleware chain (cors, json, auth)", "Low", "Middleware overhead < 5ms"),
        ("Benchmark Status Code 200 vs 401 Latency", "Compare response time of authorized vs unauthorized requests", "Low", "Unauthorized request rejects faster than authorized"),
        ("Benchmark Baseline Metric Recording", "Record all endpoint baseline benchmarks to performance report", "High", "Baseline metrics compiled")
    ]
    for idx, (n, d, p, e) in enumerate(c6, 206):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "API Performance & Benchmarks", "name": n, "description": d, "priority": p, "expected_result": e})

    # 7. Authentication Under Load (LOAD-241 to LOAD-265) - 25
    c7 = [
        ("Auth Load 15 Concurrent Logins", "15 VUs executing login POST /api/auth/login concurrently", "Critical", "All 15 logins succeed, p95 < 300ms"),
        ("Auth Load 25 Concurrent Logins", "25 VUs executing login POST /api/auth/login concurrently", "Critical", "All 25 logins succeed, p95 < 450ms"),
        ("Auth Load Bcrypt Salt Factor 10 Impact", "Measure CPU load during 20 concurrent bcrypt hash operations", "High", "CPU handles hashing without thread starvation"),
        ("Auth Load Invalid Credentials Burst", "20 VUs submitting bad credentials simultaneously", "High", "Rejections handled cleanly with 401, p95 < 250ms"),
        ("Auth Load Missing Fields Rejection Speed", "30 VUs submitting empty auth payloads", "Medium", "Rejected immediately with 400 within 30ms"),
        ("Auth Load Token Verification Concurrency", "50 VUs hitting protected routes with valid JWT tokens", "Critical", "JWT verification throughput > 300 req/s, 0% errors"),
        ("Auth Load Expired Token Rejection Concurrency", "20 VUs submitting expired tokens concurrently", "High", "Rejected cleanly with 401 within 30ms"),
        ("Auth Load Tampered Token Rejection Concurrency", "20 VUs submitting tampered token signatures", "High", "Rejected cleanly with 401 within 30ms"),
        ("Auth Load Concurrent User Registrations", "10 VUs creating new unique user accounts simultaneously", "Critical", "All 10 accounts created with unique IDs, 0% errors"),
        ("Auth Load Duplicate Registration Concurrency", "10 VUs attempting to register same email simultaneously", "High", "One succeeds, 9 receive 400 User already exists"),
        ("Auth Load Case-Insensitive Email Lookups", "20 VUs authenticating with varying uppercase/lowercase email casing", "Medium", "All logins normalize email and succeed"),
        ("Auth Load Whitespace Email Lookups", "20 VUs authenticating with emails containing leading/trailing whitespace", "Medium", "All logins trim email and succeed"),
        ("Auth Load Profile Retrieval Under Auth Load", "30 VUs requesting GET /api/auth/user simultaneously", "High", "All user profiles retrieved within 200ms"),
        ("Auth Load Profile Update Concurrency", "10 VUs updating user profiles simultaneously", "Medium", "Profile updates committed accurately"),
        ("Auth Load Authorization Header Formats", "Test requests with 'Bearer <token>', 'bearer <token>', and raw tokens", "Low", "Standard Bearer format accepted, invalid formats rejected"),
        ("Auth Load Missing Token Rejections", "50 VUs hitting protected endpoint without token", "High", "All 50 rejected immediately with 401 within 20ms"),
        ("Auth Load Token Payload Parsing Speed", "Measure jwt.decode / jwt.verify throughput across 1,000 iterations", "Medium", "Verification takes < 0.5ms per token"),
        ("Auth Load Rapid Sequential Logins Same User", "Single user logging in 20 times in rapid succession", "Medium", "All logins succeed and return valid tokens"),
        ("Auth Load Multi-User Login Mix", "20 different user accounts logging in concurrently", "High", "Each user receives correct respective profile"),
        ("Auth Load Password Complexity Variations", "Authenticate with passwords of varying lengths (6 to 64 chars)", "Medium", "Hashing handles varying lengths cleanly"),
        ("Auth Load Special Characters in Password", "Authenticate with passwords containing complex symbols", "Medium", "Passwords matched accurately under load"),
        ("Auth Load Offline Mock DB Auth Throughput", "Measure login throughput when operating in mock database fallback", "High", "Mock DB authenticates at > 500 req/s"),
        ("Auth Load Auth Error Rate Verification", "Verify http_req_failed = 0 for valid auth load tests", "Critical", "Zero unexpected auth errors"),
        ("Auth Load Latency Threshold Verification", "Verify auth p95 remains below 500ms threshold", "Critical", "p95 threshold confirmed satisfied"),
        ("Auth Load Summary Report Generation", "Compile authentication load test results into performance report", "High", "Auth metrics recorded")
    ]
    for idx, (n, d, p, e) in enumerate(c7, 241):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Authentication Under Load", "name": n, "description": d, "priority": p, "expected_result": e})

    # 8. Database Operations Under Load (LOAD-266 to LOAD-285) - 20
    c8 = [
        ("DB Load Concurrent Reads Destination Catalogue", "30 VUs reading destinations concurrently from database/mock", "High", "Database reads execute without lock contention"),
        ("DB Load Concurrent Writes Trip Creation", "15 VUs inserting new trip documents concurrently", "Critical", "Documents inserted with unique ObjectIds"),
        ("DB Load Concurrent Updates Trip Status", "15 VUs updating trip status documents concurrently", "High", "Updates apply cleanly with atomic operations"),
        ("DB Load Concurrent Deletes Trip Cleanup", "15 VUs deleting created trip documents concurrently", "High", "Documents deleted cleanly without orphan records"),
        ("DB Load Concurrent Reads Booking Retrieval", "20 VUs querying bookings by tripId", "High", "Queries resolve using index or filter efficiently"),
        ("DB Load Concurrent Writes Booking Creation", "15 VUs inserting booking documents concurrently", "High", "Bookings persist with relational integrity"),
        ("DB Load Concurrent Reads Expense Items", "25 VUs querying expenses by tripId", "High", "Expense arrays returned within 100ms"),
        ("DB Load Concurrent Writes Expense Creation", "20 VUs inserting expense documents concurrently", "High", "Expenses inserted without document lock delays"),
        ("DB Load Expense Statistics Aggregation Pipeline", "20 VUs running group-by aggregation pipeline on expenses", "High", "Aggregation computes totalSpend and breakdown accurately"),
        ("DB Load Regex Search Query Concurrency", "20 VUs running regex search across destination names", "High", "Regex queries execute within 80ms without CPU spike"),
        ("DB Load Connection Pool Allocation Speed", "Measure time to acquire connection from pool under load", "Medium", "Connection acquisition < 5ms"),
        ("DB Load Connection Release Back To Pool", "Verify connections return immediately to pool after query", "Medium", "Pool utilization stays optimal"),
        ("DB Load Large Query Result Set", "Query all destinations and trips with high limit", "Medium", "Payload deserialized and returned cleanly"),
        ("DB Load Heavy Write Burst 50 Documents", "Burst insert 50 expense records in parallel", "High", "All 50 records committed"),
        ("DB Load Read-After-Write Consistency", "Write new trip document and immediately read by ID", "High", "New document is immediately available for read"),
        ("DB Load Transaction Simulation", "Perform multi-step operation (create trip -> add booking -> add expense)", "Critical", "All relational operations succeed consistently"),
        ("DB Load Query Timeout Resilience", "Verify database driver timeout does not hang server indefinitely", "High", "Driver enforces timeout cleanly"),
        ("DB Load Mock Database In-Memory Array Churn", "Verify mockDb array push/find operations under 50 VUs concurrency", "High", "JavaScript array operations handle concurrency safely"),
        ("DB Load Database Error Handling Graceful Degradation", "Simulate DB connection hiccup and verify server returns 500 without crashing", "High", "Server survives and recovers cleanly"),
        ("DB Load Metrics Summary Compilation", "Capture database query throughput and latency metrics in report", "High", "Database metrics documented")
    ]
    for idx, (n, d, p, e) in enumerate(c8, 266):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "Database Operations Under Load", "name": n, "description": d, "priority": p, "expected_result": e})

    # 9. High-Volume Payload & Data Processing (LOAD-286 to LOAD-300) - 15
    c9 = [
        ("Payload Load 50KB Itinerary JSON", "Post trip with 50KB detailed multi-day itinerary JSON payload", "High", "Payload parsed and persisted without delay"),
        ("Payload Load 100KB Large JSON Body", "Post large trip payload with extensive activity details", "Medium", "Server processes 100KB JSON cleanly"),
        ("Payload Load 100 Concurrent Itinerary Items", "Post trip itinerary containing 100 scheduled activities", "Medium", "Itinerary stored and retrieved accurately"),
        ("Payload Load Deeply Nested JSON Parsing", "Post itinerary with multi-level nested waypoint coordinates", "Medium", "Nested structures parsed accurately"),
        ("Payload Load Unicode & Multilingual Payload", "Post itinerary with Hindi, Japanese, and accented characters", "Low", "UTF-8 strings preserved without corruption"),
        ("Payload Load Large Expense Batch", "Submit 20 expenses in rapid batch requests", "Medium", "All batch expenses recorded"),
        ("Payload Load Large Profile Avatar URL", "Update profile with 2KB data URI or long image URL", "Low", "URL stored without string truncation"),
        ("Payload Load Request Header Overhead", "Send requests with 20 custom headers to test header parsing", "Low", "Server parses headers without HTTP 431 error"),
        ("Payload Load Destination Filter Large Search Term", "Query destination search with 256-character search term", "Low", "Term handled safely without ReDoS"),
        ("Payload Load High Volume Response Transfer", "Fetch large combined user trips and bookings summary", "Medium", "Response transfers efficiently over TCP stream"),
        ("Payload Load Concurrent JSON Serialization", "30 VUs serializing large response payloads simultaneously", "Medium", "V8 JSON.stringify throughput remains high"),
        ("Payload Load Memory Allocation Under Big Payloads", "Monitor memory consumption during big payload ingestion", "Medium", "Memory buffers garbage collected promptly"),
        ("Payload Load Zero Payload Truncation", "Verify received payload length exactly matches transmitted payload", "High", "Byte-for-byte integrity verified"),
        ("Payload Load Content-Length Header Validation", "Verify server accurately reports Content-Length on responses", "Low", "Content-Length header matches body length"),
        ("Payload Load Summary Report Compilation", "Compile final k6 load test results into JSON and HTML summaries", "Critical", "Comprehensive reports generated and saved to reports directory")
    ]
    for idx, (n, d, p, e) in enumerate(c9, 286):
        cases.append({"id": f"LOAD-{idx:03d}", "category": "High-Volume Payload & Data Processing", "name": n, "description": d, "priority": p, "expected_result": e})

    return cases

# ----------------- SECURITY (SEC-001 to SEC-300) -----------------
def get_security_cases():
    cases = []
    
    # 1. Authentication Security & JWT Validation (SEC-001 to SEC-030) - 30
    c1 = [
        ("JWT Signature Verification", "Verify API rejects JWT token with forged or tampered signature", "Critical", "HTTP 401 Unauthorized, invalid token"),
        ("JWT Algorithm None Attack", "Verify API rejects JWT token configured with alg='none'", "Critical", "HTTP 401 Unauthorized, invalid token algorithm"),
        ("JWT Expired Token Rejection", "Verify API rejects JWT token with expired exp timestamp", "Critical", "HTTP 401 Unauthorized, token expired"),
        ("JWT Not Before Claim Handling", "Verify API rejects JWT token with future nbf timestamp", "High", "HTTP 401 Unauthorized, token not active"),
        ("JWT Secret Entropy & Strength", "Verify JWT_SECRET is not a trivial dictionary word (e.g. 'secret')", "Critical", "JWT secret meets minimum entropy requirements (>= 256-bit)"),
        ("JWT Missing Header Rejection", "Submit request to protected route with Authorization header absent", "Critical", "HTTP 401 Unauthorized, no token provided"),
        ("JWT Malformed Header Format", "Submit request with header 'Authorization: InvalidFormatToken'", "High", "HTTP 401 Unauthorized, malformed authorization header"),
        ("JWT Empty Bearer Token", "Submit request with header 'Authorization: Bearer '", "High", "HTTP 401 Unauthorized, token missing"),
        ("JWT Non-Bearer Scheme Rejection", "Submit request with header 'Authorization: Basic dXNlcjpwYXNz'", "High", "HTTP 401 Unauthorized, invalid auth scheme"),
        ("JWT Symmetric vs Asymmetric Confusion", "Test HMAC key confusion attack if public key is exposed", "High", "Algorithm confusion attack fails"),
        ("Bcrypt Password Hashing Standard", "Verify user passwords are saved using bcrypt with salt rounds >= 10", "Critical", "Passwords stored as valid bcrypt hashes ($2a$, $2b$, or $2y$)"),
        ("Password Plaintext Storage Prevention", "Inspect database records to confirm zero plaintext passwords exist", "Critical", "Zero plaintext passwords in user records"),
        ("Password Hash Exposure In User API", "Verify GET /api/auth/user does NOT return password hash field", "Critical", "Password field stripped from user response object"),
        ("Password Hash Exposure In Signup API", "Verify POST /api/auth/signup does NOT return password hash field", "Critical", "Password field excluded from registration response"),
        ("Password Hash Exposure In Login API", "Verify POST /api/auth/login does NOT return password hash field", "Critical", "Password field excluded from login response"),
        ("Brute Force Rate Limiting Login", "Attempt 20 rapid incorrect logins for the same account", "High", "Rate limiting or throttling slows brute force attempts"),
        ("Timing Attack Resistance On Login", "Measure response time for existing vs nonexistent email login", "Medium", "Response times are balanced to prevent user enumeration"),
        ("Credential Stuffing Defense", "Test bulk automated credential submissions against auth endpoint", "High", "System resists automated credential stuffing"),
        ("Password Minimum Length Policy", "Verify signup rejects passwords shorter than 6 characters", "High", "HTTP 400 Bad Request, password too short"),
        ("Password Maximum Length Handling", "Submit password with 10,000 characters to test DoS resilience", "Medium", "Server truncates or rejects oversized password without CPU hang"),
        ("Credential Leakage In URL Prevention", "Verify credentials are never accepted or transmitted via URL query params", "High", "Only POST request bodies accepted for auth"),
        ("Session Token Revocation On Password Reset", "Verify tokens are invalidated when user updates password", "High", "Old session tokens become invalid"),
        ("Multi-Device Session Management", "Verify multiple valid logins for same user generate unique tokens", "Medium", "Each login receives distinct valid token"),
        ("Token Entropy & Randomness", "Verify generated JWT tokens have high entropy and unique jti/signatures", "Medium", "Tokens are cryptographically non-predictable"),
        ("Auth Error Message Genericity", "Verify login failure message is generic ('Invalid credentials')", "High", "Error does not reveal whether email or password was wrong"),
        ("Signup User Enumeration Defense", "Verify signup responses do not reveal detailed internal user metadata", "Medium", "Clean conflict message returned"),
        ("Sensitive Data In JWT Payload", "Inspect decoded JWT claims to ensure no passwords or secrets in payload", "Critical", "JWT payload contains only user id and standard claims"),
        ("Token Storage LocalStorage Security", "Inspect web frontend token storage for XSS defensive posture", "Medium", "Frontend uses best practices for token management"),
        ("Mobile SharedPreferences Security", "Verify Flutter mobile app stores auth token in secure storage", "Medium", "Token stored in SharedPreferences / FlutterSecureStorage"),
        ("Session Fixation Prevention", "Verify authentication regenerates session context and issues fresh token", "High", "Pre-auth tokens cannot access post-auth state")
    ]
    for idx, (n, d, p, e) in enumerate(c1, 1):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Authentication Security & JWT Validation", "name": n, "description": d, "priority": p, "expected_result": e})

    # 2. Authorization & Access Control (BOLA/IDOR) (SEC-031 to SEC-060) - 30
    c2 = [
        ("IDOR Trip Retrieval Prevention", "User A attempts to access User B's private trip by ID GET /api/trips/:id", "Critical", "HTTP 404 or 403 Forbidden, cross-user trip access denied"),
        ("IDOR Trip Modification Prevention", "User A attempts to update User B's trip status PUT /api/trips/:id/status", "Critical", "HTTP 404 or 403 Forbidden, unauthorized modification denied"),
        ("IDOR Trip Deletion Prevention", "User A attempts to delete User B's trip DELETE /api/trips/:id", "Critical", "HTTP 404 or 403 Forbidden, unauthorized deletion denied"),
        ("IDOR Booking Retrieval Prevention", "User A attempts to access User B's booking by tripId", "Critical", "HTTP 404 or 403 Forbidden, unauthorized booking access denied"),
        ("IDOR Booking Creation Prevention", "User A attempts to create booking attached to User B's tripId", "Critical", "HTTP 404 or 403 Forbidden, booking rejected"),
        ("IDOR Expense Retrieval Prevention", "User A attempts to access expenses for User B's tripId", "Critical", "HTTP 404 or 403 Forbidden, expense access denied"),
        ("IDOR Expense Creation Prevention", "User A attempts to post expense attached to User B's tripId", "Critical", "HTTP 404 or 403 Forbidden, expense creation rejected"),
        ("IDOR Expense Stats Retrieval Prevention", "User A attempts to access expense stats for User B's tripId", "Critical", "HTTP 404 or 403 Forbidden, stats access denied"),
        ("IDOR User Profile Update Prevention", "User A attempts to update User B's profile by injecting { id: 'user_b_id' }", "Critical", "HTTP 401 or update restricted strictly to req.user.id"),
        ("Privilege Escalation Via Body Role Injection", "User registers with { role: 'admin' } in request body", "High", "Role property ignored or restricted to default user role"),
        ("Privilege Escalation Via Profile Update", "User sends PUT /api/auth/user with { role: 'admin', isAdmin: true }", "High", "Administrative privilege escalation ignored"),
        ("Unauthenticated Access To Trips List", "Attempt GET /api/trips without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Create Trip", "Attempt POST /api/trips without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Single Trip", "Attempt GET /api/trips/:id without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Delete Trip", "Attempt DELETE /api/trips/:id without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Update Trip Status", "Attempt PUT /api/trips/:id/status without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Bookings List", "Attempt GET /api/bookings without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Create Booking", "Attempt POST /api/bookings without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Trip Expenses", "Attempt GET /api/expenses/trip/:id without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Expense Stats", "Attempt GET /api/expenses/trip/:id/stats without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Add Expense", "Attempt POST /api/expenses without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To User Profile", "Attempt GET /api/auth/user without token", "Critical", "HTTP 401 Unauthorized"),
        ("Unauthenticated Access To Update Profile", "Attempt PUT /api/auth/user without token", "Critical", "HTTP 401 Unauthorized"),
        ("Public Access To Destinations Catalogue", "Verify GET /api/destinations is accessible without authentication", "High", "HTTP 200 OK, public destination browsing allowed"),
        ("Public Access To Root Health Check", "Verify GET / is accessible without authentication", "High", "HTTP 200 OK, public health check allowed"),
        ("Public Access To Signup Endpoint", "Verify POST /api/auth/signup is accessible without authentication", "High", "HTTP 201 or 400, public registration allowed"),
        ("Public Access To Login Endpoint", "Verify POST /api/auth/login is accessible without authentication", "High", "HTTP 200 or 401, public login allowed"),
        ("HTTP Method Tampering On Protected Routes", "Attempt HEAD / OPTIONS / TRACE to bypass auth guard", "High", "Auth guard enforces protection regardless of HTTP method"),
        ("Mass Assignment Vulnerability In Trip Creation", "Send unexpected admin fields in POST /api/trips payload", "High", "Only schema-defined trip fields are persisted"),
        ("Mass Assignment Vulnerability In User Update", "Send unexpected fields in PUT /api/auth/user payload", "High", "Only permitted user profile fields are updated")
    ]
    for idx, (n, d, p, e) in enumerate(c2, 31):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Authorization & Access Control", "name": n, "description": d, "priority": p, "expected_result": e})

    # 3. Session Security & Token Handling (SEC-061 to SEC-085) - 25
    c3 = [
        ("Session Expiry Enforcement", "Verify token cannot be used 1 second after expiration timestamp", "Critical", "HTTP 401 Unauthorized, token expired"),
        ("Session Token Integrity Check", "Flip a single bit in the JWT signature and verify rejection", "Critical", "HTTP 401 Unauthorized, signature verification failed"),
        ("Session Token Structure Validation", "Submit two-part JWT token (header.payload without signature)", "High", "HTTP 401 Unauthorized, malformed token"),
        ("Session Token Four-Part Reject", "Submit four-part token to verify structure validation", "High", "HTTP 401 Unauthorized, malformed token"),
        ("Authorization Header Space Normalization", "Submit 'Bearer  <token>' with multiple spaces", "Medium", "Server parses token cleanly or rejects gracefully"),
        ("Authorization Header Case Sensitivity", "Submit header with mixed case 'bEaReR <token>'", "Medium", "Server handles case-insensitivity cleanly"),
        ("Session Invalidation On User Delete", "Verify all sessions terminate if user account is removed", "High", "Subsequent requests return 401 or 404"),
        ("Session Token Non-Predictability", "Generate 100 consecutive tokens and check for sequential patterns", "High", "Zero predictable or sequential token structures"),
        ("Session Storage Plaintext Inspection", "Inspect mobile device storage to ensure tokens are not world-readable", "High", "App sandbox enforces private file permissions"),
        ("Session Cookie HttpOnly Flag", "If cookies are used for auth, verify HttpOnly flag is set", "High", "Cookie cannot be accessed via document.cookie"),
        ("Session Cookie Secure Flag", "If cookies are used for auth, verify Secure flag is set", "High", "Cookie only transmitted over HTTPS"),
        ("Session Cookie SameSite Attribute", "If cookies are used, verify SameSite=Strict or SameSite=Lax", "High", "Cookie protected against CSRF exploitation"),
        ("CSRF Protection On State-Changing Endpoints", "Verify state-changing POST/PUT/DELETE cannot be forged via CSRF", "High", "Bearer token authentication intrinsically protects against CSRF"),
        ("Replay Attack Resistance", "Verify replay of modified token is rejected", "High", "Tampered requests rejected"),
        ("Session Concurrent Logins Policy", "Verify application handles multiple active sessions per user", "Low", "Multi-device access supported safely"),
        ("Session Inactivity Timeout", "Verify token expiration lifetime is bounded (e.g. 7 days max)", "Medium", "JWT expiresIn attribute enforces bounded validity"),
        ("Token Signing Key Rotation Readiness", "Verify JWT verification supports key rotation via key ID or env", "Low", "Architecture supports secret key rotation"),
        ("Token In Query Parameter Rejection", "Attempt passing auth token as ?token=XYZ in query string", "High", "Server ignores query token for protected routes"),
        ("Token In Request Body Rejection", "Attempt passing auth token in JSON body { token: 'XYZ' }", "High", "Server enforces Authorization header strictly"),
        ("Bearer Token Whitespace Attack", "Submit token padded with null bytes (%00) or control characters", "Medium", "Server sanitizes and rejects malformed characters"),
        ("Session Hijacking Prevention via IP/UA", "Log security warnings when token IP or user agent shifts drastically", "Low", "Anomalous session activity detectable in logs"),
        ("Token Cryptographic Algorithm Hardening", "Verify HS256 / RS256 algorithm enforcement in jwt.verify", "High", "jwt.verify specifies allowed algorithms list"),
        ("Logout Token Purge In Frontend", "Verify handleLogout removes token from localStorage immediately", "High", "localStorage.getItem('token') returns null post-logout"),
        ("Logout Token Purge In Mobile", "Verify mobile logout clears stored token from SharedPreferences", "High", "ApiService._token is set to null post-logout"),
        ("Session Storage XSS Isolation", "Verify no third-party scripts have access to localStorage tokens", "Medium", "Clean dependency tree prevents script injection")
    ]
    for idx, (n, d, p, e) in enumerate(c3, 61):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Session Security & Token Handling", "name": n, "description": d, "priority": p, "expected_result": e})

    # 4. Input Validation & Parameter Tampering (SEC-086 to SEC-115) - 30
    c4 = [
        ("Negative Budget Rejection", "Submit trip planning request with budget: -5000", "High", "HTTP 400 or rejected by validation logic"),
        ("Zero Budget Rejection", "Submit trip planning request with budget: 0", "Medium", "HTTP 400 or validation requires budget > 0"),
        ("Negative Travelers Count Rejection", "Submit trip planning request with travelersCount: -2", "High", "HTTP 400 or rejected by validation logic"),
        ("Zero Travelers Count Rejection", "Submit trip planning request with travelersCount: 0", "Medium", "HTTP 400 or rejected by validation logic"),
        ("Excessive Travelers Count Rejection", "Submit trip planning request with travelersCount: 100000", "Medium", "Validation limits travelers to reasonable range"),
        ("Invalid Date Format In Trip", "Submit startDate: 'invalid-date-string'", "High", "HTTP 400 or rejected, no unhandled 500 error"),
        ("End Date Before Start Date Rejection", "Submit startDate: '2026-05-25' and endDate: '2026-05-20'", "High", "Validation rejects inverted travel dates"),
        ("Historic Travel Dates Handling", "Submit trip dates set 10 years in the past", "Low", "System handles past dates gracefully"),
        ("Negative Expense Amount Rejection", "Submit POST /api/expenses with amount: -1500", "High", "HTTP 400 or rejected by validation logic"),
        ("Non-Numeric Expense Amount Rejection", "Submit POST /api/expenses with amount: 'one thousand'", "Medium", "HTTP 400 Bad Request, amount must be numeric"),
        ("Invalid Expense Category Rejection", "Submit expense with category: 'invalid_category_xyz'", "Medium", "Category validated against permitted enumeration"),
        ("Invalid MongoDB ObjectId Format Handling", "Submit GET /api/trips/not_a_valid_object_id", "Critical", "HTTP 400 or 404, server handles invalid cast without 500 crash"),
        ("Null Byte In String Parameters", "Submit title containing null byte 'Trip%00Title'", "High", "Null byte stripped or rejected cleanly"),
        ("Oversized String Input In Trip Title", "Submit trip title with 10,000 characters", "Medium", "String truncated or rejected without buffer overflow"),
        ("Oversized String Input In User Name", "Submit user name with 5,000 characters", "Medium", "String validated and truncated safely"),
        ("Unicode Homoglyph Handling", "Submit email containing Unicode Cyrillic homoglyphs", "Low", "Homoglyphs handled safely without spoofing"),
        ("Control Characters In Input Fields", "Submit inputs containing ASCII control characters (0x01 - 0x1F)", "Low", "Control characters stripped or escaped"),
        ("Malformed JSON Body Rejection", "Send malformed JSON syntax { 'name': invalid }", "High", "HTTP 400 Bad Request emitted by express.json()"),
        ("Empty Body On POST Endpoints", "Send empty POST request body to /api/trips", "High", "HTTP 400 Bad Request, required fields missing"),
        ("Unexpected Array Where Object Expected", "Send JSON array `[]` where JSON object `{}` expected", "Medium", "HTTP 400 Bad Request, invalid payload shape"),
        ("Unexpected Number Where String Expected", "Send { email: 12345 } to login endpoint", "Medium", "Type coercion handled safely without crash"),
        ("Unexpected Boolean Where String Expected", "Send { name: true } to signup endpoint", "Medium", "Type coercion handled safely without crash"),
        ("Destination Search Special Regex Chars", "Submit search query with regex special chars '.*+?^${}()|[]\\'", "Critical", "Regex chars escaped safely, no ReDoS or unhandled crash"),
        ("Search String Truncation Limit", "Submit search query with 5,000 characters", "Low", "Query length bounded to prevent CPU exhaustion"),
        ("Trip Status Permitted Values Only", "Submit PUT /api/trips/:id/status with { status: 'hacked' }", "High", "Status validated against enum (upcoming, active, completed, cancelled)"),
        ("Booking Hotel Option Permitted Values", "Submit booking with invalid room type", "Medium", "Room type validated against available options"),
        ("Integer Overflow In Budget Field", "Submit budget: 99999999999999999999999999", "Medium", "Handled safely without numeric overflow corruption"),
        ("Scientific Notation In Numeric Fields", "Submit amount: '1e10' in expense amount", "Low", "Numeric validation handles scientific notation safely"),
        ("Empty String In Required Fields", "Submit name: '   ' with whitespace only to signup", "High", "Whitespace trimmed and rejected as empty"),
        ("Content-Type Application JSON Enforced", "Verify POST endpoints require Content-Type: application/json", "Medium", "Mismatched content-types handled cleanly")
    ]
    for idx, (n, d, p, e) in enumerate(c4, 86):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Input Validation & Parameter Tampering", "name": n, "description": d, "priority": p, "expected_result": e})

    # 5. XSS Defensive Checks & Encodings (SEC-116 to SEC-140) - 25
    c5 = [
        ("Reflected XSS In Destination Search", "Query GET /api/destinations?search=<script>alert('xss')</script>", "Critical", "Script tag is sanitized or HTML entity encoded in response"),
        ("Reflected XSS Event Handler Injection", "Query GET /api/destinations?search=<img src=x onerror=alert(1)>", "Critical", "Image onerror payload sanitized or encoded"),
        ("Reflected XSS JavaScript Pseudo-Protocol", "Query GET /api/destinations?search=javascript:alert(1)", "High", "Javascript URI sanitized"),
        ("Stored XSS In Trip Title", "Create trip with title `<script>alert('stored_xss')</script>`", "Critical", "Script tag is escaped when rendered in frontend UI"),
        ("Stored XSS In Trip Description", "Create trip with description containing `<svg onload=alert(1)>`", "Critical", "SVG payload escaped safely on dashboard"),
        ("Stored XSS In User Full Name", "Update user name to `<b onmouseover=alert(1)>Hacker</b>`", "Critical", "Onmouseover handler neutralized by React JSX escaping"),
        ("Stored XSS In Expense Title", "Create expense with title `<iframe src=javascript:alert(1)></iframe>`", "Critical", "Iframe payload escaped in expense table"),
        ("Stored XSS In Booking Details", "Create booking with details containing malicious script tags", "Critical", "Script tags escaped in bookings list"),
        ("React JSX Built-in Escaping Verification", "Verify React 19 automatically escapes interpolated string variables", "High", "React virtual DOM escapes HTML entities by default"),
        ("Dangerous React dangerouslySetInnerHTML Audit", "Audit React frontend codebase for any usage of dangerouslySetInnerHTML", "Critical", "Zero instances of unescaped dangerouslySetInnerHTML in frontend"),
        ("Content-Security-Policy Header Check", "Verify server or web host returns Content-Security-Policy header", "High", "CSP header restricts unauthorized script execution"),
        ("X-XSS-Protection Header Check", "Verify server returns X-XSS-Protection header", "Medium", "X-XSS-Protection header is present or managed via modern CSP"),
        ("HTML Entity Encoding Verification", "Verify `<` becomes `&lt;` and `>` becomes `&gt;` when output in HTML", "High", "HTML entities encoded accurately"),
        ("DOM-based XSS In Leaflet Map Popups", "Verify activity titles in Leaflet map markers cannot execute injected script", "High", "Map popup text rendered via textNode or sanitized HTML"),
        ("DOM-based XSS In Hash Routing", "Inject script payload into window.location.hash '#<script>alert(1)</script>'", "High", "Hash routing logic treats hash as plain text token"),
        ("CSS Injection In Style Attributes", "Attempt injecting CSS expression `background: url(javascript:alert(1))`", "Medium", "Inline styles use safe React style objects"),
        ("Markdown Injection Defense", "If markdown rendering is used, verify raw HTML rendering is disabled", "Medium", "Markdown renders safely without raw script tags"),
        ("SVG Image Upload/Render Sanitization", "Verify destination images or avatars do not execute embedded SVG scripts", "Medium", "External image URLs validated and rendered in <img> tags"),
        ("XSS In Chart.js Tooltips", "Inject script tags into expense category names rendered in Chart.js tooltips", "Medium", "Chart.js canvas escapes tooltip text strings"),
        ("JSON Injection In API Responses", "Verify user input cannot escape JSON string delimiters in API responses", "High", "Express res.json() serializes strings with proper JSON escaping"),
        ("HTTP Header Injection / CRLF Injection", "Inject CRLF `\r\nSet-Cookie: evil=true` into input fields", "High", "Express/Node.js HTTP parser neutralizes CRLF injection in headers"),
        ("Template Injection (SSTI) Defense", "Send `{{ 7 * 7 }}` in user name to test server-side template injection", "Medium", "String treated literally, not evaluated"),
        ("Client-side Template Injection (Angular/Vue)", "Verify frontend does not evaluate expressions dynamically", "Low", "Static JSX templates prevent dynamic expression evaluation"),
        ("External Link Rel Attribute (rel=noopener)", "Verify external links in frontend specify rel='noopener noreferrer'", "Medium", "External links protect against window.opener hijacking"),
        ("JSON-LD / Meta Tags XSS Defense", "Verify meta tags in index.html do not interpolate unescaped parameters", "Low", "Static meta tags configured safely")
    ]
    for idx, (n, d, p, e) in enumerate(c5, 116):
        cases.append({"id": f"SEC-{idx:03d}", "category": "XSS Defensive Checks & Encodings", "name": n, "description": d, "priority": p, "expected_result": e})

    # 6. NoSQL & SQL Injection Defensive Checks (SEC-141 to SEC-170) - 30
    c6 = [
        ("NoSQL Injection In Login Email", "Submit { email: { $gt: '' }, password: 'password' } to /api/auth/login", "Critical", "HTTP 400 or string cast prevents operator injection"),
        ("NoSQL Injection In Login Password", "Submit { email: 'john@example.com', password: { $ne: '' } } to login", "Critical", "HTTP 400 or string cast prevents password bypass"),
        ("String Casting In Auth Controller", "Verify email and password inputs are explicitly cast to String() in authController", "Critical", "authController enforces String(req.body.email) casting"),
        ("NoSQL Injection In User Signup", "Submit { email: { $regex: '.*' } } to signup endpoint", "Critical", "Input sanitized and stringified"),
        ("NoSQL Where Clause Injection", "Submit `$where: 'this.password.length > 0'` in query payload", "Critical", "Mongoose schema disallows $where injection"),
        ("NoSQL Regex DoS (ReDoS) In Auth", "Submit catastrophic backtracking regex pattern in email field", "High", "String regex escaping neutralizes ReDoS pattern"),
        ("Regex Escaping In User Lookup", "Verify email search uses regex escape helper `email.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')`", "Critical", "Regex escape helper applied in User.findOne()"),
        ("NoSQL Injection In Trip Status Update", "Submit { status: { $ne: null } } to PUT /api/trips/:id/status", "High", "Mongoose schema validates status string enumeration"),
        ("NoSQL Operator Injection In Trip Query", "Submit GET /api/trips?userId[$ne]=1", "High", "User ID extracted strictly from authenticated req.user.id"),
        ("NoSQL Injection In Booking Creation", "Submit { tripId: { $gt: '' } } to POST /api/bookings", "High", "ObjectId validation or string cast prevents operator injection"),
        ("NoSQL Injection In Expense Creation", "Submit { tripId: { $gt: '' }, amount: 500 } to POST /api/expenses", "High", "TripId validated as valid string/ObjectId"),
        ("SQL Injection Classic OR '1'='1' Check", "Submit `' OR '1'='1` in email, password, and search fields", "High", "Payload treated as literal string without syntax execution"),
        ("SQL Injection UNION SELECT Probe", "Submit `' UNION SELECT null, username, password FROM users--` in search", "High", "Payload treated as literal text string"),
        ("SQL Injection Comment Delimiter Probe", "Submit `admin'--` in username/email field", "High", "Payload treated as literal text without comment truncation"),
        ("SQL Injection Stacked Queries Check", "Submit `'; DROP TABLE users;--` in destination search query", "High", "Payload treated as literal string"),
        ("Mongoose Schema Type Enforcement", "Verify Mongoose schemas define strict types (String, Number, Date, ObjectId)", "High", "Mongoose schema enforces strict casting rules"),
        ("Mongoose Strict Query Mode", "Verify Mongoose strictQuery is enabled to discard unknown query parameters", "Medium", "Mongoose discards undefined schema fields"),
        ("Mock DB Injection Safety", "Verify in-memory mock DB operations use strict string comparison (===)", "High", "Mock DB uses String(u.email).trim().toLowerCase() === email"),
        ("NoSQL Operator Injection In Query String", "Submit query string `?search[$gt]=` to /api/destinations", "High", "Search parameter coerced to String or rejected"),
        ("Prototype Pollution In Body Parser", "Submit `{ '__proto__': { 'polluted': true } }` in POST body", "High", "Object prototype remains unpolluted"),
        ("Constructor Prototype Pollution", "Submit `{ 'constructor': { 'prototype': { 'isAdmin': true } } }`", "High", "Object prototype remains unpolluted"),
        ("MongoDB BSON Parser DoS", "Send deeply nested BSON document to test parser stack exhaustion", "Medium", "Body size parser limits prevent stack exhaustion"),
        ("Database Error Message Redaction", "Verify MongoDB error codes (e.g. E11000 duplicate key) do not leak raw query", "High", "Server returns clean error message without raw database query"),
        ("Database Credentials Exposure In Error", "Verify connection failure logs mask database credentials", "Critical", "mongoURI logs mask password via split('@').pop()"),
        ("MongoDB Sanitize Middleware Audit", "Check if express-mongo-sanitize or manual string coercion is applied", "Medium", "Manual String coercion and regex escaping applied across controllers"),
        ("Blind NoSQL Injection Timing Probe", "Attempt sleep-based blind NoSQL injection payload", "High", "Timing remains unaffected by injection payload"),
        ("Second-Order SQL/NoSQL Injection Check", "Verify saved input retrieved from DB is not passed to dynamic evaluators", "High", "Zero eval() or Function() usage with database data"),
        ("JSON Schema Validation Verification", "Verify request validation precedes database query execution", "Medium", "Validation guards executed before query dispatch"),
        ("Query Selector Injection In Delete Trip", "Attempt delete with selector query to delete multiple trips", "High", "Delete operates on single document matching req.user.id"),
        ("Static Code Audit For Unsanitized Mongo Queries", "Scan codebase for direct unsanitized `req.body` passed to Mongoose find", "High", "All queries pass through defined controllers with validation")
    ]
    for idx, (n, d, p, e) in enumerate(c6, 141):
        cases.append({"id": f"SEC-{idx:03d}", "category": "NoSQL & SQL Injection Defensive Checks", "name": n, "description": d, "priority": p, "expected_result": e})

    # 7. Path Traversal & File Inclusion Checks (SEC-171 to SEC-195) - 25
    c7 = [
        ("Dot-Dot-Slash Path Traversal Probe", "Submit GET /api/destinations/../../etc/passwd", "Critical", "HTTP 404 or rejected, path traversal blocked"),
        ("Encoded Dot-Dot-Slash Traversal", "Submit GET /api/destinations/%2e%2e%2f%2e%2e%2fetc/passwd", "Critical", "URL encoded traversal characters rejected or normalized"),
        ("Double Encoded Traversal Probe", "Submit GET /api/destinations/%252e%252e%252fetc/passwd", "Critical", "Double encoded traversal blocked"),
        ("Windows Backslash Path Traversal", "Submit GET /api/destinations/..\\..\\windows\\win.ini", "Critical", "Windows directory traversal blocked"),
        ("Static Asset Directory Boundary Check", "Attempt to traverse outside frontend/dist directory via static asset URL", "Critical", "Vite/Express static server confines requests strictly to dist/"),
        ("Backend Source Code File Disclosure", "Attempt GET /src/index.js or GET /backend/src/index.js via web server", "Critical", "HTTP 404, raw backend JavaScript files are not served"),
        ("Environment File Disclosure Check", "Attempt GET /.env or GET /backend/.env via HTTP requests", "Critical", "HTTP 404, environment files are never served over HTTP"),
        ("Git Repository Metadata Disclosure", "Attempt GET /.git/config or GET /.git/HEAD via HTTP", "Critical", "HTTP 404, .git directory is not accessible via web server"),
        ("Package Manifest Disclosure", "Attempt GET /package.json or GET /backend/package.json", "High", "Package manifest files not publicly exposed over HTTP"),
        ("Docker Configuration Disclosure", "Attempt GET /Dockerfile or GET /docker-compose.yml", "High", "Infrastructure files not publicly exposed"),
        ("Log File Disclosure Check", "Attempt GET /appium-server.log or GET /out.log via HTTP", "High", "Log files not accessible via web endpoints"),
        ("Absolute File Path Traversal", "Submit GET /etc/shadow or GET /C:/Windows/win.ini", "Critical", "Absolute system paths rejected"),
        ("Null Byte Path Truncation Check", "Submit GET /api/destinations/goa.jpg%00.html", "High", "Null byte truncation neutralized by Node.js path handling"),
        ("Arbitrary File Read In Uploads", "If file upload exists, verify uploaded filename cannot contain ../", "High", "Filenames sanitized to base alphanumeric characters"),
        ("Local File Inclusion (LFI) In Dynamic Require", "Audit codebase for dynamic require(req.body.module)", "Critical", "Zero dynamic require calls with user input"),
        ("Remote File Inclusion (RFI) Check", "Attempt to include remote URL http://evil.com/shell.js in file paths", "Critical", "Remote file inclusion completely disallowed"),
        ("Symlink Traversal Check", "Verify static file server does not follow symlinks outside web root", "Medium", "Symlink resolution restricted to workspace"),
        ("Default Server Welcome File Disclosure", "Verify server does not expose internal directory directory listings", "Medium", "Directory indexing disabled"),
        ("Backup File Extensions Check", "Attempt GET /index.js.bak, /index.js.old, /index.js~", "Low", "Backup file extensions return 404"),
        ("Temporary Files Disclosure Check", "Attempt GET /#index.js#, /index.js.swp (Vim swap)", "Low", "Temporary editor files return 404"),
        ("Case Sensitivity Path Normalization", "Test case folding path traversal on Windows / Linux", "Low", "Paths resolved using path.resolve and validated"),
        ("Safe Path Resolution In Express", "Verify all express.static paths use path.join / path.resolve", "High", "express.static configured with safe path resolution"),
        ("Robots.txt Security Check", "Verify robots.txt does not reveal sensitive administrative paths", "Low", "Robots.txt contains standard crawl directives"),
        ("Source Map Disclosure Audit", "Check if production frontend bundle exposes full source maps", "Medium", "Production builds configure source maps securely"),
        ("Test Artifact Directory Web Isolation", "Verify reports/ and test_cases/ are not served as public web directories", "High", "Test folders isolated from public HTTP routes")
    ]
    for idx, (n, d, p, e) in enumerate(c7, 171):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Path Traversal & File Inclusion Checks", "name": n, "description": d, "priority": p, "expected_result": e})

    # 8. CORS & Origin Validation (SEC-196 to SEC-220) - 25
    c8 = [
        ("CORS Preflight OPTIONS Handling", "Send OPTIONS /api/auth/login with Origin: http://localhost:3000", "High", "HTTP 204 or 200 with appropriate CORS headers"),
        ("Access-Control-Allow-Origin Verification", "Verify response includes Access-Control-Allow-Origin header", "High", "Access-Control-Allow-Origin is set"),
        ("CORS Wildcard With Credentials Defense", "Verify server does NOT return both Origin: * and Allow-Credentials: true", "Critical", "Wildcard origin with credentials disallowed per CORS spec"),
        ("CORS Null Origin Defense", "Send request with Origin: null", "High", "Null origin rejected or treated without credentials"),
        ("CORS Evil Domain Origin Check", "Send request with Origin: http://attacker-controlled-website.com", "Medium", "CORS policy prevents unauthorized cross-origin reading"),
        ("CORS Subdomain Prefix Bypass Check", "Send request with Origin: http://localhost:3000.evil.com", "Medium", "Invalid origin pattern not matched"),
        ("Access-Control-Allow-Methods List", "Verify Access-Control-Allow-Methods lists only GET, POST, PUT, DELETE, OPTIONS", "Medium", "Allowed methods restricted to expected verbs"),
        ("Access-Control-Allow-Headers List", "Verify Access-Control-Allow-Headers includes Content-Type, Authorization", "High", "Headers allow standard JSON and Bearer tokens"),
        ("Access-Control-Max-Age Header Check", "Verify preflight caching header Access-Control-Max-Age is reasonable", "Low", "Preflight cache duration optimizes performance"),
        ("CORS Header Injection Check", "Attempt to inject newline into Origin header", "High", "CRLF in Origin rejected by HTTP parser"),
        ("Cross-Origin Resource Blocking (CORB)", "Verify JSON responses specify nosniff to enforce CORB", "Medium", "X-Content-Type-Options: nosniff header prevents cross-origin sniffing"),
        ("Cross-Origin Opener Policy (COOP)", "Check for Cross-Origin-Opener-Policy header on frontend", "Low", "COOP header isolates browsing context"),
        ("Cross-Origin Embedder Policy (COEP)", "Check for Cross-Origin-Embedder-Policy header", "Low", "COEP header protects against speculative execution attacks"),
        ("Cross-Origin Resource Policy (CORP)", "Verify Cross-Origin-Resource-Policy header", "Low", "CORP header specifies resource sharing scope"),
        ("Mobile App Origin Handling", "Verify API accepts requests from mobile client without Origin header", "High", "Native mobile requests succeed without browser Origin header"),
        ("Localhost Frontend Dev Origin Allowed", "Verify requests from http://localhost:3000 are permitted in development", "High", "Local dev frontend connects smoothly to backend"),
        ("127.0.0.1 IP Origin Allowed", "Verify requests from http://127.0.0.1:3000 are permitted in development", "High", "Loopback IP origin connects smoothly"),
        ("Vite Dev Server Proxy Check", "Verify Vite proxy configuration does not expose internal network ports", "Low", "Proxy rules confined to local backend port"),
        ("CORS Error Response Body Cleanliness", "Verify rejected CORS preflight does not leak server stack traces", "Medium", "Clean rejection response"),
        ("Access-Control-Expose-Headers Check", "Verify sensitive response headers are not exposed via Expose-Headers", "Low", "Only necessary headers exposed"),
        ("PostMessage Origin Validation In Frontend", "Verify any window.postMessage listeners validate event.origin", "Medium", "Zero insecure postMessage wildcard listeners"),
        ("WebSocket Origin Check If Applicable", "Verify WebSocket handshake validates Origin header if WS is used", "Low", "WebSocket connections validate origin"),
        ("Flash / Silverlight Policy File Check", "Verify crossdomain.xml is not present or disallows broad access", "Low", "Legacy policy files absent"),
        ("Client-Side XHR Credential Mode", "Verify frontend fetch calls configure credentials mode appropriately", "Low", "Fetch credentials mode configured correctly"),
        ("CORS Middleware Package Audit", "Verify cors npm package is up to date without known vulnerabilities", "High", "cors package >= 2.8.5")
    ]
    for idx, (n, d, p, e) in enumerate(c8, 196):
        cases.append({"id": f"SEC-{idx:03d}", "category": "CORS & Origin Validation", "name": n, "description": d, "priority": p, "expected_result": e})

    # 9. Security Headers & Transport Security (SEC-221 to SEC-245) - 25
    c9 = [
        ("X-Content-Type-Options Header Check", "Verify server returns 'X-Content-Type-Options: nosniff'", "High", "Header present to prevent MIME-sniffing attacks"),
        ("X-Frame-Options Header Check", "Verify server returns 'X-Frame-Options: DENY' or 'SAMEORIGIN'", "High", "Header present to prevent clickjacking attacks"),
        ("Strict-Transport-Security (HSTS) Check", "Verify Strict-Transport-Security header for HTTPS deployments", "High", "HSTS header specifies max-age >= 31536000"),
        ("X-XSS-Protection Header Check", "Verify 'X-XSS-Protection: 1; mode=block' or modern CSP replacement", "Medium", "Header configured appropriately"),
        ("Referrer-Policy Header Check", "Verify 'Referrer-Policy: strict-origin-when-cross-origin' or 'no-referrer'", "Medium", "Referrer policy prevents sensitive URL leakage"),
        ("Permissions-Policy Header Check", "Verify Permissions-Policy disables unused browser features (geolocation, camera, microphone)", "Low", "Permissions-Policy header is configured"),
        ("X-Powered-By Header Removal", "Verify 'X-Powered-By: Express' header is removed from HTTP responses", "High", "X-Powered-By header is omitted to prevent technology disclosure"),
        ("Server Header Disclosure Check", "Verify 'Server' header does not disclose exact software version numbers", "Low", "Server header is generic or omitted"),
        ("Content-Type Character Set Enforcement", "Verify Content-Type header specifies 'charset=utf-8'", "Medium", "Content-Type is 'application/json; charset=utf-8'"),
        ("Cache-Control Header On Authenticated Data", "Verify sensitive user responses return 'Cache-Control: no-store, no-cache'", "High", "Prevents caching of sensitive travel and profile data"),
        ("Pragma No-Cache Backward Compatibility", "Verify Pragma: no-cache is returned for legacy HTTP/1.0 clients", "Low", "Pragma header present on sensitive routes"),
        ("Expires Header In Past", "Verify Expires: 0 or past timestamp on authenticated endpoints", "Low", "Expires header prevents browser cache retrieval"),
        ("Clear-Site-Data Header On Logout", "Check if Clear-Site-Data header is returned upon logout", "Low", "Browser cache and storage cleared if supported"),
        ("Clickjacking Defense In Frontend HTML", "Verify frontend cannot be rendered in malicious third-party iframes", "High", "X-Frame-Options or CSP frame-ancestors prevents clickjacking"),
        ("HTTPS Redirection In Production", "Verify HTTP requests redirect to HTTPS in production environment", "High", "HTTP 301/308 redirect enforces HTTPS"),
        ("TLS Protocol Version Enforcement", "Verify TLS 1.0 and 1.1 are disabled in production; require TLS 1.2 or 1.3", "Critical", "Only modern secure TLS cipher suites accepted"),
        ("Secure Cipher Suite Configuration", "Verify legacy weak ciphers (RC4, DES, 3DES, MD5) are disabled", "High", "Modern forward-secret ciphers enforced (ECDHE)"),
        ("Certificate Expiration Monitoring", "Verify TLS certificates are valid and not expired", "Critical", "Valid certificate chain in place"),
        ("Subresource Integrity (SRI) Check", "Verify CDN script tags in index.html include integrity hashes", "Medium", "Integrity attributes present on third-party scripts"),
        ("Content-Security-Policy Script-Src Directive", "Verify script-src restricts execution to self and trusted domains", "High", "Inline scripts disallowed or hashed in production CSP"),
        ("Content-Security-Policy Style-Src Directive", "Verify style-src directive is defined", "Low", "Style sources restricted"),
        ("Content-Security-Policy Object-Src Directive", "Verify object-src is set to 'none' to block Flash/plugins", "Medium", "object-src 'none' configured"),
        ("Content-Security-Policy Base-URI Directive", "Verify base-uri is set to 'self' to prevent <base> tag hijacking", "Low", "base-uri 'self' configured"),
        ("Content-Security-Policy Upgrade-Insecure-Requests", "Verify upgrade-insecure-requests directive is enabled on HTTPS", "Low", "Insecure HTTP requests automatically upgraded"),
        ("Helmet.js Integration Audit", "Audit backend Express app for helmet middleware integration", "High", "Security headers managed via Helmet or Express middleware")
    ]
    for idx, (n, d, p, e) in enumerate(c9, 221):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Security Headers & Transport Security", "name": n, "description": d, "priority": p, "expected_result": e})

    # 10. Cookie & Sensitive Data Exposure (SEC-246 to SEC-265) - 20
    c10 = [
        ("Password Hash Exclusion In User Models", "Verify UserSchema.select('-password') excludes password hash", "Critical", "Password hash never sent in user JSON responses"),
        ("Sensitive Keys In Logging Redaction", "Verify server logs do not log passwords or tokens in plain text", "Critical", "Password values masked or excluded from logger output"),
        ("Error Stack Trace Leakage In Production", "Verify 500 error responses do not return full V8 error stack traces", "High", "Generic error message returned without stack trace"),
        ("Database Connection String Redaction In Logs", "Verify MongoDB credentials in connection string are redacted", "Critical", "Password portion of URI masked in console logs"),
        ("Razorpay Payment Secret Redaction", "Verify RAZORPAY_KEY_SECRET is not printed to workflow logs or console", "Critical", "Payment secret kept strictly confidential"),
        ("JWT Secret Redaction In Environment Dumps", "Verify debug routes do not dump process.env containing JWT_SECRET", "Critical", "Zero environment dump endpoints exist in production"),
        ("Personal Identifiable Information (PII) Minimization", "Verify user email and phone are only shared with authorized owner", "High", "User data isolated per account"),
        ("Credit Card / Payment Data Non-Storage", "Verify application does not store raw credit card numbers or CVV codes", "Critical", "Zero credit card or CVV fields in database schemas"),
        ("Sensitive Data In Git History Audit", "Scan git commit history for accidentally committed API keys or tokens", "Critical", "Zero hardcoded secrets found in git commits"),
        (".gitignore Coverage For Sensitive Files", "Verify .gitignore includes .env, *.log, build/, node_modules/", "Critical", "Sensitive local files excluded from version control"),
        ("Cookie Prefix __Host- Check", "If cookies used, check for secure __Host- or __Secure- prefixes", "Low", "Cookie prefix hardening applied where applicable"),
        ("Local Storage PII Inspection", "Verify browser localStorage contains only necessary auth tokens and user data", "Medium", "No extraneous sensitive data stored client-side"),
        ("URL Query Parameter PII Inspection", "Verify user email or phone is never placed in GET query parameters", "High", "PII excluded from browser history and server access logs"),
        ("HTTP Referrer Header PII Leakage", "Verify sensitive tokens are not leaked via Referer header to external CDNs", "Medium", "Referrer-Policy prevents token leakage"),
        ("Browser Autocomplete On Sensitive Inputs", "Verify password input specifies autocomplete='current-password'", "Low", "Autocomplete attributes conform to security standards"),
        ("Password Masking On Screen", "Verify mobile and web applications mask password input visually", "High", "Input obscured by default with toggle option"),
        ("Clipboard Clearing In Mobile App", "Verify sensitive data copied to clipboard is cleared or transient", "Low", "Clipboard handling minimizes data exposure"),
        ("Android Screen Capture / Task Snapshot Guard", "Verify whether FLAG_SECURE is evaluated for payment screens", "Low", "Security posture evaluated for mobile payment views"),
        ("Memory Dump Residual Credentials Check", "Verify credentials are not held in long-lived static global variables", "Medium", "Garbage collection reclaims transient auth variables"),
        ("API Response Envelope Sensitive Data Audit", "Inspect all 13 API endpoints for accidental field leaks", "High", "All responses conform strictly to defined DTO schemas")
    ]
    for idx, (n, d, p, e) in enumerate(c10, 246):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Cookie & Sensitive Data Exposure", "name": n, "description": d, "priority": p, "expected_result": e})

    # 11. Dependency Vulnerabilities & CVE Auditing (SEC-266 to SEC-285) - 20
    c11 = [
        ("Backend npm audit Vulnerability Scan", "Execute npm audit on backend dependencies to detect known CVEs", "Critical", "Zero Critical or High exploitable vulnerabilities"),
        ("Frontend npm audit Vulnerability Scan", "Execute npm audit on frontend dependencies", "Critical", "Zero Critical or High exploitable vulnerabilities"),
        ("Express Framework CVE Audit", "Verify Express framework version is updated past known vulnerability releases", "High", "Express >= 5.x or >= 4.21.x patched against known CVEs"),
        ("Mongoose ODM CVE Audit", "Verify Mongoose is updated past known prototype pollution vulnerabilities", "High", "Mongoose >= 8.x or >= 9.x"),
        ("Bcryptjs Package CVE Audit", "Verify bcryptjs package has no active advisories", "High", "bcryptjs >= 2.4.3 or modern alternative"),
        ("JSONWebToken Package CVE Audit", "Verify jsonwebtoken package is patched against algorithm confusion CVEs", "Critical", "jsonwebtoken >= 9.0.0"),
        ("Cors Package CVE Audit", "Verify cors package has no active security advisories", "Medium", "cors package >= 2.8.5"),
        ("Dotenv Package CVE Audit", "Verify dotenv package has no active security advisories", "Low", "dotenv package >= 16.x"),
        ("React & React-DOM CVE Audit", "Verify React is on latest stable release without known XSS vulnerabilities", "Critical", "React 19.x patched against all public advisories"),
        ("Vite Build Tooling CVE Audit", "Verify Vite build tool is patched against dev server traversal CVEs", "High", "Vite >= 6.x or >= 8.x"),
        ("Chart.js Package CVE Audit", "Verify Chart.js has no active prototype pollution advisories", "Medium", "Chart.js >= 4.4.x"),
        ("Flutter SDK Dependencies Audit", "Verify pubspec.yaml dependencies (http, provider, fl_chart, flutter_map)", "High", "Zero vulnerable Dart packages"),
        ("Http Package CVE Audit (Dart)", "Verify http package is updated past known certificate validation bugs", "High", "http >= 1.2.0"),
        ("Flutter Map Dependency Audit", "Verify flutter_map package does not contain tile injection flaws", "Medium", "flutter_map >= 6.1.0"),
        ("Python Test Dependencies pip-audit", "Execute pip-audit against Python test environment dependencies", "High", "Zero known CVEs in Python test tools"),
        ("Pytest Package CVE Audit", "Verify pytest and test plugins have no active advisories", "Medium", "pytest >= 8.x"),
        ("Selenium WebDriver CVE Audit", "Verify selenium package has no active driver execution flaws", "High", "selenium >= 4.25.x"),
        ("Appium Python Client CVE Audit", "Verify Appium-Python-Client is on modern 3.x/4.x release", "Medium", "Appium-Python-Client >= 3.x"),
        ("Trivy Vulnerability Scanner Filesystem Scan", "Run Trivy fs scanner across complete repository codebase", "High", "Trivy reports zero critical exploitable CVEs"),
        ("Dependabot / Dependency Automation Review", "Verify dependency update configuration is present in repository", "Low", "Dependency update strategy documented")
    ]
    for idx, (n, d, p, e) in enumerate(c11, 266):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Dependency Vulnerabilities & CVE Auditing", "name": n, "description": d, "priority": p, "expected_result": e})

    # 12. Secrets Detection & Static Analysis (SEC-286 to SEC-300) - 15
    c12 = [
        ("Gitleaks / Semgrep Secrets Scan", "Scan entire repository for exposed API keys, private keys, or passwords", "Critical", "Zero hardcoded credentials or private keys detected"),
        ("AWS / Cloud Provider Key Scan", "Scan for AKIA... AWS access keys or cloud provider secrets", "Critical", "Zero cloud credentials found"),
        ("Private Key File Audit", "Scan repository for *.pem, *.key, id_rsa, id_ed25519 private key files", "Critical", "Zero private key files committed"),
        ("Hardcoded Database Password Check", "Scan backend source files for hardcoded database passwords", "Critical", "Zero hardcoded database credentials in committed code"),
        ("Hardcoded JWT Secret Check", "Verify fallback JWT_SECRET in source code is not used in production", "Critical", "Production mandates environment variable JWT_SECRET"),
        ("Razorpay Live Key Detection", "Scan repository to ensure no live rzp_live_ keys are committed", "Critical", "Zero production payment keys present"),
        ("Android Keystore Secrets Check", "Verify Android release signing keystore is not committed in repository", "High", "Release keystore excluded from repository"),
        (".env.example Sanitization Check", "Verify .env.example contains only dummy placeholder values", "Critical", ".env.example contains zero real credentials"),
        ("Static Analysis Semgrep Rules Run", "Run Semgrep security rules across JavaScript and Python files", "High", "Semgrep reports zero high-severity findings"),
        ("Bandit Python AST Security Scanner", "Run Bandit static analysis across scripts/ and tests/ Python code", "High", "Bandit reports zero high-severity vulnerabilities"),
        ("Oxlint / ESLint Security Rules Run", "Run linter across frontend React codebase to detect insecure patterns", "Medium", "Zero linter security warnings"),
        ("Dart Analyze Security Checks", "Run flutter analyze to verify code safety and quality in mobile/", "High", "No security or analysis errors reported"),
        ("GitHub Actions Workflow Insecure Commands", "Verify workflow YAMLs do not use insecure commands or eval with user input", "High", "Workflow steps use secure static commands"),
        ("GitHub Actions Secrets Printing Guard", "Verify workflows never echo or log secret values to console", "Critical", "Zero secrets echoed to GITHUB_STEP_SUMMARY or runner logs"),
        ("Security Audit Summary Report Generation", "Compile comprehensive JSON, HTML, and SARIF security audit reports", "Critical", "300 security checks catalogued with detailed audit status")
    ]
    for idx, (n, d, p, e) in enumerate(c12, 286):
        cases.append({"id": f"SEC-{idx:03d}", "category": "Secrets Detection & Static Analysis", "name": n, "description": d, "priority": p, "expected_result": e})

    return cases

# ----------------- MAIN GENERATOR -----------------
def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. Selenium
    import generate_all_test_cases
    sel_cases = generate_all_test_cases.generate_selenium_cases()
    assert len(sel_cases) == 300, f"Selenium count mismatch: {len(sel_cases)}"
    sel_path = os.path.join(root, "tests", "selenium", "test_cases", "test_cases.yml")
    os.makedirs(os.path.dirname(sel_path), exist_ok=True)
    with open(sel_path, "w", encoding="utf-8") as f:
        f.write(format_yaml(sel_cases))
    print(f"Generated {len(sel_cases)} Selenium test cases at {sel_path}")
    
    # 2. Appium
    app_cases = get_appium_cases()
    assert len(app_cases) == 300, f"Appium count mismatch: {len(app_cases)}"
    app_path = os.path.join(root, "tests", "appium", "test_cases", "test_cases.yml")
    os.makedirs(os.path.dirname(app_path), exist_ok=True)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(format_yaml(app_cases))
    print(f"Generated {len(app_cases)} Appium test cases at {app_path}")
    
    # 3. Load
    load_cases = get_load_cases()
    assert len(load_cases) == 300, f"Load count mismatch: {len(load_cases)}"
    load_path = os.path.join(root, "tests", "load", "test_cases", "test_cases.yml")
    os.makedirs(os.path.dirname(load_path), exist_ok=True)
    with open(load_path, "w", encoding="utf-8") as f:
        f.write(format_yaml(load_cases))
    print(f"Generated {len(load_cases)} Load test cases at {load_path}")
    
    # 4. Security
    sec_cases = get_security_cases()
    assert len(sec_cases) == 300, f"Security count mismatch: {len(sec_cases)}"
    sec_path = os.path.join(root, "tests", "security", "test_cases", "test_cases.yml")
    os.makedirs(os.path.dirname(sec_path), exist_ok=True)
    with open(sec_path, "w", encoding="utf-8") as f:
        f.write(format_yaml(sec_cases))
    print(f"Generated {len(sec_cases)} Security test cases at {sec_path}")
    
    print("\nSUCCESS: All 1,200 test case definitions generated successfully!")

if __name__ == "__main__":
    main()
