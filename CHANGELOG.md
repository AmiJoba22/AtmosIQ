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