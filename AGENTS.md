# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
currency-cycle-finder

Checker:
spread-viability-checker

## Coordination Protocol
- **Primary Agent**: real-time-fx-triangular-arbitrage
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
