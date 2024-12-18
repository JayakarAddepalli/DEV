import { useEffect, useRef, useState } from 'react'
import logo from '../assets/logo.png'
import starIcon from '../assets/star.png'
import './Home.css'
import menu from '../assets/menu.png'
import FeedBackComponent from './feedback'
import { createPortal } from 'react-dom'

function Header(props){

      
    const outerMouse = useRef(null);

    const handleMove = (e)=>{
        outerMouse.current.style.top = e.clientY+'px'
        outerMouse.current.style.left = e.clientX+'px'
    }

    useEffect(()=>document.addEventListener('mousemove', handleMove), [])

    const [clicked, setClick] = useState(false)
    
    const HandleClick = ()=>{
        setClick(!clicked)
    }

    useEffect(() => {
        function handleResize() {
            if (window.innerWidth > 880) {
                setClick(true);
            } else {
                setClick(false);
            }
        }

        handleResize();

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    const [showModel, setShowModel] = useState(false)

    useEffect(() => {
        const timer = setTimeout(() => {
            setShowModel(true);  // Show the modal after 5 seconds
        }, 5000);

        return () => clearTimeout(timer);  // Cleanup the timeout
    }, []);

  

    return(
        <>
            <header>
                <nav>
                    <div className='logo'>
                        <img src={logo} alt="Logo"></img>
                    </div>
                    <div className='navList' style={{ visibility: clicked ? 'visible' : 'hidden'}}>
                        <a href="#about" onMouseMove={props.handleMove} onMouseOut={props.handleOut} style={props.abo?{backgroundColor:'rgb(255, 0, 119)', borderRadius:'5px', boxShadow:' 0px 0px 10px rgb(255, 0, 119)'}:{backgroundColor:'transparent'}}>About</a>
                        <a href="#skills" onMouseMove={props.handleMove} onMouseOut={props.handleOut} style={props.ski?{backgroundColor:'rgb(170, 0, 255)', borderRadius:'5px', boxShadow:' 0px 0px 10px rgb(170, 0, 255)'}:{backgroundColor:'transparent'}}>Skills</a>
                        <a href="#projects" onMouseMove={props.handleMove} onMouseOut={props.handleOut} style={props.pro?{backgroundColor:'rgb(0, 157, 255)', borderRadius:'5px', boxShadow:' 0px 0px 10px rgb(0, 157, 255)'}:{backgroundColor:'transparent'}}>Projects</a>
                        <a href="#contact" onMouseMove={props.handleMove} onMouseOut={props.handleOut} style={props.con?{backgroundColor:'rgb(34, 255, 0)', borderRadius:'5px', boxShadow:' 0px 0px 10px rgb(34, 255, 0)'}:{backgroundColor:'transparent'}}>Contact</a>
                        <a href="https://github.com/JayakarAddepalli/Portfolio_react" target='_blank' rel='noreferrer' onMouseMove={props.handleMove} onMouseOut={props.handleOut}><img src={starIcon} alt='starIcon'></img></a>
                        <div id='mousePointer' ref={outerMouse}>
                            <div id='innerPointer' style={props.innerMouse?{transform:'scale(1.5,1.5)', transition:'all 1s'}:{transform:'scale(1,1)', transition:'all 1s'}}></div>
                        </div>
                    </div>
                    <span className='Menu' onClick={HandleClick} style={{opacity : clicked ? 0.5 : 1}}>
                        <img src={menu} alt='Menu'></img>
                    </span>
                </nav>
            </header>

            {showModel && createPortal(
                <FeedBackComponent onClose={() => setShowModel(false)} />,
                document.body
            )}
        </>
    )
}

export default Header