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
