# Architecture

CleanFolder separates its workflow into four stages:

1. `OrganizerConfig` loads and validates sorting rules.
2. `MovePlanner` classifies files and reserves safe destinations.
3. `MoveExecutor` creates category directories and moves files.
4. `ConsoleReporter` presents the plan or completed operation.

The planner has no write side effects, making preview mode reliable and easy to test.
