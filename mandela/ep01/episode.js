// Том 1 «Округ». Общая картина: округ Мандела, 1991, экстренное оповещение, альтернаты, признаки, инструкция, телесигнал.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,hardAlpha,vhs,dither,snow,makePerson,pose,MONO} from '../common/core.js';

export const VOL=1, D=96;
export const CAPS=[ // начало, конец, кто (R — диктор, A — альтернат), текст. Тайминги = vo/lines.tsv
  [7.0,12.2,'R','Округ Мандела. Тихое место. Леса, озёра, несколько тысяч жителей.'],
  [12.8,17.2,'R','Осенью девяносто первого здесь начали пропадать люди.'],
  [17.8,19.9,'R','А потом — возвращаться.'],
  [21.6,26.2,'R','Внимание. Экстренное оповещение для жителей округа Мандела.'],
  [26.6,31.4,'R','Поступают сообщения о существах, которые выдают себя за ваших близких.'],
  [31.8,34.0,'R','Их называют — альтернаты.'],
  [35.0,39.2,'R','Альтернат выглядит как человек, которого вы знаете.'],
  [39.6,43.6,'R','Говорит его голосом. Знает его привычки.'],
  [44.2,46.6,'R','Но что-то в нём не так.'],
  [52.6,60.4,'R','Если вы встретили альтерната: не смотрите ему в лицо. Не отвечайте. Не впускайте в дом.'],
  [61.0,64.6,'R','Сообщите в офис шерифа округа.'],
  [65.2,68.6,'R','Не пытайтесь справиться сами.'],
  [72.6,77.0,'R','Альтернаты могут проникать в телевизионный сигнал.'],
  [77.6,83.0,'R','Если на экране знакомое лицо просит вас открыть дверь —'],
  [83.4,86.2,'R','немедленно выключите телевизор.'],
  [88.6,91.2,'A','Открой дверь.'],
  [91.8,94.0,'A','Мы знаем, что ты дома.']];

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(58,RW/RH,.05,200);
const amb=new THREE.AmbientLight(0x6070a0,.6);scene.add(amb);const moonL=new THREE.DirectionalLight(0x8090c0,.5);moonL.position.set(-5,8,3);scene.add(moonL);
scene.fog=new THREE.Fog(0x05070f,8,40);scene.background=new THREE.Color(0x05070f);

// ---------- лица 32x32 ----------
function faceBase(g,w,h,seed){noise(g,w,h,['#d4ac8c','#ccA486','#d8b294'],seed);g.fillStyle='#3a2a1e';g.fillRect(0,0,32,6);g.fillRect(0,6,3,8);g.fillRect(29,6,3,8);g.fillStyle='#b88a6e';g.fillRect(14,15,4,6)}
const FACES={
  normal:(g,w,h)=>{faceBase(g,w,h,11);g.fillStyle='#2a1a12';g.fillRect(8,10,6,1);g.fillRect(18,10,6,1);g.fillStyle='#fff';g.fillRect(9,12,4,2);g.fillRect(19,12,4,2);g.fillStyle='#1a1a1a';g.fillRect(10,12,2,2);g.fillRect(20,12,2,2);g.fillStyle='#8a4a3a';g.fillRect(12,24,8,1)},
  wrong1:(g,w,h)=>{faceBase(g,w,h,11);g.fillStyle='#2a1a12';g.fillRect(4,9,6,1);g.fillRect(22,9,6,1);g.fillStyle='#fff';g.fillRect(4,11,5,3);g.fillRect(23,11,5,3);g.fillStyle='#000';g.fillRect(6,12,1,1);g.fillRect(25,12,1,1);
    g.fillStyle='#5a2a20';g.fillRect(7,24,18,1);g.fillRect(6,23,1,1);g.fillRect(25,23,1,1)},
  wrong2:(g,w,h)=>{faceBase(g,w,h,11);g.fillStyle='#000';g.fillRect(4,10,6,4);g.fillRect(22,10,6,4);g.fillStyle='#fff';g.fillRect(6,11,1,1);g.fillRect(24,11,1,1);
    g.fillStyle='#2a0a08';g.fillRect(3,22,26,4);g.fillRect(2,20,2,3);g.fillRect(28,20,2,3);g.fillStyle='#f0ece0';for(let x=4;x<28;x+=2)g.fillRect(x,22,1,2);for(let x=5;x<28;x+=2)g.fillRect(x,24,1,2)}};
