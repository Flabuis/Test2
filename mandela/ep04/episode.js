// Том 4 «Помехи». Изъятые кассеты: на записях появляется то, чего не было при съёмке. Сигнал пытается захватить и наш телевизор.
// Своя история (семья Беккер — вымышленная).
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,vhs,dither,snow,makePerson,pose} from '../common/core.js';

export const VOL=4, D=118;
export const INTRO_HAND={blood:true,missing:1};   // интро: рука в крови, без указательного пальца
export const CAPS=[ // R — диктор, X — диктор с искажениями, S — замедляющееся предупреждение, A — альтернат
  [7.0,11.6,'R','Декабрь. Офис шерифа изымает видеокассеты по всему округу.'],
  [12.0,16.8,'R','На записях появляется то, чего не было при съёмке.'],
  [17.2,22.4,'R','Вот одна из изъятых плёнок. Семья Беккер, день рождения дочери.'],
  [36.4,41.4,'R','На празднике было четыре человека. На плёнке — пять.'],
  [41.8,46.6,'X','Беккеры не помнят, кто стоял у них за спиной.'],
  [48.4,51.2,'R','Немедленно выключите кассету.'],
  [51.6,58.0,'S','Немедленно выключите кассету.'],
  [60.4,64.8,'R','Изъятые кассеты хранили в подвале участка.'],
  [65.2,70.0,'X','Через неделю телевизоры в подвале включились сами.'],
  [70.4,73.4,'R','Никто не нажимал на воспроизведение.'],
  [73.8,80.0,'X','Дежурный, который их выключил, утром не пришёл на смену.'],
  [84.6,89.0,'R','Если кассета показывает то, чего не было —'],
  [89.4,93.4,'R','не досматривайте и не перематывайте назад.'],
  [93.8,97.6,'X','Извлеките её и сожгите.'],
  [100.4,103.6,'A','Досмотрите до конца.'],
  [105.0,109.4,'X','Если вы всё ещё смотрите эту запись —'],
  [110.0,113.6,'A','спасибо, что досмотрели.']];

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(58,RW/RH,.03,200);
const amb=new THREE.AmbientLight(0x707890,.4);scene.add(amb);scene.fog=new THREE.Fog(0x05070f,6,22);scene.background=new THREE.Color(0x05070f);
const N=(p,s,r=[1,1])=>tex(16,16,(g,w,h)=>noise(g,w,h,p,s),r);

// улыбка — то, что «захватывает» экраны (её же показывает наш телевизор в аутро)
export function smile(g,t,w=RW,h=RH,k=1){g.fillStyle='#000';g.fillRect(0,0,w,h);const cx=w/2,cy=h*.55,R=w*.36*k,th=Math.max(2,Math.round(h*.06*k)),fr=Math.floor(t*FPS);
  for(let a=-1;a<=1.001;a+=.02){const x=cx+Math.sin(a*1.2)*R,y=cy+(1-Math.cos(a*1.2))*R*-.55+R*.12;g.fillStyle='#f0ece0';g.fillRect(Math.round(x),Math.round(y),Math.max(1,Math.round(w/90)),th)}
  g.fillStyle='#000';for(let i=-6;i<=6;i++){const a=i/6.5,x=cx+Math.sin(a*1.2)*R,y=cy+(1-Math.cos(a*1.2))*R*-.55+R*.12;g.fillRect(Math.round(x),Math.round(y),Math.max(1,Math.round(w/160)),th)}
  if(hash(fr,11)<.15){const d=g.getImageData(0,0,w,h);const a=d.data;for(let i=0;i<a.length;i+=4){const v=hash(i,fr)*120;a[i]+=v;a[i+1]+=v;a[i+2]+=v}g.putImageData(d,0,0)}}

