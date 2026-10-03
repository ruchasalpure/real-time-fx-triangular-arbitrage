# Duties and Responsibilities for Real-Time FX Triangular Arbitrage Agent

## Dual-Control Architecture
Maker:
currency-cycle-finder

Checker:
spread-viability-checker

## Operational Workflow
1. The Maker (currency-cycle-finder) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (spread-viability-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
