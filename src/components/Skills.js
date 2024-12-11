import './Home.css'

function SkillsSec(props){

    const skillSet = ['Angular', 'ReactJs', 'Javascript', 'CSS', 'HTML', 'Python', 'Django', 'SQL', 'Bootstrap']
    const toolsSet = ['VSCode', 'Pycharm', 'Oracle 11g', 'Figma', 'Git', 'Github']

    const data = props.skillsArr.map((i, index)=><p key={index}><img src={i} alt={index+'Image'}></img><span>{skillSet[index]}</span></p>)
    const tools = props.toolsArr.map((i,index)=><p key={index}><img src={i} alt={index+'Image'}></img><span>{toolsSet[index]}</span></p>)

    return(
        <>
            <div className="skillsSec" id='skills'>
                <div>
                    <h5>Technical Skills</h5>
                    <div className=''>
                        {data}
                    </div>
                </div>
                <div>
                    <h5>Tools I use</h5>
                    <div className=''>
                        {tools}
                    </div>
                </div>
            </div>
        </>
    )
}

export default SkillsSec