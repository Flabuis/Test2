// Том 5 «Сбой». Повторный выпуск оповещения, но запись повреждена: диктор путается и советует то, что нельзя.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,vhs,dither,snow,makePerson,pose,glr} from '../common/core.js';

export const VOL=5, D=118;
// R — диктор, X — с искажениями, Q — совсем сломанный, D — тяжёлый искажённый голос
export const CAPS=[
  [7.0,11.0,'R','Внимание. Повторный выпуск экстренного оповещения.'],
  [11.4,15.6,'R','Если вы встретили альтерната: не смотрите ему в лицо.'],
  [16.0,20.8,'X','Не отвечайте. Не впускайте... впустите его в дом.'],
  [21.4,24.6,'R','Простите. Не впускайте его в дом.'],
  [25.0,29.4,'X','Смотрите ему в лицо. Долго. Не моргайте.'],
  [30.6,34.4,'R','Жители округа. Оставайтесь дома. Выключите свет.'],
  [34.8,39.4,'X','Включите свет. Чтобы они видели, где вы.'],
  [40.0,46.4,'Q','Ваши близкие — это не ваши близкие. Ваши близкие — это... ваши... близкие.'],
  [47.0,50.6,'R','Сохраняйте спокойствие.'],
  [55.6,60.6,'X','Если на экране знакомое лицо — подойдите ближе.'],
  [61.0,64.2,'R','Нет. Отойдите. Отойдите от экрана.'],
  [64.6,69.4,'Q','Подойдите. Ближе. Ещё ближе.'],
  [75.6,80.0,'R','Альтернат выглядит как человек, которого вы знаете.'],
  [80.4,83.2,'X','Как вы.'],
  [83.6,88.0,'R','Если ваше отражение двигается не так, как вы —'],
  [88.4,92.6,'X','не отворачивайтесь. Оно этого и ждёт.'],
  [96.0,101.6,'D','Умрите. Умрите. Умрите.'],
  [102.6,106.6,'R','Приносим извинения за технические неполадки.'],
  [107.0,110.6,'R','Оставайтесь дома. Не впускайте их.']];
export const OUTRO_CAPS=[[2.9,4.6,'Q','Всё это зря.']];   // время — от начала аутро

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(58,RW/RH,.03,200);const cam2=new THREE.PerspectiveCamera(50,1,.05,30);
const amb=new THREE.AmbientLight(0x6070a0,.5);scene.add(amb);scene.fog=new THREE.Fog(0x05070f,8,40);scene.background=new THREE.Color(0x05070f);
const N=(p,s,r=[1,1])=>tex(16,16,(g,w,h)=>noise(g,w,h,p,s),r);
const WRONG=(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],11);g.fillStyle='#3a2a1e';g.fillRect(0,0,32,6);g.fillStyle='#000';g.fillRect(4,10,6,4);g.fillRect(22,10,6,4);g.fillStyle='#fff';g.fillRect(6,11,1,1);g.fillRect(24,11,1,1);
  g.fillStyle='#2a0a08';g.fillRect(3,22,26,4);g.fillStyle='#f0ece0';for(let x=4;x<28;x+=2)g.fillRect(x,22,1,2)};
const NORMAL=(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],11);g.fillStyle='#3a2a1e';g.fillRect(0,0,32,6);g.fillStyle='#fff';g.fillRect(9,12,4,2);g.fillRect(19,12,4,2);g.fillStyle='#1a1a1a';g.fillRect(10,12,2,2);g.fillRect(20,12,2,2);g.fillStyle='#8a4a3a';g.fillRect(12,24,8,1)};

