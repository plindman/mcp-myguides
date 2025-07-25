# General Guidelines for Python Development

## Summary
[TODO]

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
