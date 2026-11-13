// Интро и аутро, общие для всех серий: титр «по мотивам», комната с теликом-видиком, ряд кассет, рука вставляет кассету,
// наезд в экран. Аутро: отъезд от экрана, кассета выезжает, свет гаснет.
import {THREE,FPS,RW,RH,mulberry,hash,clamp,P,lerp,eOut,eIn,eInOut,col,M,box,draw3D,canvas2d,tex,noise,text,snow,hardAlpha,MONO} from './core.js';

export const INTRO=14, OUTRO=7, NVOL=6;
export function stageScene(){return scene}
const scene=new THREE.Scene();scene.background=new THREE.Color(0x000000);scene.fog=new THREE.Fog(0x000000,3,9);
const camera=new THREE.PerspectiveCamera(50,RW/RH,.02,50);

// ---------- текстуры ----------
const TX={
  floor:tex(32,32,(g,w,h)=>{noise(g,w,h,['#2a1c14','#24180f','#30211a'],1);g.fillStyle='rgba(0,0,0,.5)';for(let y=0;y<h;y+=8)g.fillRect(0,y,w,1)},[6,6]),
  wall:tex(16,16,(g,w,h)=>{noise(g,w,h,['#3a3428','#363024','#3e382c'],2);g.fillStyle='rgba(80,60,40,.35)';for(let x=0;x<w;x+=4)g.fillRect(x,0,1,h)},[10,4]),
  wood:tex(32,16,(g,w,h)=>{noise(g,w,h,['#5a3a24','#4e321e','#64422a'],3);g.fillStyle='rgba(20,10,5,.4)';for(let y=0;y<h;y+=4)g.fillRect(0,y,w,1)}),
  plastic:tex(8,8,(g,w,h)=>noise(g,w,h,['#3a3a3c','#363638','#3e3e40'],4)),
  plasticD:tex(8,8,(g,w,h)=>noise(g,w,h,['#1c1c1e','#19191b','#202022'],5)),
  skin:tex(8,8,(g,w,h)=>noise(g,w,h,['#c89a7a','#c09276','#d0a284','#b88a6e'],6)),
  skinD:tex(8,8,(g,w,h)=>noise(g,w,h,['#a87a5e','#9e725a','#b08266'],7)),
  sleeve:tex(8,8,(g,w,h)=>noise(g,w,h,['#6a5e52','#62564a','#72665a'],8)),
  nail:tex(4,4,(g,w,h)=>noise(g,w,h,['#e0c0b0','#d8b8a8'],9)),
};
function spineTex(n){return tex(16,64,(g,w,h)=>{g.fillStyle='#141416';g.fillRect(0,0,w,h);g.fillStyle='#d8d4c8';g.fillRect(2,6,12,46);g.fillStyle='#a82020';g.fillRect(2,6,12,4);g.fillRect(2,48,12,4);
  g.save();g.translate(11,14);g.rotate(Math.PI/2);g.fillStyle='#1a1a1a';g.font=`bold 7px ${MONO}`;g.fillText(`ТОМ ${n}`,0,0);g.restore()})}
function topLabelTex(n){return tex(64,32,(g,w,h)=>{g.fillStyle='#141416';g.fillRect(0,0,w,h);g.fillStyle='#d8d4c8';g.fillRect(6,6,52,20);g.fillStyle='#a82020';g.fillRect(6,6,52,3);
  g.fillStyle='#1a1a1a';g.font=`bold 8px ${MONO}`;g.fillText(`ТОМ ${n}`,12,12)})}

// ---------- комната ----------
{const fl=box(8,.1,8,M({map:TX.floor}));fl.position.y=-.05;scene.add(fl);const wl=box(8,4,.1,M({map:TX.wall}));wl.position.set(0,2,-.9);scene.add(wl);
 const cab=box(2.9,.6,.8,M({map:TX.wood}));cab.position.set(.6,.3,0);scene.add(cab);for(const x of[-.3,.6,1.5]){const h=box(.05,.05,.02,M({color:0x8a7a50}));h.position.set(x,.42,.41);scene.add(h)}}