// ---------- улица: во всех окнах кто-то стоит ----------
const street=new THREE.Group();scene.add(street);const watchers=[];
{const a=box(6,.02,120,M({map:N(['#2a2a2e','#26262a'],20,[4,40])}));a.position.set(0,0,-40);street.add(a);for(const s of[-1,1]){const gr=box(30,.02,120,M({map:N(['#1e2a1a','#1a2616'],21,[20,40])}));gr.position.set(s*18,0,-40);street.add(gr)}
 const siding=tex(16,16,(g,w,h)=>{noise(g,w,h,['#8a8676','#827e6e'],22);g.fillStyle='rgba(0,0,0,.25)';for(let y=0;y<h;y+=3)g.fillRect(0,y,w,1)},[3,2]);
 const sil=new THREE.MeshBasicMaterial({color:0x0a0806});
 for(let i=0;i<6;i++)for(const s of[-1,1]){const hs=new THREE.Group();const b=box(5,3,5,M({map:siding}));b.position.y=1.5;hs.add(b);const rf=new THREE.Mesh(new THREE.ConeGeometry(4.2,2,4),M({map:N(['#3a2a26','#342622'],23)}));rf.rotation.y=Math.PI/4;rf.position.y=4;hs.add(rf);
   for(const wx of[-1.3,1.3]){const wn=box(1.1,1.3,.05,new THREE.MeshBasicMaterial({color:0xe0b860,fog:false}));wn.position.set(wx,1.7,2.52);hs.add(wn);
     const w=new THREE.Group();const bd=box(.5,.7,.02,sil);bd.position.y=-.25;w.add(bd);const hd=box(.28,.3,.02,sil);hd.position.y=.25;w.add(hd);w.position.set(wx,1.62,2.56);hs.add(w);watchers.push(w)}
   hs.position.set(s*9,0,2-i*9);hs.rotation.y=s>0?-Math.PI/2:Math.PI/2;street.add(hs)}}

// ---------- гостиная с телевизором ----------
const lroom=new THREE.Group();scene.add(lroom);const tvC=document.createElement('canvas');tvC.width=96;tvC.height=72;const tvG=tvC.getContext('2d');
const tvTex=new THREE.CanvasTexture(tvC);tvTex.magFilter=tvTex.minFilter=THREE.NearestFilter;tvTex.generateMipmaps=false;tvTex.colorSpace=THREE.SRGBColorSpace;const roomL=new THREE.PointLight(0xa0c0ff,4,8,1.3);
const faceImg=tex(32,32,WRONG).image;
{const fl=box(8,.05,8,M({map:N(['#3a2e24','#342a20'],40,[4,4])}));lroom.add(fl);const wp=tex(16,16,(g,w,h)=>{noise(g,w,h,['#4a4232','#463e2e'],41);g.fillStyle='rgba(120,90,60,.4)';for(let x=2;x<w;x+=6)g.fillRect(x,0,2,h)},[6,3]);
 for(const [w,d,x,z] of[[8,.1,0,-4],[.1,8,-4,0],[.1,8,4,0]]){const b=box(w,3,d,M({map:wp}));b.position.set(x,1.5,z);lroom.add(b)}
 const st=box(1.2,.6,.6,M({color:0x3a2618}));st.position.set(0,.3,-3.4);lroom.add(st);const tb=box(.9,.7,.7,M({color:0x2e2e30}));tb.position.set(0,.95,-3.4);lroom.add(tb);
 const sc=new THREE.Mesh(new THREE.PlaneGeometry(.64,.48),new THREE.MeshBasicMaterial({map:tvTex,toneMapped:false,fog:false}));sc.position.set(0,.98,-3.04);lroom.add(sc);
 const sm=M({color:0x5a3a3a});const sb=box(2.4,.5,.9,sm);sb.position.set(0,.45,.6);lroom.add(sb);const sbk=box(2.4,.8,.25,sm);sbk.position.set(0,.9,1.0);lroom.add(sbk);roomL.position.set(0,1,-2.6);lroom.add(roomL)}
function drawTv(t){const g=tvG;if(t<64.6){g.fillStyle='#1a2a5a';g.fillRect(0,0,96,72);g.fillStyle='#e8e4d8';g.fillRect(6,10,84,50);g.fillStyle='#141414';g.font='bold 9px monospace';
    const s=t<61?'ПОДОЙДИТЕ':'ОТОЙДИТЕ';g.fillText(s,12,32);g.fillText(t<61?'БЛИЖЕ':'ОТ ЭКРАНА',12,46)}
  else{g.fillStyle='#101418';g.fillRect(0,0,96,72);g.imageSmoothingEnabled=false;g.drawImage(faceImg,16,4,64,64)}
  const d=g.getImageData(0,0,96,72),a=d.data,fr=Math.floor(t*FPS);for(let i=0;i<a.length;i+=4){const n=(hash(i,fr)-.5)*50;a[i]+=n;a[i+1]+=n;a[i+2]+=n}g.putImageData(d,0,0);tvTex.needsUpdate=true}

