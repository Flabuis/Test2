// Особое интро и аутро финала (том 7) + вид на комнату «изнутри телевизора» (акт 5). Обычные интро/аутро не трогает.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,tex,noise,text,snow,hardAlpha,MONO} from './core.js';
import {STAGE} from './stage.js';
const {scene,camera,tapes,scrX,scrTex,tvL,amb,spot,slotLed,handL,SCR,rest,cameraFor,screenNoise,VOLX,hand}=STAGE;

export const INTRO7=18, OUTRO7=10;

// ---------- серая рука с длинными пальцами ----------
const GT={sk:tex(8,8,(g,w,h)=>noise(g,w,h,['#8a8c90','#828488','#929498','#7a7c80'],201)),skd:tex(8,8,(g,w,h)=>noise(g,w,h,['#6a6c70','#646668','#707276'],202)),
  nail:tex(4,4,(g,w,h)=>noise(g,w,h,['#3a3a3c','#2e2e30'],203))};
export function makeGreyHand(){const g=new THREE.Group(),sk=M({map:GT.sk}),skd=M({map:GT.skd}),nl=M({map:GT.nail}),fingers=[],thumb=[];
  const arm=box(.07,.06,.7,sk);arm.position.set(0,0,.4);g.add(arm);const wr=box(.08,.055,.06,skd);wr.position.set(0,0,.03);g.add(wr);
  const palm=box(.1,.035,.13,sk);palm.position.set(0,0,-.065);g.add(palm);
  [[-.036,.08],[-.012,.09],[.012,.086],[.035,.07]].forEach(([x,L])=>{let parent=g;const segs=[];
    [L,L*.75,L*.65].forEach((l,k)=>{const j=new THREE.Group();j.position.set(k?0:x,0,k?-segs[k-1].l:-.13);parent.add(j);const s=box(.016,.016,l,k%2?skd:sk);s.position.z=-l/2;j.add(s);
      if(k===2){const n=box(.014,.006,.02,nl);n.position.set(0,.009,-l+.008);j.add(n)}segs.push({j,l});parent=j});fingers.push(segs)});
  let parent=g;[[.06,.4],[.05,.25]].forEach(([l],k)=>{const j=new THREE.Group();if(!k){j.position.set(-.05,-.006,-.03);j.rotation.set(0,.8,0)}else j.position.z=-.06;parent.add(j);
    const s=box(.018,.016,l,sk);s.position.z=-l/2;j.add(s);thumb.push(j);parent=j});
  g.userData.curl=k=>{fingers.forEach((f,i)=>f.forEach((s,j)=>s.j.rotation.x=-k*(.6+.2*j)));thumb[0].rotation.x=-k*.3;thumb[1].rotation.x=-k*.5};return g}

// ---------- кассета «7» (без наклейки, маркером) и восьмая без номера ----------
function blankTape(mark){const bm=M({map:tex(8,8,(g,w,h)=>noise(g,w,h,['#1c1c1e','#19191b'],204))});
  const top=mark?M({map:tex(64,32,(g)=>{g.fillStyle='#161618';g.fillRect(0,0,64,32);g.strokeStyle='#e8e8e0';g.lineWidth=3;g.beginPath();g.moveTo(22,8);g.lineTo(40,8);g.lineTo(28,26);g.stroke()})}):bm;
  const spine=mark?M({map:tex(16,64,(g)=>{g.fillStyle='#161618';g.fillRect(0,0,16,64);g.strokeStyle='#e8e8e0';g.lineWidth=2;g.beginPath();g.moveTo(4,24);g.lineTo(12,24);g.lineTo(6,40);g.stroke()})}):bm;
  const t=new THREE.Group();t.add(box(.075,.56,.30,[bm,bm,top,bm,spine,bm]));return t}
const tape7=blankTape(true),tape8=blankTape(false);scene.add(tape7,tape8);tape7.visible=tape8.visible=false;
const ghand=makeGreyHand();ghand.scale.setScalar(2.6);ghand.visible=false;scene.add(ghand);
const eyes=new THREE.Group();for(const s of[-1,1]){const e=box(.06,.035,.02,new THREE.MeshBasicMaterial({color:0xff1010,fog:false}));e.position.set(s*.07,0,0);eyes.add(e)}eyes.position.set(-1.9,1.9,-.55);eyes.visible=false;scene.add(eyes);