const faceTex={};for(const k in FACES)faceTex[k]=tex(32,32,FACES[k]);

// ---------- улица ----------
const street=new THREE.Group();scene.add(street);const lampLights=[];
const TXs={asph:tex(16,16,(g,w,h)=>noise(g,w,h,['#2a2a2e','#26262a','#2e2e32'],20),[4,40]),grass:tex(16,16,(g,w,h)=>noise(g,w,h,['#1e2a1a','#1a2616','#22301e'],21),[20,40]),
  siding:tex(16,16,(g,w,h)=>{noise(g,w,h,['#8a8676','#827e6e','#928e7e'],22);g.fillStyle='rgba(0,0,0,.25)';for(let y=0;y<h;y+=3)g.fillRect(0,y,w,1)},[3,2]),roof:tex(16,16,(g,w,h)=>noise(g,w,h,['#3a2a26','#342622','#40302a'],23),[3,3]),
  pine:tex(8,8,(g,w,h)=>noise(g,w,h,['#142218','#101c14','#18281c'],24)),walk:tex(16,16,(g,w,h)=>{noise(g,w,h,['#5a5a5c','#545456','#606062'],25);g.fillStyle='#3a3a3c';g.fillRect(0,0,w,1)},[1,40])};
{const a=box(6,.02,120,M({map:TXs.asph}));a.position.set(0,0,-40);street.add(a);for(const s of[-1,1]){const w=box(1.6,.06,120,M({map:TXs.walk}));w.position.set(s*3.8,.03,-40);street.add(w);
   const gr=box(30,.02,120,M({map:TXs.grass}));gr.position.set(s*19.6,0,-40);street.add(gr)}
 const r=mulberry(30);for(let i=0;i<8;i++)for(const s of[-1,1]){const hz=4-i*9+r()*2,hx=s*(9+r()*2);const hs=new THREE.Group();const b=box(5,3,5,M({map:TXs.siding}));b.position.y=1.5;hs.add(b);
   const rf=new THREE.Mesh(new THREE.ConeGeometry(4.2,2,4),M({map:TXs.roof}));rf.rotation.y=Math.PI/4;rf.position.y=4;rf.scale.set(1,1,1);hs.add(rf);
   for(const wx of[-1.3,1.3]){const lit=r()<.3;const wn=box(.8,.9,.05,new THREE.MeshBasicMaterial({color:lit?0xd8b060:0x0a0c14}));wn.position.set(wx,1.7,2.52);hs.add(wn)}
   const dr=box(.9,1.8,.05,M({color:0x3a2418}));dr.position.set(0,.9,2.52);hs.add(dr);hs.position.set(hx,0,hz);hs.rotation.y=s>0?-Math.PI/2:Math.PI/2;street.add(hs);
   const pn=new THREE.Mesh(new THREE.ConeGeometry(1.2,4,6),M({map:TXs.pine}));pn.position.set(hx+s*(-3.5),2,hz+4);street.add(pn)}
 for(let i=0;i<4;i++){const z=-i*10-2,s=i%2?1:-1;const pole=box(.12,4,.12,M({color:0x2a2a2a}));pole.position.set(s*3.2,2,z);street.add(pole);
   const head=box(.6,.15,.3,new THREE.MeshBasicMaterial({color:0xffd890,fog:false}));head.position.set(s*2.9,4,z);street.add(head);
   const pool=new THREE.Mesh(new THREE.CircleGeometry(2.4,10),new THREE.MeshBasicMaterial({color:0xffc070,transparent:true,opacity:.14,depthWrite:false}));pool.rotation.x=-Math.PI/2;pool.position.set(s*2.6,.04,z);street.add(pool);
   if(i<3){const l=new THREE.PointLight(0xffc880,6,12,1.5);l.position.set(s*2.9,3.8,z);street.add(l);lampLights.push(l)}}}
