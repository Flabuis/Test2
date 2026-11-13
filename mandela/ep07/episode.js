// Том 7 «Каталог» — финал. Сценарий: SCENARIO.md (автор — пользователь). История 7:00, особые интро и аутро.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,subtitle,vhs,dither,snow,makePerson,pose,canvas2d} from '../common/core.js';
import {roomFromTV} from '../common/finale.js';
import {drawEp as ep2} from '../ep02/episode.js';
import {drawEp as ep3} from '../ep03/episode.js';
import {drawEp as ep4,smile} from '../ep04/episode.js';
import {drawEp as ep6} from '../ep06/episode.js';

export const VOL=7, D=420;
// R — диктор, X — искажённый, A — альтернат, M — пастор Хейл, F — «мама» Эммы, r — настоящий голос диктора, тихо и издалека
export const CAPS=[
  [9.0,13.6,'R','Внимание. Это последний выпуск для жителей округа Мандела.'],
  [14.2,19.0,'R','С осени девяносто первого в офис шерифа поступило четыреста двенадцать заявлений о пропаже.'],
  [19.8,22.4,'R','Пропавших сегодня — ноль.'],
  [23.2,25.4,'R','Вернулись все.'],
  [28.0,33.0,'R','Семья Уэйдов вернулась в свой дом. Лили больше не боится коридора.'],
  [34.0,38.6,'R','Эмма Коул открыла дверь. Мама больше не мёрзнет.'],
  [39.6,44.4,'R','Беккеры снова празднуют день рождения. Их снова пятеро.'],
  [45.6,49.8,'X','Прихожане вернулись из церкви. Они улыбаются.'],
  [52.0,56.6,'R','Мы называли их альтернатами. Мы учили вас их узнавать.'],
  [57.4,61.0,'R','Мы ошиблись в одном.'],
  [62.0,66.0,'R','Мы думали, что они приходят из леса.'],
  [68.0,72.6,'R','Они приходят туда, где включён телевизор.'],
  [78.0,83.0,'R','Офис шерифа собрал все записи в одно дело. Мы назвали его — Каталог.'],
  [83.8,88.6,'R','Кассеты копировали и раздавали по домам. Чтобы каждый знал правила.'],
  [89.6,93.4,'R','Сто сорок копий за одну неделю.'],
  [95.0,99.6,'X','Каждая копия — ещё одна дверь.'],
  [101.0,106.2,'R','Дежурный, который их выключил, не пришёл на смену. Он пришёл через неделю.'],
  [107.0,111.0,'X','Он сделал ещё сорок копий.'],
  [113.0,117.6,'R','Каждое оповещение. Каждая инструкция. Каждое «не смотрите».'],
  [118.4,122.2,'R','Чтобы предупредить вас, мы показывали их вам.'],
  [123.2,126.4,'A','Спасибо, что смотрели.'],
  [130.0,134.6,'R','В томе четыре мы просили вас выключить кассету.'],
  [135.4,138.0,'R','Вы не выключили.'],
  [139.0,143.4,'X','Никто не выключил.'],
  [146.0,151.0,'R','Внимание. Ниже — последняя запись пастора Хейла. Она пришла к нам без отправителя.'],
  [175.0,179.6,'M','Он обещал, что умершие вернутся. И они вернулись.'],
  [180.4,184.6,'M','Миссис Ли сидит на своём месте. Она умерла в восемьдесят седьмом.'],
  [185.6,189.4,'M','Она знает все псалмы. Она поёт громче всех.'],
  [191.0,194.4,'M','Но она не моргает.'],
  [198.0,202.6,'M','Я понял, что он делает. Он не воскрешает.'],
  [203.6,206.0,'M','Он копирует.'],
  [208.0,213.4,'M','Каждый, кто смотрел на свет, отдал ему своё лицо. Каждый, кто ответил, — свой голос.'],
  [214.4,219.0,'M','А каждый, кто смотрел запись, — свои глаза.'],
  [221.0,225.6,'M','Ангел не просит открыть дверь. Я говорил это вам.'],
  [226.4,229.0,'M','Я ошибался.'],
  [230.0,234.0,'M','Ему не нужна дверь. Ему нужен экран.'],
  [237.0,240.6,'M','Они встают. Все сразу.'],
  [244.0,246.2,'A','Не бойтесь.'],
  [250.0,254.6,'M','Если вы досмотрели до этого места — ему осталось немного.'],
  [255.4,258.4,'M','Не смотрите вве...'],
  [262.0,264.6,'A','Посмотри.'],
  [273.0,277.6,'R','Я больше не буду читать по бумажке.'],
  [278.6,283.4,'R','В здании я один. Ночная смена не пришла. Утренняя — тоже.'],
  [284.6,289.4,'R','Я вёл этот выпуск три месяца. Я сам записал «всё это зря».'],
  [290.2,293.0,'R','Я не помню, как.'],
  [295.0,300.6,'R','Вы вставляли эти кассеты по одной. Каждый раз одной и той же рукой.'],
  [301.6,305.0,'R','Посмотрите на неё сейчас.'],
  [307.0,310.4,'R','Сколько у вас пальцев?'],
  [314.0,318.6,'R','Если вы видите это — значит, седьмая кассета дошла до вас.'],
  [319.4,323.4,'R','Я её не записывал.'],
  [326.0,330.6,'R','Последнее правило. Самое важное.'],
  [331.4,335.0,'R','Кто бы ни подал вам следующую кассету —'],
  [336.0,339.4,'X','возьмите её.'],
  [341.0,345.4,'R','Нет. Не берите. Не...'],
  [347.0,351.0,'A','Не оборачивайтесь. Я сяду рядом.'],
  [364.0,368.6,'X','Округ Мандела. Тихое место. Леса, озёра, несколько тысяч жителей.'],
  [369.6,373.4,'X','Пропавших нет. Все дома.'],
  [376.0,379.6,'F','Привет, солнышко. Это мама.'],
  [382.0,386.4,'A','Ты смотрел шесть кассет. Ты смотришь седьмую.'],
  [387.4,391.0,'A','Мы смотрели на тебя всё это время.'],
  [395.0,399.0,'A','Теперь твоя очередь подать кассету.'],
  [404.0,407.0,'A','Открой дверь.'],
  [410.0,413.0,'r','...не оборачивайтесь.']];

