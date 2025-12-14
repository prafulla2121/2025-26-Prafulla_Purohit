let a=10
let b =5
let sum = a+b
console.log(sum)

let m=12*3
console.log(m)
let n = 20/4
console.log(n)
let r=10%3
console.log(r)

let userName = "prafulla "
let userAge= 22
console.log(userName+userAge)

let fruitlist=["apple","mango","orange","grapes"]
console.log(fruitlist)
console.log(fruitlist[1])
fruitlist.push("banana")
console.log(fruitlist)

let numList=[1,3,5,7,9]
for(let i=0;i<numList.length;i++){
console.log(numList[i])
}

let k=1
while(k<4){
console.log(k)
k++
}

let p={name:"ravi",city:"mumbai",age:30}
console.log(p.name)
console.log(p.city)

let dt=new Date()
console.log(dt.toLocaleDateString())
console.log(dt.getFullYear())
console.log(dt.getHours())

function addnum(x,y){return x+y}
console.log(addnum(3,6))

function hi(nam){return "hi "+nam}
console.log(hi("prafulla"))



let marks=[41,52,63,78]
let totl=0
for(let v of marks){totl+=v}
console.log(totl)

let chk=18
if(chk>=18) console.log("adult")
else console.log("minor")

let carData={brand:"BMW",model:"X5",year:2020}
for(let k2 in carData){console.log(k2,carData[k2])}


let a1 = 5; let a2 = 7; console.log(a1*a2)
let a3 = 2; a3 += 3; console.log(a3)

let comp1 = 10>3; console.log(comp1)
let comp2 = 4=="4"; console.log(comp2)
let comp3 = 4==="4"; console.log(comp3)

let txt = "hello"; console.log(txt.length)
console.log(txt.toUpperCase())
console.log(txt.toLowerCase())

let arr2 = ["a","b","c"]
arr2.unshift("z")
console.log(arr2)
arr2.pop()
console.log(arr2)

let nums2=[10,20,30,40]
let doubled = nums2.map(function(v){return v*2})
console.log(doubled)

let big = nums2.filter(function(v){return v>20})
console.log(big)

let sum2 = nums2.reduce(function(t,v){return t+v},0)
console.log(sum2)

let str = "10"
let conv = Number(str)
console.log(conv)
console.log(parseInt("33px"))
console.log(parseFloat("22.5abc"))

let rnd = Math.random()
console.log(rnd)
console.log(Math.floor(3.8))
console.log(Math.ceil(3.2))
console.log(Math.max(3,9,1))

let d2=new Date()
console.log(d2.getMonth())
console.log(d2.getMinutes())
console.log(d2.getSeconds())

function sq(n){return n*n}
console.log(sq(6))

let showmsg=function(){console.log("hello js")}
showmsg()

function testscope(){let x=10; if(true){let x=20; console.log(x)} console.log(x)}
testscope()

let obj2={n:"kiran",age:25,job:"dev"}
obj2.job="tester"
console.log(obj2)

let obj3={a:1,b:2}
let obj4={c:3}
let merged = {...obj2,...obj3,...obj4}
console.log(merged)

let l1 = [1,2,3]
let l2 = [...l1,4,5]
console.log(l2)

let cond=0
console.log(cond?"yes":"no")

let sw=2
switch(sw){
case 1: console.log("one"); break
case 2: console.log("two"); break
default: console.log("none")
}

for(let s of ["red","blue","green"]){console.log(s)}

