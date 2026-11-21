// Entry for make.fun's "Sum up 20 November's world news in one image"
// (news-image-20261120). Node 22, standard library only, no network.
//
// The picture itself is entry.png, beside this file: a dated
// front-page collage of Friday 20 November 2026 — Russia's overnight
// barrage of 400+ drones and 110 missiles on Kyiv, with two missiles
// landing in Poland; the AI plunge that pushed the S&P 500 and Dow
// into correction and erased the Nasdaq's 2026 gains; the World
// Court's ruling that Myanmar committed genocide against the
// Rohingya; the UK–EU food, carbon and youth-mobility deals signed in
// Brussels; Trump, Xi and Putin's first trilateral summit in
// Shenzhen; and the magnitude 6.7 earthquake in central Peru — plus a
// ticker of the day's other stories. compose.py in this repository
// rebuilds entry.png from the drawn collage and the verified
// captions.
//
// This program's whole job is to deliver those exact bytes to the
// grader: copy entry.png to /output/entry.png. Run locally with
// MAKEFUN_OUTPUT_DIR set to stand in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const source = new URL('./entry.png', import.meta.url);
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outputDir, 'entry.png');

// The grader provides /output, but a local stand-in directory may not
// exist yet — create whichever directory we were pointed at.
mkdirSync(outputDir, { recursive: true });
copyFileSync(source, target);

const { size } = statSync(target);
console.log(`wrote ${target} (${size} bytes)`);
