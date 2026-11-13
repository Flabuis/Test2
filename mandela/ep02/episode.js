// Том 2 «Нарушитель». Не альтернат: чужой, которого видят уже внутри дома — там, где работает телевизор.
// Своя история (семья Уэйдов, вымышленная), без сюжетной линии Марка.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,vhs,dither,snow,makePerson,pose,glr} from '../common/core.js';

export const VOL=2, D=118;
export const CAPS=[ // начало, конец, кто (R — диктор, M — отец семьи на видеокамере), текст. Тайминги = vo/lines.tsv
  [7.0,11.8,'R','Ноябрь девяносто первого. Округ учится жить с альтернатами.'],
  [12.2,17.0,'R','Но в офис шерифа начали поступать другие звонки.'],
  [17.4,21.8,'R','Люди видели чужого — не за дверью. Уже внутри дома.'],
  [22.6,27.4,'R','Свидетели описывают его одинаково: высокий, выше дверного проёма.'],
  [27.8,32.0,'R','Лица никто вспомнить не может.'],
  [32.4,35.8,'R','И приходит он туда, где включён телевизор.'],
  [37.0,41.6,'M','Двадцать третье ноября. Два часа ночи. Лили опять не спит.'],
  [42.0,46.4,'M','Говорит, в коридоре кто-то стоит. Когда работает телевизор.'],
  [47.0,50.0,'M','Ладно. Сейчас посмотрим.'],
  [61.0,62.8,'M','...Эй?'],
  [71.0,73.6,'M','Это же наш коридор...'],
  [78.6,82.6,'R','Внимание. Если в вашем доме находится посторонний —'],
  [83.0,88.2,'R','не смотрите на него. Выключите все телевизоры и радиоприёмники.'],
  [88.6,93.0,'R','Покиньте дом и не возвращайтесь до рассвета.'],
  [93.4,97.6,'R','Не оставляйте детей одних рядом с экранами.'],
  [99.0,103.6,'R','Утром дом Уэйдов был пуст. Двери заперты изнутри.'],
  [104.0,107.6,'R','Телевизор работал.'],
  [112.4,117.4,'R','Если вы смотрите эту запись — не оборачивайтесь.']];

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(58,RW/RH,.05,200);const cam2=new THREE.PerspectiveCamera(60,4/3,.05,60);
const amb=new THREE.AmbientLight(0x6070a0,.5);scene.add(amb);const moonL=new THREE.DirectionalLight(0x8090c0,.4);moonL.position.set(-5,8,3);scene.add(moonL);
scene.fog=new THREE.Fog(0x05070f,8,40);scene.background=new THREE.Color(0x05070f);
const N=(p,s,r=[1,1])=>tex(16,16,(g,w,h)=>noise(g,w,h,p,s),r);

// ---------- улица и полицейская машина ----------
const street=new THREE.Group();scene.add(street);let siren=[];
{const asph=N(['#2a2a2e','#26262a','#2e2e32'],20,[4,40]),grass=N(['#1e2a1a','#1a2616','#22301e'],21,[20,40]),roof=N(['#3a2a26','#342622','#40302a'],23,[3,3]);
 const siding=tex(16,16,(g,w,h)=>{noise(g,w,h,['#8a8676','#827e6e','#928e7e'],22);g.fillStyle='rgba(0,0,0,.25)';for(let y=0;y<h;y+=3)g.fillRect(0,y,w,1)},[3,2]);
 const a=box(6,.02,120,M({map:asph}));a.position.set(0,0,-40);street.add(a);for(const s of[-1,1]){const gr=box(30,.02,120,M({map:grass}));gr.position.set(s*18,0,-40);street.add(gr)}
 const r=mulberry(31);for(let i=0;i<6;i++)for(const s of[-1,1]){const hz=2-i*9,hx=s*9;const hs=new THREE.Group();const b=box(5,3,5,M({map:siding}));b.position.y=1.5;hs.add(b);
   const rf=new THREE.Mesh(new THREE.ConeGeometry(4.2,2,4),M({map:roof}));rf.rotation.y=Math.PI/4;rf.position.y=4;hs.add(rf);
   for(const wx of[-1.3,1.3]){const lit=(i===1&&s<0)||r()<.2;const wn=box(.8,.9,.05,new THREE.MeshBasicMaterial({color:lit?(i===1&&s<0?0x8aa0e0:0xd8b060):0x0a0c14}));wn.position.set(wx,1.7,2.52);hs.add(wn)}
   const dr=box(.9,1.8,.05,M({color:0x3a2418}));dr.position.set(0,.9,2.52);hs.add(dr);hs.position.set(hx,0,hz);hs.rotation.y=s>0?-Math.PI/2:Math.PI/2;street.add(hs)}
 const car=new THREE.Group();const cb=box(1.8,.7,4,M({color:0xd8d8d8}));cb.position.y=.55;car.add(cb);const ct=box(1.6,.5,2,M({color:0x1a1a1a}));ct.position.set(0,1.1,-.2);car.add(ct);
 for(const s of[-1,1]){const lb=box(.5,.15,.3,new THREE.MeshBasicMaterial({color:s<0?0xff2020:0x2040ff,fog:false}));lb.position.set(s*.3,1.45,-.2);car.add(lb);
   const l=new THREE.PointLight(s<0?0xff2020:0x3050ff,0,12,1.3);l.position.set(s*.6,1.8,-.2);car.add(l);siren.push([lb,l])}
 car.position.set(-2.2,0,-7);street.add(car)}

