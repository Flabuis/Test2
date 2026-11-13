// Том 3 «Автоответчик». Альтернаты звонят голосами тех, кого больше нет. Своя история (Эмма Коул — вымышленная).
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,vhs,dither,snow,makePerson,pose} from '../common/core.js';

export const VOL=3, D=118;
export const INTRO_CUT=8.05;   // интро: рука пропадает на склейке, кассета вставляется сама
export const CAPS=[ // R — диктор, F — «мама» по телефону, W — «мама», голос уже не тот
  [7.0,11.4,'R','Альтернаты не всегда стучат в дверь. Иногда они звонят.'],
  [11.8,16.4,'R','Голос они берут у тех, кого с нами больше нет.'],
  [16.8,19.8,'R','Это плёнка из автоответчика Эммы Коул.'],
  [20.6,25.0,'F','Привет, солнышко. Это мама. Перезвони, когда сможешь.'],
  [25.6,30.4,'R','Мать Эммы умерла за две недели до этого звонка.'],
  [31.4,36.2,'F','Солнышко, ты дома? Я стою у тебя под дверью. Открой маме.'],
  [37.2,42.0,'W','Почему ты не открываешь? Мама замёрзла. Мама видит свет.'],
  [47.6,51.6,'W','Открой. Открой. Открой.'],
  [52.6,55.6,'R','Камера над входом. Той же ночью.'],
  [78.6,83.0,'R','Не отвечайте на звонки после полуночи.'],
  [83.4,87.6,'R','Не перезванивайте на номера тех, кого больше нет.'],
  [88.0,92.4,'R','Не задавайте проверочных вопросов.'],
  [92.8,95.8,'R','Они знают ответы.'],
  [105.0,108.6,'F','Привет, солнышко. Это мама.']];
const MSG=[[20.0,'1/4','ВТ 21:04'],[30.8,'2/4','ВТ 23:52'],[36.6,'3/4','СР 01:13'],[42.4,'4/4','СР 03:36'],[104.4,'5/5','СЕЙЧАС']];
const RINGS=[96.6,99.1,101.6];

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(58,RW/RH,.03,200);
const amb=new THREE.AmbientLight(0x6070a0,.4);scene.add(amb);scene.fog=new THREE.Fog(0x05070f,6,30);scene.background=new THREE.Color(0x05070f);
const N=(p,s,r=[1,1])=>tex(16,16,(g,w,h)=>noise(g,w,h,p,s),r);