const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(56,RW/RH,.05,120);
const amb=new THREE.AmbientLight(0x6070a0,.35);scene.add(amb);scene.fog=new THREE.Fog(0x05070f,6,26);scene.background=new THREE.Color(0x05070f);
const N=(p,s,r=[1,1])=>tex(16,16,(g,w,h)=>noise(g,w,h,p,s),r);
function screenCanvas(w=64,h=48){const c=document.createElement('canvas');c.width=w;c.height=h;const tx=new THREE.CanvasTexture(c);tx.magFilter=tx.minFilter=THREE.NearestFilter;tx.generateMipmaps=false;tx.colorSpace=THREE.SRGBColorSpace;return{c,g:c.getContext('2d'),tx}}
function monitor(w=.7,h=.56){const g=new THREE.Group();g.add(box(w,h,.5,M({map:N(['#2a2a2c','#262628'],100)})));const s=screenCanvas();const sc=new THREE.Mesh(new THREE.PlaneGeometry(w*.72,h*.68),new THREE.MeshBasicMaterial({map:s.tx,toneMapped:false,fog:false}));sc.position.z=.256;g.add(sc);g.userData.s=s;return g}
const [epC,epX]=canvas2d();   // кадры чужих томов для флешбэков и мониторов

// ---------- студия ----------
const studio=new THREE.Group();scene.add(studio);let anchor,chair,tall;const mons=[];const deskL=new THREE.PointLight(0xffe0b0,3,6,1.3),figL=new THREE.PointLight(0x8090b0,0,4,1.5);
{const fl=box(14,.05,14,M({map:N(['#1e1e22','#1a1a1e'],110,[6,6])}));studio.add(fl);
 const logo=screenCanvas(128,48);{const g=logo.g;g.fillStyle='#0a1430';g.fillRect(0,0,128,48);g.fillStyle='#c8b060';g.fillRect(6,10,26,28);g.fillStyle='#0a1430';g.fillRect(17,14,4,20);g.fillRect(10,20,18,4);
   g.fillStyle='#e8e4d8';g.font='bold 11px monospace';g.fillText('ОКРУГ МАНДЕЛА',38,22);g.font='9px monospace';g.fillText('ЭКСТРЕННЫЙ ЭФИР',38,36);logo.tx.needsUpdate=true}
 const bd=new THREE.Mesh(new THREE.PlaneGeometry(4,1.5),new THREE.MeshBasicMaterial({map:logo.tx,fog:false,color:0x8090a0}));bd.position.set(0,2.6,-3.4);studio.add(bd);
 const wall=box(14,5,.1,M({color:0x14161c}));wall.position.set(0,2.5,-3.5);studio.add(wall);
 for(let i=0;i<3;i++){const m=monitor();m.position.set(-1.2+i*1.2,1.35,-3.1);studio.add(m);mons.push(m)}
 const desk=box(2.0,.08,.9,M({color:0x3a3028}));desk.position.set(0,.78,-.75);studio.add(desk);const dl=box(1.9,.74,.8,M({color:0x2a2420}));dl.position.set(0,.37,-.75);studio.add(dl);
 const paper=box(.3,.01,.4,M({color:0xe8e4d8}));paper.position.set(.2,.83,-.6);studio.add(paper);
 chair=new THREE.Group();const seat=box(.6,.12,.6,M({color:0x1a1a1e}));seat.position.y=.5;chair.add(seat);const bk=box(.6,.8,.1,M({color:0x1a1a1e}));bk.position.set(0,.95,.3);chair.add(bk);const pole=box(.08,.45,.08,M({color:0x5a5a5e}));pole.position.y=.25;chair.add(pole);
 anchor=makePerson({shirt:['#2a2e3a','#262a34'],pants:['#2a2e3a','#262a34'],hair:['#3a3a3a','#333333'],faces:{normal:(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],120);g.fillStyle='#3a3a3a';g.fillRect(0,0,16,3);g.fillStyle='#1a1a1a';g.fillRect(4,7,2,2);g.fillRect(10,7,2,2);g.fillStyle='#8a5a4a';g.fillRect(6,11,4,1);g.fillStyle='rgba(60,40,40,.4)';g.fillRect(3,9,3,1);g.fillRect(10,9,3,1)}}});
 const tie=box(.06,.4,.02,M({color:0x6a1a1a}));tie.position.set(0,1.3,.17);anchor.add(tie);anchor.position.set(0,-.28,.05);chair.add(anchor);chair.position.set(0,0,0);studio.add(chair);
 const tl=new THREE.Group();{const cl=M({map:N(['#16161a','#121216'],60)}),sk=M({map:N(['#d8d4cc','#cecac2'],61)});for(const s of[-1,1]){const l=box(.12,1.4,.14,cl);l.position.set(s*.1,.7,0);tl.add(l);const a=box(.09,1.35,.1,cl);a.position.set(s*.25,1.6,0);tl.add(a)}
   const t=box(.36,.95,.2,cl);t.position.y=1.85;tl.add(t);const hd=box(.24,.3,.24,sk);hd.position.y=2.6;tl.add(hd)}tall=tl;tall.position.set(-1.0,0,-2.4);studio.add(tall);
 deskL.position.set(.4,1.9,.9);studio.add(deskL);figL.position.set(-.6,2.4,-1.8);studio.add(figL);
 for(const s of[-1,1]){const st=box(.06,2.2,.06,M({color:0x3a3a3e}));st.position.set(s*2.4,1.1,1.2);studio.add(st);const lh=box(.4,.3,.3,M({color:0x2a2a2e}));lh.position.set(s*2.4,2.25,1.2);studio.add(lh)}}

