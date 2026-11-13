// Том 6 «Свет». По мотивам линии ложного архангела: над округом висит свет, он называет себя ангелом и обещает вернуть умерших.
// Своя история (пастор Хейл и его приход — вымышленные). Диктор глючит, но меньше, чем в томе 5.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,vhs,dither,snow,makePerson,pose} from '../common/core.js';

export const VOL=6, D=118;
// R — диктор, X — с искажениями, M — пастор на любительской записи, A — «ангел»
export const CAPS=[
  [7.0,11.4,'R','Январь девяносто второго. Над округом Мандела видели свет.'],
  [11.8,16.6,'R','Не самолёт и не звезда. Свет висел над полями и не двигался.'],
  [17.0,22.6,'X','Те, кто смотрел на него дольше минуты, начинали слышать голос.'],
  [25.0,28.6,'M','Прихожане говорят, что видели ангела.'],
  [29.0,34.4,'M','Он называет себя Гавриилом. Обещает, что умершие вернутся.'],
  [35.2,40.0,'M','Это не ангел. Ангел не просит открыть дверь.'],
  [46.0,51.6,'X','Свидетели описывают крылья. И глаза. Слишком много глаз.'],
  [57.2,59.4,'A','Не бойтесь.'],
  [64.6,69.4,'R','Если над вашим домом свет — задёрните шторы.'],
  [69.8,73.6,'R','Не выходите на улицу. Не смотрите вверх.'],
  [74.0,78.4,'X','Он слышит, к кому вы обращаетесь.'],
  [78.8,81.0,'X','И он отвечает.'],
  [85.0,88.4,'R','Утром церковь была пуста.'],
  [88.8,93.0,'R','Прихожане вернулись через три дня. Все.'],
  [93.4,96.0,'X','Они улыбались.'],
  [106.0,110.6,'R','Если вы видите свет — не смотрите вверх.'],
  [111.4,113.6,'A','Посмотри.']];

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(58,RW/RH,.05,400);
const amb=new THREE.AmbientLight(0x6070a0,.45);scene.add(amb);scene.fog=new THREE.Fog(0x05070f,10,90);scene.background=new THREE.Color(0x05070f);
const N=(p,s,r=[1,1])=>tex(16,16,(g,w,h)=>noise(g,w,h,p,s),r);
const SMILE=(g,w,h)=>{noise(g,w,h,['#d8b8a0','#d0b098'],11);g.fillStyle='#3a2a1e';g.fillRect(0,0,32,6);g.fillStyle='#000';g.fillRect(8,11,4,4);g.fillRect(20,11,4,4);
  g.fillStyle='#2a0a08';g.fillRect(5,21,22,3);g.fillRect(4,19,2,3);g.fillRect(26,19,2,3);g.fillStyle='#f0ece0';for(let x=6;x<26;x+=2)g.fillRect(x,21,1,2)};

