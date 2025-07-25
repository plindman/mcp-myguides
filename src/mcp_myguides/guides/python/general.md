# General Guidelines for Python Development

## Summary
These guidelines provide a comprehensive framework for Python development, covering best practices in documentation, efficient environment and dependency management with `uv`, preferred libraries for various tasks, robust security practices including secrets management and static analysis, adherence to source code standards (style, type hints, docstrings), and a strong emphasis on test-first development, including unit, integration, and end-to-end testing. They also outline scenarios where deviations are acceptable and critical 'red lines' that must never be crossed.

## When to Deviate from Guidelines

These guidelines optimize for most scenarios but aren't absolute rules:

**Acceptable Deviations:**
- **Performance-critical code**: Skip type checking if it impacts hot paths
- **Prototype/spike work**: Defer testing and documentation until direction is clear
- **Legacy integration**: Use required libraries even if not on preferred list
- **External constraints**: Client/platform requirements override preferences
- **Emergency fixes**: Skip full review process for critical production issues

**Deviation Process:**
1. Document reason in commit message or PR description
2. Create follow-up issue for compliance if applicable
3. Update guidelines if pattern emerges repeatedly

**Red Lines (Never Deviate):**
- Security practices (bandit, secret management)
- Version control hygiene (no direct main commits)
- Dependency management through uv