const farMan=makePerson({shirt:['#5a5a60','#525258'],faces:{normal:FACES.normal},faceSize:32});farMan.position.set(-2.4,0,-31);street.add(farMan);
const farLamp=new THREE.PointLight(0xffc880,0,10,1.4);farLamp.position.set(-2.6,3.8,-31);street.add(farLamp);
const farHead=box(.6,.15,.3,new THREE.MeshBasicMaterial({color:0xffd890,fog:false}));farHead.position.set(-2.9,4,-31);street.add(farHead);
const farPole=box(.12,4,.12,M({color:0x2a2a2a}));farPole.position.set(-3.2,2,-31);street.add(farPole);

// ---------- двор через окно ----------
const yard=new THREE.Group();scene.add(yard);let yMan;
{const gr=box(40,.02,40,M({map:TXs.grass}));gr.position.set(0,0,-12);yard.add(gr);
 const wm=M({color:0x1a1612});for(const [w,h,x,y] of[[6,1.0,0,.5],[6,1.2,0,2.9],[2.2,4,-2.0,1.6],[2.2,4,2.0,1.6]]){const b=box(w,h,.2,wm);b.position.set(x,y,0);yard.add(b)}
 const fr=M({color:0x6a6050});for(const [w,h,x,y] of[[1.9,.06,0,1.0],[1.9,.06,0,2.3],[.06,1.36,-.92,1.65],[.06,1.36,.92,1.65],[.04,1.3,0,1.65]]){const b=box(w,h,.08,fr);b.position.set(x,y,.06);yard.add(b)}
 const cm=M({color:0x4a2a2a});for(const s of[-1,1]){const c=box(.5,2.2,.05,cm);c.position.set(s*1.05,1.7,.2);yard.add(c)}
 const sill=box(2.1,.08,.3,fr);sill.position.set(0,.98,.15);yard.add(sill);
 for(let i=-6;i<=6;i++){const p=box(.08,.9,.08,M({color:0x8a8a80}));p.position.set(i*.7,.45,-12);yard.add(p)}const rail=box(9,.06,.06,M({color:0x8a8a80}));rail.position.set(0,.8,-12);yard.add(rail);
 const pole=box(.12,4,.12,M({color:0x2a2a2a}));pole.position.set(3.4,2,-10);yard.add(pole);const hd=box(.6,.15,.3,new THREE.MeshBasicMaterial({color:0xffd890,fog:false}));hd.position.set(3.1,4,-10);yard.add(hd);
 const l=new THREE.PointLight(0xffc880,12,14,1.2);l.position.set(2.6,3.8,-6.5);yard.add(l);
 yMan=makePerson({shirt:['#5a5a60','#525258'],faces:{normal:FACES.normal,wrong1:FACES.wrong1,wrong2:FACES.wrong2},faceSize:32});yMan.position.set(1.2,0,-5.2);yard.add(yMan);
 const pn=new THREE.Mesh(new THREE.ConeGeometry(1.4,5,6),M({map:TXs.pine}));pn.position.set(-4,2.5,-14);yard.add(pn)}

