import jayakar from '../assets/photo.jpg'
import './Home.css'

function HeroSection(props){

    const skillsBanner = props.skillsArr.map((i,index)=>{
        if(index<7){
            return <img src={i} alt='banners'></img>
        }
    }) 
    
    return(
        <>
            <div className='leftHeroSec' id='herosection'>
                <div>
                    <h1>Hi there, I'm Jayakar</h1>
                    <h2>from India,</h2>
                    <h3>passionate about creating<br></br> stunning digital experiences.</h3>
                    <div className='buttons'>
                        <button className='firstBtn'>UI/UX</button>
                        <button className='secBtn'>Responsive</button>
                        <button className='thirdBtn'>Interactive</button>
                    </div>
                </div>
                <div>
                    <div className='backgroundLayout'>
                        {skillsBanner}
                    </div>
                    <img src={jayakar} alt="jayakar"></img>
                </div>
            </div>
        </>
    )
}

export default HeroSection