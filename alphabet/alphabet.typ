#set text(
  size: 12pt
  , font: "FiraCode Nerd Font"
  , hyphenate: true
)
#set page(margin: (
  top: 15mm
  , bottom: 15mm
  , right: 25mm
  , left: 25mm
))
#set par(
  leading: 7pt
  , spacing: 7pt
)

#show table.cell: it => {
  if it.y > 0 and (it.x == 1 or it.x == 3 or it.x == 5) {
    set text(size: 13pt, font: "Gentium")
    it
  } else {
    it
  }
}


#align(center)[
  = Английский алфавит
  #v(15pt)

  #table(
    columns: (0.33fr, 0.33fr, 0.33fr, 0.5fr, 0.5fr, 1fr)
    , stroke: 0.5pt + black
    , align: center + horizon
    , fill: (x, y) =>
      if x == 0 and y > 0 {
        if (y == 1
           or y == 5
           or y == 9
           or y == 15
           or y == 21
           or y == 25) {
          red.lighten(35%)
        } else {
          blue.lighten(35%)
        }
      }

    // Header
    , table.cell(
      colspan: 3
      ,[*Название буквы*]
    )
    , table.cell(
      colspan: 2
      ,[*Основные звуки*]
    )
    , [*Другие звуки*]

    // 'A' letter
    , [A a], [\[eɪ\]], [эй], [\[eɪ\]#h(10pt)\[æ\]], [эй э], [\[ɑː\]#h(10pt)\[eə\]#h(10pt)\[ɔ\]#h(10pt)\[ɔː\]]

    // 'B' letter
    , [B b], [\[bɪː\]], [би], [\[b\]], [б], [\[- \] = -bt, -mb]

    // 'C' letter
    , [C c], [\[cɪː\]], [си], [\[s\]#h(10pt)\[k\]], [с к], [\[k \] = ck,#h(10pt)\[tʃ\] = ch]

    // 'D' letter
    , [D d], [\[dɪː\]], [ди], [\[d\]], [д], []

    // 'E' letter
    , [E e], [\[ɪː\]], [и], [\[ɪː\]#h(10pt)\[e\]], [и э], [\[əː\]#h(10pt)\[ɪə\]#h(10pt)\[- \]]

    // 'F' letter
    , [F f], [\[ef\]], [эф], [\[f\]], [ф], []

    // 'G' letter
    , [G g], [\[dʒɪ\]], [джи], [\[g\]#h(10pt)\[dʒ\]], [], [\[ʒ\]#h(10pt)\[ŋ\] = ng]

    // 'H' letter
    , [H h], [\[eɪtʃ\]], [эйч], [\[h\]], [х], [\[- \] = wh]

    // 'I' letter
    , [I i], [\[aɪ\]], [ай], [\[aɪ\]#h(10pt)\[ɪ\]], [], [\[əː\]#h(10pt)\[aɪə\]]

    // 'J' letter
    , [J j], [\[dʒeɪ\]], [джей], [\[dʒ\]], [дж], []

    // 'K' letter
    , [K k], [\[keɪ\]], [кей], [\[k\]], [к], [\[- \] = kn-]

    // 'L' letter
    , [L l], [\[el\]], [эл], [\[l\]], [л], [\[- \] = -lf, -lk, -lm]

    // 'M' letter
    , [M m], [\[em\]], [эм], [\[m\]], [м], []

    // 'N' letter
    , [N n], [\[en\]], [эн], [\[n\]], [н], [\[ŋ\] = ng,#h(10pt)\[- \] = -mn]

    // 'O' letter
    , [O o], [\[ou\]], [оу], [\[ou\]#h(10pt)\[ɔ\]], [], [\[ɔː\]#h(10pt)\[əː\]#h(10pt)\[ʌ\]]

    // 'P' letter
    , [P p], [\[pɪː\]], [пи], [\[p\]], [п], [\[f\] = ph]

    // 'Q' letter
    , [Q q], [\[kjuː\]], [кью], [\[k\]], [к], [\[kw \] = qu]

    // 'R' letter 
    , [R r], [\[ɑːʳ\]], [ар], [\[r\]], [р], [\[ɔː\] \[eə\] \[ɑː\] \[əː\] \[ɪə\] \[juə\] \[aɪə\] \[ə\]]

    // 'S' letter
    , [S s], [\[es\]], [эс], [\[s\]#h(10pt)\[z\]], [с з], [\[ʒ\]#h(10pt)\[ʃ\] = sh]

    // 'T' letter
    , [T t], [\[tɪː\]], [ти], [\[t\]], [т], [\[ð\]#h(10pt)\[θ\] = th]

    // 'U' letter
    , [U u], [\[juː\]], [ю], [\[juː\]#h(10pt)\[ʌ\]], [ю], [\[əː\]#h(10pt)\[juə\]#h(10pt)\[u\]#h(10pt)\[uː\]]

    // 'V' letter
    , [V v], [\[vɪː\]], [ви], [\[v\]], [в], []

    // 'W' letter
    , [W w], [\[’dʌbljuː\]], [#text(size: 10pt, "дабл ю")], [\[w\]], [], [\[- \] = wr]

    // 'X' letter
    , [X x], [\[eks\]], [икс], [\[ks\]#h(10pt)\[gz\]], [], []

    // 'Y' letter
    , [Y y], [\[waɪ\]], [вай], [\[j\]#h(10pt)\[aɪ\]#h(10pt)\[ɪ\]], [], [\[aɪə\]]

    // 'Z' letter
    , [Z z], [\[zed\]], [зет], [\[z\]], [з], []
  )
]
