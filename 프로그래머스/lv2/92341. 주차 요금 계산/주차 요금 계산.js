function solution(fees, records) {
    const cars = {};
    records.forEach(e=>{
        let [time,car,type] = e.split(" ");
        const [h,m] = time.split(":");
        time = h*60 + Number(m)
        
        if(!cars[car]){
            cars[car] = {time: 0, car }
        }
        cars[car].type = type;
        if(type === "OUT"){
            cars[car].time += time - cars[car].lastInTime
            return;
        }
        cars[car].lastInTime = time;
        
    })
    return Object.values(cars).sort((a,b)=>a.car-b.car)
    .map(e=>{
        if(e.type === "IN"){
            e.time += 1439 - e.lastInTime
        }
        if(fees[0] > e.time){
            return fees[1]
        }
        return fees[1] + Math.ceil((e.time-fees[0])/fees[2])*fees[3]
    })
}