// ---------- поле, церковь снаружи, свет в небе ----------
const field=new THREE.Group();scene.add(field);const skyL=new THREE.PointLight(0xe8f0ff,0,140,1.0);
const glow=new THREE.Mesh(new THREE.IcosahedronGeometry(3,1),new THREE.MeshBasicMaterial({color:0xf8fbff,fog:false,transparent:true,opacity:1}));
{const gr=box(200,.05,200,M({map:N(['#c8ccd4','#c0c4cc','#d0d4dc'],60,[40,40])}));gr.position.z=-60;field.add(gr);
 const st=new THREE.BufferGeometry();const r=mulberry(61),a=[];for(let i=0;i<300;i++){const th=r()*Math.PI*2,ph=.1+r()*1.3;a.push(Math.cos(th)*Math.cos(ph)*200,Math.sin(ph)*200,Math.sin(th)*Math.cos(ph)*200)}
 st.setAttribute('position',new THREE.Float32BufferAttribute(a,3));field.add(new THREE.Points(st,new THREE.PointsMaterial({color:0xe0e0f0,size:1.2,sizeAttenuation:false,fog:false})));
 const ch=new THREE.Group();const nave=box(6,4,10,M({map:N(['#b8b0a0','#b0a898'],62)}));nave.position.y=2;ch.add(nave);const roof=new THREE.Mesh(new THREE.ConeGeometry(4.6,2.6,4),M({color:0x3a2e2a}));roof.rotation.y=Math.PI/4;roof.scale.z=2.2;roof.position.y=5.2;ch.add(roof);
 const tw=box(2,7,2,M({map:N(['#b8b0a0','#b0a898'],63)}));tw.position.set(0,3.5,5.5);ch.add(tw);const sp=new THREE.Mesh(new THREE.ConeGeometry(1.4,3,4),M({color:0x3a2e2a}));sp.rotation.y=Math.PI/4;sp.position.set(0,8.5,5.5);ch.add(sp);
 const cr=box(.15,1,.15,M({color:0x8a8a8a}));cr.position.set(0,10.4,5.5);ch.add(cr);const cr2=box(.6,.15,.15,M({color:0x8a8a8a}));cr2.position.set(0,10.6,5.5);ch.add(cr2);
 for(const z of[-3,0,3])for(const s of[-1,1]){const w=box(.05,1.4,.7,new THREE.MeshBasicMaterial({color:0xd8a040}));w.position.set(s*3.03,2.2,z);ch.add(w)}
 ch.position.set(-14,0,-40);ch.rotation.y=.5;field.add(ch);
 for(let i=0;i<18;i++){const p=box(.12,1.2,.12,M({color:0x4a3a2a}));p.position.set(-30+i*3.4,.6,-20);field.add(p)}const fe=box(62,.06,.06,M({color:0x4a3a2a}));fe.position.set(0,1,-20);field.add(fe);
 glow.position.set(8,40,-120);field.add(glow);skyL.position.set(8,36,-110);field.add(skyL)}
// крылатая фигура со множеством глаз
const angel=new THREE.Group();const eyes=[];
{const wm=new THREE.MeshBasicMaterial({color:0x6a7088,fog:false,side:THREE.DoubleSide});const core=new THREE.Mesh(new THREE.IcosahedronGeometry(1.4,0),new THREE.MeshBasicMaterial({color:0xfafcff,fog:false}));angel.add(core);
 for(let i=0;i<6;i++){const a=i/6*Math.PI*2+.26;const w=new THREE.Group();for(let k=0;k<4;k++){const f=box(1.1,7-k*1.2,.1,wm);f.position.set(k*.9,(7-k*1.2)/2,0);f.rotation.z=-.15*k;w.add(f)}w.rotation.z=a;w.position.set(Math.cos(a+Math.PI/2)*1.5,Math.sin(a+Math.PI/2)*1.5,-.5);angel.add(w)}
 const r=mulberry(70);for(let i=0;i<34;i++){const a=r()*Math.PI*2,d=2.4+r()*8;const e=new THREE.Group();const wh=new THREE.Mesh(new THREE.IcosahedronGeometry(.45,0),new THREE.MeshBasicMaterial({color:0xffffff,fog:false}));e.add(wh);
   const pu=new THREE.Mesh(new THREE.IcosahedronGeometry(.2,0),new THREE.MeshBasicMaterial({color:0x000000,fog:false}));pu.position.z=.32;e.add(pu);e.position.set(Math.cos(a)*d,Math.sin(a)*d,.6);angel.add(e);eyes.push(e)}
 angel.position.set(8,40,-120);angel.scale.setScalar(3.4);scene.add(angel)}

