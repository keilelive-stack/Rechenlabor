const fs=require('fs'), vm=require('vm'), path=require('path');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
vm.runInNewContext(html.match(/<script>([\s\S]*)<\/script>/)[1]+`
const r=tests();console.log(JSON.stringify(r,null,2));if(r.some(x=>x[1]!=='PASS'))throw Error('Selbsttest fehlgeschlagen');
for(let b of [0,.004,.009,.018]){let s=maxStar(2.5,b).model;console.log('beta',b,'M/Msun',s.M/Ms,'R/km',s.R/1000,'IR/um',10*Math.exp(-s.nuR));}
`,{console});