// телевизор-видеодвойка
const SCR={w:.76,h:.57,y:1.24,z:.462};
const [scrC,scrX]=canvas2d();const scrTex=new THREE.CanvasTexture(scrC);scrTex.magFilter=scrTex.minFilter=THREE.NearestFilter;scrTex.generateMipmaps=false;scrTex.colorSpace=THREE.SRGBColorSpace;
const tv=new THREE.Group();scene.add(tv);let slotLed;
{const pm=M({map:TX.plastic}),dm=M({map:TX.plasticD});
 const body=box(1.06,1.02,.84,pm);body.position.set(0,1.11,0);tv.add(body);
 const back=box(.8,.7,.4,pm);back.position.set(0,1.18,-.6);tv.add(back);
 for(const [w,h,x,y] of[[1.0,.08,0,1.56],[1.0,.06,0,.92],[.1,.64,-.47,1.24],[.1,.64,.47,1.24]]){const b=box(w,h,.06,dm);b.position.set(x,y,.43);tv.add(b)}
 const scr=new THREE.Mesh(new THREE.PlaneGeometry(SCR.w,SCR.h),new THREE.MeshBasicMaterial({map:scrTex,toneMapped:false,fog:false}));scr.position.set(0,SCR.y,SCR.z);tv.add(scr);
 const panel=box(1.02,.3,.05,dm);panel.position.set(0,.76,.43);tv.add(panel);
 const slot=box(.6,.05,.02,new THREE.MeshBasicMaterial({color:0x020202}));slot.position.set(-.12,.78,.46);tv.add(slot);
 const flap=box(.6,.012,.02,M({map:TX.plastic}));flap.position.set(-.12,.81,.465);tv.add(flap);
 slotLed=box(.03,.015,.01,new THREE.MeshBasicMaterial({color:0x300000}));slotLed.position.set(.32,.79,.462);tv.add(slotLed);
 for(let i=0;i<3;i++){const k=new THREE.Mesh(new THREE.CylinderGeometry(.025,.025,.03,8),pm);k.rotation.x=Math.PI/2;k.position.set(.25+i*.07,.7,.465);tv.add(k)}
 const ant=new THREE.Group();for(const s of[-1,1]){const a=new THREE.Mesh(new THREE.CylinderGeometry(.008,.008,.8,4),M({color:0x888888}));a.position.set(s*.2,.38,0);a.rotation.z=-s*.5;ant.add(a)}ant.position.set(0,1.62,-.3);tv.add(ant);
 const tvb=box(.3,.04,.2,pm);tvb.position.set(0,1.62,-.3);tv.add(tvb)}
// кассеты на полке
const VOLX=n=>1.1+(n-1)*.1;
function makeTape(n){const g=new THREE.Group(),bm=M({map:TX.plasticD});const b=box(.075,.56,.30,[bm,bm,M({map:topLabelTex(n)}),bm,M({map:spineTex(n)}),bm]);g.add(b);return g}
const tapes=[];for(let n=1;n<=NVOL;n++){const t=makeTape(n);t.position.set(VOLX(n),.6+.28,.0);t.rotation.y=.04*(hash(n,1)-.5);scene.add(t);tapes.push(t)}
// рука (правая, ладонью вниз, пальцы вперёд по -z)
const hand=new THREE.Group();scene.add(hand);const fingers=[],thumb=[];
{const sk=M({map:TX.skin}),skd=M({map:TX.skinD}),sl=M({map:TX.sleeve}),nl=M({map:TX.nail});
 const fore=box(.1,.095,.4,sl);fore.position.set(0,.005,.25);hand.add(fore);const cuff=box(.11,.105,.05,M({color:0x4a4038}));cuff.position.set(0,.01,.06);hand.add(cuff);
 const wrist=box(.1,.07,.06,sk);wrist.position.set(0,0,.02);hand.add(wrist);
 const palm=box(.11,.04,.12,sk);palm.position.set(0,0,-.06);hand.add(palm);const knuck=box(.105,.03,.02,skd);knuck.position.set(0,.012,-.115);hand.add(knuck);
 [[-.039,.044],[-.013,.05],[.013,.047],[.037,.038]].forEach(([x,L],i)=>{let parent=hand,z=-.12;const segs=[];
   [L,L*.7,L*.6].forEach((l,k)=>{const j=new THREE.Group();j.position.set(k?0:x,0,k?-segs[k-1].l:z);parent.add(j);const s=box(.022-k*.002,.022-k*.002,l,k%2?skd:sk);s.position.z=-l/2;j.add(s);
     if(k===2){const n=box(.016,.006,.012,nl);n.position.set(0,.011,-l+.007);j.add(n)}segs.push({j,l});parent=j});fingers.push(segs)});
 let parent=hand;[[.04,.4],[.035,.25]].forEach(([l,a],k)=>{const j=new THREE.Group();if(!k){j.position.set(-.055,-.008,-.03);j.rotation.set(0,.75,0)}else j.position.z=-.04;parent.add(j);
   const s=box(.026,.024,l,sk);s.position.z=-l/2;j.add(s);if(k===1){const n=box(.018,.006,.012,nl);n.position.set(0,.012,-l+.008);j.add(n)}thumb.push(j);parent=j})}