// ---------- гостиная с телевизором ----------
const lroom=new THREE.Group();scene.add(lroom);const [tvC,tvX]=[document.createElement('canvas'),null];tvC.width=64;tvC.height=48;const tvG=tvC.getContext('2d');
const tvTex=new THREE.CanvasTexture(tvC);tvTex.magFilter=tvTex.minFilter=THREE.NearestFilter;tvTex.generateMipmaps=false;tvTex.colorSpace=THREE.SRGBColorSpace;const roomL=new THREE.PointLight(0xa0c0ff,4,8,1.3);
{const fl=box(8,.05,8,M({map:tex(16,16,(g,w,h)=>noise(g,w,h,['#3a2e24','#342a20','#40322a'],40),[4,4])}));lroom.add(fl);
 const wp=tex(16,16,(g,w,h)=>{noise(g,w,h,['#4a4232','#463e2e','#4e4636'],41);g.fillStyle='rgba(120,90,60,.4)';for(let x=2;x<w;x+=6)g.fillRect(x,0,2,h)},[6,3]);
 for(const [w,d,x,z] of[[8,.1,0,-4],[.1,8,-4,0],[.1,8,4,0]]){const b=box(w,3,d,M({map:wp}));b.position.set(x,1.5,z);lroom.add(b)}
 const st=box(1.2,.6,.6,M({color:0x3a2618}));st.position.set(0,.3,-3.4);lroom.add(st);const tb=box(.9,.7,.7,M({color:0x2e2e30}));tb.position.set(0,.95,-3.4);lroom.add(tb);
 const sc=new THREE.Mesh(new THREE.PlaneGeometry(.64,.48),new THREE.MeshBasicMaterial({map:tvTex,toneMapped:false,fog:false}));sc.position.set(0,.98,-3.04);lroom.add(sc);
 const sm=M({color:0x5a3a3a});const sb=box(2.4,.5,.9,sm);sb.position.set(0,.45,.6);lroom.add(sb);const sbk=box(2.4,.8,.25,sm);sbk.position.set(0,.9,1.0);lroom.add(sbk);for(const s of[-1,1]){const a=box(.25,.65,.9,sm);a.position.set(s*1.3,.55,.6);lroom.add(a)}
 const lamp=box(.3,.4,.3,M({color:0x6a5a40}));lamp.position.set(-2.6,1.2,-3.4);lroom.add(lamp);
 roomL.position.set(0,1,-2.6);lroom.add(roomL)}

// ---------- крупный план головы ----------
const close=new THREE.Group();scene.add(close);const cHead=makePerson({shirt:['#5a5a60','#525258'],faces:{normal:FACES.normal,wrong1:FACES.wrong1,wrong2:FACES.wrong2},faceSize:32});close.add(cHead);
const closeL=new THREE.PointLight(0xffc880,5,6,1.2);closeL.position.set(1.2,2.2,1.4);close.add(closeL);

