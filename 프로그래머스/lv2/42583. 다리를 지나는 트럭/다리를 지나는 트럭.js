function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = [];
    let sum = 0;
    while(truck_weights.length>0){
        answer++;
        if(bridge.length === bridge_length){
            sum-=bridge.shift()
        }
        if(sum+truck_weights[0]>weight){
            bridge.push(0)
            continue
        }
        let truck_weight = truck_weights.shift()
        bridge.push(truck_weight)
        sum+=truck_weight;
    }
    answer+=bridge_length
    return answer;
}