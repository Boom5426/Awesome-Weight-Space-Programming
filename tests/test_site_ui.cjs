// Browser-state regression tests with Node's built-in VM, no npm dependencies.
const assert=require("node:assert/strict");
const fs=require("node:fs");
const vm=require("node:vm");
const path=require("node:path");
const ROOT=path.resolve(__dirname,"..");

function scriptOf(file){
  const html=fs.readFileSync(path.join(ROOT,file),"utf8");
  const match=html.match(/<script>([\s\S]*?)<\/script>/);
  assert.ok(match,"missing executable browser script in "+file);
  return match[1];
}
function element(id,tagName="div"){
  let value="",html="",options=[];
  const obj={
    id,tagName:tagName.toUpperCase(),hidden:false,disabled:false,textContent:"",href:"",placeholder:"",
    handlers:{},attributes:{},children:[],
    addEventListener(type,callback){this.handlers[type]=callback;},
    setAttribute(key,val){this.attributes[key]=val;},
    getAttribute(key){return this.attributes[key];},
    focus(){this.focused=true;},
    appendChild(x){this.children.push(x);return x;},
    replaceChildren(){this.children=[];},
    getBBox(){return{x:-950,y:-480,width:1900,height:960};},
    getBoundingClientRect(){return {left:0,top:0,width:390,height:800};},
    setPointerCapture(){},
  };
  Object.defineProperty(obj,"innerHTML",{
    get(){return html;},
    set(s){html=String(s);
      if(obj.tagName==="SELECT"){
        options=[...html.matchAll(/<option value="([^"]*)"/g)].map(m=>m[1]);
        value=options.includes(value)?value:(options[0]||"");
      }
    }
  });
  Object.defineProperty(obj,"value",{
    get(){return value;},
    set(s){const proposed=String(s);
      value=obj.tagName==="SELECT"&&options.length&&!options.includes(proposed)?"":proposed;
    }
  });
  return obj;
}
function harness(file,search){
  const selectIds=new Set(["leaf","year","code","review"]);
  const ids=new Map();
  const domHandlers={};
  const location={search,pathname:"/Awesome-Weight-Space-Programming/"+(file==="landscape.html"?"landscape.html":""),protocol:"https:",href:""};
  const document={
    documentElement:{lang:"en"},
    activeElement:{tagName:"BODY"},
    getElementById(id){if(!ids.has(id))ids.set(id,element(id,selectIds.has(id)?"select":"div"));return ids.get(id);},
    addEventListener(type,fn){domHandlers[type]=fn;},
    createElementNS(_ns,tag){return element(tag);},
  };
  for(const id of selectIds){const e=document.getElementById(id);e.innerHTML='<option value="">All</option>';}
  const windowHandlers={};
  const window={addEventListener(type,fn){windowHandlers[type]=fn;}};
  const history={replaceState(_a,_b,url){location.search=(String(url).split("?")[1]||"")?"?"+String(url).split("?")[1]:"";}};
  const context=vm.createContext({document,window,location,history,URLSearchParams,console,requestAnimationFrame:fn=>fn()});
  vm.runInContext(scriptOf(file),context,{filename:file});
  return {ctx:context,ids,document,location,windowHandlers,get:id=>document.getElementById(id),
    evaluate:source=>vm.runInContext(source,context)};
}
function cards(h){return (h.get("results").innerHTML.match(/<article class="item">/g)||[]).length;}
function drive(h,id,event,arg){const fn=h.get(id).handlers[event];assert.equal(typeof fn,"function","handler missing "+id+"."+event);fn(arg);}

const all=harness("index.html","");
assert.equal(all.evaluate("PAPERS.length"),145);
assert.equal(all.evaluate("group"),"");
assert.equal(cards(all),24,"default page should be paginated");
assert.equal(all.get("more").hidden,false);
drive(all,"more","click");
assert.equal(cards(all),48,"load more should append another page");
drive(all,"langToggle","click");
assert.equal(all.document.documentElement.lang,"zh");
assert.ok(all.location.search.includes("lang=zh"));
assert.equal(cards(all),48,"switching language should preserve pagination");
assert.ok(all.get("count").textContent.includes("显示"));

const foundation=harness("index.html","?branch=foundations&leaf=fast");
assert.equal(foundation.evaluate("group"),"related");
assert.equal(foundation.evaluate("track"),"foundations.fast");
assert.equal(cards(foundation),6);
assert.ok(foundation.get("count").textContent.includes("6 matches"));

const reports=harness("index.html","?branch=resources&leaf=reports");
assert.equal(reports.evaluate("group"),"reports");
assert.equal(cards(reports),9);
const tools=harness("index.html","?branch=resources&leaf=tools");
assert.equal(tools.evaluate("group"),"resources");
assert.equal(cards(tools),6);

const chinese=harness("index.html","?lang=zh&group=weight-centric&q=权重");
assert.equal(chinese.document.documentElement.lang,"zh");
assert.equal(chinese.evaluate("group"),"weight-centric");
assert.ok(chinese.get("count").textContent.includes("条匹配结果"));
assert.ok(cards(chinese)>0,"Chinese terms should search the bilingual source data");
assert.ok(chinese.get("results").innerHTML.includes("核心思路"));

const year=harness("index.html","?year=2017");
assert.equal(year.get("year").value,"2017","deep-link year should not be reset before select options initialize");
assert.equal(cards(year),year.evaluate('PAPERS.filter(p=>p.year===2017).length'));

const reviewed=harness("index.html","?review=source_checked");
assert.equal(cards(reviewed),8);
assert.ok(reviewed.get("results").innerHTML.includes("Source-reported result"));
assert.ok(!reviewed.get("results").innerHTML.includes("undefined"));

const map=harness("landscape.html","?lang=zh");
assert.equal(map.document.documentElement.lang,"zh");
assert.ok(map.get("mapTitle").textContent.includes("导航"));
assert.equal((map.get("mobileLinks").innerHTML.match(/<a href=/g)||[]).length,20);
assert.ok(map.get("mobileLinks").innerHTML.includes("lang=zh"));
const scene=map.get("scene");
const leaf=scene.children.find(e=>e.attributes.class?.startsWith("node leaf")&&e.attributes["aria-label"]?.includes("几何"));
assert.ok(leaf,"a focusable Chinese geometry leaf must exist");
drive({get:()=>leaf},"leaf","click");
assert.ok(map.location.href.includes("branch=weight-centric"));
assert.ok(map.location.href.includes("leaf=geometry"));
assert.ok(map.location.href.includes("lang=zh"));
drive(map,"langToggle","click");
assert.equal(map.document.documentElement.lang,"en");

console.log("Browser-state smoke tests passed: search, pagination, Chinese, years, deep-links, evidence and map.");
