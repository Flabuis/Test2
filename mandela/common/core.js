// Общие вещи для всех серий: рендерер 320x240 в духе PS1, материалы, текстуры, люди, текст, VHS-обработка.
import * as THREE from 'three';
export { THREE };
export const FPS = 15, RW = 320, RH = 240;

// ---------- утилиты ----------
export function mulberry(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
export const hash=(a,b)=>mulberry((a*73856093)^(b*19349663))();
export const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
export const P=(t,a,b)=>clamp((t-a)/(b-a));
export const lerp=(a,b,k)=>a+(b-a)*k;
export const eOut=k=>1-Math.pow(1-k,3), eIn=k=>k*k*k, eInOut=k=>k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2;
export const col=h=>new THREE.Color(h);

// ---------- рендерер (один на всё) ----------
export const glr=new THREE.WebGLRenderer({antialias:false,preserveDrawingBuffer:true});
glr.setPixelRatio(1);glr.setSize(RW,RH,false);
const SNAP={value:new THREE.Vector2(RW/2,RH/2)};
export function ps1(mat){mat.onBeforeCompile=s=>{s.uniforms.uSnap=SNAP;
  s.vertexShader=s.vertexShader.replace('#include <common>','#include <common>\nuniform vec2 uSnap;\nvarying float vAffW;')
   .replace('#include <project_vertex>',`#include <project_vertex>
    vec4 sp=gl_Position; sp.xy=floor(sp.xy/sp.w*uSnap+0.5)/uSnap*sp.w; gl_Position=sp; vAffW=gl_Position.w;
    #ifdef USE_MAP
    vMapUv*=vAffW;
    #endif`);
  s.fragmentShader=s.fragmentShader.replace('#include <common>','#include <common>\nvarying float vAffW;')
   .replace('#include <map_fragment>',`#ifdef USE_MAP
    vec4 sampledDiffuseColor=texture2D(map,vMapUv/vAffW); diffuseColor*=sampledDiffuseColor;
    #endif`)};
  mat.customProgramCacheKey=()=>'ps1'+(mat.map?'m':'')+(mat.emissiveMap?'e':'');return mat}
export const M=(o={})=>ps1(new THREE.MeshLambertMaterial({flatShading:true,...o}));
export const box=(w,h,d,m)=>new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);
// сцену в 2D-канвас 320x240
export function draw3D(scene,camera,ctx){camera.updateMatrixWorld();glr.render(scene,camera);ctx.drawImage(glr.domElement,0,0)}
export function canvas2d(w=RW,h=RH){const c=document.createElement('canvas');c.width=w;c.height=h;return[c,c.getContext('2d',{willReadFrequently:true})]}

// ---------- текстуры ----------
export function tex(w,h,fn,rep=[1,1]){const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');fn(g,w,h);
  const t=new THREE.CanvasTexture(c);t.magFilter=t.minFilter=THREE.NearestFilter;t.generateMipmaps=false;t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(...rep);t.colorSpace=THREE.SRGBColorSpace;return t}
export function noise(g,w,h,pal,seed){const r=mulberry(seed);for(let y=0;y<h;y++)for(let x=0;x<w;x++){g.fillStyle=pal[Math.floor(r()*pal.length)];g.fillRect(x,y,1,1)}}

// ---------- человек (низкополигональный, на шарнирах) ----------
// o: shirt, pants, skin, hair — палитры; face — функция рисования лица 16x16
export function makePerson(o){const pal=(p,s)=>tex(8,8,(g,w,h)=>noise(g,w,h,p,s));
  const mP=M({map:pal(o.pants||['#3a3a40','#34343a'],1)}),mS=M({map:pal(o.shirt||['#6a6a70','#5e5e66'],2)}),mSk=M({map:pal(o.skin||['#d8b090','#d0a888'],3)}),mH=M({map:pal(o.hair||['#3a2a1e','#2e2218'],4)});
  const g=new THREE.Group(),legs=[],arms=[];
  for(const s of[-1,1]){const lg=new THREE.Group();lg.position.set(s*.12,.88,0);const l=box(.18,.8,.2,mP);l.position.y=-.4;lg.add(l);const b=box(.22,.14,.3,M({color:0x1e1a18}));b.position.set(0,-.81,.03);lg.add(b);g.add(lg);legs.push(lg)}
  const tor=box(.56,.72,.32,mS);tor.position.y=1.22;g.add(tor);
  for(const s of[-1,1]){const a=new THREE.Group();a.position.set(s*.37,1.52,0);const u=box(.16,.66,.18,mS);u.position.y=-.32;a.add(u);const hd=box(.13,.13,.13,mSk);hd.position.y=-.7;a.add(hd);g.add(a);arms.push(a)}
  const head=new THREE.Group();head.position.y=1.6;const faces={};const fs=o.faceSize||16;for(const [k,fn] of Object.entries(o.faces||{}))faces[k]=M({map:tex(fs,fs,fn)});
  const fm=faces.normal||mSk;const hb=box(.38,.42,.38,[mSk,mSk,mH,mSk,fm,mH]);hb.position.y=.22;head.add(hb);const cap=box(.4,.1,.4,mH);cap.position.y=.45;head.add(cap);g.add(head);
  g.userData={arms,legs,head,hb,faces};return g}
