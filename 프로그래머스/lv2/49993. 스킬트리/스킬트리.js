function solution(skill, skill_trees) {
    let regex = new RegExp(`[^${skill}]`,'g');
    return skill_trees.map(e=> e.replace(regex,"")).filter(e=>{
        return skill.indexOf(e) === 0 || e === ""
    }) .length
}