// ---------- церковь внутри ----------
const church=new THREE.Group();scene.add(church);let pastor;const flock=[];const winM=[];const candleL=new THREE.PointLight(0xffc070,3,9,1.3);const outL=new THREE.PointLight(0xe8f0ff,0,14,1.2);
{const fl=box(8,.05,14,M({map:N(['#4a3a2a','#443424','#503e2e'],80,[4,8])}));church.add(fl);const wm=M({map:N(['#8a8478','#827c70'],81,[4,2])});
 for(const [w,d,x,z] of[[8,.1,0,-6],[.1,14,-4,0],[.1,14,4,0],[8,.1,0,6]]){const b=box(w,5,d,wm);b.position.set(x,2.5,z);church.add(b)}
 for(const z of[-3,0,3])for(const s of[-1,1]){const m=new THREE.MeshBasicMaterial({color:0x403020});const w=box(.05,1.8,.8,m);w.position.set(s*3.94,2.6,z);church.add(w);winM.push(m)}
 const alt=box(2,1,.8,M({color:0x6a4a30}));alt.position.set(0,.5,-5.2);church.add(alt);const cr=box(.12,1.2,.12,M({color:0xc8b060}));cr.position.set(0,2.6,-5.9);church.add(cr);const cr2=box(.6,.12,.12,M({color:0xc8b060}));cr2.position.set(0,2.85,-5.9);church.add(cr2);
 const pul=box(.8,1.1,.6,M({color:0x5a3e28}));pul.position.set(-1.6,.55,-3.8);church.add(pul);
 for(let rI=0;rI<5;rI++)for(const s of[-1,1]){const pw=box(2.6,.5,.5,M({color:0x5a4030}));pw.position.set(s*1.8,.45,-1.6+rI*1.3);church.add(pw);const bk=box(2.6,.6,.08,M({color:0x5a4030}));bk.position.set(s*1.8,.9,-1.36+rI*1.3);church.add(bk)}
 for(const x of[-.7,.7]){const c=box(.06,.25,.06,M({color:0xf0e8d8}));c.position.set(x,1.12,-5.2);church.add(c);const f=new THREE.Mesh(new THREE.ConeGeometry(.03,.07,4),new THREE.MeshBasicMaterial({color:0xffd060,fog:false}));f.position.set(x,1.29,-5.2);church.add(f)}
 candleL.position.set(0,1.6,-4.6);church.add(candleL);outL.position.set(3.2,2.6,0);church.add(outL);
 pastor=makePerson({shirt:['#141416','#18181a'],pants:['#141416','#18181a'],faces:{normal:(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],90);g.fillStyle='#8a8a8a';g.fillRect(0,0,16,3);g.fillStyle='#1a1a1a';g.fillRect(4,7,2,2);g.fillRect(10,7,2,2);g.fillStyle='#6a3a2a';g.fillRect(6,11,4,1)}}});
 const col_=box(.2,.06,.05,M({color:0xffffff}));col_.position.set(0,1.56,.17);pastor.add(col_);pastor.position.set(-1.6,0,-4.3);church.add(pastor);
 const r=mulberry(91);for(let rI=0;rI<4;rI++)for(const s of[-1,1])for(let k=0;k<2;k++){if(r()<.2)continue;const p=makePerson({shirt:[['#4a5a6a','#425262'],['#6a4a4a','#624242'],['#4a6a4a','#426242'],['#5a5a5a','#525252']][Math.floor(r()*4)],faceSize:32,faces:{normal:SMILE}});
   p.position.set(s*1.8+(k-.5)*1.1,0,-1.6+rI*1.3+.25);p.rotation.y=Math.PI;church.add(p);flock.push(p)}}