function curl(k){fingers.forEach((f,i)=>f.forEach((s,j)=>s.j.rotation.x=-k*(.75+.15*j)*(1-.05*i)));thumb[0].rotation.x=-k*.3;thumb[1].rotation.x=-k*.6}
// свет
const amb=new THREE.AmbientLight(0x404858,.25);scene.add(amb);
const tvL=new THREE.PointLight(0xa8c0ff,0,5,1.6);tvL.position.set(0,1.24,.9);scene.add(tvL);
const handL=new THREE.PointLight(0xc8d0ff,0,2.5,1.5);scene.add(handL);
const spot=new THREE.SpotLight(0xffe0b0,0,6,.32,.5,1.2);spot.position.set(1.35,2.9,.9);spot.target.position.set(1.35,.85,0);scene.add(spot,spot.target);

// ---------- экран ----------
function screenNoise(t,k=1){snow(scrX,t,k)}
function screenPlay(t,vol){scrX.fillStyle='#1830a0';scrX.fillRect(0,0,RW,RH);text(scrX,'▶ PLAY',20,18,{size:16});if(Math.floor(t*2)%2)text(scrX,`ТОМ ${vol}`,20,44,{size:12})}
const rest=(n)=>new THREE.Vector3(VOLX(n),.88,0);
// положение кассеты в руке относительно ладони
const HS=2.3; // рука в масштабе кассет

function cameraFor(z,m=0){ // z: 0 — общий план, 1 — экран во весь кадр; m: 0..1 — подъезд к руке
  const fit=(SCR.h/2)/Math.tan(THREE.MathUtils.degToRad(camera.fov/2));const W=new THREE.Vector3(.55,1.3,3.1).lerp(new THREE.Vector3(.75,1.25,2.0),m),L=new THREE.Vector3(.55,.98,0).lerp(new THREE.Vector3(.65,1.0,0),m);
  const S=new THREE.Vector3(0,SCR.y,SCR.z+fit),SL=new THREE.Vector3(0,SCR.y,SCR.z);camera.position.copy(W).lerp(S,z);camera.lookAt(L.clone().lerp(SL,z))}

// кассета n: рука берёт и вставляет. k — время от начала действия
function handAct(t,vol){const tape=tapes[vol-1],r=rest(vol),slotP=new THREE.Vector3(-.12,.78,.46);hand.visible=true;hand.scale.setScalar(HS);
  // ключевые точки — для центра кассеты; рука держится за её верх/торец со смещением OFF
  const YAW=.8,od=(y,d)=>new THREE.Vector3(Math.sin(YAW)*d,y,Math.cos(YAW)*d);const OFF=od(.30,.46),OFFF=od(.12,.44);
  const away=new THREE.Vector3(2.4,1.5,1.6),lift=r.clone().add(new THREE.Vector3(-.25,.45,.55)),pre=slotP.clone().add(new THREE.Vector3(0,0,.55)),inS=slotP.clone().add(new THREE.Vector3(0,0,-.16)),deep=slotP.clone().add(new THREE.Vector3(0,0,-.36));
  let tp=r.clone(),rz=0,c=.15,rx=-.15,off=OFF.clone(),hp=null;
  if(t<7.4){hp=away}
  else if(t<8.2){hp=away.clone().lerp(r.clone().add(OFF).add(new THREE.Vector3(0,.12,0)),eOut(P(t,7.4,8.2)));rx=-.5}
  else if(t<8.5){hp=r.clone().add(OFF).add(new THREE.Vector3(0,.12*(1-P(t,8.2,8.4)),0));c=lerp(.15,1,P(t,8.25,8.5));rx=-.5}
  else if(t<9.2){const k=eInOut(P(t,8.5,9.2));tp=r.clone().lerp(lift,k);rz=lerp(0,Math.PI/2,k);off=OFF.clone().lerp(OFFF,k);c=1;rx=lerp(-.5,-.15,k)}
  else if(t<10.0){tp=lift.clone().lerp(pre,eInOut(P(t,9.2,10.0)));rz=Math.PI/2;off=OFFF;c=1}
  else if(t<10.6){tp=pre.clone().lerp(inS,eInOut(P(t,10.0,10.6)));rz=Math.PI/2;off=OFFF;c=lerp(1,.3,P(t,10.4,10.6))}
  else{tp=inS.clone().lerp(deep,eOut(P(t,10.6,10.9)));rz=Math.PI/2;c=.3;hp=inS.clone().add(OFFF).lerp(away,eIn(P(t,10.7,11.7)));if(t>11.7)hand.visible=false}
  hand.position.copy(hp||tp.clone().add(off));hand.rotation.set(0,YAW,0);hand.rotateX(rx);curl(c);
  tape.position.copy(tp);tape.rotation.set(0,0,rz)}