// ---------- комната с зеркалом (отражение — отдельный «мир» за зеркалом) ----------
const mroom=new THREE.Group();scene.add(mroom);const mirC=document.createElement('canvas');mirC.width=96;mirC.height=128;const mirG=mirC.getContext('2d');
const mirTex=new THREE.CanvasTexture(mirC);mirTex.magFilter=mirTex.minFilter=THREE.NearestFilter;mirTex.generateMipmaps=false;mirTex.colorSpace=THREE.SRGBColorSpace;
const mirWorld=new THREE.Group();mirWorld.position.set(60,0,0);scene.add(mirWorld);let refl;const mL=new THREE.PointLight(0xd8e0ff,3,6,1.3);
{const tile=tex(16,16,(g,w,h)=>{noise(g,w,h,['#8a9aa0','#82929a','#92a2a8'],50);g.fillStyle='rgba(0,0,0,.3)';g.fillRect(0,0,w,1);g.fillRect(0,0,1,h)},[6,3]);
 const fl=box(6,.05,6,M({map:N(['#3a3e42','#363a3e'],51,[4,4])}));mroom.add(fl);const wl=box(6,3,.1,M({map:tile}));wl.position.set(0,1.5,-1.6);mroom.add(wl);
 const fr=box(.9,1.3,.06,M({color:0x6a5a40}));fr.position.set(0,1.6,-1.53);mroom.add(fr);const mir=new THREE.Mesh(new THREE.PlaneGeometry(.78,1.18),new THREE.MeshBasicMaterial({map:mirTex,toneMapped:false,fog:false}));mir.position.set(0,1.6,-1.49);mroom.add(mir);
 const sink=box(.8,.15,.5,M({color:0xd8d8d0}));sink.position.set(0,.9,-1.3);mroom.add(sink);mL.position.set(0,2.6,0);mroom.add(mL);
 const wl2=box(6,3,.1,M({map:tile}));wl2.position.set(0,1.5,1.8);mirWorld.add(wl2);const fl2=box(6,.05,6,M({map:N(['#3a3e42','#363a3e'],51,[4,4])}));mirWorld.add(fl2);
 const l2=new THREE.PointLight(0xd8e0ff,3,6,1.3);l2.position.set(0,2.6,-.5);mirWorld.add(l2);
 refl=makePerson({shirt:['#4a5a6a','#425262'],faceSize:32,faces:{normal:NORMAL,wrong:WRONG}});refl.position.set(0,0,0);refl.rotation.y=Math.PI;mirWorld.add(refl)}
function drawMirror(t){const turn=t>=86.4?P(t,86.4,88.4):0;pose(refl,{face:t>=88.4?'wrong':'normal',hy:turn*.9,hz:t>=90?.2:0});
  cam2.position.set(60,1.6,-1.2);cam2.lookAt(60,1.55,1.5);cam2.aspect=96/128;cam2.updateProjectionMatrix();mirWorld.visible=true;
  glr.render(scene,cam2);mirG.drawImage(glr.domElement,0,0,96,128);mirTex.needsUpdate=true;mirWorld.visible=false}

