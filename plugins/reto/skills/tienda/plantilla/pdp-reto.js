/* Plantilla de página de producto del Reto. Arma las 29 secciones, en el orden probado, a partir de datos.json.
   No editar: todo lo que cambia de un producto a otro va en datos.json.
   Uso: PDPReto.render(document.getElementById('pdp'), datos, {variantes:[...]})  (variantes solo en Shopify) */
(function(){
const IC={
 gota:'<path d="M12 3c4 4 6 7 6 10a6 6 0 0 1-12 0c0-3 2-6 6-10z"/>',
 persona:'<path d="M7 21l2-6 3 2 2-5 3 9M12 4a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"/>',
 corazon:'<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/>',
 check:'<path d="M5 12l4 4 10-10"/>',
 rayo:'<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 escudo:'<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>',
 capsula:'<rect x="4" y="9" width="16" height="7" rx="3.5"/><path d="M12 9v7"/>',
 fruta:'<circle cx="8" cy="15" r="4"/><circle cx="16" cy="16" r="4"/><path d="M8 11c1-4 4-7 8-8M16 12c0-3-1-6 0-9"/>',
 hoja:'<path d="M12 21V9M12 9c-3 0-6-2-7-6 4 0 6 2 7 6zM12 9c3 0 6-2 7-6-4 0-6 2-7 6z"/>',
 montana:'<path d="M5 20l4-8 3 4 3-6 4 10"/>',
 sol:'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/>',
 vaso:'<path d="M7 3h10l-1 18H8z"/><path d="M7.5 9h9"/>',
 frasco:'<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M5 9h14"/>',
 mas:'<path d="M4 12h16M12 4v16"/>',
 chat:'<path d="M5 19l1.5-4A7 7 0 1 1 9 18z"/>',
 estrella:'<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.5 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
 camion:'<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>'
};
const svg=(n,cls='')=>`<svg class="${cls}" viewBox="0 0 24 24">${IC[n]||IC.check}</svg>`;
const st=n=>'★★★★★'.slice(0,n||5);

function render(root,D,opt){
 opt=opt||{};
 const M=D.marca, C=M.colores;
 root.style.setProperty('--p',C.principal);root.style.setProperty('--a',C.acento);root.style.setProperty('--f',C.fresco);
 root.style.setProperty('--t',C.tinta);root.style.setProperty('--fondo',C.fondo);root.style.setProperty('--b',C.blanco||'#FFFDF9');
 if(C.texto_suave)root.style.setProperty('--mut',C.texto_suave);if(C.linea)root.style.setProperty('--linea',C.linea);
 root.style.setProperty('--ft',`'${M.fuentes.titulos}'`);root.style.setProperty('--fx',`'${M.fuentes.textos}'`);
 const V=opt.variantes||null;
 const fmt=c=>{try{return new Intl.NumberFormat(D.idioma||'es-MX',{style:'currency',currency:opt.moneda||'USD',currencyDisplay:'narrowSymbol'}).format(c/100)}catch(e){return (c/100).toFixed(2)}};
 const O=D.ofertas.map((o,k)=>{const v=V&&V[o.variante!=null?o.variante:k];if(!v)return o;const u=o.unidades||1;
  return Object.assign({},o,{id:v.id,precio:fmt(v.p),antes:v.c>v.p?fmt(v.c):'',por_unidad:fmt(Math.round(v.p/u))+' '+(D.texto_por_unidad||'por unidad'),ahorro:v.c>v.p?(D.texto_ahorro||'Ahorra')+' '+fmt(v.c-v.p):''})});
 const B=D.botones;
 const h=[];
 // 1-3 barra, encabezado, cinta
 h.push(`<div class="top"><div><b>${D.barra.titulo}</b><small>${D.barra.sub}</small></div><div class="cd" data-fin="${D.barra.fin}"></div></div>`);
 h.push(`<header><div class="w"><svg class="ic" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg><img class="logo" src="${M.logo}" alt="${M.nombre}"><svg class="ic" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg><svg class="ic" viewBox="0 0 24 24"><path d="M5 8h14l-1 12H6zM9 8a3 3 0 0 1 6 0"/></svg></div></header>`);
 const cinta=(D.cinta.map(b=>'<em>●</em>'+b).join('')).repeat(4);
 h.push(`<div class="mq"><span>${cinta}</span></div>`);
 // 4-15 bloque de compra
 h.push(`<main class="w"><div class="pdp"><div class="car"><div class="track">${D.galeria.map(g=>`<img src="${g}" alt="">`).join('')}</div>
 <button class="arr l" data-go="-1" aria-label="Anterior">‹</button><button class="arr r" data-go="1" aria-label="Siguiente">›</button>
 <div class="thumbs">${D.galeria.map((g,k)=>`<img src="${g}" alt="" data-i="${k}">`).join('')}</div><div class="dots">${D.galeria.map(()=>'<i></i>').join('')}</div></div>
 <div class="buy" id="pdp-buy"><div class="proof"><span class="stars">${st()}</span>${D.prueba.texto}<div class="av">${D.prueba.caras.map(c=>`<img src="${c}" alt="">`).join('')}</div></div>
 <p class="cat">${D.categoria}</p><h1>${D.titulo}</h1><p class="sub">${D.frase}</p>
 <div class="icons">${D.iconos.map(t=>`<div>${svg('check')}${t}</div>`).join('')}</div>
 <div class="price"><b data-pnow></b><s data-pwas></s><span class="save" data-psave></span></div>
 <div class="offers" data-offers></div>
 <div class="unl"><span>${D.regalos_titulo||'REGALOS DESBLOQUEADOS'}</span><div class="gifts" data-gifts></div></div>
 <div class="del" data-del></div>
 <button class="atc" data-atc>${B.agregar} <span class="pill" data-atcp></span> →</button>
 ${D.suscripcion?`<p class="subn">${D.suscripcion}</p>`:''}
 <div class="acc">${D.desplegables.map(d=>`<details><summary>${d.t}</summary><p>${d.p}</p></details>`).join('')}</div>
 </div></div></main>`);
 // 16 bloque oscuro
 const BO=D.bloque_oscuro;
 h.push(`<section class="s dark"><div class="w stat"><h2>${BO.titulo}</h2><div class="n">${BO.numero}</div><p>${BO.texto}</p><a class="cta" href="#pdp-buy">${B.pruebalo}</a></div></section>`);
 // 17 ingredientes
 const I=D.ingredientes;
 h.push(`<section class="s" style="background:var(--fondo)"><div class="w"><h2>${I.titulo} <span class="ac">${I.titulo_acento||''}</span></h2><p class="lead">${I.sub}</p></div>
 <div class="hs" data-hs="ingr">${I.items.map(x=>`<div class="ing"><img src="${x.img}" alt=""><h3>${x.t}</h3><p>${x.p}</p></div>`).join('')}</div>
 <div class="nav"><button data-hsb="ingr" data-d="-1">‹</button><button data-hsb="ingr" data-d="1">›</button></div></section>`);
 // 18 reseñas con fotos
 const R=D.resenas;
 h.push(`<section class="s"><div class="w"><p class="lead" style="margin-bottom:2px"><span class="stars">${st()}</span></p><h2>${R.titulo}</h2><p class="lead">${R.sub}</p></div>
 <div class="ugc">${R.fotos.map(f=>`<img src="${f}" alt="">`).join('')}</div>
 <div class="hs" data-hs="revs">${R.items.map(r=>`<div class="rev"><span class="stars">${st(r.estrellas)}</span><h3>"${r.titulo}"</h3><p>${r.texto}</p><small>${r.nombre}${r.ciudad?' · '+r.ciudad:''} · <span class="ok">✓ ${R.verificada||'Compra verificada'}</span></small></div>`).join('')}</div>
 <div class="nav"><button data-hsb="revs" data-d="-1">‹</button><button data-hsb="revs" data-d="1">›</button></div></section>`);
 // 19 siéntete mejor
 const SM=D.sientete;
 h.push(`<section class="s dark feel"><div class="w"><h2>${SM.titulo}</h2><p class="lead">${SM.sub}</p>
 <div class="row3">${SM.iconos.map(x=>`<div>${svg(x.icono)}${x.t}</div>`).join('')}</div>
 <div class="glow"><img src="${M.producto_sin_fondo}" alt="${M.nombre}"></div></div></section>`);
 // 20-21 beneficios reales
 const BE=D.beneficios;
 h.push(`<section class="s" style="padding-top:56px"><div class="w"><h2 style="color:var(--a)">${BE.titulo}</h2><p class="lead">${BE.sub}</p>
 <div class="bens">${BE.items.map(x=>`<div class="ben"><img src="${x.img}" alt=""><div><b>${x.t}</b><span>${x.p}</span></div><i>+</i></div>`).join('')}</div>
 <a class="cta v" href="#pdp-buy" style="max-width:560px;margin-top:14px">${B.pruebalo}</a></div></section>`);
 h.push(`<div class="mq"><span>${cinta}</span></div>`);
 // 22 razones
 const RZ=D.razones;
 h.push(`<section class="s" style="background:var(--fondo)"><div class="w"><h2><span class="ac">${RZ.titulo_acento}</span> ${RZ.titulo}</h2><p class="lead">${RZ.sub}</p></div>
 <div class="hs" data-hs="rz">${RZ.items.map((x,k)=>`<div class="reason"><img src="${x.img}" alt=""><em>${RZ.etiqueta||'Razón'} ${k+1}</em><h3>${x.t}</h3><p>${x.p}</p></div>`).join('')}</div>
 <div class="nav"><button data-hsb="rz" data-d="-1">‹</button><button data-hsb="rz" data-d="1">›</button></div>
 <div class="w" style="margin-top:14px"><a class="cta v" href="#pdp-buy">${B.pruebalo}</a></div></section>`);
 // 23 comparación
 const CP=D.comparacion;
 h.push(`<section class="s vs"><div class="w"><h2>${CP.titulo}</h2><p class="lead">${CP.sub}</p>
 <div class="cmp"><div class="hd"></div><div class="hd us"><img src="${CP.nuestro_img}" alt=""><b>${M.nombre}</b></div><div class="hd"><img src="${CP.otro_img}" alt=""><span>${CP.otro_nombre}</span></div>
 ${CP.filas.map(f=>`<div class="l">${f}</div><div class="y">✓</div><div class="n">✕</div>`).join('')}</div>
 <a class="cta" href="#pdp-buy">${B.pruebalo}</a></div></section>`);
 // 24 garantía
 const G=D.garantia;
 h.push(`<section class="s"><div class="w guar"><div class="seal">${G.dias}<small>${G.unidad||'DÍAS'}</small></div><p class="k">${G.kicker}</p><h2>${G.titulo}</h2><p>${G.texto}</p>
 <a class="cta v" href="#pdp-buy">${B.pruebalo}</a><img class="pt" src="${G.img}" alt=""></div></section>`);
 // 25 videos
 const VI=D.videos;
 h.push(`<section class="s" style="background:var(--fondo)"><div class="w"><h2>${VI.titulo} <span class="ac">${VI.titulo_acento}</span></h2><p class="lead">${VI.sub}</p></div>
 <div class="hs v" data-hs="vids">${VI.items.map(x=>`<div class="vid">${x.video?`<video src="${x.video}" poster="${x.poster||''}" playsinline preload="metadata"></video>`:`<img src="${x.poster}" alt="">`}<span>"${x.frase}"</span></div>`).join('')}</div>
 <div class="nav"><button data-hsb="vids" data-d="-1">‹</button><button data-hsb="vids" data-d="1">›</button></div></section>`);
 // 26 oferta otra vez
 const RE=D.repetir;
 h.push(`<section class="s again"><div class="w box"><div class="fan">${RE.imgs.map(i=>`<img src="${i}" alt="">`).join('')}</div>
 <h2><em>${RE.titulo_acento}</em> ${RE.titulo}</h2><p class="lead">${RE.sub}</p>
 <div class="offers" data-offers></div><div class="del" data-del></div>
 <button class="atc" data-atc>${B.agregar} <span class="pill" data-atcp></span> →</button>
 ${D.suscripcion?`<p class="subn">${D.suscripcion}</p>`:''}</div></section>`);
 // 27 preguntas frecuentes
 const F=D.preguntas;
 h.push(`<section class="s"><div class="w" style="max-width:600px"><h2>${F.titulo}</h2><p class="lead">${F.sub}</p>
 <div class="acc">${F.items.map(q=>`<details><summary>${q.q}</summary><p>${q.a}</p></details>`).join('')}</div>
 <a class="cta v" href="#pdp-buy" style="margin-top:14px">${B.pruebalo}</a></div></section>`);
 // 28 lista de reseñas
 const L=D.lista_resenas;
 h.push(`<section class="s"><div class="w"><p class="lead" style="margin-bottom:2px"><span class="stars">${st()}</span> ${L.linea}</p><h2>${L.titulo}</h2><p class="lead" style="font-size:12px">${L.sub}</p>
 <div class="list">${L.items.map(r=>`<div class="rev"><span class="stars">${st(r.estrellas)}</span> ${(r.estrellas||5).toFixed(1)}<h3>"${r.texto}"</h3><small>${r.nombre}</small><div class="tags">${(r.etiquetas||[]).map(t=>`<span>${t}</span>`).join('')}</div></div>`).join('')}</div>
 ${L.mas?`<a class="more" href="#">${L.mas}</a>`:''}</div></section>`);
 // 29 pie
 const P=D.pie;
 h.push(`<footer><div class="w"><img class="flogo" src="${M.logo}" alt="${M.nombre}"><h3>${P.titulo}</h3><p>${P.texto}</p>
 <div class="nl"><input placeholder="${P.placeholder||'Tu correo'}"><button>${P.boton||'Enviar'}</button></div>
 <ul>${P.links.map(l=>`<li>${l}</li>`).join('')}</ul><div class="disc">${P.legal.map(l=>`<p>${l}</p>`).join('')}</div>
 <p class="cur">${P.pais}</p><p class="disc">© ${new Date().getFullYear()} ${M.nombre}</p></div></footer>`);
 h.push(`<div class="sticky"><img src="${D.galeria[0]}" alt=""><div><b>${D.nombre_producto}</b><span data-stp></span></div><button data-tobuy>${B.fijo}</button></div>`);
 if(D.whatsapp)h.push(`<a class="wa" href="https://wa.me/${D.whatsapp}" target="_blank" rel="noopener" aria-label="WhatsApp"><svg width="26" height="26" viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/></svg></a>`);
 root.innerHTML=h.join('\n');

 // ---------- comportamiento ----------
 const $=(s,r=root)=>r.querySelector(s),$$=(s,r=root)=>[...r.querySelectorAll(s)];
 const tr=$('.track'),th=$$('.thumbs img'),dt=$$('.dots i'),n=D.galeria.length;
 const cur=()=>Math.round(tr.scrollLeft/tr.clientWidth);
 const mark=()=>{const c=cur();th.forEach((x,k)=>x.classList.toggle('on',k===c));dt.forEach((x,k)=>x.classList.toggle('on',k===c))};
 tr.addEventListener('scroll',()=>requestAnimationFrame(mark));mark();
 $$('[data-go]').forEach(b=>b.onclick=()=>tr.scrollTo({left:Math.max(0,Math.min(n-1,cur()+ +b.dataset.go))*tr.clientWidth,behavior:'smooth'}));
 th.forEach(t=>t.onclick=()=>tr.scrollTo({left:+t.dataset.i*tr.clientWidth,behavior:'smooth'}));
 $$('[data-hsb]').forEach(b=>b.onclick=()=>{const e=$(`[data-hs="${b.dataset.hsb}"]`);e.scrollBy({left:+b.dataset.d*(e.firstElementChild.offsetWidth+12),behavior:'smooth'})});
 let sel=D.oferta_elegida!=null?D.oferta_elegida:1;
 const pinta=()=>{
  $$('[data-offers]').forEach(b=>{b.innerHTML='';O.forEach((o,k)=>{const d=document.createElement('div');d.className='off'+(k===sel?' on':'');
   let pi='';for(let j=0;j<(o.unidades||1);j++)pi+=`<img src="${D.img_paquete||D.galeria[0]}" style="left:${j*10}px" alt="">`;
   d.innerHTML=(o.etiqueta?`<span class="tag ${o.etiqueta_color==='fresco'?'g':''}">${o.etiqueta}</span>`:'')+`<div class="pi">${pi}</div><div><b>${o.nombre}</b><small>${o.por_unidad||''}</small></div><div class="p"><b>${o.precio}</b><br>${o.antes?`<s>${o.antes}</s>`:''}</div>`+(o.regalo&&k===sel?`<div class="gift">${o.regalo}</div>`:'');
   d.onclick=()=>{sel=k;pinta()};b.appendChild(d)})});
  const o=O[sel];$('[data-pnow]').textContent=o.precio;$('[data-pwas]').textContent=o.antes||'';$('[data-psave]').textContent=o.ahorro||'';
  $$('[data-atcp]').forEach(e=>e.innerHTML=(o.antes?`<s>${o.antes}</s>`:'')+o.precio);$('[data-stp]').textContent=o.nombre+' · '+o.precio;
  $('[data-gifts]').innerHTML=(D.regalos||[]).map((g,k)=>{const on=sel>=g.nivel;return(k?'<i>+</i>':'')+`<div class="${on?'':'lock'}"><img src="${g.img}" alt=""><s>${g.antes}</s>${on?'<b>'+g.nombre+'</b>':'🔒 '+(D.bloqueado||'Bloqueado')}</div>`}).join('');
 };pinta();
 const f=d=>d.toLocaleDateString(D.idioma||'es-MX',{weekday:'short',day:'numeric',month:'short'});
 const a=new Date(),b=new Date();a.setDate(a.getDate()+D.entrega.min);b.setDate(b.getDate()+D.entrega.max);
 $$('[data-del]').forEach(e=>e.innerHTML=`${D.entrega.texto||'Pide hoy y te llega entre el'} <b>${f(a)}</b> y el <b>${f(b)}</b>`);
 const cd=$('.cd'),fin=new Date(cd.dataset.fin);const tick=()=>{let s=Math.max(0,(fin-new Date())/1000|0);const d=s/86400|0,hh=s%86400/3600|0,m=s%3600/60|0,x=s%60;
  cd.innerHTML=[[d,'Días'],[hh,'Hrs'],[m,'Min'],[x,'Seg']].map(([v,l])=>`<span>${String(v).padStart(2,'0')}<i>${l}</i></span>`).join(':')};tick();setInterval(tick,1000);
 $$('.vid').forEach(v=>{const vd=v.querySelector('video');if(!vd)return;v.onclick=()=>{$$('.vid video').forEach(o=>{if(o!==vd){o.pause();o.parentNode.classList.remove('playing')}});if(vd.paused){vd.play();v.classList.add('playing')}else{vd.pause();v.classList.remove('playing')}};vd.onended=()=>v.classList.remove('playing')});
 const stk=$('.sticky'),atc=$('[data-atc]');new IntersectionObserver(([e])=>stk.classList.toggle('on',!e.isIntersecting&&e.boundingClientRect.top<0)).observe(atc);
 $('[data-tobuy]').onclick=()=>atc.scrollIntoView({behavior:'smooth',block:'center'});
 $$('[data-atc]').forEach(btn=>btn.onclick=async()=>{const o=O[sel];
  if(o.id&&opt.carrito!==false){btn.disabled=true;try{await fetch('/cart/add.js',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({items:[{id:o.id,quantity:1}]})});location.href=opt.ir_a||'/checkout'}catch(e){btn.disabled=false}}
  else{btn.animate([{transform:'scale(1)'},{transform:'scale(.97)'},{transform:'scale(1)'}],{duration:200})}});
}
window.PDPReto={render};
})();
