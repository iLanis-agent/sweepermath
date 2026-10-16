import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def leaf_cubic_feet(lawn, rate):
    if not (lawn > 0):
        raise ValueError("the lawn size must be above zero")
    if not (rate > 0):
        raise ValueError("the leaf rate must be above zero")
    return lawn / 1000 * rate

def hopper_truth(lawn, rate, hopper):
    if not (hopper > 0):
        raise ValueError("the hopper size must be above zero")
    leaves = leaf_cubic_feet(lawn, rate)
    fills = math.ceil(leaves / hopper)
    if fills <= 1:
        verdict = "one fill and done"
    elif fills <= 3:
        verdict = "a few trips to the pile"
    elif fills <= 8:
        verdict = "a working pile honestly"
    else:
        verdict = "the pile will need its own zip code"
    return f"{lawn} square feet at {rate} cubic feet of leaves a thousand is {fixed1(leaves)} cubic feet - {fills} {plural(fills, 'fill', 'fills')} of the {hopper}-cubic-foot hopper, {verdict}."

def lap_truth(lawn, width, pace):
    if not (lawn > 0):
        raise ValueError("the lawn size must be above zero")
    if not (width > 0):
        raise ValueError("the sweep width must be above zero")
    if not (pace > 0):
        raise ValueError("the pace must be above zero")
    minutes = lawn / (width / 12 * pace)
    if minutes <= 10:
        verdict = "a quick lap honestly"
    elif minutes <= 25:
        verdict = "a working set of laps"
    elif minutes <= 60:
        verdict = "a long loop honestly"
    else:
        verdict = "a marathon of laps honestly"
    return f"{lawn} square feet at a {width}-inch sweep and {pace} feet a minute is {fixed1(minutes)} minutes of laps - {verdict}."

def season_truth(fills, weeks, hopper):
    if not (fills > 0):
        raise ValueError("the fills must be above zero")
    if not (weeks > 0):
        raise ValueError("the weeks must be above zero")
    if not (hopper > 0):
        raise ValueError("the hopper size must be above zero")
    pile = fills * weeks * hopper
    if pile <= 50:
        verdict = "a modest pile honestly"
    elif pile <= 150:
        verdict = "a working pile"
    elif pile <= 400:
        verdict = "a pile taller than the fence"
    else:
        verdict = "a neighborhood landmark honestly"
    return f"{fills} {plural(fills, 'fill', 'fills')} a weekend over {weeks} {plural(weeks, 'week', 'weeks')} of the {hopper}-cubic-foot hopper is {fixed1(pile)} cubic feet of leaves - {verdict}."

FNS = {"hopperTruth": hopper_truth, "lapTruth": lap_truth, "seasonTruth": season_truth}

cases = [
 {"fn":"hopperTruth","args":[5000,8,25]},
 {"fn":"hopperTruth","args":[3000,8,25]},
 {"fn":"hopperTruth","args":[9000,8,25]},
 {"fn":"hopperTruth","args":[25000,8,25]},
 {"fn":"hopperTruth","args":[60000,8,25]},
 {"fn":"hopperTruth","args":[1000,4,12]},
 {"fn":"hopperTruth","args":[0,8,25]},
 {"fn":"hopperTruth","args":[5000,0,25]},
 {"fn":"hopperTruth","args":[5000,8,0]},
 {"fn":"lapTruth","args":[5000,42,200]},
 {"fn":"lapTruth","args":[2000,42,200]},
 {"fn":"lapTruth","args":[15000,42,200]},
 {"fn":"lapTruth","args":[40000,42,200]},
 {"fn":"lapTruth","args":[100000,42,200]},
 {"fn":"lapTruth","args":[5000,26,150]},
 {"fn":"lapTruth","args":[0,42,200]},
 {"fn":"lapTruth","args":[5000,0,200]},
 {"fn":"lapTruth","args":[5000,42,0]},
 {"fn":"seasonTruth","args":[2,6,25]},
 {"fn":"seasonTruth","args":[1,2,25]},
 {"fn":"seasonTruth","args":[1,6,25]},
 {"fn":"seasonTruth","args":[2,8,25]},
 {"fn":"seasonTruth","args":[3,8,25]},
 {"fn":"seasonTruth","args":[1,1,25]},
 {"fn":"seasonTruth","args":[0,6,25]},
 {"fn":"seasonTruth","args":[2,0,25]},
 {"fn":"seasonTruth","args":[2,6,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
