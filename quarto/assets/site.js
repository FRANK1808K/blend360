/* Study website behaviour / Comportamiento del sitio de estudio.
   - Page tools: "mark as studied", reading time, show/hide solutions, print, open on GitHub.
   - Task lists (- [ ]) become real checkboxes saved in the browser (the study plan, for example).
   - Home: countdowns, "what to do this week" and progress per area.
   - "My progress": pages studied, mock exam log, mistake notebook, simulator attempts, backup.
   Everything is saved only in this browser (localStorage). / Todo se guarda solo en este navegador. */
(function () {
  "use strict";

  var LANG = (document.documentElement.lang || "es").slice(0, 2) === "en" ? "en" : "es";
  var meta = document.querySelector('meta[name="quarto:offset"]');
  var ROOT = meta ? meta.getAttribute("content") : "./";
  var REPO = "https://github.com/FRANK1808K/blend360/blob/HEAD/";
  var MANIFEST = window.B360_MANIFEST || { es: [], en: [] };
  var DAY = 864e5;

  var T = {
    es: {
      mark: "Marcar como estudiada", done: "Estudiada", min: function (n) { return "~" + n + " min de lectura"; },
      show: function (n) { return "Mostrar soluciones (" + n + ")"; }, hide: "Ocultar soluciones",
      print: "Imprimir / PDF", github: "Ver en GitHub",
      days: function (n) { return n === 1 ? "día" : "días"; }, today: "¡Es hoy!", past: "Ya pasó",
      aws: "AWS AI Practitioner (AIF-C01)", blend: "Prueba Blend360 All Star",
      week: "Esta semana", daily: "Todos los días: inglés 30–40 min + razonamiento 15–20 min.",
      of: " de ", pages: "páginas estudiadas", areaDone: "estudiado",
      empty: "Todavía no hay registros.", del: "Borrar", confirmReset: "¿Borrar TODO tu progreso guardado en este navegador? No se puede deshacer.",
      imported: "Progreso importado.", badFile: "Ese archivo no es una copia válida del progreso.",
      due: "Para repasar hoy", later: "Programados", mastered: "Dominado", again: "+3 días",
      top: "Tu causa de error más frecuente", noErrors: "Aún no anotas errores. Cada fallo de un simulacro es una entrada.",
      causes: { concept: "No sabía el concepto", english: "No entendí el inglés", time: "Me faltó tiempo", careless: "Descuido", trap: "Caí en una trampa" },
      advice: {
        concept: "Vuelve a la teoría del tema y rehaz los ejercicios fallados dentro de 2 días.",
        english: "Repasa las palabras clave en «Cómo leer preguntas» y agrega flashcards con las palabras que no sabías.",
        time: "Haz bloques cronometrados (12 min por SQL, 1 min por pregunta de opción múltiple) y salta las difíciles.",
        careless: "Antes de responder, subraya la palabra que cambia todo (NOT, EXCEPT, LEAST, MOST) y revisa tu respuesta una vez.",
        trap: "Anota la trampa como regla en el cuaderno y repásala con los cheatsheets de pares que se confunden."
      },
      sim: "Intentos en el simulador Blend360", simAif: "Intentos en el simulador AIF-C01", lab: "Laboratorio de código",
      noSim: "Sin intentos todavía (o los hiciste en otro navegador).", solved: "resueltos",
      modes: { abstract: "Razonamiento", tech: "Técnico (opción múltiple)", sql: "Reto SQL" }
    },
    en: {
      mark: "Mark as studied", done: "Studied", min: function (n) { return "~" + n + " min read"; },
      show: function (n) { return "Show solutions (" + n + ")"; }, hide: "Hide solutions",
      print: "Print / PDF", github: "View on GitHub",
      days: function (n) { return n === 1 ? "day" : "days"; }, today: "It's today!", past: "Done",
      aws: "AWS AI Practitioner (AIF-C01)", blend: "Blend360 All Star test",
      week: "This week", daily: "Every day: English 30–40 min + reasoning 15–20 min.",
      of: " of ", pages: "pages studied", areaDone: "studied",
      empty: "No entries yet.", del: "Delete", confirmReset: "Delete ALL the progress saved in this browser? This cannot be undone.",
      imported: "Progress imported.", badFile: "That file is not a valid progress backup.",
      due: "To review today", later: "Scheduled", mastered: "Mastered", again: "+3 days",
      top: "Your most frequent cause of mistakes", noErrors: "No mistakes logged yet. Every mock exam miss is an entry.",
      causes: { concept: "Didn't know the concept", english: "Didn't understand the English", time: "Ran out of time", careless: "Careless", trap: "Fell for a trap" },
      advice: {
        concept: "Go back to the topic's theory and redo the missed exercises within 2 days.",
        english: "Review the key words in “How to read questions” and add flashcards with the words you didn't know.",
        time: "Do timed blocks (12 min per SQL problem, 1 min per multiple-choice question) and skip the hard ones.",
        careless: "Before answering, underline the word that changes everything (NOT, EXCEPT, LEAST, MOST) and check once.",
        trap: "Write the trap down as a rule in the notebook and review it with the confusable-pairs cheat sheet."
      },
      sim: "Blend360 simulator attempts", simAif: "AIF-C01 simulator attempts", lab: "Code lab",
      noSim: "No attempts yet (or you took them in another browser).", solved: "solved",
      modes: { abstract: "Reasoning", tech: "Technical (multiple choice)", sql: "SQL challenge" }
    }
  }[LANG];

  // ---------------------------------------------------------------- storage / almacenamiento
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem("b360:" + k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem("b360:" + k, JSON.stringify(v)); } catch (e) { /* no storage / sin almacenamiento */ } },
    raw: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } }
  };
  function isDone(key) { return !!store.get("done", {})[key]; }
  function setDone(key, on) {
    var d = store.get("done", {});
    if (on) d[key] = Date.now(); else delete d[key];
    store.set("done", d);
  }
  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) { if (k === "class") e.className = attrs[k]; else e.setAttribute(k, attrs[k]); }
    if (html !== undefined) e.innerHTML = html;
    return e;
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function today() { var d = new Date(); d.setHours(0, 0, 0, 0); return d; }
  function parseDay(s) { var p = s.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function iso(d) { return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  function fmtDay(s) { return parseDay(s).toLocaleDateString(LANG === "en" ? "en-US" : "es-CO", { day: "numeric", month: "short" }); }

  // ---------------------------------------------------------------- page tools / herramientas
  var tools = document.querySelector(".page-tools");
  if (tools) {
    var key = tools.getAttribute("data-key");
    var doneBtn = el("button", { type: "button", class: "b-pill" });
    var paint = function () {
      var on = isDone(key);
      doneBtn.classList.toggle("is-done", on);
      doneBtn.setAttribute("aria-pressed", on);
      doneBtn.innerHTML = on ? "✅ " + T.done : "☐ " + T.mark;
    };
    doneBtn.addEventListener("click", function () { setDone(key, !isDone(key)); paint(); });
    paint();
    tools.appendChild(doneBtn);
    tools.appendChild(el("span", { class: "b-pill is-static" }, "⏱ " + T.min(tools.getAttribute("data-min"))));
    var details = document.querySelectorAll("main details");
    if (details.length >= 2) {
      var solBtn = el("button", { type: "button", class: "b-pill" }, "👁 " + T.show(details.length));
      solBtn.addEventListener("click", function () {
        var open = !Array.prototype.every.call(details, function (d) { return d.open; });
        details.forEach(function (d) { d.open = open; });
        solBtn.innerHTML = open ? "🙈 " + T.hide : "👁 " + T.show(details.length);
      });
      tools.appendChild(solBtn);
    }
    var printBtn = el("button", { type: "button", class: "b-pill" }, "🖨 " + T.print);
    printBtn.addEventListener("click", function () { window.print(); });
    tools.appendChild(printBtn);
    tools.appendChild(el("a", { class: "b-pill", href: REPO + tools.getAttribute("data-src"), target: "_blank", rel: "noopener" }, "↗ " + T.github));
  }

  // ---------------------------------------------------------------- task lists / listas de tareas
  var pageKey = tools ? tools.getAttribute("data-key") : location.pathname;
  var boxes = document.querySelectorAll('main li input[type="checkbox"]');
  if (boxes.length) {
    var saved = store.get("tasks:" + pageKey, []);
    boxes.forEach(function (box, i) {
      box.disabled = false;
      box.checked = saved.indexOf(i) >= 0;
      box.addEventListener("change", function () {
        var now = [];
        boxes.forEach(function (b, j) { if (b.checked) now.push(j); });
        store.set("tasks:" + pageKey, now);
      });
    });
  }

  // ---------------------------------------------------------------- dates / fechas
  var EXAMS = { aws: "2026-11-16", blend: "2026-12-18" };
  function daysTo(s) { return Math.round((parseDay(s) - today()) / DAY); }
  document.querySelectorAll("[data-countdown]").forEach(function (box) {
    var which = box.getAttribute("data-countdown");
    var n = daysTo(EXAMS[which]);
    box.classList.toggle("past", n < 0);
    box.innerHTML = '<div class="b-count-num">' + (n > 0 ? n + " " + T.days(n) : n === 0 ? T.today : T.past) + "</div>" +
      '<div class="b-count-label">' + T[which] + " · " + fmtDay(EXAMS[which]) + "</div>";
  });

  // The study plan week by week (guides/plan-de-estudio.md) / El plan semana a semana.
  var PLAN = [
    ["2026-10-26", "2026-11-01", 1, { es: "Fase 1 · Semana 1: AWS + base Blend360", en: "Phase 1 · Week 1: AWS + Blend360 base" }, [
      ["aws-ai-practitioner/domains/01-fundamentals-ai-ml/index.html", "AWS AIF-C01: dominios 1 y 2", "AWS AIF-C01: domains 1 and 2"],
      ["02-sql/index.html", "SQL: secciones 1–6 + ejercicios 1–10", "SQL: sections 1–6 + exercises 1–10"],
      ["01-razonamiento-abstracto/ejercicios.html", "Razonamiento: series A y B, sin tiempo", "Reasoning: series A and B, untimed"],
      ["english/como-leer-preguntas.html", "Inglés: cómo leer preguntas + flashcards en Anki", "English: how to read questions + Anki flashcards"]]],
    ["2026-11-02", "2026-11-08", 1, { es: "Fase 1 · Semana 2", en: "Phase 1 · Week 2" }, [
      ["aws-ai-practitioner/domains/03-applications-foundation-models/index.html", "AWS AIF-C01: dominios 3 y 4", "AWS AIF-C01: domains 3 and 4"],
      ["06-aws/index.html", "Fundamentos de nube (sirven para los dos exámenes) + SQL 11–21", "Cloud fundamentals (useful for both exams) + SQL 11–21"],
      ["simulador/index.html", "Razonamiento: secciones C–F + simulador en modo práctica", "Reasoning: sections C–F + simulator practice mode"],
      ["english/vocabulario-tecnico.html", "Inglés: vocabulario de AWS + gramática 1–3", "English: AWS vocabulary + grammar 1–3"]]],
    ["2026-11-09", "2026-11-15", 1, { es: "Fase 1 · Semana 3: simulacros AIF-C01", en: "Phase 1 · Week 3: AIF-C01 mock exams" }, [
      ["aws-ai-practitioner/practice-questions/index.html", "AWS: dominio 5 + 2 simulacros completos + repaso de errores", "AWS: domain 5 + 2 full mock exams + review mistakes"],
      ["06-aws/analisis-de-datos.html", "Blend (ligero): análisis de datos en AWS + 30 preguntas", "Blend (light): data analytics on AWS + 30 questions"],
      ["simulacros/simulacro-razonamiento-01.html", "Simulacro de razonamiento #1 (30 min): anota el puntaje", "Reasoning mock #1 (30 min): log your score"],
      ["aws-ai-practitioner/cheatsheets/final-review-48h.html", "14–15 nov: repaso final del AIF-C01, sin temas nuevos", "Nov 14–15: AIF-C01 final review, nothing new"]]],
    ["2026-11-16", "2026-11-16", 1, { es: "🟧 Hoy: examen AWS AIF-C01", en: "🟧 Today: AWS AIF-C01 exam" }, [
      ["aws-ai-practitioner/guides/exam-playbook.html", "Repasa el playbook del examen y descansa después. ¡Éxitos!", "Read the exam playbook and rest afterwards. Good luck!"]]],
    ["2026-11-17", "2026-11-22", 2, { es: "Fase 2 · Semana 4: SQL + Python base", en: "Phase 2 · Week 4: SQL + Python basics" }, [
      ["02-sql/ejercicios.html", "SQL: ejercicios 22–35 (CASE y ventanas) + repetir los fallados", "SQL: exercises 22–35 (CASE and windows) + redo the missed ones"],
      ["03-python/index.html", "Python: teoría completa + quiz «¿qué imprime?»", "Python: full theory + “what does it print?” quiz"],
      ["simulador/index.html", "Python: ejercicios 1–13 en el laboratorio", "Python: exercises 1–13 in the code lab"],
      ["english/vocabulario-tecnico.html", "Inglés: vocabulario de SQL y Python", "English: SQL and Python vocabulary"]]],
    ["2026-11-23", "2026-11-29", 2, { es: "Fase 2 · Semana 5: Python avanzado + algoritmos", en: "Phase 2 · Week 5: advanced Python + algorithms" }, [
      ["03-python/pandas.html", "Python: ejercicios 14–25 + pandas", "Python: exercises 14–25 + pandas"],
      ["04-algoritmos-y-estructuras/index.html", "Algoritmos: teoría completa + problemas 🟢", "Algorithms: full theory + 🟢 problems"],
      ["english/entrevista-y-frases.html", "Inglés: escribe y memoriza tu presentación personal", "English: write and memorise your self-introduction"],
      ["simulador/index.html", "Razonamiento: 1 simulacro completo de 30 min", "Reasoning: 1 full 30-minute mock"]]],
    ["2026-11-30", "2026-12-06", 2, { es: "Fase 2 · Semana 6: algoritmos, BD, problemas, estadística", en: "Phase 2 · Week 6: algorithms, DB, problem solving, statistics" }, [
      ["05-bases-de-datos/index.html", "Algoritmos 🟡 + bases de datos completo", "Algorithms 🟡 + all of databases"],
      ["07-resolucion-de-problemas/index.html", "Resolución de problemas completo", "All of problem solving"],
      ["08-estadistica-y-ml/index.html", "Estadística y ML + 25 preguntas", "Statistics and ML + 25 questions"],
      ["simulacros/simulacro-tecnico-01.html", "Sábado 5 dic: simulacro técnico #1 (90 min, condiciones reales)", "Saturday Dec 5: technical mock #1 (90 min, real conditions)"]]],
    ["2026-12-07", "2026-12-13", 2, { es: "Fase 2 · Semana 7: simulacros y puntos débiles", en: "Phase 2 · Week 7: mock exams and weak spots" }, [
      ["simulador/index.html", "3 simulacros técnicos + 3 de razonamiento en el simulador", "3 technical + 3 reasoning mocks in the simulator"],
      ["02-sql/ejercicios.html", "Repite sin mirar SQL 16, 21, 26, 28, 32, 34 y 35", "Redo SQL 16, 21, 26, 28, 32, 34 and 35 without looking"],
      ["progreso.html#cuaderno-de-errores", "Cada día: 2 SQL (12 min) + 2 Python (15 min) y repaso del cuaderno de errores", "Daily: 2 SQL (12 min) + 2 Python (15 min) and review the mistake notebook", "progreso.en.html#mistake-notebook"]]],
    ["2026-12-14", "2026-12-15", 2, { es: "Fase 2 · Semana 8: cierre", en: "Phase 2 · Week 8: wrap-up" }, [
      ["simulador/index.html", "Último simulacro completo: razonamiento 30 + técnico 90 seguidos", "Last full mock: reasoning 30 + technical 90 back to back"],
      ["cheatsheets/index.html", "Repaso de errores + los cheatsheets", "Review mistakes + the cheat sheets"]]],
    ["2026-12-16", "2026-12-17", 3, { es: "Fase 3 · Repaso final", en: "Phase 3 · Final review" }, [
      ["cheatsheets/repaso-final-48h.html", "Sigue el repaso final de 48 h. Nada nuevo.", "Follow the final 48-hour review. Nothing new."]]],
    ["2026-12-18", "2026-12-18", 4, { es: "🟦 Hoy: prueba Blend360 All Star", en: "🟦 Today: Blend360 All Star test" }, [
      ["cheatsheets/repaso-final-48h.html", "Lee solo tu lista de errores y el plan del día. ¡A ganar!", "Read only your mistake list and the day plan. Go win it!"]]]
  ];
  // English pages link to the English twins (the AIF-C01 domains and the simulators exist only once).
  // Las páginas en inglés enlazan a sus gemelos en inglés (los dominios AIF-C01 y los simuladores existen una sola vez).
  function localHref(it) {
    if (LANG !== "en") return it[0];
    if (it[3]) return it[3];
    return /^(simulador|aws-ai-practitioner)\//.test(it[0]) ? it[0] : it[0].replace(/\.html(#.*)?$/, ".en.html$1");
  }
  var plan = document.getElementById("b-today");
  if (plan) {
    var t0 = today(), week = null;
    PLAN.forEach(function (w) { if (t0 >= parseDay(w[0]) && t0 <= parseDay(w[1])) week = w; });
    if (!week && t0 < parseDay(PLAN[0][0])) week = PLAN[0];
    var phase = week ? week[2] : 5;
    document.querySelectorAll("[data-phase]").forEach(function (p) { p.classList.toggle("now", +p.getAttribute("data-phase") === phase); });
    if (week) {
      plan.innerHTML = '<span class="b-phase">' + T.week + " · " + fmtDay(week[0]) + (week[1] !== week[0] ? " – " + fmtDay(week[1]) : "") + "</span>" +
        "<h3>" + esc(week[3][LANG]) + "</h3><ul>" + week[4].map(function (it) {
          return '<li><a href="' + ROOT + localHref(it) + '">' + esc(LANG === "en" ? it[2] : it[1]) + "</a></li>";
        }).join("") + "</ul><p class=\"b-empty\" style=\"margin:.6rem 0 0\">" + T.daily + "</p>";
    } else {
      plan.innerHTML = "<h3>" + (LANG === "en" ? "The plan is over. Well done! 🎉" : "El plan terminó. ¡Bien hecho! 🎉") + "</h3>";
    }
  }

  // ---------------------------------------------------------------- progress / progreso
  function stats(groups) {
    var seen = {}, all = 0, done = 0, areas = {};
    groups.forEach(function (g) {
      var a = areas[g.area] || (areas[g.area] = { title: g.areaTitle, all: 0, done: 0 });
      g.items.forEach(function (it) {
        a.all++; if (isDone(it.key)) a.done++;
        if (seen[it.key]) return;
        seen[it.key] = 1; all++; if (isDone(it.key)) done++;
      });
    });
    return { all: all, done: done, areas: areas };
  }
  function pct(a, b) { return b ? Math.round(100 * a / b) : 0; }
  function bar(p) { return '<div class="b-bar' + (p >= 100 ? " ok" : "") + '"><span style="width:' + p + '%"></span></div>'; }

  var homeProgress = document.getElementById("b-home-progress");
  if (homeProgress) {
    var s = stats(MANIFEST[LANG]);
    homeProgress.innerHTML = Object.keys(s.areas).map(function (k) {
      var a = s.areas[k], p = pct(a.done, a.all);
      return '<div class="b-card"><div class="b-card-title">' + esc(a.title) + "</div>" + bar(p) +
        '<div class="b-card-meta">' + a.done + T.of + a.all + " · " + p + "%</div></div>";
    }).join("");
  }

  var app = document.getElementById("b-progress");
  if (app) renderProgress(app);

  function renderProgress(app) {
    var groups = MANIFEST[LANG];
    var s = stats(groups), p = pct(s.done, s.all), r = 50, len = 2 * Math.PI * r;
    var html = '<div class="b-ring"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="bg" cx="60" cy="60" r="' + r + '"/>' +
      '<circle class="fg" cx="60" cy="60" r="' + r + '" stroke-dasharray="' + len.toFixed(1) + '" stroke-dashoffset="' + (len * (1 - p / 100)).toFixed(1) + '"/></svg>' +
      '<div><div class="b-ring-num">' + p + '%</div><div>' + s.done + T.of + s.all + " " + T.pages + "</div></div></div>";
    var lastArea = null;
    groups.forEach(function (g, gi) {
      if (g.area !== lastArea) { html += "<h3>" + esc(g.areaTitle) + "</h3>"; lastArea = g.area; }
      var d = g.items.filter(function (it) { return isDone(it.key); }).length;
      html += '<div class="b-group"><div class="b-group-head"><span>' + esc(g.title === g.areaTitle ? (LANG === "en" ? "Section home" : "Portada de la sección") : g.title) + "</span><small>" + d + T.of + g.items.length + "</small></div>" +
        bar(pct(d, g.items.length)) + "<ul>" + g.items.map(function (it, ii) {
          var on = isDone(it.key), id = "b-p-" + gi + "-" + ii;
          return '<li class="' + (on ? "done" : "") + '"><input type="checkbox" id="' + id + '" data-key="' + esc(it.key) + '"' + (on ? " checked" : "") +
            '> <a href="' + ROOT + it.href + '">' + esc(it.label) + "</a></li>";
        }).join("") + "</ul></div>";
    });
    app.innerHTML = html;
    app.querySelectorAll("input[data-key]").forEach(function (box) {
      box.addEventListener("change", function () { setDone(box.getAttribute("data-key"), box.checked); renderProgress(app); });
    });
  }

  // ---------------------------------------------------------------- mock exam log / registro de simulacros
  var EXAM_TYPES = [
    ["razonamiento", 30, 80, "Razonamiento abstracto (30 min)", "Abstract reasoning (30 min)"],
    ["tecnico-sim", 40, 85, "Técnico: simulador (40 preguntas)", "Technical: simulator (40 questions)"],
    ["tecnico-01", 40, 85, "Técnico #1 (90 min)", "Technical #1 (90 min)"],
    ["reto-sql", 5, 80, "Reto SQL (5 consultas, 60 min)", "SQL challenge (5 queries, 60 min)"],
    ["aws-30", 30, 80, "AWS: 30 preguntas", "AWS: 30 questions"],
    ["aif-01", 65, 85, "AIF-C01 · Simulacro 01", "AIF-C01 · Mock exam 01"],
    ["aif-02", 65, 85, "AIF-C01 · Simulacro 02", "AIF-C01 · Mock exam 02"],
    ["otro", 10, 80, "Otro", "Other"]
  ];
  function examType(id) { return EXAM_TYPES.filter(function (e) { return e[0] === id; })[0] || EXAM_TYPES[EXAM_TYPES.length - 1]; }
  function causeOptions() { return Object.keys(T.causes).map(function (k) { return '<option value="' + k + '">' + T.causes[k] + "</option>"; }).join(""); }

  var scoreApp = document.getElementById("b-scores");
  if (scoreApp) renderScores(scoreApp);

  function renderScores(box) {
    var rows = store.get("scores", []);
    var L = LANG === "en";
    box.innerHTML =
      '<form class="b-form" id="b-score-form">' +
      '<label>' + (L ? "Date" : "Fecha") + '<input type="date" name="date" required value="' + iso(today()) + '"></label>' +
      '<label class="wide">' + (L ? "Test" : "Prueba") + '<select name="type">' + EXAM_TYPES.map(function (e) { return '<option value="' + e[0] + '">' + (L ? e[4] : e[3]) + "</option>"; }).join("") + "</select></label>" +
      '<label>' + (L ? "Correct" : "Correctas") + '<input type="number" name="score" min="0" required></label>' +
      '<label>' + (L ? "Out of" : "De") + '<input type="number" name="total" min="1" required value="30"></label>' +
      '<label>' + (L ? "Minutes used" : "Minutos usados") + '<input type="number" name="minutes" min="0"></label>' +
      '<label>' + (L ? "Main cause of mistakes" : "Causa principal de error") + '<select name="cause"><option value="">—</option>' + causeOptions() + "</select></label>" +
      '<button class="b-btn primary" type="submit">＋ ' + (L ? "Log result" : "Registrar resultado") + "</button></form>" +
      chart(rows) + table(rows);
    var form = box.querySelector("form");
    form.type.addEventListener("change", function () { form.total.value = examType(form.type.value)[1]; });
    form.total.value = examType(form.type.value)[1];
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      rows.push({ date: form.date.value, type: form.type.value, score: +form.score.value, total: +form.total.value,
        minutes: form.minutes.value ? +form.minutes.value : null, cause: form.cause.value });
      rows.sort(function (a, b) { return a.date < b.date ? -1 : 1; });
      store.set("scores", rows);
      renderScores(box);
    });
    box.querySelectorAll("[data-del]").forEach(function (b) {
      b.addEventListener("click", function () { rows.splice(+b.getAttribute("data-del"), 1); store.set("scores", rows); renderScores(box); });
    });
  }
  function chart(rows) {
    if (rows.length < 2) return "";
    var W = 640, H = 200, P = 30, n = rows.length;
    var x = function (i) { return P + (W - 2 * P) * (n === 1 ? .5 : i / (n - 1)); };
    var y = function (v) { return H - P - (H - 2 * P) * v / 100; };
    var pts = rows.map(function (r, i) { return [x(i), y(pct(r.score, r.total)), r]; });
    var svg = '<svg class="b-chart" viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + (LANG === "en" ? "Score trend" : "Evolución del puntaje") + '">';
    [0, 50, 100].forEach(function (v) { svg += '<line class="grid" x1="' + P + '" x2="' + (W - P) + '" y1="' + y(v) + '" y2="' + y(v) + '"/><text x="0" y="' + (y(v) + 4) + '">' + v + "%</text>"; });
    svg += '<line class="goal" x1="' + P + '" x2="' + (W - P) + '" y1="' + y(80) + '" y2="' + y(80) + '"/><text x="' + (W - P - 70) + '" y="' + (y(80) - 6) + '">' + (LANG === "en" ? "goal 80%" : "meta 80 %") + "</text>";
    svg += '<polyline class="line" points="' + pts.map(function (p) { return p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + '"/>';
    pts.forEach(function (p) { svg += '<circle class="dot' + (p[2].type.indexOf("aif") === 0 ? " aws" : "") + '" cx="' + p[0].toFixed(1) + '" cy="' + p[1].toFixed(1) + '" r="5"><title>' + esc(fmtDay(p[2].date) + " · " + (LANG === "en" ? examType(p[2].type)[4] : examType(p[2].type)[3]) + " · " + pct(p[2].score, p[2].total) + "%") + "</title></circle>"; });
    return svg + "</svg>";
  }
  function table(rows) {
    if (!rows.length) return '<p class="b-empty">' + T.empty + "</p>";
    var L = LANG === "en";
    return "<table><thead><tr><th>" + (L ? "Date" : "Fecha") + "</th><th>" + (L ? "Test" : "Prueba") + "</th><th>" + (L ? "Score" : "Puntaje") +
      "</th><th>" + (L ? "Time" : "Tiempo") + "</th><th>" + (L ? "Cause" : "Causa") + "</th><th></th></tr></thead><tbody>" +
      rows.map(function (r, i) {
        var e = examType(r.type), p = pct(r.score, r.total);
        return "<tr><td>" + fmtDay(r.date) + "</td><td>" + esc(L ? e[4] : e[3]) + "</td><td>" + r.score + "/" + r.total +
          ' <span class="b-chip ' + (p >= e[2] ? "ok" : "bad") + '">' + p + "%</span></td><td>" + (r.minutes != null ? r.minutes + " min" : "—") +
          "</td><td>" + (r.cause ? esc(T.causes[r.cause]) : "—") + '</td><td><button class="b-x" title="' + T.del + '" data-del="' + i + '">✕</button></td></tr>';
      }).join("") + "</tbody></table>";
  }

  // ---------------------------------------------------------------- mistake notebook / cuaderno de errores
  var TOPICS = ["SQL", "Python", "pandas", "Algoritmos / Algorithms", "Bases de datos / Databases", "AWS", "Estadística y ML / Statistics",
    "Resolución de problemas / Problem solving", "Razonamiento / Reasoning", "Inglés / English",
    "AIF-C01 D1", "AIF-C01 D2", "AIF-C01 D3", "AIF-C01 D4", "AIF-C01 D5"];
  var errApp = document.getElementById("b-errors");
  if (errApp) renderErrors(errApp);

  function renderErrors(box) {
    var rows = store.get("errors", []), L = LANG === "en", t0 = iso(today());
    var plus = function (n) { return iso(new Date(today().getTime() + n * DAY)); };
    var counts = {};
    rows.forEach(function (r) { if (r.cause) counts[r.cause] = (counts[r.cause] || 0) + 1; });
    var top = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; })[0];
    var active = rows.map(function (r, i) { return [r, i]; }).filter(function (x) { return !x[0].mastered; })
      .sort(function (a, b) { return a[0].due < b[0].due ? -1 : 1; });
    var item = function (x) {
      var r = x[0], late = r.due <= t0;
      return '<div class="b-group"><div class="b-group-head"><span>' + esc(r.topic) + " · " + esc(r.what) + '</span><small><span class="b-chip ' + (late ? "bad" : "") + '">' +
        (late ? "⏰ " : "📅 ") + fmtDay(r.due) + "</span></small></div>" +
        (r.rule ? "<div>💡 " + esc(r.rule) + "</div>" : "") + (r.cause ? '<div class="b-empty">' + esc(T.causes[r.cause]) + "</div>" : "") +
        '<div class="b-actions"><button class="b-pill" data-ok="' + x[1] + '">✅ ' + T.mastered + '</button><button class="b-pill" data-again="' + x[1] + '">↻ ' + T.again + "</button>" +
        '<button class="b-pill" data-rm="' + x[1] + '">✕ ' + T.del + "</button></div></div>";
    };
    var due = active.filter(function (x) { return x[0].due <= t0; }), later = active.filter(function (x) { return x[0].due > t0; });
    box.innerHTML =
      '<form class="b-form">' +
      '<label>' + (L ? "Topic" : "Tema") + '<select name="topic">' + TOPICS.map(function (t) { return "<option>" + t + "</option>"; }).join("") + "</select></label>" +
      '<label>' + (L ? "Why" : "Por qué") + '<select name="cause">' + causeOptions() + "</select></label>" +
      '<label>' + (L ? "Review on" : "Repasar el") + '<input type="date" name="due" value="' + plus(2) + '"></label>' +
      '<label class="wide">' + (L ? "What did I get wrong?" : "¿Qué fallé?") + '<input name="what" required placeholder="' + (L ? "e.g. LEFT JOIN + WHERE turned it into an INNER JOIN" : "p. ej. LEFT JOIN + WHERE lo convirtió en INNER JOIN") + '"></label>' +
      '<label class="wide">' + (L ? "Rule so it does not happen again" : "Regla para que no se repita") + '<input name="rule" placeholder="' + (L ? "e.g. filter the right table in ON, not in WHERE" : "p. ej. el filtro de la tabla derecha va en el ON, no en el WHERE") + '"></label>' +
      '<button class="b-btn primary" type="submit">＋ ' + (L ? "Add to notebook" : "Agregar al cuaderno") + "</button></form>" +
      (top ? '<div class="callout callout-style-default callout-tip"><div class="callout-body-container callout-body" style="padding:.8rem 1rem"><strong>' + T.top + ": " + esc(T.causes[top]) + " (" + counts[top] + ")</strong><br>" + esc(T.advice[top]) + "</div></div>" : "") +
      "<h4>" + T.due + " (" + due.length + ")</h4>" + (due.length ? due.map(item).join("") : '<p class="b-empty">' + (rows.length ? "✓" : T.noErrors) + "</p>") +
      (later.length ? "<h4>" + T.later + " (" + later.length + ")</h4>" + later.map(item).join("") : "") +
      (rows.length - active.length ? '<p class="b-empty">✅ ' + T.mastered + ": " + (rows.length - active.length) + "</p>" : "");
    var form = box.querySelector("form");
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      rows.push({ topic: form.topic.value, cause: form.cause.value, due: form.due.value || plus(2), what: form.what.value.trim(), rule: form.rule.value.trim(), added: t0 });
      store.set("errors", rows);
      renderErrors(box);
    });
    var act = function (attr, fn) {
      box.querySelectorAll("[" + attr + "]").forEach(function (b) {
        b.addEventListener("click", function () { fn(rows[+b.getAttribute(attr)], +b.getAttribute(attr)); store.set("errors", rows); renderErrors(box); });
      });
    };
    act("data-ok", function (r) { r.mastered = t0; });
    act("data-again", function (r) { r.due = plus(3); });
    act("data-rm", function (r, i) { rows.splice(i, 1); });
  }

  // ---------------------------------------------------------------- simulators / simuladores
  var simApp = document.getElementById("b-sim");
  if (simApp) {
    var L = LANG === "en";
    var hist = store.raw("sim3090-history", []);
    var aif = store.raw("aifc01-sim-history", []);
    var solved = (store.raw("sim3090-lab", {}).solved || []);
    var count = function (prefix) { return solved.filter(function (k) { return k.indexOf(prefix + ":") === 0; }).length; };
    var labRows = [["SQL", count("sql"), 36], ["Python", count("py"), 25], [L ? "Algorithms" : "Algoritmos", count("algo"), 20]];
    simApp.innerHTML =
      "<h4>" + T.lab + "</h4>" + labRows.map(function (r) {
        return "<div><strong>" + r[0] + "</strong> · " + r[1] + "/" + r[2] + " " + T.solved + bar(pct(r[1], r[2])) + "</div>";
      }).join("") +
      "<h4>" + T.sim + "</h4>" + (hist.length ? "<table><tbody>" + hist.map(function (h) {
        return "<tr><td>" + new Date(h.date).toLocaleDateString(L ? "en-US" : "es-CO", { day: "numeric", month: "short" }) + "</td><td>" + esc(T.modes[h.mode] || h.mode) + "</td><td>" + esc(h.score) + "</td><td>" + esc(h.time || "") + "</td></tr>";
      }).join("") + "</tbody></table>" : '<p class="b-empty">' + T.noSim + "</p>") +
      "<h4>" + T.simAif + "</h4>" + (aif.length ? "<table><tbody>" + aif.slice().reverse().map(function (h) {
        return "<tr><td>" + new Date(h.date).toLocaleDateString(L ? "en-US" : "es-CO", { day: "numeric", month: "short" }) + "</td><td>" + esc(h.modeName || "") +
          '</td><td><span class="b-chip ' + (h.pct >= 85 ? "ok" : "bad") + '">' + h.pct + "%</span></td></tr>";
      }).join("") + "</tbody></table>" : '<p class="b-empty">' + T.noSim + "</p>");
  }

  // ---------------------------------------------------------------- backup / copia de seguridad
  var backup = document.getElementById("b-backup");
  if (backup) {
    var L2 = LANG === "en";
    backup.innerHTML = '<div class="b-actions">' +
      '<button class="b-btn" id="b-export">⬇ ' + (L2 ? "Download backup" : "Descargar copia") + "</button>" +
      '<label class="b-btn" style="cursor:pointer">⬆ ' + (L2 ? "Restore backup" : "Restaurar copia") + '<input type="file" accept="application/json" id="b-import" hidden></label>' +
      '<button class="b-btn" id="b-reset">🗑 ' + (L2 ? "Delete everything" : "Borrar todo") + "</button></div>";
    var KEYS = /^(b360:|sim3090-history$|sim3090-lab$|aifc01-sim-history$)/;
    document.getElementById("b-export").addEventListener("click", function () {
      var data = {};
      try { for (var i = 0; i < localStorage.length; i++) { var k = localStorage.key(i); if (KEYS.test(k)) data[k] = localStorage.getItem(k); } } catch (e) { /* none */ }
      var a = el("a", { href: URL.createObjectURL(new Blob([JSON.stringify({ b360: 1, saved: new Date().toISOString(), data: data }, null, 1)], { type: "application/json" })),
        download: "progreso-blend360-" + iso(today()) + ".json" });
      document.body.appendChild(a); a.click(); a.remove();
    });
    document.getElementById("b-import").addEventListener("change", function (ev) {
      var file = ev.target.files[0];
      if (!file) return;
      file.text().then(function (txt) {
        var j = JSON.parse(txt);
        if (!j || j.b360 !== 1 || typeof j.data !== "object") throw new Error("bad");
        Object.keys(j.data).forEach(function (k) { if (KEYS.test(k)) localStorage.setItem(k, j.data[k]); });
        alert(T.imported); location.reload();
      }).catch(function () { alert(T.badFile); });
    });
    document.getElementById("b-reset").addEventListener("click", function () {
      if (!confirm(T.confirmReset)) return;
      try { Object.keys(localStorage).forEach(function (k) { if (/^b360:/.test(k)) localStorage.removeItem(k); }); } catch (e) { /* none */ }
      location.reload();
    });
  }
})();
