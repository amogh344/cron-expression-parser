# cron-expression-parser

A command-line cron expression parser that expands time fields into their individual values.

## Overview

A small Python CLI tool that parses standard 5-field cron expressions and outputs a formatted table showing the exact minutes, hours, days, and months the command would run.

## Usage

Run the script by passing the cron expression and command as a single argument:

```bash
python3 main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

Output:

```text
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Supported Syntax

| Symbol / Syntax | Description | Example |
| --- | --- | --- |
| `*` | Every allowed value in the field range | `*` |
| `N` | Explicit single value | `5` |
| `A-B` | Inclusive range of values | `1-5` |
| `*/S` | Step interval across range | `*/15` |
| `A-B/S` | Step interval within range | `1-10/2` |
| `x,y,...` | List of values or ranges | `1,5,10` |

## Field Ranges

- **minute**: 0 - 59
- **hour**: 0 - 23
- **day of month**: 1 - 31
- **month**: 1 - 12
- **day of week**: 0 - 6 (0 = Sunday)

