function solution(today, terms, privacies) {
    var answer = [];
    let termType = {};
    terms.forEach(e=>{
      let [type,term] = e.split(" ");
        termType[type] = +term
    })
    privacies.forEach((e,i)=>{
        let [time,term] = e.split(" ")
        let [y,m,d]= time.split(".").map(e=>+e)
        let [ty,tm,td] =today.split(".").map(e=>+e);
        let diff = (ty-y)*12*28+(tm-m)*28+(td-d)
        let exp = termType[term]*28
        if(exp<=diff){
            answer.push(i+1)
        }
        
    })
    
    return answer;
}