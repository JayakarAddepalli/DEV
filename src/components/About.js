import './Home.css'

function AboutSec(props){
    return(
        <>
            <div className="aboutSection" id='about' ref={props.aboutRef}>
                <p>I am Addepalli Jayakar, a proactive and detail-oriented software developer aspiring to contribute my skills to a dynamic team. With a solid educational background in BTech (ECE) from JNTUK and extensive hands-on experience in frontend technologies like HTML5, CSS3, JavaScript, and frameworks such as React, Angular, I am equipped to deliver innovative digital solutions. My proficiency extends to backend development with Python, Django, and SQL, bolstered by practical expertise in Git, GitHub, and software tools like VS Code and PyCharm.</p><br></br>
                <p>Driven by a passion for problem-solving and continuous learning, I have successfully completed projects ranging from automatic plant irrigation systems to e-commerce platforms. These experiences have honed my ability to collaborate effectively and integrate user-centric features that enhance application performance and security.</p><br></br>
                <p>I am dedicated to professional growth and stay current with industry trends through ongoing learning initiatives. Recently, I have obtained certifications in JavaScript programming and React JS Basics, further enhancing my skill set and ensuring I am well-prepared to tackle complex software challenges.</p><br></br>
                <p>Currently, I am advancing my skills through ongoing professional development, including certifications in JavaScript programming and React JS Basics. I recently achieved a commendable score in the TCS National Qualifier Test, underscoring my commitment to excellence and readiness for new challenges in the software development landscape.</p><br></br>
                <p>I am eager to leverage my technical skills and soft skills in communication and teamwork to contribute meaningfully to your esteemed organization's success. Please feel free to reach out via email at <a href='mailto:addepallijayakar@gmail.com' target='_blank' onMouseMove={props.handleMove} onMouseOut={props.handleOut}>addepallijayakar@gmail.com</a> or connect with me on <a href='https://www.linkedin.com/in/addepallijayakar270602/' rel='norefferer' target='_blank' onMouseMove={props.handleMove} onMouseOut={props.handleOut} style={{color:'blue'}}>LinkedIn</a> and <a href='https://github.com/JayakarAddepalli' rel='norefferer' target='_blank' onMouseMove={props.handleMove} onMouseOut={props.handleOut} style={{color:'blue'}}>GitHub</a> to explore potential collaborations.</p>
            </div>
        </>
    )
}

export default AboutSec