// ---------- архив офиса шерифа ----------
const archive=new THREE.Group();scene.add(archive);const copyMons=[];const arcL=new THREE.PointLight(0xfff0d0,4,9,1.3),arcL2=new THREE.PointLight(0xfff0d0,3,9,1.3);
{const fl=box(6,.05,30,M({map:N(['#3a3a3c','#363638'],130,[4,16])}));fl.position.z=-10;archive.add(fl);const r=mulberry(131);
 const tapeM=M({map:N(['#141416','#18181a'],132)}),lab=[1,2,3,4,5,6].map(n=>M({map:tex(8,16,(g)=>{g.fillStyle='#d8d4c8';g.fillRect(0,0,8,16);g.fillStyle='#a82020';g.fillRect(0,0,8,2);g.fillStyle='#141414';g.font='bold 7px monospace';g.fillText(String(n),2,12)})}));
 for(const sx of[-1.5,1.5])for(let seg=0;seg<5;seg++){const z0=-2-seg*4.4;const frame=box(.5,2.6,.06,M({color:0x5a5a5e}));frame.position.set(sx,1.3,z0+2.1);archive.add(frame);
   for(let lv=0;lv<5;lv++){const sh=box(.5,.04,4.2,M({color:0x6a6a6e}));sh.position.set(sx,.2+lv*.52,z0);archive.add(sh);
     for(let k=0;k<18;k++){const tp=box(.3,.19,.07,tapeM);tp.position.set(sx+(sx<0?.06:-.06),.32+lv*.52,z0-1.9+k*.22);archive.add(tp);const lb=box(.005,.12,.05,lab[Math.floor(r()*6)]);lb.position.set(sx+(sx<0?.215:-.215),.32+lv*.52,z0-1.9+k*.22);archive.add(lb)}}}
 const tbl=box(2.6,.06,1.0,M({color:0x5a4a3a}));tbl.position.set(0,.76,-24);archive.add(tbl);const tl=box(2.5,.74,.9,M({color:0x4a3a2a}));tl.position.set(0,.37,-24);archive.add(tl);
 for(let i=0;i<4;i++){const v=box(.5,.1,.36,M({color:0x1a1a1c}));v.position.set(-.9+i*.6,.84,-23.8);archive.add(v);const m=monitor(.5,.4);m.position.set(-.9+i*.6,1.12,-24.1);archive.add(m);copyMons.push(m)}
 const ec=new THREE.Group();const s=box(.5,.08,.5,M({color:0x3a2a20}));s.position.y=.45;ec.add(s);const b=box(.5,.6,.06,M({color:0x3a2a20}));b.position.set(0,.8,.25);ec.add(b);for(const x of[-.2,.2])for(const z of[-.2,.2]){const l=box(.04,.45,.04,M({color:0x3a2a20}));l.position.set(x,.22,z);ec.add(l)}
 ec.position.set(.4,0,-23.0);ec.rotation.y=.3;archive.add(ec);arcL.position.set(0,2.6,-8);archive.add(arcL);arcL2.position.set(0,2.4,-22);archive.add(arcL2)}

