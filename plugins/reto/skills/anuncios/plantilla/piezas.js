// Dibuja una pieza de anuncio. Datos en window.CAMPANA (los pone armar_anuncios.py). La pieza se elige con #ID (ej. #1A).
(function(){
  const C = window.CAMPANA, M = C.marca, col = M.colores, root = document.documentElement.style;
  root.setProperty('--principal', col.principal); root.setProperty('--acento', col.acento); root.setProperty('--fresco', col.fresco);
  root.setProperty('--tinta', col.tinta); root.setProperty('--fondo', col.fondo); root.setProperty('--blanco', col.blanco);
  root.setProperty('--ft-titulos', `"${M.fuentes.titulos}"`); root.setProperty('--ft-texto', `"${M.fuentes.textos}"`);
  const e = s => String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const em = s => e(s).replace(/\*(.+?)\*/g,'<em>$1</em>');   // *texto* = color de acento
  const T = {
    nota: p => `<div class="pz nota"><div class="bar"><span>‹ Notas</span><span>···</span></div>
      <div class="fecha">${e(p.fecha || 'Hoy, 11:48 p. m.')}</div><h1>${e(p.titulo)}</h1>
      <ul>${p.lineas.map((l,i)=>`<li class="${(p.marcadas||[]).includes(i)?'ok':''}">${e(l)}</li>`).join('')}</ul>
      ${p.foto?`<div class="foto"><img src="${p.foto}"></div>`:''}${p.ia?'<div class="ia nt">Imagen creada con IA</div>':''}</div>`,
    post: p => `<div class="pz post"><div class="who"><div class="av"><img src="${M.logo_claro || M.logo}"></div>
      <div><div class="nm">${e(p.nombre || M.nombre)}</div><div class="hd">${e(p.usuario || '@'+M.nombre.toLowerCase())}</div></div></div>
      <p>${e(p.texto)}</p>${p.foto?`<div class="img"><img src="${p.foto}"></div>`:''}${p.ia?'<div class="ia nt">Imagen creada con IA</div>':''}
      </div>`,
    ugc: p => `<div class="pz ugc"><img class="bg" src="${p.foto}"><div class="burbujas ${p.abajo?'abajo':''} ${p.estilo||''}">
      ${p.burbujas.map(b=>`<span class="b">${e(b)}</span>`).join('')}</div>${p.sello?`<div class="sello">${e(p.sello)}</div>`:''}<div class="ia">Imagen creada con IA</div></div>`,
    beneficios: p => `<div class="pz ben"><img class="logo" src="${M.logo}"><h1>${em(p.titulo)}</h1>
      <ul>${p.puntos.map(x=>`<li><i>✓</i><span>${e(x)}</span></li>`).join('')}</ul>
      <img class="frasco" src="${M.producto_sin_fondo}"><div class="pie"><span>${e(p.pie)}</span>${p.boton?`<b>${e(p.boton)}</b>`:''}</div></div>`,
    oferta: p => `<div class="pz ofe"><img class="logo" src="${M.logo_claro || M.logo}"><h1>${em(p.titulo)}</h1>
      <div class="tres"><img src="${M.producto_sin_fondo}"><img src="${M.producto_sin_fondo}"><img src="${M.producto_sin_fondo}"></div>
      <div class="precio">${e(p.precio)}${p.antes?`<s>${e(p.antes)}</s>`:''}</div><div class="sub">${e(p.sub||'')}</div>${p.boton?`<div class="boton">${e(p.boton)}</div>`:''}</div>`,
    bloqueo: p => `<div class="pz blq"><img class="bg" src="${p.fondo}"><div class="fe">${e(p.fecha||'miércoles, 19 de noviembre')}</div><div class="hr">${e(p.hora)}</div>
      <div class="nots">${p.notificaciones.map(n=>`<div class="nt2"><i>${n.logo?`<img src="${M.logo_claro||M.logo}">`:'🔔'}</i><b>${e(n.app)}<small>${e(n.cuando||'ahora')}</small></b><span>${e(n.texto)}</span></div>`).join('')}</div></div>`,
    calendario: p => `<div class="pz cal"><div class="mes">${e(p.mes)}</div><div class="sub">${e(p.sub||'')}</div>
      ${p.dias.map(d=>`<div class="dia"><b>${e(d.dia)}<span>${e(d.num)}</span></b><div>${d.eventos.map(ev=>`<div class="ev ${ev.color||'c1'}">${e(ev.texto)}${ev.hora?`<small>${e(ev.hora)}</small>`:''}</div>`).join('')}</div></div>`).join('')}${p.producto?`<img class="fr" src="${M.producto_sin_fondo}">`:''}</div>`,
    editorial: p => `<div class="pz edi"><img class="bg" src="${p.foto}"><div class="tx"><div class="kick">${e(p.kicker||M.nombre)}</div><h1>${em(p.titulo)}</h1></div>
      ${p.pie?`<div class="pie">${e(p.pie)}</div>`:''}<img class="frasco" src="${M.producto_sin_fondo}"></div>`,
    postit: p => `<div class="pz pst"><img class="bg" src="${p.fondo}"><div class="nota2">${p.lineas.map(l=>`<p>${e(l).replace(/\*(.+?)\*/g,'<u>$1</u>')}</p>`).join('')}</div>${p.producto?`<img class="frasco" src="${M.producto_sin_fondo}">`:''}</div>`,
    comparacion: p => `<div class="pz cmp"><h1>${em(p.titulo)}</h1><div class="cols">
      <div class="col yo"><div class="ft"><img src="${M.producto_sin_fondo}"></div><h2>${e(M.nombre)}</h2><ul>${p.nuestro.map(x=>`<li><b>✓</b>${e(x)}</li>`).join('')}</ul></div>
      <div class="col otro"><div class="ft"><img src="${p.foto_otro}"></div><h2>${e(p.nombre_otro)}</h2><ul>${p.otro.map(x=>`<li><b>✕</b>${e(x)}</li>`).join('')}</ul></div></div>
      ${p.nota?`<p class="nota-al-pie">${e(p.nota)}</p>`:''}</div>`
  };
  const todos = C.conjuntos.flatMap(c => c.anuncios);
  const id = decodeURIComponent(location.hash.slice(1));
  const ad = todos.find(a => a.id === id) || todos.find(a => a.pieza);
  if (!ad || !ad.pieza) { document.body.innerHTML = '<p style="font:40px sans-serif;padding:60px">No hay pieza con ese ID.</p>'; return; }
  try { document.body.innerHTML = T[ad.pieza.plantilla](ad.pieza);
        if (ad.pieza.ia && !document.querySelector('.ia')) document.querySelector('.pz').insertAdjacentHTML('beforeend', '<div class="ia nt">Imagen creada con IA</div>'); }
  catch (err) { document.body.innerHTML = '<p style="font:40px sans-serif;padding:60px;color:#b00">ERROR en ' + ad.id + ': ' + err + '</p>'; }
})();
