# Testing

**Philosophy: Test-First Development**
- **Primary verification**: Tests should be your main way to verify functionality, not manual app testing
- **Fast feedback loop**: Running tests should be faster than starting the app
- **Confidence in changes**: Comprehensive tests allow safe refactoring and feature additions
- **Documentation**: Tests serve as living documentation of expected behavior

* We use `pytest` for our test suite where applicable.
* Install pytest-related dependencies as needed (e.g pytest-cov)
* Tests should be fast, isolated, and deterministic. Use mocking where appropriate to isolate tests from external dependencies.
* Use conftest.py for shared fixtures and configuration
* Use pytest.ini for pytest configuration
* pytest-asyncio is used for testing async code
* pytest-mock is used for mocking
* pytest-cov is used for coverage reporting

**Test-Driven Development Workflow**
- Write failing test first: Define expected behavior
- Run test: Confirm it fails for the right reason
- Write minimal code: Make test pass
- Refactor: Improve code while keeping tests green
- Repeat: For each new feature or bug fix

**When Manual Testing is Acceptable**
- UI/UX validation (visual appearance, user experience)
- Integration with external systems during initial setup
- Performance testing with real-world data volumes
- Accessibility testing with screen readers
- Browser compatibility testing

**Never Manual Test These**
- Business logic validation
- API endpoint behavior
- Data validation and transformation
- Error handling and edge cases
- Configuration and environment handling

### Test Coverage Targets

* All new features and bug fixes **must** be accompanied by comprehensive tests.
* Aim for at least 90% test coverage where practical. Use pytest-cov to measure.

Coverage Goals by Module Type:
- **Core business logic:** 95-100% coverage (critical functionality)
- **API endpoints:** 90-95% coverage (user-facing behavior)
- **Data models/schemas:** 85-90% coverage (validation logic)
- **Utilities/helpers:** 80-85% coverage (reusable components)
- **Configuration/settings:** 70-80% coverage (environment handling)
- **UI/CLI interfaces:** 60-70% coverage (integration focused)

### Test Structure and Organization
```
tests/
├── conftest.py              # Shared fixtures and configuration
├── unit/                    # Fast, isolated unit tests
├── integration/             # Integration tests with external dependencies
├── e2e/                     # End-to-end tests
└── fixtures/                # Test data and fixtures
└── data/                     # sample_data.json, mock_responses.py etc...
```

**Key Principles:**
- One concern per test: Each test should verify one specific behavior
- Clear naming: Test name should describe what's being tested and expected outcome
- AAA pattern: Arrange (setup), Act (execute), Assert (verify)
- Explicit assertions: Assert specific values, not just truthiness
- Meaningful test data: Use realistic data that makes test intent clear

### 5.4 Testing specific components

**Testing FastAPI Applications**

For FastAPI applications, we use `TestClient` for robust and isolated testing. This allows you to simulate requests to your application without actually running a live server. https://fastapi.tiangolo.com/tutorial/testing/ for more info.

**Testing FastMCP Applications**

For FastMCP applications, we use `Client` for robust and isolated testing. This allows you to simulate requests to your application without actually running a live server. https://gofastmcp.com/patterns/testing for more info.

**Database State Management for Tests**

When testing endpoints that interact with the database, it's crucial to ensure a clean and consistent database state for each test. We achieve this using `pytest` fixtures to drop and recreate tables before each test run.

Use function-scoped fixtures for test data, session-scoped for expensive setup like database engines.