// ---------- кресло и тот, кто в нём сидит (акт 5) ----------
const chair=new THREE.Group();const sitter=new THREE.Group();const handsL=makeGreyHand(),handsR=makeGreyHand();
{const cm=M({map:tex(8,8,(g,w,h)=>noise(g,w,h,['#3a2a28','#342624','#40302c'],205))});const seat=box(1.0,.45,.9,cm);seat.position.y=.25;chair.add(seat);const bk=box(1.0,1.0,.2,cm);bk.position.set(0,.85,.4);chair.add(bk);
 for(const s of[-1,1]){const a=box(.18,.55,.9,cm);a.position.set(s*.55,.45,0);chair.add(a)}
 const dk=M({color:0x08080a});const tor=box(.56,.8,.32,dk);tor.position.set(0,.95,.2);sitter.add(tor);const hd=box(.36,.42,.36,dk);hd.position.set(0,1.62,.18);sitter.add(hd);
 for(const s of[-1,1]){const lg=box(.18,.18,.6,dk);lg.position.set(s*.13,.55,-.15);sitter.add(lg);const sh=box(.16,.5,.18,dk);sh.position.set(s*.13,.25,-.42);sitter.add(sh)}
 chair.add(sitter);handsL.scale.setScalar(2.4);handsR.scale.setScalar(2.4);handsL.position.set(-.55,.78,.05);handsR.position.set(.55,.78,.05);chair.add(handsL,handsR);
 chair.position.set(.2,0,2.6);chair.visible=false;scene.add(chair)}
const backWall=box(8,4,.1,M({map:STAGE.TX.wall}));backWall.position.set(0,2,4.6);backWall.visible=false;scene.add(backWall);
const doorF=new THREE.Group();{const fr=M({color:0x2a1e16});for(const [w,h,x,y] of[[1.1,.08,0,2.1],[.08,2.1,-.55,1.05],[.08,2.1,.55,1.05]]){const b=box(w,h,.08,fr);b.position.set(x,y,0);doorF.add(b)}
  const d=box(1.0,2.05,.05,M({color:0x3a2a1e}));d.position.set(0,1.03,.02);doorF.add(d);doorF.userData.d=d}doorF.position.set(-1.6,0,4.52);doorF.rotation.y=Math.PI;doorF.visible=false;scene.add(doorF);
const roomL=new THREE.PointLight(0xa8c0ff,0,7,1.3);roomL.position.set(0,1.3,1.0);scene.add(roomL);
const tvCam=new THREE.PerspectiveCamera(66,RW/RH,.05,40);

function credits(t,ctx){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);const a=P(t,.3,.9)*(1-P(t,3.4,4.0));if(a<=0)return;ctx.globalAlpha=Math.round(a*8)/8;
  text(ctx,'по мотивам',RW/2,62,{align:'center',color:'#a0a0a0'});text(ctx,'THE MANDELA CATALOGUE',RW/2,84,{align:'center',size:16});text(ctx,'автор оригинала — Alex Kister',RW/2,112,{align:'center',color:'#d0d0d0'});
  text(ctx,'неофициальная фан-адаптация.',RW/2,156,{align:'center',size:9,color:'#808080'});text(ctx,'все права на оригинал принадлежат автору.',RW/2,168,{align:'center',size:9,color:'#808080'});ctx.globalAlpha=1;hardAlpha(ctx,1)}
function resetRoom(){chair.visible=backWall.visible=doorF.visible=false;roomL.intensity=0;hand.visible=false;eyes.visible=false;ghand.visible=false;tape7.visible=tape8.visible=false;
  tapes.forEach((tp,i)=>{tp.visible=true;tp.position.copy(rest(i+1));const r=mulberry(300+i);tp.rotation.set(0,(r()-.5)*.5,(r()-.5)*.35);tp.position.y+=r()*.02})}   // стоят криво

// ---------- особое интро ----------
export function introFinal(t,ctx,epFrame){if(t<4.0){credits(t,ctx);return}
  resetRoom();const fade=P(t,4.0,5.6);
  if(t<16.2)screenNoise(t,t<8?.8:.45);else if(t<16.4){scrX.fillStyle='#000';scrX.fillRect(0,0,RW,RH)}else scrX.drawImage(epFrame(0),0,0);scrTex.needsUpdate=true;
  const fl=.85+hash(Math.floor(t*FPS),3)*.3;tvL.intensity=(t<8?1.6:t<16.2?1.0:1.3)*fl*fade;amb.intensity=.25*fade;spot.intensity=t<4.8?0:t<4.9?3:7;slotLed.material.color.set(t>15.6?0xff2020:0x300000);
  // чужая рука из темноты слева с кассетой «7»
  const slot=new THREE.Vector3(-.12,.78,.46),YAW=-.85,off=new THREE.Vector3(Math.sin(YAW)*.5,.13,Math.cos(YAW)*.5);
  const from=new THREE.Vector3(-2.3,.95,.9),pre=slot.clone().add(new THREE.Vector3(0,0,.55)),inS=slot.clone().add(new THREE.Vector3(0,0,-.16)),deep=slot.clone().add(new THREE.Vector3(0,0,-.36));
  if(t>=12.0){let tp,c=1,hp=null;
    if(t<15.0)tp=from.clone().lerp(pre,eInOut(P(t,12.0,15.0)));else if(t<15.6)tp=pre.clone().lerp(inS,eInOut(P(t,15.0,15.6)));else{tp=inS.clone().lerp(deep,eOut(P(t,15.6,15.9)));c=.3;hp=inS.clone().add(off).lerp(from.clone().add(off),eIn(P(t,15.7,16.8)))}
    tape7.visible=true;tape7.position.copy(tp);tape7.rotation.set(0,0,Math.PI/2);ghand.visible=t<16.8;ghand.position.copy(hp||tp.clone().add(off));ghand.rotation.set(0,YAW,0);ghand.rotateX(-.1);ghand.userData.curl(c)}
  eyes.visible=t>=15.4&&t<16.5;
  const drift=P(t,8,12)*.25;cameraFor(eInOut(P(t,16.4,18.0)),drift);handL.position.copy(ghand.position).add(new THREE.Vector3(.4,.5,.6));handL.intensity=ghand.visible?.9:0;
  draw3D(scene,camera,ctx);if(fade<1){ctx.fillStyle=`rgba(0,0,0,${Math.round((1-fade)*16)/16})`;ctx.fillRect(0,0,RW,RH)}}