export function pose(g,o={}){const U=g.userData;U.arms[0].rotation.set(o.ax0||0,0,o.az0??-.06);U.arms[1].rotation.set(o.ax1||0,0,o.az1??.06);
  U.legs[0].rotation.set(o.l0||0,0,0);U.legs[1].rotation.set(o.l1||0,0,0);U.head.rotation.set(o.hx||0,o.hy||0,o.hz||0);if(o.face&&U.faces[o.face])U.hb.material[4]=U.faces[o.face]}

// ---------- текст ----------
export const MONO='"PT Mono", monospace';
export async function loadFonts(){await document.fonts.load(`bold 10px ${MONO}`,'АБВабвЁёABC0123456789▶■:.,!?—«»');await document.fonts.load(`10px ${MONO}`,'Аа');return document.fonts.check(`10px ${MONO}`,'Аа')}
export function text(g,s,x,y,o={}){const size=o.size||10;g.font=`${o.bold===false?'':'bold '}${size}px ${MONO}`;g.textAlign=o.align||'left';g.textBaseline='top';
  if(o.shadow!==false){g.fillStyle=o.shadowColor||'#000';g.fillText(s,x+1,y+1)}g.fillStyle=o.color||'#fff';g.fillText(s,x,y)}
// жёсткая альфа после текста (без сглаживания, «пиксельно»)
export function hardAlpha(g,thr=100){const d=g.getImageData(0,0,g.canvas.width,g.canvas.height),a=d.data;for(let i=3;i<a.length;i+=4)a[i]=a[i]>thr?255:0;g.putImageData(d,0,0)}
// субтитры внизу: белый текст на чёрной плашке, перенос строк
export function subtitle(g,s,t,t0,t1){if(t<t0||t>t1)return;g.font=`bold 10px ${MONO}`;const words=s.split(' '),lines=[''];
  for(const w of words){const tryL=(lines.at(-1)+' '+w).trim();if(g.measureText(tryL).width>290){lines.push(w)}else lines[lines.length-1]=tryL}
  lines.forEach((l,i)=>{const y=RH-14-(lines.length-1-i)*12,w=g.measureText(l).width;g.fillStyle='rgba(0,0,0,.75)';g.fillRect(Math.round(RW/2-w/2-3),y-1,Math.round(w+6),12);text(g,l,RW/2,y,{align:'center',shadow:false})})}

// ---------- PS1-дизер (15-бит цвет) ----------
const BAYER=[0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5];
export function dither(g){const d=g.getImageData(0,0,RW,RH),a=d.data;for(let y=0;y<RH;y++)for(let x=0;x<RW;x++){const i=(y*RW+x)*4,b=(BAYER[(y&3)*4+(x&3)]/16-.5)*8;
  for(let c=0;c<3;c++)a[i+c]=clamp(Math.round((a[i+c]+b)/8)*8,0,255)}g.putImageData(d,0,0)}

// ---------- VHS: сдвиг цвета, шум, полосы трекинга, дрожание строк ----------
export function vhs(g,t,amt=1){const fr=Math.floor(t*FPS),d=g.getImageData(0,0,RW,RH),a=d.data,o=new Uint8ClampedArray(a);
  const band=(((t*.09)%1)*1.4-.2)*RH,bandH=5+3*Math.sin(t*1.7);
  for(let y=0;y<RH;y++){let sh=Math.round((hash(y,fr)-.5)*2*amt*(Math.abs(y-band)<bandH?6:.6));const row=y*RW*4;
    for(let x=0;x<RW;x++){const xs=clamp(x+sh,0,RW-1),xr=clamp(xs+2,0,RW-1),i=row+x*4;
      a[i]=o[row+xr*4];a[i+1]=o[row+xs*4+1];a[i+2]=o[row+clamp(xs-1,0,RW-1)*4+2];
      const n=(hash(x*13+y*7,fr)-.5)*22*amt;a[i]+=n;a[i+1]+=n;a[i+2]+=n;
      if(Math.abs(y-band)<bandH&&hash(x,y+fr)<.025*amt){a[i]=a[i+1]=a[i+2]=220}}}
  g.putImageData(d,0,0)}
// «снег» (белый шум) на весь канвас
export function snow(g,t,k=1){const fr=Math.floor(t*FPS*2),d=g.getImageData(0,0,g.canvas.width,g.canvas.height),a=d.data,w=g.canvas.width;
  for(let i=0;i<a.length;i+=4){const v=hash(i*7+3,fr)*255*k;a[i]=a[i+1]=a[i+2]=v;a[i+3]=255}g.putImageData(d,0,0)}
// масштабирование в итоговый 960x720 + строки развёртки
export function present(src,out,dx=0,dy=0){const ox=out.getContext('2d');ox.imageSmoothingEnabled=false;ox.fillStyle='#000';ox.fillRect(0,0,960,720);ox.drawImage(src,dx*3,dy*3,960,720);
  ox.fillStyle='rgba(0,0,0,.22)';for(let y=2;y<720;y+=3)ox.fillRect(0,y,960,1)}
