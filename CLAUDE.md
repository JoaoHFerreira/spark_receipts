# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PySpark-based data analysis project (`spark-collection`) that analyzes CSV data, specifically focused on passenger survival analysis. The project demonstrates data transformations, aggregations, and analytics using Apache Spark.

## Architecture

- **Single-file architecture**: Main logic is contained in `main.py`
- **PySpark framework**: Uses PySpark SQL for data processing and analysis
- **Data pipeline approach**: Reads CSV → Transforms data → Aggregates → Displays results

## Key Dependencies

- `pyspark>=4.0.0`: Core Spark framework for distributed data processing
- `black>=25.1.0`: Code formatting
- `kagglehub>=0.3.13`: For accessing datasets

## Development Commands

### Environment Setup
```bash
# Install dependencies (uses uv for package management based on pyproject.toml)
uv sync
```

### Running the Application
```bash
# Run main analysis script
python main.py
```

### Code Formatting
```bash
# Format code with Black
black main.py
```

## Code Architecture Notes

- **SparkSession configuration**: Uses explicit localhost binding (`spark.driver.bindAddress`)
- **Data transformations**: Column renaming, age grouping, filtering
- **Aggregation patterns**: Uses groupBy with multiple aggregation functions (avg, count, round)
- **Hardcoded CSV path**: Currently points to a specific local file path that may need updating

## Important Implementation Details

- The CSV file path in `main.py:11` is hardcoded and references a specific user directory
- Age grouping logic creates "Senior" (50+), "Adult" (18-49), and "Child" (<18) categories
- Survival analysis focuses on passengers with non-zero fare amounts
- Results are ordered by passenger class and survival rate