// ---------- кухня с автоответчиком ----------
const kitchen=new THREE.Group();scene.add(kitchen);const reels=[],ledM=new THREE.MeshBasicMaterial({color:0xff2020});let handset;
const dispC=document.createElement('canvas');dispC.width=48;dispC.height=16;const dispG=dispC.getContext('2d');
const dispTex=new THREE.CanvasTexture(dispC);dispTex.magFilter=dispTex.minFilter=THREE.NearestFilter;dispTex.generateMipmaps=false;
const lampK=new THREE.PointLight(0xffd8a0,2.2,5,1.4);
{const tbl=box(2.4,.08,1.2,M({map:N(['#6a4a30','#624428','#704e34'],70)}));tbl.position.set(0,.76,0);kitchen.add(tbl);for(const [x,z] of[[-1.1,-.5],[1.1,-.5],[-1.1,.5],[1.1,.5]]){const l=box(.06,.76,.06,M({color:0x4a3220}));l.position.set(x,.38,z);kitchen.add(l)}
 const wall=box(6,3,.1,M({map:tex(16,16,(g,w,h)=>{noise(g,w,h,['#5a5a48','#545442','#60604e'],71);g.fillStyle='rgba(255,255,255,.08)';for(let y=0;y<h;y+=4)for(let x=(y/4%2)*2;x<w;x+=4)g.fillRect(x,y,2,2)},[6,3])}));wall.position.set(0,1.5,-.7);kitchen.add(wall);
 const fl=box(6,.05,6,M({map:N(['#3a3430','#36302c','#3e3834'],72,[6,6])}));kitchen.add(fl);
 // автоответчик
 const am=new THREE.Group();const body=box(.5,.12,.34,M({map:N(['#2a2a2c','#262628','#2e2e30'],73)}));body.position.y=.06;am.add(body);
 const win=box(.22,.01,.12,new THREE.MeshBasicMaterial({color:0x101014}));win.position.set(-.08,.121,.0);am.add(win);
 for(const x of[-.13,-.03]){const r=new THREE.Group();const rr=new THREE.Mesh(new THREE.CylinderGeometry(.035,.035,.012,8),M({color:0xd8d8d8}));r.add(rr);const sp=box(.06,.014,.012,M({color:0x202020}));r.add(sp);r.position.set(x,.128,0);am.add(r);reels.push(r)}
 const led=box(.025,.012,.025,ledM);led.position.set(.16,.126,-.08);am.add(led);
 const disp=new THREE.Mesh(new THREE.PlaneGeometry(.14,.045),new THREE.MeshBasicMaterial({map:dispTex}));disp.rotation.x=-Math.PI/2;disp.position.set(.14,.122,.07);am.add(disp);
 for(let i=0;i<4;i++){const b=box(.04,.012,.03,M({color:0x505054}));b.position.set(-.18+i*.06,.126,.13);am.add(b)}
 am.position.set(.1,.8,0);kitchen.add(am);
 // телефон
 const ph=new THREE.Group();const pb=box(.26,.1,.3,M({color:0xa8a090}));pb.position.y=.05;ph.add(pb);const dial=new THREE.Mesh(new THREE.CylinderGeometry(.08,.08,.02,10),M({color:0xd8d0c0}));dial.position.set(0,.11,.05);ph.add(dial);
 handset=new THREE.Group();const hs=box(.34,.06,.08,M({color:0xa8a090}));handset.add(hs);for(const s of[-1,1]){const e=box(.08,.06,.1,M({color:0xa8a090}));e.position.set(s*.15,-.03,0);handset.add(e)}handset.position.set(0,.15,-.08);ph.add(handset);
 ph.position.set(-.55,.8,.05);ph.rotation.y=.2;kitchen.add(ph);
 const cup=new THREE.Mesh(new THREE.CylinderGeometry(.05,.04,.1,7),M({color:0xe8e0d0}));cup.position.set(.7,.85,.2);kitchen.add(cup);
 lampK.position.set(.6,1.6,.8);kitchen.add(lampK)}
function setDisp(s){dispG.fillStyle='#200404';dispG.fillRect(0,0,48,16);dispG.fillStyle='#ff4030';dispG.font='bold 11px monospace';dispG.fillText(s,4,12);dispTex.needsUpdate=true}

// ---------- вход в дом: камера наблюдения ----------
const porch=new THREE.Group();scene.add(porch);let door,mom,momC;
const porchL=new THREE.PointLight(0xfff0d0,9,9,1.3);
{const sn=box(30,.05,30,M({map:N(['#d8dce4','#d0d4dc','#e0e4ec'],80,[10,10])}));sn.position.set(0,0,8);porch.add(sn);
 const wallP=box(8,4,.2,M({map:tex(16,16,(g,w,h)=>{noise(g,w,h,['#7a7468','#726c60','#827c70'],81);g.fillStyle='rgba(0,0,0,.3)';for(let y=0;y<h;y+=3)g.fillRect(0,y,w,1)},[4,2])}));wallP.position.set(0,2,-.1);porch.add(wallP);
 const deck=box(3,.3,1.6,M({map:N(['#5a4a3a','#524234','#625240'],82)}));deck.position.set(0,.15,.8);porch.add(deck);for(let i=0;i<2;i++){const st=box(1.2,.15,.35,M({color:0x5a4a3a}));st.position.set(0,.075+i*0,1.8+i*.0);porch.add(st)}
 door=new THREE.Group();const dm=box(.95,2.0,.06,M({color:0x3a2a1e}));dm.position.x=.475;door.add(dm);const knob=box(.05,.05,.06,M({color:0xc8b060}));knob.position.set(.85,1.0,.05);door.add(knob);door.position.set(-.475,1.3,.02);porch.add(door);
 const dark=box(.95,2.0,.02,new THREE.MeshBasicMaterial({color:0x020202}));dark.position.set(0,1.3,-.01);porch.add(dark);
 const lamp=box(.2,.25,.15,new THREE.MeshBasicMaterial({color:0xfff4d8}));lamp.position.set(.9,2.6,.1);porch.add(lamp);porchL.position.set(.9,2.5,.6);porch.add(porchL);
 for(const x of[-5,6]){const t=new THREE.Mesh(new THREE.ConeGeometry(1.4,5,6),M({map:N(['#1a2a1e','#162618','#1e2e22'],83)}));t.position.set(x,2.5,9);porch.add(t)}
 const fence=box(12,.8,.08,M({color:0x6a6a60}));fence.position.set(0,.4,11);porch.add(fence)}
