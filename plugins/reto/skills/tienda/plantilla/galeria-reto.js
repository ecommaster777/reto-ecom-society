/* Plantilla de las 7 piezas del carrusel (estructura probada de suplementos). No editar: el contenido va en datos.json, bloque "carrusel".
   Con #1 ... #7 en la URL muestra solo esa pieza (para exportarla); sin número muestra las 7. */
(function(){
const IC={gota:'<path d="M12 3c4 4 6 7 6 10a6 6 0 0 1-12 0c0-3 2-6 6-10z"/>',persona:'<path d="M7 21l2-6 3 2 2-5 3 9M12 4a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"/>',corazon:'<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/>',check:'<path d="M5 12l4 4 10-10"/>',rayo:'<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',escudo:'<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>',capsula:'<rect x="4" y="9" width="16" height="7" rx="3.5"/><path d="M12 9v7"/>',fruta:'<circle cx="8" cy="15" r="4"/><circle cx="16" cy="16" r="4"/><path d="M8 11c1-4 4-7 8-8M16 12c0-3-1-6 0-9"/>',hoja:'<path d="M12 21V9M12 9c-3 0-6-2-7-6 4 0 6 2 7 6zM12 9c3 0 6-2 7-6-4 0-6 2-7 6z"/>',montana:'<path d="M5 20l4-8 3 4 3-6 4 10"/>',sol:'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/>',vaso:'<path d="M7 3h10l-1 18H8z"/><path d="M7.5 9h9"/>',frasco:'<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M5 9h14"/>',mas:'<path d="M4 12h16M12 4v16"/>',chat:'<path d="M5 19l1.5-4A7 7 0 1 1 9 18z"/>'};
const svg=n=>`<svg viewBox="0 0 24 24">${IC[n]||IC.check}</svg>`;
function render(root,D){
 const M=D.marca,C=M.colores,K=D.carrusel;
 const v={'--p':C.principal,'--a':C.acento,'--f':C.fresco,'--t':C.tinta,'--fondo':C.fondo,'--b':C.blanco||'#FFFDF9','--ft':`'${M.fuentes.titulos}'`,'--fx':`'${M.fuentes.textos}'`,'--tile':K.p1.color_recuadros||'color-mix(in srgb,var(--f) 30%,var(--fondo))'};
 Object.entries(v).forEach(([k,x])=>root.style.setProperty(k,x));
 const P=[];
 const p1=K.p1;P.push(`<div class="g p1"><div class="ph" style="background-image:url('${p1.foto}')"></div><div class="tl">${p1.recuadros.map(r=>`<div class="t">${svg(r.icono)}${r.t}</div>`).join('')}</div>${p1.sello?`<div class="badge">${p1.sello}</div>`:''}</div>`);
 const p2=K.p2;P.push(`<div class="g p2"><h2>${p2.titulo}</h2><p class="l">${p2.sub}</p><div class="ic3">${p2.iconos.map(r=>`<div>${svg(r.icono)}${r.t}</div>`).join('')}</div><div class="ring"></div><img src="${M.producto_sin_fondo}" alt=""></div>`);
 const p3=K.p3;P.push(`<div class="g p3" style="background-image:linear-gradient(color-mix(in srgb,var(--p) 92%,transparent),color-mix(in srgb,var(--p) 92%,transparent)),url('${p3.fondo}')"><h2>${p3.titulo}</h2><div class="tiles">${p3.sellos.map(r=>`<div>${svg(r.icono)}${r.t}</div>`).join('')}</div><ul>${p3.puntos.map(x=>`<li>${x}</li>`).join('')}</ul></div>`);
 const p4=K.p4;P.push(`<div class="g p4"><h2>"${p4.cita} <em>${p4.cita_acento}</em>."</h2><p>${p4.texto}</p><b>${p4.nombre}</b><div class="who" style="background-image:url('${p4.foto}')"></div><img class="bt" src="${M.producto_sin_fondo}" alt=""></div>`);
 const p5=K.p5,pos=[[330,60],[50,300],[720,300],[50,730],[720,730],[330,930]];
 P.push(`<div class="g p5"><div class="cap" style="background-image:url('${p5.foto}')"></div>${p5.detalles.slice(0,6).map((r,k)=>`<div class="c" style="left:${pos[k][0]}px;top:${pos[k][1]}px"><i>${svg(r.icono)}</i>${r.t}</div>`).join('')}</div>`);
 const p6=K.p6;P.push(`<div class="g p6"><h2>${p6.titulo}</h2><div class="tb"><div class="a">${p6.filas.slice(0,5).map(r=>`<div class="r">${svg(r.icono)}${r.t}</div>`).join('')}</div><div class="bb">${p6.filas.slice(0,5).map(()=>`<div class="r">✕</div>`).join('')}</div></div><img class="us" src="${M.producto_sin_fondo}" alt=""><img class="them" src="${p6.otro_img}" alt=""></div>`);
 const p7=K.p7;P.push(`<div class="g p7"><h2>${p7.titulo}</h2><div class="box"><div class="row"><span><b>${p7.porcion_t}</b> ${p7.porcion}<br><b>${p7.porciones_t}</b> ${p7.porciones}</span></div><div class="row"><span>${p7.cabecera}</span><span>${p7.vd||'% VD'}</span></div>${p7.ingredientes.map(x=>`<div class="row"><span><b>${x.n}</b><small>${x.detalle||''}</small></span><span>${x.cantidad||'*'}</span></div>`).join('')}</div><p class="ot">${p7.nota}</p><div class="steps">${p7.pasos.map(r=>`<div>${svg(r.icono)}${r.t}</div>`).join('')}</div></div>`);
 const n=parseInt(location.hash.slice(1));
 root.innerHTML=(n>=1&&n<=7)?P[n-1]:P.join('');
}
window.GaleriaReto={render};
})();