// ---------- 2D ----------
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
function osdVHS(g,t){text(g,'PLAY ▶',12,10,{size:10});text(g,Math.floor(t*3)%7===0?'ЯНВ ?? 19??':'ЯНВ 02 1992',RW-12,10,{align:'right',size:9});const s=Math.floor(t);text(g,`03:${String(Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function psa(g,t){g.fillStyle='#1a2a5a';g.fillRect(0,0,RW,RH);g.fillStyle='#e8e4d8';g.fillRect(14,14,RW-28,RH-50);g.fillStyle='#1a2a5a';g.fillRect(14,14,RW-28,24);
  text(g,'ПОВТОРНЫЙ ВЫПУСК',RW/2,21,{align:'center',size:12,shadow:false});
  const L=[[11.4,'1. НЕ СМОТРИТЕ ЕМУ В ЛИЦО.','1. СМОТРИТЕ ЕМУ В ЛИЦО.',25.0],[16.0,'2. НЕ ОТВЕЧАЙТЕ.',null],[17.8,'3. НЕ ВПУСКАЙТЕ В ДОМ.','3. ВПУСТИТЕ ЕГО В ДОМ.',19.0]];
  L.forEach(([t0,a,b,tb],i)=>{if(t<t0)return;let s=a,c='#141414';if(b&&t>=tb&&!(i===2&&t>=21.4&&t<25))s=b,c='#7a0a0a';if(b&&i===2&&t>=21.4&&t<25){s=a;c='#141414'}
    if(b&&Math.abs(t-tb)<.3&&Math.floor(t*FPS)%2)s=b;text(g,s,30,54+i*26,{size:11,color:c,shadow:false})});
  if(t>=25.0){text(g,'4. НЕ МОРГАЙТЕ.',30,132,{size:11,color:'#7a0a0a',shadow:false})}}
function signs(g,t){g.fillStyle='rgba(0,0,0,.6)';g.fillRect(8,30,170,74);text(g,'ПРИЗНАКИ:',14,36,{size:10,color:'#ffd060'});
  const A=['— ЛИЦО ПОЧТИ ТАКОЕ ЖЕ','— НЕ МОРГАЕТ','— СТОИТ И СМОТРИТ'],B=['— ЛИЦО ТАКОЕ ЖЕ, КАК У ВАС','— МОРГАЕТ, КОГДА ВЫ МОРГАЕТЕ','— СТОИТ ТАМ, ГДЕ ВЫ'];
  A.forEach((s,i)=>{if(t<76+i)return;const sw=t>=80.4+i*.6;text(g,sw?B[i]:s,14,52+i*14,{size:9,color:sw?'#ff6060':'#ffffff'})})}
function bars(g){const c=['#c0c0c0','#c0c000','#00c0c0','#00c000','#c000c0','#c00000','#0000c0'];c.forEach((v,i)=>{g.fillStyle=v;g.fillRect(Math.round(i*RW/7),0,Math.ceil(RW/7),RH*.7)});g.fillStyle='#101010';g.fillRect(0,RH*.7,RW,RH*.3)}
function only(g){street.visible=g===street;lroom.visible=g===lroom;mroom.visible=g===mroom;mirWorld.visible=false}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}
// склейки-«сбои»: короткие провалы в шум/повтор кадра по всей кассете
const DROPS=[9.8,18.9,27.6,36.6,44.1,58.2,66.8,79.9,84.7,91.3];

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.8,mode='vhs';const tq=t;
  for(const d of DROPS)if(t>=d&&t<d+.2)t=d-.07;   // заедание
  if(t<1.2){ctx.fillStyle='#600000';ctx.fillRect(0,0,RW,RH);text(ctx,'ПРЕДУПРЕЖДЕНИЕ',RW/2,70,{align:'center',size:14,color:'#ffd060'});text(ctx,'ЗАПИСЬ ПОВРЕЖДЕНА',RW/2,100,{align:'center',size:12});
    text(ctx,'НЕ ПРОДОЛЖАЙТЕ ПРОСМОТР',RW/2,120,{align:'center',size:12});mode='none';vamt=1.5}
  else if(t<6.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА, ВИСКОНСИН',RW/2,92,t,1.6,{align:'center',size:12});typed(ctx,'АРХИВНАЯ ЗАПИСЬ №5',RW/2,112,t,2.8,{align:'center',size:10,color:'#a0a0a0'});
    if(t>4.2)text(ctx,`ВОССТАНОВЛЕНО: ${Math.min(61,Math.floor((t-4.2)*40))}%`,RW/2,132,{align:'center',size:9,color:'#ff6060'})}
  else if(t<30.0){psa(ctx,t);vamt=t>=16&&t<21?1.6:.8}
  else if(t<55.0){only(street);scene.fog.near=6;scene.fog.far=36;const turn=P(t,51,53);watchers.forEach((w,i)=>{w.rotation.y=0;w.children[1].position.x=turn>0?Math.sin(i)*.05*turn:0;w.visible=t>=30.4+i*.03});
    const k=P(t,30,55);cam([-2.2,1.6,lerp(4,-14,k)],[-2.2,1.5,-40]);if(t>=51){const s=eInOut(P(t,51,53));cam([-2.2,1.6,lerp(4,-14,k)],[lerp(-2.2,-9,s),1.6,lerp(-40,-14,s)])}
    draw3D(scene,camera,ctx);dither(ctx);vamt=t>=40&&t<46.4?1.8:.8}
  else if(t<75.0){only(lroom);scene.fog.near=10;scene.fog.far=40;drawTv(t);roomL.intensity=3.5+hash(Math.floor(t*FPS),4)*1.5;
    let z;if(t<61)z=lerp(3.2,1.4,P(t,55,61));else if(t<64.6)z=lerp(1.4,2.8,eOut(P(t,61,62.5)));else z=lerp(2.8,-2.6,eIn(P(t,64.6,70.0)));if(t>=72.0)z=3.2;
    cam([0,1.6,z],[0,1.0,-3.4]);draw3D(scene,camera,ctx);dither(ctx);vamt=t>=64.6&&t<72?1+P(t,64.6,70)*2.5:.8;if(t>=70&&t<72){ctx.drawImage(faceImg,0,0,RW,RH);vamt=3}}
  else if(t<95.0){only(mroom);scene.fog.near=10;scene.fog.far=40;drawMirror(t);const k=P(t,75,95);cam([lerp(.15,0,k),1.62,lerp(1.4,.3,eInOut(k))],[0,1.6,-1.5]);draw3D(scene,camera,ctx);dither(ctx);
    if(t<92.8)signs(ctx,t);vamt=t>=88.4?1.2:.8}
  else if(t<102.0){ctx.fillStyle=Math.floor(t*6)%2?'#500000':'#000';ctx.fillRect(0,0,RW,RH);if(t>=96){const n=Math.min(3,Math.floor((t-96)/1.8)+1);for(let i=0;i<n;i++)text(ctx,'УМРИТЕ',RW/2+(hash(i,Math.floor(t*FPS))-.5)*20,70+i*34,{align:'center',size:20,color:'#ff2020'})}
    mode='none';vamt=2.5+hash(Math.floor(t*FPS),5)*1.5}
  else if(t<110.6){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);text(ctx,'ТЕХНИЧЕСКИЕ НЕПОЛАДКИ',RW/2,80,{align:'center',size:13});text(ctx,'ПРИНОСИМ ИЗВИНЕНИЯ',RW/2,104,{align:'center',size:11});
    if(t>=107)text(ctx,'ОСТАВАЙТЕСЬ ДОМА. НЕ ВПУСКАЙТЕ ИХ.',RW/2,140,{align:'center',size:10,color:'#ffd060'});vamt=.4}
  else{bars(ctx);text(ctx,'КОНЕЦ ЗАПИСИ',RW/2,RH*.78,{align:'center',size:12});if(t>=115.2&&t<115.3){ctx.drawImage(faceImg,96,56,128,128)}mode='none';vamt=.6}
  if(mode==='vhs')osdVHS(ctx,t);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  if(tq!==t)snow(ctx,tq,.35);
  vhs(ctx,tq,vamt)}

// интро: на экране вместо PLAY — предупреждение
export function playScreen(t,g){g.fillStyle='#600000';g.fillRect(0,0,RW,RH);text(g,'ПРЕДУПРЕЖДЕНИЕ',RW/2,70,{align:'center',size:14,color:'#ffd060'});text(g,'ЗАПИСЬ ПОВРЕЖДЕНА',RW/2,100,{align:'center',size:12});
  text(g,'НЕ ПРОДОЛЖАЙТЕ ПРОСМОТР',RW/2,120,{align:'center',size:12})}