// ---------- церковь (запись пастора) ----------
const church=new THREE.Group();scene.add(church);let pastor;const flock=[];const winM=[];const chL=new THREE.PointLight(0xffd0a0,3,10,1.2),winL=new THREE.PointLight(0xe8f0ff,0,14,1.2);
const SMILE=(g,w,h)=>{noise(g,w,h,['#d8b8a0','#d0b098'],11);g.fillStyle='#3a2a1e';g.fillRect(0,0,32,6);g.fillStyle='#000';g.fillRect(8,11,4,4);g.fillRect(20,11,4,4);
  g.fillStyle='#2a0a08';g.fillRect(5,21,22,3);g.fillRect(4,19,2,3);g.fillRect(26,19,2,3);g.fillStyle='#f0ece0';for(let x=6;x<26;x+=2)g.fillRect(x,21,1,2)};
const LEE=(g,w,h)=>{SMILE(g,w,h);g.fillStyle='#b8b8b8';g.fillRect(0,0,32,7);g.fillRect(0,7,3,10);g.fillRect(29,7,3,10)};
{const fl=box(8,.05,14,M({map:N(['#4a3a2a','#443424'],80,[4,8])}));church.add(fl);const wm=M({map:N(['#8a8478','#827c70'],81,[4,2])});
 for(const [w,d,x,z] of[[8,.1,0,-6],[.1,14,-4,0],[.1,14,4,0],[8,.1,0,6]]){const b=box(w,5,d,wm);b.position.set(x,2.5,z);church.add(b)}
 for(const z of[-3,0,3])for(const s of[-1,1]){const m=new THREE.MeshBasicMaterial({color:0x605040});const w=box(.05,1.8,.8,m);w.position.set(s*3.94,2.6,z);church.add(w);winM.push(m)}
 for(let rI=0;rI<5;rI++)for(const s of[-1,1]){const pw=box(2.6,.5,.5,M({color:0x5a4030}));pw.position.set(s*1.8,.45,1.0+rI*1.3);church.add(pw);const bk=box(2.6,.6,.08,M({color:0x5a4030}));bk.position.set(s*1.8,.9,1.24+rI*1.3);church.add(bk)}
 pastor=makePerson({shirt:['#141416','#18181a'],pants:['#141416','#18181a'],faces:{normal:(g,w,h)=>{noise(g,w,h,['#d4ac8c','#cca486'],90);g.fillStyle='#8a8a8a';g.fillRect(0,0,16,3);g.fillStyle='#1a1a1a';g.fillRect(4,7,2,2);g.fillRect(10,7,2,2);g.fillStyle='#6a3a2a';g.fillRect(6,11,4,1);g.fillStyle='rgba(80,40,40,.5)';g.fillRect(3,9,3,1);g.fillRect(10,9,3,1)}}});
 const col_=box(.2,.06,.05,M({color:0xffffff}));col_.position.set(0,1.56,.17);pastor.add(col_);pastor.position.set(-.5,0,-1.2);pastor.rotation.y=Math.PI;church.add(pastor);
 const r=mulberry(91);let first=true;for(let rI=0;rI<4;rI++)for(const s of[-1,1])for(let k=0;k<2;k++){if(r()<.15)continue;const lee=first&&s<0;first=false;
   const p=makePerson({shirt:lee?['#5a4a6a','#524262']:[['#4a5a6a','#425262'],['#6a4a4a','#624242'],['#4a6a4a','#426242'],['#5a5a5a','#525252']][Math.floor(r()*4)],faceSize:32,faces:{normal:lee?LEE:SMILE}});
   p.position.set(s*1.8+(k-.5)*1.1,0,1.0+rI*1.3-.25);p.rotation.y=Math.PI;church.add(p);flock.push(p)}
 chL.position.set(0,2.4,-3);church.add(chL);winL.position.set(3.2,2.6,1.5);church.add(winL)}