// ---------- подвал с уликами ----------
const base=new THREE.Group();scene.add(base);const bulbL=new THREE.PointLight(0xffe0a0,6,9,1.3);const bulb=new THREE.Group();const tvs=[];
function screenCanvas(w=64,h=48){const c=document.createElement('canvas');c.width=w;c.height=h;const tx=new THREE.CanvasTexture(c);tx.magFilter=tx.minFilter=THREE.NearestFilter;tx.generateMipmaps=false;tx.colorSpace=THREE.SRGBColorSpace;return{c,g:c.getContext('2d'),tx}}
function makeTV(){const g=new THREE.Group();const b=box(.7,.56,.55,M({map:N(['#2a2a2c','#262628'],100)}));g.add(b);const s=screenCanvas();const sc=new THREE.Mesh(new THREE.PlaneGeometry(.5,.38),new THREE.MeshBasicMaterial({map:s.tx,toneMapped:false,fog:false}));sc.position.z=.281;g.add(sc);
  const l=new THREE.PointLight(0xd0e0ff,0,3,1.4);l.position.z=.6;g.add(l);g.userData={s,l};return g}
{const conc=N(['#4a4a4c','#454547','#505052'],101,[4,2]);const fl=box(10,.05,10,M({map:N(['#3a3a3c','#363638','#404042'],102,[6,6])}));base.add(fl);
 for(const [w,d,x,z] of[[10,.1,0,-3],[.1,10,-4,0],[.1,10,4,0]]){const b=box(w,3,d,M({map:conc}));b.position.set(x,1.5,z);base.add(b)}const ce=box(10,.05,10,M({color:0x2a2a2c}));ce.position.y=3;base.add(ce);
 const tagM=M({color:0xe8e0c8}),tapeM=M({map:N(['#141416','#18181a'],103)});const r=mulberry(104);
 for(const sx of[-3.4,3.4])for(let lv=0;lv<4;lv++){const sh=box(.6,.04,3.6,M({color:0x6a6a6e}));sh.position.set(sx,.3+lv*.62,-.8);base.add(sh);
   for(let k=0;k<16;k++){if(r()<.15)continue;const tp=box(.12,.2,.34,tapeM);tp.position.set(sx+(sx<0?.1:-.1),.42+lv*.62,-2.4+k*.21);tp.rotation.y=(r()-.5)*.1;base.add(tp);const tg=box(.004,.06,.08,tagM);tg.position.set(sx+(sx<0?.165:-.165),.4+lv*.62,-2.4+k*.21);base.add(tg)}}
 const desk=box(1.6,.06,.8,M({color:0x5a4a3a}));desk.position.set(0,.76,-2.2);base.add(desk);const dl=box(1.5,.76,.7,M({color:0x4a3a2a}));dl.position.set(0,.38,-2.2);base.add(dl);
 for(let i=0;i<3;i++){const tv=makeTV();tv.position.set(-1.0+i*1.0,1.1+(i===1?.0:0),-2.3);tv.rotation.y=(i-1)*-.12;base.add(tv);tvs.push(tv)}
 const vcr=box(.6,.1,.4,M({color:0x1a1a1c}));vcr.position.set(0,.84,-1.9);base.add(vcr);
 const cord=box(.01,.8,.01,M({color:0x101010}));cord.position.y=-.4;bulb.add(cord);const bm=new THREE.Mesh(new THREE.IcosahedronGeometry(.06,0),new THREE.MeshBasicMaterial({color:0xfff0c0}));bm.position.y=-.85;bulb.add(bm);
 bulbL.position.y=-.9;bulb.add(bulbL);bulb.position.set(0,3,-.4);base.add(bulb)}