// «мама»: женщина в тёмном пальто, длинные волосы
const momFaces={normal:(g,w,h)=>{noise(g,w,h,['#d8b4a0','#d0ac98'],90);g.fillStyle='#6a5040';g.fillRect(0,0,32,7);g.fillRect(0,7,4,14);g.fillRect(28,7,4,14);g.fillStyle='#2a1a12';g.fillRect(9,13,5,2);g.fillRect(18,13,5,2);g.fillStyle='#8a5a50';g.fillRect(12,23,8,1)},
  up:(g,w,h)=>{noise(g,w,h,['#e0dcd8','#d8d4d0','#ccc8c4'],91);g.fillStyle='#6a5040';g.fillRect(0,0,32,4);g.fillRect(0,4,3,26);g.fillRect(29,4,3,26);g.fillRect(3,4,3,6);g.fillRect(26,4,3,6);
    g.fillStyle='#000';g.fillRect(6,10,8,8);g.fillRect(18,10,8,8);g.fillStyle='#fff';g.fillRect(9,13,1,1);g.fillRect(21,13,1,1);g.fillStyle='rgba(60,30,30,.5)';g.fillRect(6,18,8,2);g.fillRect(18,18,8,2);
    g.fillStyle='#100202';g.fillRect(13,21,6,9);g.fillRect(12,22,1,6);g.fillRect(19,22,1,6)}};
function makeMom(){const p=makePerson({shirt:['#2a2a30','#24242a'],pants:['#2a2a30','#24242a'],hair:['#6a5040','#5e4636'],skin:['#d8b4a0','#d0ac98'],faces:momFaces,faceSize:32});
  const hm=M({map:N(['#6a5040','#5e4636'],92)});const back=box(.42,.6,.08,hm);back.position.set(0,.05,-.2);p.userData.head.add(back);
  const coat=box(.62,.9,.36,M({map:N(['#2a2a30','#24242a'],93)}));coat.position.y=.85;p.add(coat);return p}
mom=makeMom();porch.add(mom);
// следы на снегу от забора к двери — копятся от кадра к кадру
const tracks=[];{const tm=new THREE.MeshBasicMaterial({color:0x3a3e48});for(let i=0;i<22;i++){const z=10.4-i*.44,x=.8-.8*(i/21)+(i%2?.12:-.12);const f=box(.12,.01,.22,tm);f.position.set(x,.03,z);porch.add(f);tracks.push([f,z>7.6?56:z>5.6?60:z>2.6?64:68])}}momC=makeMom();scene.add(momC);const upL=new THREE.PointLight(0xfff0d0,0,5,1.3);upL.position.set(.3,2.9,.6);scene.add(upL);