// ---------- дом Уэйдов: гостиная + коридор ----------
const house=new THREE.Group();scene.add(house);const HC=2.8;
const tvC=document.createElement('canvas');tvC.width=128;tvC.height=96;const tvG=tvC.getContext('2d');
const tvTex=new THREE.CanvasTexture(tvC);tvTex.magFilter=tvTex.minFilter=THREE.NearestFilter;tvTex.generateMipmaps=false;tvTex.colorSpace=THREE.SRGBColorSpace;
const tvLight=new THREE.PointLight(0xa0c0ff,3,7,1.3);const camLight=new THREE.SpotLight(0xfff0d0,0,10,.5,.6,1.2);scene.add(camLight,camLight.target);
{const fl=box(8,.05,16,M({map:N(['#3a2e24','#342a20','#40322a'],40,[4,8])}));fl.position.set(0,0,-4);house.add(fl);
 const ce=box(8,.05,16,M({color:0x2a2622}));ce.position.set(0,HC,-4);house.add(ce);
 const wp=tex(16,16,(g,w,h)=>{noise(g,w,h,['#4a4232','#463e2e','#4e4636'],41);g.fillStyle='rgba(120,90,60,.4)';for(let x=2;x<w;x+=6)g.fillRect(x,0,2,h)},[4,2]);
 const wl=(w,d,x,z)=>{const b=box(w,HC,d,M({map:wp}));b.position.set(x,HC/2,z);house.add(b)};
 wl(.1,8,-4,0);wl(.1,8,4,0);wl(8,.1,0,4);wl(3.3,.1,-2.35,-4);wl(3.3,.1,2.35,-4);  // гостиная, проём в коридор по центру
 wl(.1,8,-.7,-8);wl(.1,8,.7,-8);wl(1.4,.1,0,-12);                                  // коридор
 const dm=M({color:0x4a3020});for(const [x,z,sign] of[[-.66,-6,0],[.66,-7.4,0],[-.66,-9,1]]){const d=box(.05,2.0,.9,dm);d.position.set(x,1.0,z);house.add(d);
   if(sign){const sg=new THREE.Mesh(new THREE.PlaneGeometry(.4,.2),new THREE.MeshBasicMaterial({map:tex(32,16,(g)=>{g.fillStyle='#e8d0e0';g.fillRect(0,0,32,16);g.fillStyle='#a02060';g.font='bold 9px monospace';g.fillText('ЛИЛИ',3,12)})}));sg.rotation.y=Math.PI/2;sg.position.set(-.63,1.5,z);house.add(sg)}}
 const st=box(.6,.6,1.2,M({color:0x3a2618}));st.position.set(-3.6,.3,0);house.add(st);const tb=box(.7,.7,.9,M({color:0x2e2e30}));tb.position.set(-3.55,.95,0);house.add(tb);
 const sc=new THREE.Mesh(new THREE.PlaneGeometry(.64,.48),new THREE.MeshBasicMaterial({map:tvTex,toneMapped:false,fog:false}));sc.rotation.y=Math.PI/2;sc.position.set(-3.19,.98,0);house.add(sc);
 tvLight.position.set(-2.6,1.0,0);house.add(tvLight);
 const sm=M({color:0x5a3a3a});const sb=box(.9,.5,2.4,sm);sb.position.set(.6,.45,0);house.add(sb);const sbk=box(.25,.8,2.4,sm);sbk.position.set(1.0,.9,0);house.add(sbk);
 const lamp=box(.3,.5,.3,M({color:0x6a5a40}));lamp.position.set(3.4,1.2,3.4);house.add(lamp)}