// ---------- 2D ----------
function typed(g,s,x,y,t,t0,o){const n=Math.floor((t-t0)*28);if(n<=0)return;text(g,s.slice(0,n),x,y,o)}
function osdAir(g,t){text(g,'ЭФИР ●',12,10,{size:10,color:Math.floor(t*2)%2?'#ff4040':'#a02020'});text(g,'ФЕВ 29 1992',RW-12,10,{align:'right',size:9});const s=Math.floor(t);text(g,`04:${String(Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`,RW-12,20,{align:'right',size:9})}
function osdCam(g,t){if(Math.floor(t*2)%2){g.fillStyle='#ff2020';g.beginPath();g.arc(16,15,4,0,7);g.fill()}text(g,'REC',24,10,{size:10,color:'#ff4040'});text(g,'??.??.92',12,RH-36,{size:9})}
function sepia(g,k=1){const d=g.getImageData(0,0,RW,RH),a=d.data;for(let i=0;i<a.length;i+=4){const l=a[i]*.3+a[i+1]*.59+a[i+2]*.11;a[i]=lerp(a[i],l*1.1,k);a[i+1]=lerp(a[i+1],l*.88,k);a[i+2]=lerp(a[i+2],l*.62,k)}g.putImageData(d,0,0)}
function flash(ctx,fn,tt){fn(tt,epX);ctx.drawImage(epX.canvas,0,0);sepia(ctx,.9);ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(0,0,RW,RH)}
function only(g){studio.visible=g===studio;archive.visible=g===archive;church.visible=g===church}
function cam(p,l){camera.position.set(...p);camera.lookAt(...l)}
function copyScreen(g,t,i){g.fillStyle='#0a1040';g.fillRect(0,0,64,48);g.fillStyle='#e8e4d8';g.font='bold 7px monospace';g.fillText('КОПИЯ',4,12);g.fillText(String(100+i*13+Math.floor(t/3)%13),38,12);
  g.fillText(`ТОМ ${1+(i+Math.floor(t/5))%6}`,4,24);g.fillStyle='#333';g.fillRect(4,32,56,6);g.fillStyle='#7aff8a';g.fillRect(4,32,Math.round(56*((t*.13+i*.27)%1)),6)}