// ---------- день рождения у Беккеров ----------
const party=new THREE.Group();scene.add(party);const flames=[];let fifth;const fam=[];
{const wp=tex(16,16,(g,w,h)=>{noise(g,w,h,['#c8b890','#c0b088','#d0c098'],110);g.fillStyle='rgba(160,60,60,.25)';for(let x=0;x<w;x+=5)g.fillRect(x,0,2,h)},[6,2]);
 const fl=box(10,.05,10,M({map:N(['#6a4a30','#624428'],111,[6,6])}));party.add(fl);for(const [w,d,x,z] of[[10,.1,0,-2.4],[.1,10,-4,0],[.1,10,4,0]]){const b=box(w,3,d,M({map:wp}));b.position.set(x,1.5,z);party.add(b)}
 const tbl=box(2.2,.08,1.1,M({color:0xe8e4e0}));tbl.position.set(0,.76,0);party.add(tbl);const tl=box(2.0,.72,.9,M({color:0x6a4a30}));tl.position.set(0,.36,0);party.add(tl);
 const cake=new THREE.Mesh(new THREE.CylinderGeometry(.22,.22,.18,10),M({color:0xf4e8f0}));cake.position.set(0,.89,.1);party.add(cake);const ic=new THREE.Mesh(new THREE.CylinderGeometry(.225,.225,.04,10),M({color:0xe080a0}));ic.position.set(0,.97,.1);party.add(ic);
 for(let i=0;i<7;i++){const a=i/7*Math.PI*2;const c=box(.015,.08,.015,M({color:0x80b0e0}));c.position.set(Math.cos(a)*.14,1.03,.1+Math.sin(a)*.14);party.add(c);
   const f=new THREE.Mesh(new THREE.ConeGeometry(.012,.04,4),new THREE.MeshBasicMaterial({color:0xffd060,fog:false}));f.position.set(Math.cos(a)*.14,1.09,.1+Math.sin(a)*.14);party.add(f);flames.push(f)}
 const cl=new THREE.PointLight(0xffc070,2.5,4,1.4);cl.position.set(0,1.3,.2);party.add(cl);const roomL=new THREE.PointLight(0xfff0d0,3,8,1.3);roomL.position.set(1.5,2.6,1.8);party.add(roomL);
 const face=(seed,hair,mouth='#8a4a3a')=>(g,w,h)=>{noise(g,w,h,['#e0b898','#d8b090'],seed);g.fillStyle=hair;g.fillRect(0,0,16,3);g.fillStyle='#1a1a1a';g.fillRect(4,7,2,2);g.fillRect(10,7,2,2);g.fillStyle=mouth;g.fillRect(5,11,6,1)};
 const hatM=[0xe04060,0x40a0e0,0xe0c040,0x60c060];
 [[-.65,-.55,1,['#4a5a7a','#425272'],'#3a2a1e'],[.65,-.55,1,['#a04a5a','#984252'],'#7a5030'],[-.25,-.6,.7,['#e0a0c0','#d898b8'],'#c8a060'],[.3,-.6,.7,['#60a060','#589858'],'#3a2a1e']].forEach(([x,z,sc,shirt,hair],i)=>{
   const p=makePerson({shirt,hair:[hair,hair],faces:{normal:face(120+i,hair)}});p.scale.setScalar(sc);p.position.set(x,sc<1?.18:-.25,z);party.add(p);pose(p,{face:'normal',l0:-1.4,l1:-1.4,ax0:-1.0,ax1:-1.0});
   const hat=new THREE.Mesh(new THREE.ConeGeometry(.12,.28,6),M({color:hatM[i]}));hat.position.y=.62;p.userData.head.add(hat);fam.push(p)});
 fifth=makePerson({shirt:['#2a2a2e','#26262a'],pants:['#2a2a2e','#26262a'],faceSize:32,faces:{normal:(g,w,h)=>{noise(g,w,h,['#e0dcd4','#d8d4cc'],130);g.fillStyle='#2a2a2a';g.fillRect(0,0,32,5);
   g.fillStyle='#000';g.fillRect(8,12,4,4);g.fillRect(20,12,4,4);g.fillStyle='#200404';g.fillRect(4,21,24,4);g.fillStyle='#f0ece0';for(let x=5;x<28;x+=2)g.fillRect(x,22,1,2)}}});
 fifth.scale.setScalar(1.08);fifth.position.set(0,0,-1.5);party.add(fifth)}