// ---------- особое аутро: в белый шум, чёрный, на секунду полка с 7 кассетами и восьмой ----------
export function outroFinal(t,ctx,epFrame,D){
  if(t<5.0){const k=P(t,0,3.0);ctx.drawImage(epFrame(D-.01),0,0);if(k>0){const a=ctx.globalAlpha;ctx.globalAlpha=Math.round(k*8)/8;const [c,g]=[document.createElement('canvas'),null];c.width=RW;c.height=RH;const cg=c.getContext('2d');snow(cg,t,1-P(t,3,5));ctx.drawImage(c,0,0);ctx.globalAlpha=a}
    if(t>=3.0){ctx.fillStyle=`rgba(0,0,0,${Math.round(P(t,3,5)*16)/16})`;ctx.fillRect(0,0,RW,RH)}return}
  if(t<6.0||t>=8.2){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);return}
  resetRoom();tapes.forEach((tp,i)=>{tp.rotation.set(0,0,0);tp.position.copy(rest(i+1))});tape7.visible=tape8.visible=true;tape7.position.copy(rest(7));tape7.rotation.set(0,0,0);tape8.position.copy(rest(8));tape8.rotation.set(0,0,0);
  scrX.fillStyle='#000';scrX.fillRect(0,0,RW,RH);scrTex.needsUpdate=true;tvL.intensity=0;amb.intensity=.15;spot.intensity=3.5;slotLed.material.color.set(0x300000);
  camera.position.set(1.6,1.15,1.7);camera.lookAt(1.45,.85,0);draw3D(scene,camera,ctx);const k=Math.min(P(t,6.0,6.6),1-P(t,7.6,8.2));ctx.fillStyle=`rgba(0,0,0,${Math.round((1-k)*16)/16})`;ctx.fillRect(0,0,RW,RH)}

// ---------- акт 5: наша комната, вид изнутри телевизора ----------
// o.reach: 0..1 — рука протягивает кассету к экрану; o.door: 0..1 — дверь за креслом приоткрывается
export function roomFromTV(t,ctx,o={}){resetRoom();tapes.forEach(tp=>tp.visible=false);chair.visible=backWall.visible=doorF.visible=true;
  tvL.intensity=0;spot.intensity=0;amb.intensity=.12;roomL.intensity=(3.4+hash(Math.floor(t*FPS),9)*.6)*(o.dim??1);
  handsL.userData.curl(.4+.05*Math.sin(t*1.3));handsR.userData.curl(.4);sitter.children[1].rotation.set(0,0,Math.sin(t*.4)*.04);
  const r=o.reach||0;handsR.position.set(lerp(.55,.25,r),lerp(.78,1.2,r),lerp(.05,-1.7,eInOut(r)));handsR.rotation.set(lerp(0,-.25,r),0,0);
  tape8.visible=r>0;if(r>0){handsR.updateMatrixWorld();tape8.position.copy(new THREE.Vector3(0,-.02,-.22).applyMatrix4(handsR.matrixWorld));tape8.rotation.set(0,Math.PI,Math.PI/2)}
  doorF.userData.d.rotation.y=-(o.door||0)*1.0;
  tvCam.position.set(0,1.24,.5);tvCam.lookAt(.15,1.0,3.0);tvCam.updateMatrixWorld();draw3D(scene,tvCam,ctx);
  // стекло кинескопа изнутри: виньетка и холодный оттенок
  const g=ctx.createRadialGradient(RW/2,RH/2,RH*.25,RW/2,RH/2,RW*.62);g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(1,'rgba(0,0,8,.85)');ctx.fillStyle=g;ctx.fillRect(0,0,RW,RH);
  ctx.fillStyle='rgba(60,90,140,.12)';ctx.fillRect(0,0,RW,RH)}