function monScreen(m,t,kind){const g=m.userData.s.g;if(kind==='smile')smile(g,t,64,48,.9);else if(kind==='warn'){ep4(52.6+((t*.7)%5),epX);g.drawImage(epX.canvas,0,0,64,48)}
  else if(kind==='snow'){const d=g.getImageData(0,0,64,48),a=d.data,fr=Math.floor(t*FPS*2);for(let i=0;i<a.length;i+=4){const v=hash(i,fr)*200;a[i]=a[i+1]=a[i+2]=v;a[i+3]=255}g.putImageData(d,0,0)}
  else if(kind==='air'){g.fillStyle='#0a1430';g.fillRect(0,0,64,48);g.fillStyle='#c8b060';g.fillRect(26,8,12,14);g.fillStyle='#e8e4d8';g.font='bold 7px monospace';g.fillText('ПОСЛЕДНИЙ',8,32);g.fillText('ВЫПУСК',16,42)}
  else if(kind==='off'){g.fillStyle='#08090a';g.fillRect(0,0,64,48)}else kind(g);m.userData.s.tx.needsUpdate=true}
// склейки в записи пастора: головы прихожан меняют положение синхронно, по одной позиции за склейку
const HEADS=[[0,0],[.35,0],[.35,.15],[-.3,0],[0,.25],[-.45,-.1],[0,0]];
function churchCut(t){return Math.floor((t-152)/8)}

