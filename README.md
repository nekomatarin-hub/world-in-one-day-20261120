# world-in-one-day-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nekomatarin-hub/world-in-one-day-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/nekomatarin-hub/world-in-one-day-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world news of **Friday 20 November 2026**: a dated front-page collage of six stories — Russia's overnight barrage of 400+ drones and 110 missiles on Kyiv, with two missiles and a suspected drone coming down in Poland (NATO called it a grave violation of its airspace); the AI and chip sell-off that pushed the S&P 500 and the Dow into correction and the Nasdaq down 5%, erasing its 2026 gains; the International Court of Justice ruling that Myanmar committed genocide against the Rohingya; Prime Minister Burnham signing the UK–EU food, carbon-market and youth-mobility agreements in Brussels; Trump, Xi and Putin's first trilateral summit in Shenzhen ending with few concrete results; and a magnitude 6.7 earthquake striking central Peru — plus a ticker of the day's other headlines (the Hormuz tanker fire and Trump's Iran timeline, student protests across 25 European countries, the Palisades Fire arson conviction, and Japan's core inflation rising to a year high).

The artwork is a six-panel editorial collage drawn without text; every word on the final image is set in a real font by `compose.py`, so no label is garbled. Facts were checked against the day's reporting (One Turn's daily brief) before the captions were written.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png — the exact 1024x1024 PNG the judge sees
```

To rebuild the picture itself: `python3 compose.py` (needs Pillow) regenerates `entry.png` from the collage in `assets/`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=fs66msvv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