// ---------- кадр интро ----------
// ctx — канвас 320x240; epFrame(tEp) рисует кадр серии в канвас и возвращает его; vol — номер тома
export function intro(t,ctx,epFrame,vol){
  if(t<4.6){ctx.fillStyle='#000';ctx.fillRect(0,0,RW,RH);const a=P(t,.3,.9)*(1-P(t,4.0,4.6));if(a<=0)return;ctx.globalAlpha=Math.round(a*8)/8;
    text(ctx,'по мотивам',RW/2,62,{align:'center',color:'#a0a0a0'});text(ctx,'THE MANDELA CATALOGUE',RW/2,84,{align:'center',size:16});
    text(ctx,'автор оригинала — Alex Kister',RW/2,112,{align:'center',color:'#d0d0d0'});
    text(ctx,'неофициальная фан-адаптация.',RW/2,156,{align:'center',size:9,color:'#808080'});text(ctx,'все права на оригинал принадлежат автору.',RW/2,168,{align:'center',size:9,color:'#808080'});
    ctx.globalAlpha=1;hardAlpha(ctx,1);return}
  tapes.forEach((tp,i)=>{tp.visible=true;tp.position.copy(rest(i+1));tp.rotation.set(0,0,0)});hand.visible=false;
  const fade=P(t,4.6,6.2);
  // экран
  if(t<10.9)screenNoise(t,.8);else if(t<11.1){scrX.fillStyle='#000';scrX.fillRect(0,0,RW,RH)}else if(t<12.6)screenPlay(t,vol);else scrX.drawImage(epFrame(0),0,0);
  scrTex.needsUpdate=true;
  const flick=.85+hash(Math.floor(t*FPS),3)*.3;tvL.intensity=(t<10.9?1.6:t<11.1?.2:1.3)*flick*fade;amb.intensity=.25*fade;
  spot.intensity=t<5.5?0:t<5.6?3:8*(.95+.05*hash(Math.floor(t*FPS),5));slotLed.material.color.set(t>10.5?0xff2020:0x300000);
  handAct(t,vol);
  cameraFor(eInOut(P(t,12.0,14.0)),eInOut(P(t,6.8,8.4))*(1-eInOut(P(t,9.0,10.0))));handL.position.copy(hand.position).add(new THREE.Vector3(.3,.5,.6));handL.intensity=hand.visible?1.4:0;
  draw3D(scene,camera,ctx);
  if(fade<1){ctx.fillStyle=`rgba(0,0,0,${Math.round((1-fade)*16)/16})`;ctx.fillRect(0,0,RW,RH)}
  // название поверх кассет
  if(t>=5.3&&t<7.6&&!(t<5.7&&Math.floor(t*FPS)%2)){const v=new THREE.Vector3(1.35,1.38,0).project(camera),x=Math.round((v.x*.5+.5)*RW),y=Math.round((-v.y*.5+.5)*RH);
    text(ctx,'THE MANDELA',x,y-12,{align:'center',size:13,color:'#e8e2d0'});text(ctx,'CATALOGUE',x,y+2,{align:'center',size:13,color:'#e8e2d0'});
    text(ctx,'фан-адаптация',x,y+18,{align:'center',size:8,color:'#a09a8a'})}
}

// ---------- кадр аутро ----------
// hook(t, scene) — необязательный крючок серии: можно добавить в комнату что-то своё (по умолчанию аутро одинаковое)
export function outro(t,ctx,epFrame,vol,D,hook){
  tapes.forEach((tp,i)=>{tp.visible=i!==vol-1;tp.position.copy(rest(i+1));tp.rotation.set(0,0,0)});hand.visible=false;
  const tape=tapes[vol-1];const ej=P(t,2.8,3.3);tape.visible=t>=2.8;tape.position.set(-.12,.78,lerp(.34,.58,eOut(ej)));tape.rotation.set(0,0,Math.PI/2);
  if(t<1.0)scrX.drawImage(epFrame(D-.01),0,0);else if(t<2.8)screenNoise(t,.8);else{scrX.fillStyle='#000';scrX.fillRect(0,0,RW,RH)}scrTex.needsUpdate=true;
  const flick=.85+hash(Math.floor(t*FPS),3)*.3;tvL.intensity=(t<1?.6:t<2.8?1.6:.0)*flick;amb.intensity=.25;slotLed.material.color.set(t<2.8?0xff2020:0x300000);
  spot.intensity=t<4.2?8:0;
  cameraFor(1-eInOut(P(t,0,2.6)));if(hook)hook(t,scene);
  draw3D(scene,camera,ctx);
  const dk=P(t,4.0,6.6);if(dk>0){ctx.fillStyle=`rgba(0,0,0,${Math.round(dk*16)/16})`;ctx.fillRect(0,0,RW,RH)}
}