// ---------- кадр серии ----------
export function drawEp(t,ctx){t=Math.floor(t*FPS+1e-6)/FPS;let vamt=.5,mode='air';const fr=Math.floor(t*FPS);
  if(t<7.0){ctx.fillStyle='#1830a0';ctx.fillRect(0,0,RW,RH);typed(ctx,'ОКРУГ МАНДЕЛА.',RW/2,82,t,.6,{align:'center',size:14});typed(ctx,'ПОСЛЕДНИЙ ВЫПУСК.',RW/2,106,t,1.8,{align:'center',size:12});typed(ctx,'ФЕВРАЛЬ 1992',RW/2,132,t,3.0,{align:'center',size:10,color:'#c8c8e8'});mode='none'}
  // ---- акт 1: студия, диктор спиной; флешбэки в сепии ----
  else if(t<75.0){const FB=[[29.0,31.6,ep2,64.0],[35.0,37.6,ep3,113.4],[40.4,43.0,ep4,46.65],[46.0,48.6,ep6,103.0]];const fb=FB.find(f=>t>=f[0]&&t<f[1]);
    if(fb){flash(ctx,fb[2],fb[3]+(t-fb[0])*.3);mode='none';vamt=.6}
    else{only(studio);chair.rotation.y=Math.PI;anchor.visible=true;tall.visible=false;figL.intensity=0;mons.forEach((m,i)=>monScreen(m,t,t<25.4||i===1?'air':'snow'));pose(anchor,{face:'normal',l0:-1.5,l1:-1.5,ax0:-1.0,ax1:-1.0,hx:.25});
      deskL.intensity=3+hash(fr,2)*.3;const k=P(t,7,75);cam([lerp(.9,.5,k),1.75,lerp(2.6,1.6,k)],[0,1.4,-3.2]);draw3D(scene,camera,ctx);dither(ctx);vamt=t>=45.6&&t<49.8?1:.5}}
  // ---- акт 2: архив, копии ----
  else if(t<146.0){only(archive);mode='air';
    const kind=(t>=123.2&&t<127.4)?'smile':(t>=130&&t<143.4)?'warn':null;copyMons.forEach((m,i)=>monScreen(m,t,kind||((g)=>copyScreen(g,t,i))));
    let p,l;if(t<110){const k=P(t,75,110);p=[0,1.6,lerp(1,-17,eInOut(k))];l=[0,1.2,lerp(-6,-24,k)]}else{const k=P(t,110,146);p=[lerp(.3,-.2,k),lerp(1.6,1.45,k),lerp(-17,-21.6,eInOut(P(t,110,124)))];l=[0,1.05,-24]}
    cam(p,l);draw3D(scene,camera,ctx);dither(ctx);vamt=kind==='smile'?1.6:t>=139&&t<143.4?1.2:.5}
  else if(t<152.0){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);typed(ctx,'ПОСЛЕДНЯЯ ЗАПИСЬ ПАСТОРА ХЕЙЛА',RW/2,96,t,146.2,{align:'center',size:11});typed(ctx,'ОТПРАВИТЕЛЬ: —',RW/2,116,t,148.0,{align:'center',size:10,color:'#a0a0a0'});mode='air'}
  // ---- акт 3: запись из церкви, статичная камера ----
  else if(t<270.0){mode='cam';
    if(t<256.8){only(church);const ci=churchCut(t),hd=HEADS[ci%HEADS.length],stand=t>=237.6;const glowK=P(t,152,256);
      winM.forEach(m=>m.color.copy(col('#605040').lerp(col('#ffffff'),glowK)));winL.intensity=glowK*10;chL.intensity=3*(1-glowK*.5);amb.intensity=.5;
      flock.forEach(p=>{pose(p,stand?{face:'normal',hy:hd[0],hz:hd[1]}:{face:'normal',l0:-1.5,l1:-1.5,hy:hd[0],hz:hd[1]});p.position.y=stand?0:-.4});
      pose(pastor,{face:'normal',ax1:t<250?-.5+Math.sin(t*1.7)*.15:-.2,hx:t>=255.4?-.5:0});const sh=(hash(fr,4)-.5)*.015;cam([.3+sh,1.65,-4.6],[0,1.35,2.5]);draw3D(scene,camera,ctx);dither(ctx);
      if(((t-152)%8)<.14&&t>153)snow(ctx,t,.6);vamt=t>=250?.8+P(t,250,256.8)*1.4:.55}
    else if(t<259.0){ctx.fillStyle=`rgb(${255},${255},${255})`;ctx.fillRect(0,0,RW,RH);if(t<257.6){only(church);cam([.3,1.65,-4.6],[0,1.35,2.5]);draw3D(scene,camera,ctx);ctx.fillStyle=`rgba(255,255,255,${Math.round(P(t,256.8,257.6)*16)/16})`;ctx.fillRect(0,0,RW,RH)}vamt=.3}
    else if(t<259.5){ep6(56.7+(t-259)*2,epX);ctx.drawImage(epX.canvas,0,0);mode='none';vamt=2.5}
    else if(t<264.6){ctx.fillStyle='#f4f4f4';ctx.fillRect(0,0,RW,RH);snow(ctx,t,P(t,259.5,264.6)*.9+.1);vamt=1.5}
    else{ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);snow(ctx,t,.5*(1-P(t,268,270)));mode='none';vamt=1}}
  // ---- акт 4: студия, диктор говорит от себя ----
  else if(t<360.0){only(studio);mode='air';const gone=t>=345.8;anchor.visible=!gone;chair.rotation.y=lerp(Math.PI,0,eInOut(P(t,271.2,273.4)));
    pose(anchor,{face:'normal',l0:-1.5,l1:-1.5,ax0:-.9,ax1:t>=301.6&&t<311?-1.6:-.9,az1:t>=301.6&&t<311?-.3:.06,hx:.05});
    tall.visible=t>=278;tall.position.set(gone?-.2:-1.0,0,gone?-1.6:-2.4);figL.intensity=t>=278?lerp(0,.8,P(t,278,330)):0;
    mons.forEach((m,i)=>monScreen(m,t,t>=345.8&&t<350?'smile':t>=336?'snow':'off'));deskL.intensity=(gone?1.4:3)*(t>=336&&hash(fr,6)<.15?.3:1);
    const k=P(t,270,345);cam([lerp(.5,.2,k),1.65,lerp(1.6,1.05,k)],[0,1.45,-1.5]);draw3D(scene,camera,ctx);dither(ctx);vamt=t>=336&&t<345.8?.9+P(t,336,345.4)*1.8:.5;
    if(t>=345.4&&t<345.8){snow(ctx,t,.9);vamt=3}if(t>=357.6){snow(ctx,t,P(t,357.6,360));vamt=2}}
  // ---- акт 5: наша комната, вид изнутри телевизора ----
  else{mode='none';const reach=t>=395?eInOut(P(t,395,399)):0;const door=t>=404?eOut(P(t,404,409))*.6:0;roomFromTV(t,ctx,{reach,door,dim:t>=404&&t<410?.4:1});dither(ctx);vamt=t<362?1.6-P(t,360,362):.45;
    if(t>=413){ctx.fillStyle=`rgba(0,0,0,${Math.round(P(t,413,419)*.7*16)/16})`;ctx.fillRect(0,0,RW,RH)}}
  if(mode==='air')osdAir(ctx,t);if(mode==='cam')osdCam(ctx,t);
  for(const [a,b,,s] of CAPS)subtitle(ctx,s,t,a,b);
  vhs(ctx,t,vamt)}
