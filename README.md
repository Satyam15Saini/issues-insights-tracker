# 📦 issues-insights-tracker
Issues Insights Tracker is a containerized microservices application that helps you track, process, and analyze issues in a structured way. It’s built using FastAPI for the REST API, Celery for handling background tasks, PostgreSQL for data storage, and Redis as the message broker.

# 🚩 The Problem

In many applications, we need to: Store and manage issues or tickets, e.g. bug reports, feature requests, complaints. Run heavy processing in the background (like analyzing issue patterns, sending notifications), without blocking user requests. Have a scalable system that can reliably handle many requests. But manually wiring up API, database, background workers and message queues is time-consuming, error-prone, and hard to maintain.

# ✅ The Solution

This project solves it by: Using FastAPI to provide a high-performance API for creating & viewing issues. Using Celery to process time-consuming tasks in the background (via Redis). Using PostgreSQL to persist issue data. Using Docker Compose to spin up the API, worker, database, and Redis all together in isolated containers.