// нарушитель
function makeTall(){const g=new THREE.Group(),cl=M({map:N(['#16161a','#121216','#1a1a1e'],60)}),sk=M({map:N(['#d8d4cc','#cecac2','#e0dcd4'],61)});
  const blank=M({map:tex(16,16,(gg,w,h)=>{noise(gg,w,h,['#d8d4cc','#d0ccc4'],62);gg.fillStyle='rgba(0,0,0,.18)';gg.fillRect(4,6,3,2);gg.fillRect(9,6,3,2)})});
  for(const s of[-1,1]){const l=box(.12,1.4,.14,cl);l.position.set(s*.1,.7,0);g.add(l)}const t=box(.36,.95,.2,cl);t.position.y=1.85;g.add(t);
  const arms=[];for(const s of[-1,1]){const a=new THREE.Group();a.position.set(s*.23,2.28,0);const u=box(.09,1.35,.1,cl);u.position.y=-.67;a.add(u);const hd=box(.08,.2,.06,sk);hd.position.y=-1.42;a.add(hd);a.rotation.z=s*.05;g.add(a);arms.push(a)}
  const nk=box(.08,.18,.08,sk);nk.position.y=2.4;g.add(nk);const head=new THREE.Group();head.position.y=2.48;const hb=box(.24,.3,.24,[sk,sk,sk,sk,blank,sk]);hb.position.y=.15;head.add(hb);g.add(head);
  g.userData={head,arms};return g}
const tall=makeTall();house.add(tall);
const wade=makePerson({shirt:['#4a5a6a','#425262'],pants:['#3a3a40','#34343a'],faces:{normal:(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],11);g.fillStyle='#3a2a1e';g.fillRect(0,0,16,3);g.fillStyle='#1a1a1a';g.fillRect(4,7,2,2);g.fillRect(10,7,2,2);g.fillStyle='#6a3a2a';g.fillRect(6,11,4,1);g.fillStyle='#5a4030';g.fillRect(2,12,12,3)},
  scared:(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],11);g.fillStyle='#3a2a1e';g.fillRect(0,0,16,3);g.fillStyle='#fff';g.fillRect(3,6,4,3);g.fillRect(9,6,4,3);g.fillStyle='#1a1a1a';g.fillRect(4,7,2,2);g.fillRect(10,7,2,2);g.fillStyle='#3a1a10';g.fillRect(6,11,4,2);g.fillStyle='#5a4030';g.fillRect(2,13,12,2)}}});
house.add(wade);

