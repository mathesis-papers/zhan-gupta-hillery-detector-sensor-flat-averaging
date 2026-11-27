'use strict';

const filmText = (line, x, y, size, alpha, colour = C.white) =>
  txt(line, x, y, { size, a: alpha, fam: F.mono, align: 'center', c: colour, w: 700 });

SCENES.open = scene => {
  const shown = at(scene, 0, 0.6);
  filmText('WHICH SENSOR FIRED?', W / 2, 300, 67, shown, C.cyan);
  for (const [index, x] of [560, 960, 1360].entries()) {
    panel(x - 136, 395, 272, 180, shown, index === 1 ? C.now : C.cyan, `SENSOR ${index + 1}`);
    filmText(index === 1 ? '?' : '·', x, 518, 84, shown, index === 1 ? C.now : C.white);
  }
  filmText('Two different probes tie. Does averaging break the tie?', W / 2, 730, 37, at(scene, 1, 0.6));
};

SCENES.count = scene => {
  filmText('TWO COMPLEMENTARY WEIGHT LAYERS', W / 2, 238, 49, at(scene, 0, 0.5), C.cyan);
  const lists = [['100', '010', '001'], ['011', '101', '110']];
  for (const [column, words] of lists.entries()) {
    const left = 300 + column * 760;
    panel(left, 310, 560, 395, at(scene, 0, 0.5), C.cyan, `WEIGHT ${column + 1}`);
    words.forEach((word, index) => {
      const y = 435 + 94 * index;
      filmText(word.slice(0, 2), left + 192, y, 64, at(scene, 0, 0.5), C.now);
      filmText(word[2], left + 249, y, 64, at(scene, 0, 0.5));
      filmText(word[0] === word[1] ? 'match' : 'mismatch', left + 410, y, 29, at(scene, 1, 0.5));
    });
  }
  filmText('One match + two opposite-order mismatches, in both lists', W / 2, 805, 32, at(scene, 2, 0.5));
};

SCENES.flat = scene => {
  filmText('THE GRAM TABLE STAYS THE SAME', W / 2, 223, 52, at(scene, 0, 0.5), C.cyan);
  const shown = at(scene, 0, 0.5);
  const mixture = Math.min(1, Math.max(0, scene.p * 1.35 - 0.1));
  panel(285, 315, 810, 340, shown, C.cyan, 'COEFFICIENT-SQUARE MIXTURE');
  filmText('weight 2', 425, 485, 30, shown);
  filmText('weight 1', 955, 485, 30, shown);
  filmText('────────────────────────', 690, 545, 37, shown);
  filmText('●', 438 + 504 * mixture, 545, 42, shown, C.now);
  panel(1145, 315, 500, 340, shown, C.cyan, 'AT THE ANGLE π / 4');
  for (let row = 0; row < 3; row += 1) {
    for (let column = 0; column < 3; column += 1) {
      filmText(row === column ? '1' : '1/3', 1250 + 145 * column, 422 + 87 * row, 47, shown,
        row === column ? C.white : C.now);
    }
  }
  filmText('Same overlaps  →  same positive minimum error', W / 2, 775, 39, at(scene, 1, 0.5));
};

SCENES.close = scene => {
  const shown = at(scene, 0, 0.6);
  filmText('WEAK AVERAGING SURVIVES', W / 2, 330, 63, shown, C.cyan);
  filmText('error of averaged weights  ≤  weighted average of errors', W / 2, 512, 39, shown);
  filmText('Equality is possible — even above zero.', W / 2, 635, 43, shown, C.now);
  filmText('Haobo Ma and Wenlin Zhang · Mathesis v3', W / 2, 763, 30, shown);
};