// ---------- 2D ----------
function osdVHS(g,t){text(g,'PLAY ▶',12,10,{size:10});text(g,'ДЕК 03 1991',RW-12,10,{align:'right',size:9});const s=Math.floor(t);text(g,`09:${String(40+Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
// камера наблюдения: ч/б, контраст, зерно
function cctv(g,t,stamp){const d=g.getImageData(0,0,RW,RH),a=d.data,fr=Math.floor(t*FPS);for(let i=0;i<a.length;i+=4){let v=(a[i]*.3+a[i+1]*.59+a[i+2]*.11);v=clamp((v-20)*1.35,0,255)+(hash(i,fr)-.5)*34;a[i]=a[i+1]=a[i+2]=v}g.putImageData(d,0,0);
  g.fillStyle='rgba(0,0,0,.25)';for(let y=0;y<RH;y+=2)g.fillRect(0,y,RW,1);text(g,'CAM 02  ВХОД',10,10,{size:10});text(g,'СР 04.12.91',RW-10,10,{size:10,align:'right'});text(g,stamp,RW-10,22,{size:10,align:'right'})}
const STEPS=[[78.8,'— НЕ ОТВЕЧАЙТЕ НА ЗВОНКИ ПОСЛЕ ПОЛУНОЧИ.'],[83.4,'— НЕ ПЕРЕЗВАНИВАЙТЕ УМЕРШИМ.'],[88.0,'— НЕ ЗАДАВАЙТЕ ПРОВЕРОЧНЫХ ВОПРОСОВ.']];
function psa(g,t){g.fillStyle='#1a2a5a';g.fillRect(0,0,RW,RH);g.fillStyle='#e8e4d8';g.fillRect(14,14,RW-28,RH-50);g.fillStyle='#1a2a5a';g.fillRect(14,14,RW-28,24);
  text(g,'ЗВОНКИ ОТ БЛИЗКИХ',RW/2,21,{align:'center',size:12,shadow:false});STEPS.forEach(([t0,s],i)=>{if(t>=t0)text(g,s,24,56+i*24,{size:10,color:'#141414',shadow:false})});
  if(t>=92.8){const on=Math.floor(t*3)%2;text(g,'ОНИ ЗНАЮТ ОТВЕТЫ.',RW/2,140,{align:'center',size:14,color:on?'#a01010':'#141414',shadow:false})}}

function only(g){kitchen.visible=g===kitchen;porch.visible=g===porch;momC.visible=false;upL.intensity=0}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}
const STAMPS=[[52,'01:13:07',null],[56,'01:47:31',[.8,7.6,Math.PI]],[60,'02:20:12',[.3,5.6,Math.PI+.1]],[64,'02:58:44',[0,2.6,Math.PI]],[68,'03:36:02',[0,1.0,Math.PI]],[72,'03:36:40','up']];

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.6,mode='vhs';
  if(t<.6){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);text(ctx,'▶ PLAY',20,18,{size:16});mode='none'}
  else if(t<6.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА, ВИСКОНСИН',RW/2,96,t,1.0,{align:'center',size:12});typed(ctx,'АРХИВНАЯ ЗАПИСЬ №3',RW/2,116,t,2.4,{align:'center',size:10,color:'#a0a0a0'})}
  else if(t<52.0||(t>=96&&t<112)){only(kitchen);scene.fog.near=4;scene.fog.far=14;
    // сообщение, которое сейчас играет
    const cur=MSG.filter(m=>t>=m[0]).pop();const playing=cur&&t<(cur[0]===42.4?51.8:cur[0]===104.4?111.8:cur[0]+5.6);
    setDisp(cur?(playing?cur[1]:'0'+(MSG.indexOf(cur)<3?String(4-MSG.indexOf(cur)-1):'')):'4');if(cur&&playing)setDisp(cur[1]);
    reels.forEach((r,i)=>r.rotation.y=playing?t*(6+i*2):0);ledM.color.set(playing?0xff2020:(Math.floor(t*2)%2?0xff2020:0x300000));
    let rk=0;for(const r0 of RINGS)if(t>=r0&&t<r0+1.4)rk=1;handset.position.y=.15+(rk?Math.abs(Math.sin(t*60))*.012:0);handset.rotation.z=rk?Math.sin(t*50)*.03:0;
    lampK.intensity=t>=96?.9:2.2;
    if(t<20)cam([lerp(.9,.55,P(t,6,20)),1.25,lerp(1.4,.9,P(t,6,20))],[0,.85,0]);
    else if(t<52){const k=P(t,20,52);cam([lerp(.45,.28,k),lerp(1.15,1.05,k),lerp(.62,.42,k)],[.12,.82,0]);vamt=t>42.4?.6+P(t,42.4,51.6)*1.6:.6}
    else{const k=P(t,96,112);cam([lerp(-.1,.2,k),lerp(1.3,1.05,k),lerp(1.2,.5,k)],[-.2,.85,0]);vamt=.7}
    draw3D(scene,camera,ctx);dither(ctx);
    if(t>=43.0&&t<47.4){ctx.fillStyle='rgba(0,0,0,.5)';ctx.fillRect(110,40,100,16);text(ctx,'...ДЫХАНИЕ...',RW/2,43,{align:'center',size:9,color:'#c0c0c0'})}
    if(t>=96&&t<104.2){ctx.fillStyle='rgba(0,0,0,.6)';ctx.fillRect(60,30,200,22);if(Math.floor(t*2)%2)text(ctx,'НЕ БЕРИТЕ ТРУБКУ',RW/2,34,{align:'center',size:13,color:'#ff3030'})}}
  else if(t<78.0||t>=112){only(porch);mode='cctv';scene.fog.near=10;scene.fog.far=40;scene.background.set(0x000000);
    const st=t>=112?[112,'03:41:15','open']:STAMPS.filter(s=>t>=s[0]).pop();mom.visible=false;door.rotation.y=st[2]==='open'?-1.3:0;porchL.intensity=9*(t>=112&&Math.floor(t*FPS)%7===0?.3:1);
    if(st[2]==='up'){only(kitchen);kitchen.visible=false;momC.visible=true;momC.position.set(0,0,0);pose(momC,{face:'up',hx:-1.1,hz:.25});scene.fog.near=20;
      camera.fov=58;camera.updateProjectionMatrix();upL.intensity=4;cam([0,2.55+Math.sin(t*.7)*.01,.5],[0,1.8,.05]);vamt=1.0+P(t,74.5,77.8)*2}
    else{if(Array.isArray(st[2])){const [x,z,ry]=st[2];mom.visible=true;mom.position.set(x,z<1.7?.3:0,z);mom.rotation.y=ry;pose(mom,{face:'normal',hz:st[0]===64?.35:0})}
      cam([.9,2.9,.35],[-.3,0,6])}
    amb.intensity=1.1;tracks.forEach(([tr,ti])=>tr.visible=t>=112||t>=ti);if(st[2]==='up')tracks.forEach(([tr])=>tr.visible=false);
    draw3D(scene,camera,ctx);cctv(ctx,t,st[1]);amb.intensity=.4;
    if(t>=112&&Math.floor(t*2)%2){ctx.fillStyle='#000';ctx.fillRect(RW/2-84,RH/2-10,168,20);text(ctx,'ДАТЧИК ДВЕРИ: ОТКРЫТА',RW/2,RH/2-6,{align:'center',size:11,color:'#ff3030'})}
    if(t>=75.0&&t<78.0&&Math.floor(t*FPS)%4===0)snow(ctx,t,.5)}
  else if(t<96.0){psa(ctx,t);for(const f of[85.9,90.3])if(t>=f&&t<f+.14){only(kitchen);kitchen.visible=false;momC.visible=true;pose(momC,{face:'up',hx:-1.1});upL.intensity=4;cam([0,2.55,.5],[0,1.8,.05]);draw3D(scene,camera,ctx);cctv(ctx,t,'');vamt=2}}
  else{}
  if(mode==='vhs')osdVHS(ctx,t);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  // табличка сообщения автоответчика
  const cur=MSG.find(m=>t>=m[0]&&t<m[0]+1.8);if(cur&&(t<52||t>=96)){ctx.fillStyle='rgba(0,0,0,.6)';ctx.fillRect(8,30,124,30);text(ctx,`СООБЩЕНИЕ ${cur[1]}`,14,34,{size:10,color:'#ff6050'});text(ctx,cur[2],14,46,{size:9})}
  vhs(ctx,t,vamt)}

// крючок интро: после склейки за полкой с кассетами стоит тёмный человек с красными глазами
const watcher=new THREE.Group();{const dk=M({color:0x060608});const b=box(.5,1.4,.3,dk);b.position.y=1.0;watcher.add(b);const sh=box(.7,.2,.3,dk);sh.position.y=1.65;watcher.add(sh);
  const hd=box(.3,.36,.3,dk);hd.position.y=1.95;watcher.add(hd);for(const s of[-1,1]){const e=box(.06,.035,.02,new THREE.MeshBasicMaterial({color:0xff1010,fog:false}));e.position.set(s*.07,1.98,.16);watcher.add(e);
    const a=box(.12,1.0,.14,dk);a.position.set(s*.33,1.15,0);watcher.add(a)}}
const rim=new THREE.PointLight(0x6070a0,0,2.2,1.5);let wAdded=false;
export function introHook(t,stage){if(!wAdded){stage.add(watcher);stage.add(rim);wAdded=true}rim.position.set(2.3,2.2,-1.1);rim.intensity=t>=INTRO_CUT?.8:0;
  watcher.visible=t>=INTRO_CUT;watcher.position.set(1.95,0,-.72);watcher.rotation.y=-.35;
  watcher.children.forEach(c=>{if(c.material&&c.material.color&&c.material.color.r>.5)c.visible=!(t>11.2&&t<11.35)})}