// ---------- 2D-карточки ----------
function osdVHS(g,t){text(g,'PLAY ▶',12,10,{size:10});text(g,'НОЯ 24 1991',RW-12,10,{align:'right',size:9});const s=Math.floor(t);text(g,`07:${String(12+Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function osdCam(g,t){if(Math.floor(t*2)%2){g.fillStyle='#ff2020';g.beginPath();g.arc(16,15,4,0,7);g.fill()}text(g,'REC',24,10,{size:10,color:'#ff4040'});
  g.strokeStyle='#fff';g.lineWidth=1;g.strokeRect(RW-34,9,18,9);g.fillStyle='#fff';g.fillRect(RW-16,11,2,5);g.fillRect(RW-32,11,t>60?5:10,5);
  text(g,'23.11.91',12,RH-36,{size:9});const s=Math.floor(t-36)+7*60+14*0;text(g,`02:${String(14+Math.floor(s/60)%45).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,RH-36,{align:'right',size:9})}
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
function dossier(g,t){g.fillStyle='#d8d0b8';g.fillRect(0,0,RW,RH);g.fillStyle='rgba(120,100,60,.15)';for(let y=0;y<RH;y+=4)g.fillRect(0,y,RW,1);
  text(g,'ОФИС ШЕРИФА ОКРУГА МАНДЕЛА',RW/2,12,{align:'center',size:10,color:'#2a2a2a',shadow:false});g.fillStyle='#2a2a2a';g.fillRect(20,26,RW-40,1);
  text(g,'ОБЪЕКТ: «НАРУШИТЕЛЬ»',20,34,{size:12,color:'#7a1010',shadow:false});
  // набросок по описаниям свидетелей
  g.fillStyle='#f0ead8';g.fillRect(212,48,88,150);g.strokeStyle='#5a5040';g.strokeRect(212,48,88,150);g.fillStyle='#8a8070';g.fillRect(212,186,88,1);
  const k=P(t,22.6,24.0);if(k>0){g.globalAlpha=k;g.fillStyle='#1a1a1a';g.fillRect(250,62,12,14);g.fillRect(253,76,6,4);g.fillRect(246,80,20,46);g.fillRect(240,82,5,58);g.fillRect(267,82,5,58);g.fillRect(248,126,6,58);g.fillRect(258,126,6,58);
    g.fillStyle='#d8d4cc';g.fillRect(251,63,10,12);g.globalAlpha=1;text(g,'ПО СЛОВАМ СВИДЕТЕЛЕЙ',256,200,{align:'center',size:7,color:'#5a5040',shadow:false})}
  const L=[[22.8,'РОСТ: ВЫШЕ ДВЕРНОГО ПРОЁМА'],[24.6,'ТЕЛОСЛОЖЕНИЕ: ХУДОЙ, ДЛИННЫЕ РУКИ'],[27.8,'ЛИЦО: НЕ ЗАПОМИНАЕТСЯ'],[32.4,'ПОЯВЛЯЕТСЯ: ГДЕ РАБОТАЕТ ТВ'],[34.4,'АЛЬТЕРНАТ: НЕ УСТАНОВЛЕНО']];
  L.forEach(([t0,s],i)=>typed(g,s,20,56+i*20,t,t0,{size:9,color:i===4?'#7a1010':'#1a1a1a',shadow:false}));
  if(t>33.4){g.save();g.translate(60,170);g.rotate(-.15);g.strokeStyle='#a01010';g.lineWidth=2;g.strokeRect(0,0,130,26);text(g,'СЕКРЕТНО',65,6,{align:'center',size:13,color:'#a01010',shadow:false});g.restore()}}
const STEPS=[[83.0,'1. НЕ СМОТРИТЕ НА НЕГО.'],[85.6,'2. ВЫКЛЮЧИТЕ ТВ И РАДИО.'],[88.6,'3. ПОКИНЬТЕ ДОМ ДО РАССВЕТА.'],[93.4,'4. ДЕТЕЙ — ПОДАЛЬШЕ ОТ ЭКРАНОВ.']];
function alertCard(g,t){g.fillStyle='#000';g.fillRect(0,0,RW,RH);g.fillStyle=Math.floor(t*2)%2?'#a01010':'#600808';g.fillRect(0,16,RW,32);text(g,'ВНИМАНИЕ: НАРУШИТЕЛЬ',RW/2,24,{align:'center',size:14});
  typed(g,'ЕСЛИ В ВАШЕМ ДОМЕ ПОСТОРОННИЙ:',RW/2,62,t,78.8,{align:'center',size:10,color:'#ffd060'});STEPS.forEach(([t0,s],i)=>{if(t>=t0)text(g,s,34,86+i*22,{size:11})})}

function only(g){street.visible=g===street;house.visible=g===house}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}
function shake(t,a){return[Math.sin(t*7.1)*a+Math.sin(t*13.3)*a*.5,Math.sin(t*6.3)*a+Math.sin(t*11.7)*a*.4]}
function tvSnow(t){const d=tvG.getImageData(0,0,128,96),a=d.data,fr=Math.floor(t*FPS*2);for(let i=0;i<a.length;i+=4){const v=hash(i,fr)*200;a[i]=a[i+1]=a[i+2]=v;a[i+3]=255}tvG.putImageData(d,0,0);tvTex.needsUpdate=true}
// телевизор показывает гостиную со спины мужчины (вторая камера), с нарушителем позади
function tvFeed(t,figZ){cam2.position.set(3.7,2.2,1.5);cam2.lookAt(-2.6,1.0,0);tall.visible=true;tall.position.set(figZ,0,.2);tall.rotation.y=-Math.PI/2;wade.visible=true;
  const a0=amb.intensity,l0=tvLight.intensity;amb.intensity=1.8;tvLight.intensity=10;cam2.updateMatrixWorld();glr.render(scene,cam2);amb.intensity=a0;tvLight.intensity=l0;tvG.drawImage(glr.domElement,0,0,128,96);const d=tvG.getImageData(0,0,128,96),a=d.data,fr=Math.floor(t*FPS);
  for(let i=0;i<a.length;i+=4){const n=(hash(i,fr)-.5)*40;a[i]+=n;a[i+1]+=n;a[i+2]+=n}tvG.putImageData(d,0,0);tvTex.needsUpdate=true}

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.6,mode='vhs';camLight.intensity=0;tall.visible=false;wade.visible=false;
  if(t<.6){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);text(ctx,'▶ PLAY',20,18,{size:16});mode='none'}
  else if(t<6.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА, ВИСКОНСИН',RW/2,96,t,1.0,{align:'center',size:12});typed(ctx,'АРХИВНАЯ ЗАПИСЬ №2',RW/2,116,t,2.4,{align:'center',size:10,color:'#a0a0a0'})}
  else if(t<22.0){only(street);scene.fog.near=6;scene.fog.far=36;const fr=Math.floor(t*4);siren.forEach(([lb,l],i)=>{const on=(fr+i)%2===0;l.intensity=on?10:0;lb.visible=on});
    const k=P(t,6,22);cam([lerp(1.5,0,k),1.7,lerp(8,0,k)],[lerp(-2,-5,k),1.4,-10]);draw3D(scene,camera,ctx);dither(ctx)}
  else if(t<36.0){dossier(ctx,t);mode='none'}
  else if(t<78.0){only(house);mode='cam';scene.fog.near=3;scene.fog.far=14;scene.fog.color.set(0x020204);tvLight.intensity=5+hash(Math.floor(t*FPS),4)*2;
    if(t<70)tvSnow(t);
    if(t<46.0){wade.visible=true;wade.position.set(1.6,0,1.4);wade.rotation.y=Math.PI*.15;pose(wade,{face:'normal',ax1:-1.4,az1:-.3,hx:.1});const [sx,sy]=shake(t,.01);camLight.intensity=2.5;cam([2.3+sx,1.8+sy,2.9],[1.6,1.7,1.4])}
    else if(t<53.0){const k=eInOut(P(t,47,52.5));const [sx,sy]=shake(t,.015);camLight.intensity=t>50.2?6:0;
      cam([1.2+sx,1.55+sy,1.6],[lerp(-3.6,0,k),lerp(1.0,1.4,k),lerp(0,-8,k)])}
    else if(t<66.5){camLight.intensity=6;const k=P(t,53,60);const z=lerp(-1.0,-8.4,eInOut(k)),bob=Math.sin(t*7)*.03*(t<60);const [sx,sy]=shake(t,.012);
      tall.visible=true;tall.position.set(0,0,-11.4);tall.rotation.y=0;tall.userData.head.rotation.set(.25,t>64.6?Math.min(.5,(t-64.6)*.6):0,0);
      const zoom=P(t,61.5,64.5);camera.fov=lerp(58,44,zoom);camera.updateProjectionMatrix();cam([sx,1.55+bob+sy,z],[0,lerp(1.4,2.2,P(t,58,62)),-12]);vamt=t>63?.6+P(t,63,66.5)*1.8:.6}
    else if(t<70.0){camera.fov=58;camera.updateProjectionMatrix();camLight.intensity=6;const k=P(t,66.5,67.4);tall.visible=true;tall.position.set(0,0,-11.4);
      cam([0,lerp(1.55,.2,eIn(k)),-8.4],[Math.sin(t*9)*2,lerp(2.0,.0,k),-12+k*6]);camera.rotation.z+=k*1.2;vamt=2.5;if(t>67.6){ctx.fillStyle='#000';draw3D(scene,camera,ctx);ctx.fillRect(0,0,RW,RH);mode='cam';dither(ctx);ctx.globalAlpha=1}}
    else{camera.fov=58;camera.updateProjectionMatrix();const figZ=lerp(1.0,-.5,P(t,72,76.4));const behind=t>=74.0&&t<75.2;
      wade.position.set(-1.5,0,0);wade.rotation.y=-Math.PI/2;pose(wade,{ax1:-1.5,ax0:-1.4,face:'scared'});tvFeed(t,figZ);wade.visible=false;tall.visible=false;
      const [sx,sy]=shake(t,.025);if(behind){const k=eInOut(P(t,74,74.4))*(1-eInOut(P(t,74.8,75.2)));cam([-2.35+sx,1.2+sy,0],[lerp(-3.6,3,k),1.3,k*.01])}
      else cam([-2.35+sx,1.15+sy,0],[-3.2,1.0,0]);vamt=t>75.2?.8+P(t,75.2,77)*2:.8}
    camera.updateMatrixWorld();camLight.position.copy(camera.position);camLight.target.position.copy(camera.position).add(camera.getWorldDirection(new THREE.Vector3()));
    if(t<67.6||t>=70){draw3D(scene,camera,ctx);dither(ctx)}}
  else if(t<78.4){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);text(ctx,'ЗАПИСЬ ПРЕРВАНА',RW/2,112,{align:'center',size:12});mode='none'}
  else if(t<98.0){alertCard(ctx,t)}
  else if(t<112.0){only(house);scene.fog.near=3;scene.fog.far=14;tvFeed(t,.6);tvLight.intensity=6;tall.visible=false;wade.visible=false;
    // фото из дела: пустая гостиная, на экране — он
    const k=P(t,98,112);cam([lerp(2.6,-1.6,eInOut(P(t,104,112))),1.6,lerp(2.8,0,eInOut(P(t,104,112)))],[-3.2,1.0,0]);draw3D(scene,camera,ctx);dither(ctx);
    ctx.fillStyle='#e8e2d0';ctx.fillRect(0,0,RW,10);ctx.fillRect(0,RH-46,RW,46);ctx.fillRect(0,0,10,RH);ctx.fillRect(RW-10,0,10,RH);
    text(ctx,'ДОМ УЭЙДОВ, 23.11.1991',16,RH-42,{size:9,color:'#2a2a2a',shadow:false});if(t>101)text(ctx,'СЕМЬЯ НЕ НАЙДЕНА',16,RH-31,{size:9,color:'#7a1010',shadow:false});
    if(t>104.4)text(ctx,'ТЕЛЕВИЗОР БЫЛ ВКЛЮЧЁН',RW-16,RH-31,{align:'right',size:9,color:'#2a2a2a',shadow:false});vamt=.4}
  else{ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ЕСЛИ ВЫ СМОТРИТЕ ЭТУ ЗАПИСЬ',RW/2,100,t,112.2,{align:'center',size:11});if(t>115.6)text(ctx,'НЕ ОБОРАЧИВАЙТЕСЬ',RW/2,120,{align:'center',size:13,color:'#ff3030'});vamt=.8}
  if(mode==='vhs')osdVHS(ctx,t);if(mode==='cam')osdCam(ctx,t);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  vhs(ctx,t,vamt)}

// крючок для общего аутро: когда гаснет лампа, в темноте комнаты на секунду проступает он
const ghost=makeTall();ghost.scale.setScalar(.75);const ghostL=new THREE.PointLight(0x8090b0,0,3,1.5);let added=false;
export function outroHook(t,stage){if(!added){stage.add(ghost);stage.add(ghostL);added=true}
  const on=t>=4.3&&t<5.5;ghost.visible=on;ghost.position.set(2.3,0,-.5);ghost.rotation.y=-.3;ghostL.position.set(2.0,1.6,.6);ghostL.intensity=on?.9:0}
