# AtmosIQ Changelog

## Version 1.1

### Engineering Improvements

- Added `.env.example`
- Added fail-fast API key validation
- Improved project onboarding
- Improved configuration management

Learned:
- Environment variables
- Fail-fast design
- Secrets management


## Task 2 – Dependency Management

### Added
- Added missing direct dependencies:
  - `pgeocode`
  - `timezonefinder`

### Changed
- Pinned all direct dependencies to exact versions in `requirements.txt`.
- Removed `pandas` because it is a transitive dependency and is not directly imported by the application.
- Verified the project installs successfully in a clean virtual environment using the updated `requirements.txt`.

### Why
- Ensures reproducible builds across different environments.
- Makes project setup more reliable for collaborators.
- Prevents "works on my machine" issues caused by dependency version differences.
- Improves the accuracy and maintainability of the project's dependency manifest.

### Software Engineering Concepts Learned
- Dependency Management
- Direct vs. Transitive Dependencies
- Exact Version Pinning
- Reproducible Builds
- Manifest Accuracy
- Clean Environment Verification

## Task 3 – Defensive Programming & API Validation

### Changed
- Added JSON parsing error handling to the AirNow API client.
- Distinguished API failures from valid responses with no nearby monitoring stations.
- Added validation for required AirNow response fields before data enters the application.
- Improved user-facing warning messages for different failure scenarios.
- Prevented crashes caused by malformed or incomplete API responses.

### Why
- Improves application reliability when consuming external APIs.
- Prevents invalid data from propagating through the application.
- Provides users with accurate and meaningful feedback during failures.
- Makes AtmosIQ more resilient and production-ready.

### Software Engineering Concepts Learned
- Defensive Programming
- Boundary Validation
- Exception Handling
- Error Handling
- Function Contracts
- Defense in Depth
- User Experience During Failures


## Task 4 – API Caching & Performance Optimization

### Changed
- Added application-level caching to the AirNow API client using `@st.cache_data`.
- Configured a cache Time-To-Live (TTL) of 30 minutes.
- Reduced unnecessary API requests for repeated ZIP code searches.
- Improved application performance and reduced reliance on external API calls.

### Why
- Improves response times for repeated requests.
- Reduces API usage and helps avoid rate limits.
- Increases application reliability during temporary API outages.
- Provides a scalable caching strategy while maintaining reasonably fresh air quality data.

### Software Engineering Concepts Learned
- Application-Level Caching
- Session State vs. Application Cache
- Time-To-Live (TTL)
- API Rate Limiting
- Performance Optimization
- Resilience Engineering


## Task 5 – Named Constants & DRY Principle

### Added
- Created `constants.py` as the single source of truth for AQI thresholds, labels, colors, and emojis.

### Changed
- Replaced hardcoded AQI values across:
  - `services/recommendation.py`
  - `services/chatbot.py`
  - `ui/charts.py`
- Updated chart ranges to derive boundaries from named constants.
- Fixed a small indentation issue in `services/chatbot.py`.

### Why
- Removes duplicated AQI domain values.
- Makes the code easier to read and maintain.
- Prevents future inconsistencies between chatbot logic, recommendations, and charts.
- Applies the DRY principle across the project.

### Software Engineering Concepts Learned
- Named Constants
- Magic Numbers
- DRY Principle
- Single Source of Truth
- Refactoring Without Behavior Changes

## Task 6 – Readability Improvement for NaN Handling

### Changed
- Replaced the unclear NaN self-comparison in `services/timezone_service.py`.
- Added `pd.isna()` to make missing coordinate detection more readable.

### Why
- Improves code clarity.
- Replaces clever logic with explicit intent.
- Makes the timezone lookup code easier to understand and maintain.

### Software Engineering Concepts Learned
- NaN Handling
- Clarity Over Cleverness
- Readability
- Maintainability

Task 7 – Structured Application Logging
Overview

Implemented structured logging across the application using Python's built-in logging module. Logging replaces ad hoc debugging with consistent, timestamped log messages that improve troubleshooting and observability while protecting sensitive information.

Key Improvements
Configured centralized logging in config.py
Added console and rotating file logging (logs/atmosiq.log)
Prevented duplicate log handlers
Added informative log messages throughout the application
Logged API request lifecycle and application events
Logged warnings for invalid or missing data
Logged errors for HTTP failures and unexpected exceptions
Excluded sensitive information such as API keys and user data from logs
Added logs/ to .gitignore
Benefits
Simplifies debugging during development
Creates an audit trail for application events
Improves production troubleshooting
Prevents sensitive credentials from appearing in log files
Supports future scalability and monitoring




Task 8 – Unit Testing with pytest
Overview

Added a comprehensive automated test suite using pytest to validate the application's core business logic and API error handling. Tests ensure the application behaves correctly under both normal and failure scenarios while allowing future refactoring with confidence.

Test Coverage
AQI Recommendation Logic
Verified every AQI category boundary
Tested all recommendation tiers
Validated label and color consistency
Confirmed correct return types
Data Formatting
Verified PM2.5 is prioritized when available
Tested fallback behavior for other pollutants
Validated handling of invalid readings
Tested empty and malformed datasets
Confirmed required data fields remain accessible
AirNow API
Successful API responses
Empty API responses
HTTP error handling
Connection failures
Timeout handling
Invalid JSON handling
Testing Infrastructure
Added requirements-dev.txt for development dependencies
Added tests/ package
Added conftest.py for test environment configuration
Used unittest.mock.patch to mock HTTP requests
Prevented real API calls during testing
Cleared Streamlit cache between tests for isolated execution