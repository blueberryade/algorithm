function solution(dots) {
    const [a,b,c,d] = dots.sort((a,b)=>a[0]-b[0]);
    let v1 = (b[1]-a[1])/(b[0]-a[0])
    let v2 = (d[1]-c[1])/(d[0]-c[0])
    
    return v1===v2 ? 1 : 0;
}