// ---------- 2D-карточки ----------
function osd(g,t,tt){text(g,'PLAY ▶',12,10,{size:10});const s=Math.floor(tt);const hh=23,mm=42+Math.floor(s/60),ss=s%60;text(g,`ОКТ 14 1991`,RW-12,10,{align:'right',size:9});text(g,`${hh}:${String(mm).padStart(2,'0')}:${String(ss).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function bars(g){const c=['#c0c0c0','#c0c000','#00c0c0','#00c000','#c000c0','#c00000','#0000c0'];c.forEach((v,i)=>{g.fillStyle=v;g.fillRect(Math.round(i*RW/7),0,Math.ceil(RW/7),RH*.7)});g.fillStyle='#101010';g.fillRect(0,RH*.7,RW,RH*.3)}
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
function alertCard(g,t){g.fillStyle='#0a0e2a';g.fillRect(0,0,RW,RH);g.fillStyle='#a01010';g.fillRect(0,18,RW,30);if(Math.floor(t*2)%2)text(g,'ЭКСТРЕННОЕ ОПОВЕЩЕНИЕ',RW/2,26,{align:'center',size:13});
  // эмблема
  g.fillStyle='#c8b060';g.beginPath();g.moveTo(RW/2,58);g.lineTo(RW/2+14,64);g.lineTo(RW/2+12,82);g.lineTo(RW/2,90);g.lineTo(RW/2-12,82);g.lineTo(RW/2-14,64);g.closePath();g.fill();g.fillStyle='#0a0e2a';g.fillRect(RW/2-6,68,12,2);g.fillRect(RW/2-1,64,2,16);
  typed(g,'ДЕПАРТАМЕНТ ГРАЖДАНСКОЙ ЗАЩИТЫ',RW/2,98,t,21.4,{align:'center',size:10,color:'#c8c8d8'});typed(g,'ОКРУГ МАНДЕЛА, ШТАТ ВИСКОНСИН',RW/2,112,t,22.6,{align:'center',size:10,color:'#c8c8d8'});
  if(t>26.6){typed(g,'ЗАФИКСИРОВАНЫ СЛУЧАИ ПОДМЕНЫ ЛИЧНОСТИ.',RW/2,140,t,26.6,{align:'center',size:10});typed(g,'ОСТАВАЙТЕСЬ ДОМА.',RW/2,154,t,28.4,{align:'center',size:10,color:'#ff6060'})}
  if(t>31.8){text(g,'ОБОЗНАЧЕНИЕ: «АЛЬТЕРНАТ»',RW/2,180,{align:'center',size:11,color:Math.floor(t*4)%2?'#ffffff':'#ffd060'})}}
const STEPS=[[53.6,'1. НЕ СМОТРИТЕ ЕМУ В ЛИЦО.'],[56.4,'2. НЕ ОТВЕЧАЙТЕ.'],[58.2,'3. НЕ ВПУСКАЙТЕ В ДОМ.'],[61.0,'4. СООБЩИТЕ В ОФИС ШЕРИФА.'],[65.2,'5. НЕ ДЕЙСТВУЙТЕ В ОДИНОЧКУ.']];
function stepsCard(g,t){g.fillStyle='#1a2a5a';g.fillRect(0,0,RW,RH);g.fillStyle='#e8e4d8';g.fillRect(14,14,RW-28,RH-50);g.fillStyle='#1a2a5a';g.fillRect(14,14,RW-28,24);
  text(g,'ЕСЛИ ВЫ ВСТРЕТИЛИ АЛЬТЕРНАТА:',RW/2,21,{align:'center',size:11,shadow:false});STEPS.forEach(([t0,s],i)=>{if(t>=t0)text(g,s,28,52+i*22,{size:11,color:'#141414',shadow:false})});
  if(t>66.5)text(g,'ОФИС ШЕРИФА ОКРУГА МАНДЕЛА',RW/2,RH-58,{align:'center',size:9,color:'#5a5a6a',shadow:false})}
function drawTvScreen(t){const g=tvG;if(t<77.4){g.fillStyle='#0a0e2a';g.fillRect(0,0,64,48);g.fillStyle='#a01010';g.fillRect(0,6,64,8);g.fillStyle='#ddd';g.fillRect(8,24,48,2);g.fillRect(12,30,40,2)}
  else{const k=t<80?'normal':t<84?'wrong1':'wrong2';const img=faceTex[k].image;g.fillStyle='#101418';g.fillRect(0,0,64,48);g.imageSmoothingEnabled=false;g.drawImage(img,12,0,40,40);g.fillStyle='#2a2a30';g.fillRect(14,40,36,8)}
  const d=g.getImageData(0,0,64,48),a=d.data,fr=Math.floor(t*FPS);for(let i=0;i<a.length;i+=4){const n=(hash(i,fr)-.5)*50;a[i]+=n;a[i+1]+=n;a[i+2]+=n}g.putImageData(d,0,0);tvTex.needsUpdate=true}

function only(g){street.visible=g===street;yard.visible=g===yard;lroom.visible=g===lroom;close.visible=g===close}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.6,osdOn=true;
  if(t<.6){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);text(ctx,'▶ PLAY',20,18,{size:16});osdOn=false}
  else if(t<6.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА, ВИСКОНСИН',RW/2,96,t,1.0,{align:'center',size:12});typed(ctx,'АРХИВНАЯ ЗАПИСЬ №1',RW/2,116,t,2.4,{align:'center',size:10,color:'#a0a0a0'})}
  else if(t<20.0){only(street);scene.fog.near=6;scene.fog.far=36;const k=P(t,6,20);cam([0,1.6,lerp(6,-6,k)],[0,1.5,-30]);farMan.visible=t>=17.6;farLamp.intensity=t>=17.6?8:0;
    lampLights.forEach((l,i)=>l.intensity=6*(i===1&&t>15&&hash(Math.floor(t*FPS),9)<.3?.2:1));pose(farMan,{face:'normal'});draw3D(scene,camera,ctx);dither(ctx)}
  else if(t<21.4){bars(ctx);osdOn=false}
  else if(t<34.0){alertCard(ctx,t)}
  else if(t<46.4){only(yard);scene.fog.near=8;scene.fog.far=30;const k=P(t,34,46.4);cam([lerp(-.3,0,k),1.55,lerp(2.6,1.0,k)],[lerp(.3,.8,k),1.35,-5]);
    pose(yMan,{face:'normal',hz:t>42.6?Math.min(.35,(t-42.6)*.25):0});draw3D(scene,camera,ctx);dither(ctx);
    if(t>=39.6){ctx.fillStyle='rgba(0,0,0,.55)';ctx.fillRect(8,30,150,76);text(ctx,'ПРИЗНАКИ:',14,36,{size:10,color:'#ffd060'});
      ['— ЛИЦО ПОЧТИ ТАКОЕ ЖЕ','— НЕ МОРГАЕТ','— УЛЫБКА ШИРЕ ОБЫЧНОГО','— СТОИТ И СМОТРИТ НА ДОМ'].forEach((s,i)=>{if(t>=39.8+i*1.5)text(ctx,s,14,52+i*12,{size:9})})}}
  else if(t<52.4){only(close);scene.fog.near=20;scene.fog.far=60;cHead.position.set(0,0,0);const face=t<48.2?'normal':t<50.4?'wrong1':'wrong2';pose(cHead,{face,hz:Math.sin(t*.8)*.05+(t>50.4?.18:0)});
    const k=P(t,46.4,52.4);cam([0,1.82,lerp(1.5,.75,eInOut(k))],[0,1.82,0]);draw3D(scene,camera,ctx);dither(ctx);vamt=t>50.4?1.4:.7}
  else if(t<72.0){stepsCard(ctx,t);if(t>69.2){vamt=2.5;if(t>70.6&&t<71.0){ctx.drawImage(faceTex.wrong2.image,96,56,128,128)}}}
  else if(t<88.0){only(lroom);scene.fog.near=10;scene.fog.far=40;drawTvScreen(t);roomL.intensity=3.5+hash(Math.floor(t*FPS),4)*1.5;const k=P(t,72,88);cam([lerp(.8,0,k),1.5,lerp(3.4,.6,eInOut(k))],[0,1.0,-3.4]);
    draw3D(scene,camera,ctx);dither(ctx);vamt=t>84?1.2:.6}
  else if(t<94.0){only(close);scene.fog.near=20;scene.fog.far=60;pose(cHead,{face:'wrong2',hz:.18+Math.sin(t*3)*.03});cam([0,1.82,lerp(.8,.62,P(t,88,94))],[0,1.82,0]);draw3D(scene,camera,ctx);dither(ctx);vamt=1.6+P(t,92,94)*2;
    if(Math.floor(t*3)%2)text(ctx,'ОТКРОЙ ДВЕРЬ',RW/2,30,{align:'center',size:14,color:'#ff3030'})}
  else{ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);snow(ctx,t,.25);ctx.fillStyle='#000';ctx.fillRect(60,104,200,30);text(ctx,'СИГНАЛ ПОТЕРЯН',RW/2,112,{align:'center',size:12});osdOn=false}
  if(osdOn)osd(ctx,t,t+14*60);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  vhs(ctx,t,vamt);
}
