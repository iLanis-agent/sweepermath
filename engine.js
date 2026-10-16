// Sweeper Math engine - hypothetical arithmetic on labeled norms only.
// No verdicts about what any sweeper can pick up: lawn condition and machine
// limits are the manual's call.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function leafCubicFeet(lawn, rate) {
  if (!(lawn > 0)) throw new Error("the lawn size must be above zero");
  if (!(rate > 0)) throw new Error("the leaf rate must be above zero");
  return lawn / 1000 * rate;
}

function hopperTruth(lawn, rate, hopper) {
  if (!(hopper > 0)) throw new Error("the hopper size must be above zero");
  const leaves = leafCubicFeet(lawn, rate);
  const fills = Math.ceil(leaves / hopper);
  let verdict;
  if (fills <= 1) verdict = "one fill and done";
  else if (fills <= 3) verdict = "a few trips to the pile";
  else if (fills <= 8) verdict = "a working pile honestly";
  else verdict = "the pile will need its own zip code";
  return `${lawn} square feet at ${rate} cubic feet of leaves a thousand is ${fixed1(leaves)} cubic feet - ${fills} ${plural(fills, "fill", "fills")} of the ${hopper}-cubic-foot hopper, ${verdict}.`;
}

function lapTruth(lawn, width, pace) {
  if (!(lawn > 0)) throw new Error("the lawn size must be above zero");
  if (!(width > 0)) throw new Error("the sweep width must be above zero");
  if (!(pace > 0)) throw new Error("the pace must be above zero");
  const minutes = lawn / (width / 12 * pace);
  let verdict;
  if (minutes <= 10) verdict = "a quick lap honestly";
  else if (minutes <= 25) verdict = "a working set of laps";
  else if (minutes <= 60) verdict = "a long loop honestly";
  else verdict = "a marathon of laps honestly";
  return `${lawn} square feet at a ${width}-inch sweep and ${pace} feet a minute is ${fixed1(minutes)} minutes of laps - ${verdict}.`;
}

function seasonTruth(fills, weeks, hopper) {
  if (!(fills > 0)) throw new Error("the fills must be above zero");
  if (!(weeks > 0)) throw new Error("the weeks must be above zero");
  if (!(hopper > 0)) throw new Error("the hopper size must be above zero");
  const pile = fills * weeks * hopper;
  let verdict;
  if (pile <= 50) verdict = "a modest pile honestly";
  else if (pile <= 150) verdict = "a working pile";
  else if (pile <= 400) verdict = "a pile taller than the fence";
  else verdict = "a neighborhood landmark honestly";
  return `${fills} ${plural(fills, "fill", "fills")} a weekend over ${weeks} ${plural(weeks, "week", "weeks")} of the ${hopper}-cubic-foot hopper is ${fixed1(pile)} cubic feet of leaves - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { leafCubicFeet, hopperTruth, lapTruth, seasonTruth };
}
