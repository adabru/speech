https://alphacephei.com/vosk/

#################
TALON

- Wiki: https://talon.wiki/
- GitHub: https://github.com/talonvoice
- https://talon-knausj-cheatsheet.netlify.app/

- ISSUES
  - font type error: https://github.com/talonvoice/talon/issues/395

#################
KALDI

- opened issue: https://github.com/pykaldi/pykaldi/issues/294
- Kaldi training
- Sphinx - force aligned trainingsdaten + abspielen von allen aufnahmen pro phone
- kann man das erkennen von Wörtern auch bei Grummel/Garbage abstellen
  (z.B. blub -> führt zu 'YES')
- ambigueties auflösen - zu ähnliche Phrasen
  - sphinx: IY buchstaben (e,b)
  - Montag, falls noch amib.. auf ASCII zurückfallen
- neue Audioaufnahmen: "pause", "continue", "hold" ,"release", etc.

- testen an browser, code editor und desktop
  - compose key (ß, ä, ö, ü, €) in sway

optional

- move speechwindow to good position
- 5s delay für speechwindow aus sway_conf entfernen
  Error: This application failed to start because no Qt platform plugin could be initialized
  Vermutung: xwayland braucht Zeit zum starten
- visuelles feedback bei confirmation (Yes, No)
- GUI für Aufnahmen

links
https://pykaldi.github.io/index.html
https://kaldi-asr.org/doc/online_decoding.html#GMM-based
https://github.com/pykaldi/pykaldi

#################
Sphinx

- keyword list https://cmusphinx.github.io/wiki/tutoriallm/#using-keyword-lists-with-pocketsphinx
- language model : http://www.speech.cs.cmu.edu/tools/product/1638013916_02308/
- create lm online: http://www.speech.cs.cmu.edu/tools/lmtool-new.html
- get pronounciation: http://www.speech.cs.cmu.edu/cgi-bin/cmudict

training

```sh
cd sphinx/own
sphinxtrain run
```

HINTS:

- arecord -r 16000 -f S16_LE yes_001.wav
- arecord -r 16000 -f S16_LE --device="hw:2,0" test.wav
- python -m sounddevice

REFS:
https://stackoverflow.com/questions/11739675/why-am-i-missing-the-an4-1-1-match-file-in-this-speech-recognition-code

- Problem ''.' is no longer in @INC; did you mean do "./etc/sphinx_train.cfg"?'
  https://sourceforge.net/p/cmusphinx/discussion/help/thread/20595a03/
- Problem:
  MODULE: DECODE Decoding using models previously trained
  Aligning results to find error rate
  Can't open /home/slava/speech_commands/sphinx/own//result/own-1-2.match
  Can't open /home/slava/speech_commands/sphinx/own//result/own-2-2.match
  word_align.pl failed with error code 65280 at /usr/lib/sphinxtrain/scripts/decode/slave.pl line 173.

  Nach der Einstellung "CFG_CD_TRAIN = True" in der sphinx_train.cfg, ist der Fehler sowohl bei der Kotextabh. als auch unabhängigen nicht wieder aufgetaucht:

  Skipped: $ST::CFG_MMIE set to 'no' in sphinx_train.cfg
  MODULE: 90 deleted interpolation
  Skipped for continuous models
  MODULE: DECODE Decoding using models previously trained
  Aligning results to find error rate
  SENTENCE ERROR: 100.0% (1/1) WORD ERROR RATE: 150.0% (3/2)

Generate lm

- anyks-lm https://github.com/anyks/alm
  - funktioniert noch nicht
  - install
    pip install pybind11
    pip install anyks-lm
- CMUCLMTK https://cmusphinx.github.io/wiki/tutoriallm/#language-models

  - t -S cmuclmtk # generates also <s></s>key

- SRILM

  - t -S kaldi-srilm: package outdated, funktioniert nicht mehr
    https://stackoverflow.com/questions/33432085/correct-parameters-for-wngram2idngram

- quick_lm, fix <s></s>key issue:
  http://www.speech.cs.cmu.edu/tools/factory.html
  http://www.speech.cs.cmu.edu/tools/download/quick_lm.pl

#################
Brainstorming

- Sphinx :
  - schnelles Training + Ausführung, wenig ram
  * free text
    ? ambiguities mit "pseudo" (alpha) ersetzen - Risiko?
- Kaldi
- Online - latenz & internet Ausfall

- key words

  - modi: je nach Fenstertitel / Dateiendung / manuell?
  - code: (if, then, ..)
  - "open browser"

- phones: ASCII Zahlen / Unicode statt Buchstaben

- Brumm Frequenz und Länge

select microphone in PulseAudio Settings > Recording > ASR, alternatively:
pactl set default ...
pw-record --list-targets

##############################################

# ONYX

##############################################

# import alm

# alm.setSize(3)

# alm.setThreads(0)

# alm.setLocale("en_US.UTF-8")

# alm.setOption(alm.options_t.allowUnk)

# alm.setOption(alm.options_t.resetUnk)

# alm.setOption(alm.options_t.mixDicts)

# alm.setOption(alm.options_t.tokenWords)

# alm.setOption(alm.options_t.interpolate)

# alm.init(alm.smoothing_t.modKneserNey, True, True)

# p = alm.getParams()

# p.algorithm

# p.mod

# p.prepares

# p.modified

# alm.addWord("hello")

# alm.addText("The future is now", 0)

# def status(text, status):

# print(text, status)

# def printStatus(status):

# print(status)

# def statusWriteArpa(status):

# print("Write ARPA", status)

# def statusBuildArpa(status):

# print("Build ARPA", status)

# alm.collectCorpus("./corpus.txt", status)

# alm.pruneVocab(-15.0, 0, 0, printStatus)

# print("pruneArpa")

# alm.pruneArpa(0.015, 3, printStatus)

# alm.writeWords("./words.txt", printStatus)

# alm.writeVocab("./lm.vocab", printStatus)

# alm.writeNgrams("./lm.ngram", printStatus)

# alm.writeMap("./lm.map", printStatus, "|")

# alm.writeSuffix("./suffix.txt", printStatus)

# alm.writeAbbrs("./words.abbr", printStatus)

# print(alm.getAbbrs())

# print(alm.getSuffixes())

# print("buildArpa")

# alm.buildArpa(printStatus)

# alm.writeArpa("./lm.arpa", printStatus)
