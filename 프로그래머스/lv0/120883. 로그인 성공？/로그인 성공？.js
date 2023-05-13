function solution(id_pw, db) {
     let id = db.filter((e)=> e[0]===id_pw[0])
     return id.length<=0 ? "fail" : id[0][1]===id_pw[1] ? "login" : "wrong pw"

}