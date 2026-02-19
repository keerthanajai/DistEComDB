# DistEComDB  
A Distributed E-Commerce Database System using CockroachDB and FastAPI

## Overview

DistEComDB is a distributed SQL-based e-commerce database system built using CockroachDB and FastAPI. The system demonstrates horizontal scalability, automatic sharding, Raft-based replication, fault tolerance, and distributed query execution.

The project simulates large-scale product and review workloads using the Amazon SNAP dataset.

---

## Architecture

The system consists of:

- 🐘 CockroachDB multi-node cluster (range-based sharding + replication factor 3)
- FastAPI application gateway
- Docker Compose orchestration
- Locust for performance testing

Client → FastAPI → Distributed SQL → CockroachDB Cluster

---

## Tech Stack

- Python
- FastAPI
- CockroachDB (v24.x)
- Docker & Docker Compose
- Locust (Load Testing)

---

## Project Structure

