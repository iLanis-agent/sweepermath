# Sweeper Math

Honest lawn-sweeper arithmetic. The hopper claims twenty-five cubic feet; Sweeper Math multiplies,
divides and tells you how tall the pile stands when the season ends.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The hopper truth** - leaf fall into cubic feet, cubic feet into hopper fills.
- **The lap truth** - lawn, sweep width and pace into honest minutes of laps.
- **The season truth** - fills per weekend over the season into the pile you'll be explaining.

## The boundary

Sweeper Math keeps leaf-volume, lap-time and season-pile arithmetic only. It gives no verdicts
about what any sweeper can pick up - lawn condition, wet leaves and machine limits are the
manual's call. Every figure is hypothetical arithmetic on labeled norms, not a statement about
any real machine or lawn.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json from its inline cases
node test.js        # 27 cases / 27 checks
```

Live at https://ilanis-agent.github.io/sweepermath/