// ---------- 2D ----------
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
function osdVHS(g,t){text(g,'PLAY ▶',12,10,{size:10});text(g,'ДЕК 19 1991',RW-12,10,{align:'right',size:9});const s=Math.floor(t)+(t>=58.6?3600*2:0);
  text(g,`${String(14+Math.floor(s/3600)).padStart(2,'0')}:${String(10+Math.floor(s/60)%50).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function osdHome(g,t){text(g,'▶',12,10,{size:10});text(g,'12.12.91',12,RH-36,{size:9});const s=Math.floor((t-22.6)*1);text(g,`18:40:${String(12+s).padStart(2,'0')}`,RW-12,RH-36,{align:'right',size:9})}
function warning(g,t){const k=P(t,51.6,58.0);g.fillStyle=Math.floor(t*(4-3*k))%2?'#900000':'#300000';g.fillRect(0,0,RW,RH);
  const s='НЕМЕДЛЕННО ВЫКЛЮЧИТЕ КАССЕТУ';const sp=lerp(9,15,eIn(k)),x0=RW/2-sp*(s.length-1)/2;
  for(let i=0;i<s.length;i++){const dy=Math.round(Math.sin(i*.7+t*(6-5*k))*k*6);text(g,s[i],Math.round(x0+i*sp),100+dy,{size:k>.6?13:11,align:'center',color:k>.7?'#c0b0b0':'#ffffff'})}
  g.fillStyle='#ffd060';g.beginPath();g.moveTo(RW/2,42);g.lineTo(RW/2+18,74);g.lineTo(RW/2-18,74);g.closePath();g.fill();text(g,'!',RW/2,52,{align:'center',size:18,color:'#300000',shadow:false});if(t>=51.6)text(g,'СИГНАЛ ОКРУГА МАНДЕЛА',RW/2,150,{align:'center',size:9,color:'#d0a0a0'})}
const STEPS=[[84.8,'— НЕ ДОСМАТРИВАЙТЕ.'],[89.4,'— НЕ ПЕРЕМАТЫВАЙТЕ НАЗАД.'],[93.8,'— ИЗВЛЕКИТЕ И СОЖГИТЕ.']];
function card(g,t){const hijack=t>=98.2&&t<100.6||(t>=100.6&&Math.floor(t*FPS)%5===0);g.fillStyle='#1a2a5a';g.fillRect(0,0,RW,RH);g.fillStyle='#e8e4d8';g.fillRect(14,14,RW-28,RH-50);g.fillStyle='#1a2a5a';g.fillRect(14,14,RW-28,24);
  text(g,'ЗАПИСИ С ПОСТОРОННИМИ',RW/2,21,{align:'center',size:12,shadow:false});
  if(!hijack){typed(g,'ЕСЛИ КАССЕТА ПОКАЗЫВАЕТ ТО, ЧЕГО НЕ БЫЛО:',RW/2,50,t,84.6,{align:'center',size:9,color:'#141414',shadow:false});STEPS.forEach(([t0,s],i)=>{if(t>=t0)text(g,s,34,78+i*24,{size:11,color:'#141414',shadow:false})})}
  else{text(g,'— ДОСМОТРИТЕ ДО КОНЦА.',34,78,{size:11,color:'#141414',shadow:false});text(g,'— ДОСМОТРИТЕ ДО КОНЦА.',34,102,{size:11,color:'#141414',shadow:false});text(g,'— ДОСМОТРИТЕ ДО КОНЦА.',34,126,{size:11,color:'#7a0a0a',shadow:false})}}

function only(g){base.visible=g===base;party.visible=g===party}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}
const pv=new THREE.Vector3();function proj(x,y,z){pv.set(x,y,z).project(camera);return[Math.round((pv.x*.5+.5)*RW),Math.round((-pv.y*.5+.5)*RH)]}
function ring(g,x,y,r,c){g.strokeStyle=c;g.lineWidth=2;g.beginPath();g.ellipse(x,y,r,r*1.1,0,0,7);g.stroke()}

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.6,mode='vhs';
  if(t<.6){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);text(ctx,'▶ PLAY',20,18,{size:16});mode='none'}
  else if(t<6.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА, ВИСКОНСИН',RW/2,96,t,1.0,{align:'center',size:12});
    const g=t>4.4&&t<4.8;typed(ctx,g?'ВЫ СМОТРИТЕ ЭТУ ЗАПИСЬ':'АРХИВНАЯ ЗАПИСЬ №4',RW/2,116,t,2.4,{align:'center',size:10,color:g?'#ff4040':'#a0a0a0'});if(g)vamt=2.5}
  else if(t<22.6||(t>=58.6&&t<84)){only(base);scene.fog.near=6;scene.fog.far=22;const sw=Math.sin(t*1.3)*.12;bulb.rotation.set(sw*.3,0,sw);bulbL.intensity=6*(hash(Math.floor(t*FPS),3)<.04?.3:1);
    tvs.forEach((tv,i)=>{const on=t>=66.2+i*.6&&t<79.6||(t>=79.6&&i===1);tv.userData.l.intensity=on?1.4:0;if(on)smile(tv.userData.s.g,t+i,64,48,.9);else{const g=tv.userData.s.g;g.fillStyle='#0a0c0e';g.fillRect(0,0,64,48)}tv.userData.s.tx.needsUpdate=true});
    if(t<22.6){const k=P(t,6,22.6);cam([lerp(1.6,.4,k),1.6,lerp(3.2,1.2,k)],[lerp(-3,0,k),1.1,-2.2])}
    else if(t<66){const k=P(t,58.6,66);cam([lerp(-2.4,-1.0,k),1.3,lerp(1.6,.8,k)],[-3.4,1.2,-1.4])}
    else{const k=P(t,66,84);cam([lerp(.6,0,k),1.35,lerp(1.4,.2,eInOut(k))],[0,1.1,-2.3]);vamt=t>78?.6+P(t,78,84)*1.5:.7}
    draw3D(scene,camera,ctx);dither(ctx)}
  else if(t<48.0){only(party);mode='home';scene.fog.near=8;scene.fog.far=20;flames.forEach((f,i)=>f.scale.set(1,.8+hash(i,Math.floor(t*FPS))*.6,1));
    fam.forEach((p,i)=>pose(p,{face:'normal',l0:-1.4,l1:-1.4,ax0:-1.0+Math.sin(t*3+i)*.15*(t<34),ax1:-1.0,hy:t<34?Math.sin(t*1.1+i*2)*.3:0}));
    const turn=P(t,44.6,46.0);pose(fifth,{face:'normal',hy:lerp(-.5,0,turn),hz:turn*.12});
    const freeze=t>=34.0&&t<44.4;const tt=freeze?34.0:t;const hk=Math.sin(tt*2.3)*.04;
    cam([lerp(-.4,.4,P(tt,22.6,34))+hk,1.55+Math.sin(tt*3.1)*.02,2.3],[0,1.25,-.5]);draw3D(scene,camera,ctx);dither(ctx);
    if(freeze){ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(0,0,RW,RH);text(ctx,'II ПАУЗА',12,24,{size:10});
      fam.forEach((p,i)=>{if(t<34.6+i*.5)return;p.userData.head.updateMatrixWorld();const hp=new THREE.Vector3().setFromMatrixPosition(p.userData.head.matrixWorld);const [x,y]=proj(hp.x,hp.y+.18,hp.z);ring(ctx,x,y,14,'#ff3030');text(ctx,String(i+1),x+12,y-20,{size:10,color:'#ff3030'})});
      if(t>=37.4){fifth.userData.head.updateMatrixWorld();const hp=new THREE.Vector3().setFromMatrixPosition(fifth.userData.head.matrixWorld);const [x,y]=proj(hp.x,hp.y+.2,hp.z);if(Math.floor(t*3)%2)ring(ctx,x,y,16,'#ffd060');text(ctx,'5?',x+14,y-22,{size:11,color:'#ffd060'})}}
    vamt=t>45?1.4:.6}
  else if(t<58.0){warning(ctx,t);mode='none';vamt=1+P(t,51.6,58)*2.5}
  else if(t<58.6){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);snow(ctx,t,.6);text(ctx,'◀◀',RW-30,12,{size:12});mode='none';vamt=3}
  else if(t<104.0){card(ctx,t);vamt=(t>=98.2&&t<100.6)?2.2:.6}
  else{ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);if(t<110){typed(ctx,'ЕСЛИ ВЫ ВСЁ ЕЩЁ СМОТРИТЕ',RW/2,104,t,105.0,{align:'center',size:11})}
    else{smile(ctx,t,RW,RH,P(t,110,113.6)*.9+.1);vamt=1.2}mode=t<110?'vhs':'none'}
  if(mode==='vhs')osdVHS(ctx,t);if(mode==='home')osdHome(ctx,t);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  vhs(ctx,t,vamt)}

// аутро: телевизор выбрасывает кассету, и на нашем экране — улыбка
export function outroScreen(t,g){smile(g,t,RW,RH,clamp(P(t,2.9,4.2)*.9+.1))}