// ---------- 2D ----------
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
function osdVHS(g,t){text(g,'PLAY ▶',12,10,{size:10});text(g,'ЯНВ 21 1992',RW-12,10,{align:'right',size:9});const s=Math.floor(t);text(g,`23:${String(5+Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function osdCam(g,t){if(Math.floor(t*2)%2){g.fillStyle='#ff2020';g.beginPath();g.arc(16,15,4,0,7);g.fill()}text(g,'REC',24,10,{size:10,color:'#ff4040'});text(g,'19.01.92',12,RH-36,{size:9})}
const STEPS=[[64.8,'— ЗАДЁРНИТЕ ШТОРЫ.'],[69.8,'— НЕ ВЫХОДИТЕ НА УЛИЦУ.'],[71.6,'— НЕ СМОТРИТЕ ВВЕРХ.'],[74.0,'— НЕ МОЛИТЕСЬ ВСЛУХ.']];
function card(g,t){g.fillStyle='#000';g.fillRect(0,0,RW,RH);g.fillStyle='#e8e4d8';g.fillRect(0,16,RW,30);text(g,'НЕ СМОТРИТЕ НА НЕБО',RW/2,23,{align:'center',size:14,color:'#141414',shadow:false});
  STEPS.forEach(([t0,s],i)=>{if(t>=t0)text(g,s,40,66+i*24,{size:11})});if(t>=78.8){text(g,'ОН ОТВЕЧАЕТ.',RW/2,170,{align:'center',size:13,color:Math.floor(t*3)%2?'#ffffff':'#a0a0a0'})}}
function only(g){field.visible=g===field;church.visible=g===church;angel.visible=g===field}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.6,mode='vhs';const fr=Math.floor(t*FPS);
  if(t<.6){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);text(ctx,'▶ PLAY',20,18,{size:16});mode='none'}
  else if(t<6.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА, ВИСКОНСИН',RW/2,96,t,1.0,{align:'center',size:12});typed(ctx,'АРХИВНАЯ ЗАПИСЬ №6',RW/2,116,t,2.4,{align:'center',size:10,color:'#a0a0a0'})}
  else if(t<24.0||(t>=40.6&&t<64.0)||t>=104){only(field);scene.fog.near=10;scene.fog.far=t>=40.6&&t<64?lerp(90,260,P(t,40.6,56)):90;
    const near=t>=40.6&&t<64;angel.visible=near&&t>=47||(t>=104&&t>=111.4);skyL.intensity=near?lerp(1,3,P(t,40.6,56)):1;
    glow.visible=!angel.visible;glow.material.opacity=1;
    // глаза: закрыты (сплющены) — и все разом открываются
    const open=t>=56.0&&t<64||t>=111.4;eyes.forEach((e,i)=>{e.scale.set(1,open?1:.08+.04*Math.sin(t*2+i),1);e.lookAt(camera.position)});angel.rotation.z=Math.sin(t*.2)*.05;
    if(t<24){const k=P(t,6,24);cam([lerp(-4,-2,k),1.6,lerp(10,4,k)],[lerp(-10,4,k),lerp(4,20,k),-80])}
    else if(t<64){const k=P(t,40.6,56);const z=lerp(0,-60,eInOut(k)),sh=t>=56?(hash(fr,3)-.5)*.6*(1-P(t,56,59)):0;cam([sh+lerp(0,4,k),lerp(1.6,6,k),z],[8,lerp(14,40,k),-120]);
      if(t>=59.6){cam([4,6,-60],[8,40,-120]);camera.fov=lerp(58,22,eIn(P(t,59.6,63.8)));camera.updateProjectionMatrix()}vamt=t>=56?1.2+P(t,59.6,64)*1.5:.6}
    else{const k=P(t,104,118);cam([0,1.6,lerp(6,4,k)],[lerp(6,8,k),lerp(10,36,eInOut(P(t,107,111))),-110]);vamt=t>=111.4?2:.7}
    draw3D(scene,camera,ctx);camera.fov=58;camera.updateProjectionMatrix();dither(ctx);if(t>=56.0&&t<56.15){ctx.fillStyle='#fff';ctx.fillRect(0,0,RW,RH)}}
  else if(t<40.6||(t>=84&&t<104)){only(church);scene.fog.near=8;scene.fog.far=30;const tape=t<40.6;
    const glowK=tape?P(t,30,40):.05;winM.forEach(m=>m.color.copy(col('#403020').lerp(col('#ffffff'),glowK)));outL.intensity=tape?glowK*14:0;candleL.intensity=tape?3*(1-glowK*.6)+hash(fr,2)*.6:0;amb.intensity=tape?.45:.9;
    pastor.visible=tape;flock.forEach(p=>p.visible=!tape);
    if(tape){mode='cam';pose(pastor,{face:'normal',ax1:-.6+Math.sin(t*2)*.2*(t<35),hy:t>=38?lerp(0,1.2,P(t,38,39)):0});const sh=(hash(fr,4)-.5)*.02;cam([.4+sh,1.6,lerp(1.6,.4,P(t,24,40))],[-1.6,1.55,-4.3]);vamt=t>=38.6?.8+P(t,38.6,40.6)*2.5:.6}
    else{const turn=P(t,96.4,101.6);flock.forEach((p,i)=>{p.rotation.y=Math.PI+lerp(0,Math.PI,eInOut(clamp(turn*1.4-i*.04)));pose(p,{face:'normal'})});
      const k=P(t,84,104);cam([0,1.8,lerp(5.4,4.4,k)],[0,1.2,-4]);vamt=t>=101?1+P(t,101,104)*2:.6}
    draw3D(scene,camera,ctx);dither(ctx);if(tape&&t>=39.9){ctx.fillStyle='#fff';ctx.fillRect(0,0,RW,RH)}}
  else if(t<84.0){card(ctx,t);vamt=t>=74?.9:.6}
  if(mode==='vhs')osdVHS(ctx,t);if(mode==='cam')osdCam(ctx,t);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  vhs(ctx,t,vamt)}
