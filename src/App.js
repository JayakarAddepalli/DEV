import { useEffect, useRef, useState } from 'react';
import './App.css';
import Header from './components/Home';
import HeroSection from './components/HeroSection';
import AboutSec from './components/About';
import SkillsSec from './components/Skills';
import ProjectSec from './components/Projects';
import ContactSec from './components/Contact';
import HomeComp from './components/HomeComp';
import JSIcon from './assets/icons8-javascript-144.png'
import HTMLIcon from './assets/icons8-html-logo-144_n3MsJnY.png'
import CSSIcon from './assets/icons8-css-logo-144.png'
import reactIcon from './assets/react.png'
import angularIcon from './assets/angular.png'
import PyIcon from './assets/icons8-python-144_1.png'
import DjangoIcon from './assets/icons8-django-144.png'
import Bootstrap from './assets/bootstrap.png'
import sql from './assets/database.png'
import vsCode from './assets/visual-studio.png'
import py from './assets/icons8-pycharm-480.png'
import dataOracle from './assets/oracle.png'
import figma from './assets/figma_iQCLSPR.png'
import git from './assets/social.png'
import gitHub from './assets/github.png'

function App() {

  const aboutRef = useRef(null);
  const [abo, setAbo] = useState(false);
  const [ski, setSki] = useState(false);
  const [pro, setPro] = useState(false);
  const [con, setCon] = useState(false);
  const [upScroll, setUpScroll] = useState(false);
  
  const [innerMouse, setInnerMouse] = useState(false);

  const handleScroll = ()=>{
    console.log(aboutRef.current.getBoundingClientRect().top)

    if((aboutRef.current.getBoundingClientRect().top>10)){
      setAbo(false)
      setSki(false)
      setPro(false)
      setCon(false)
      setUpScroll(false)
    }

    else if((aboutRef.current.getBoundingClientRect().top<10) && (aboutRef.current.getBoundingClientRect().top>-490)){
      setAbo(true)
      setSki(false)
      setPro(false)
      setCon(false)
      setUpScroll(true)
    }
    else if((aboutRef.current.getBoundingClientRect().top<-490) && (aboutRef.current.getBoundingClientRect().top>-800)){
      setAbo(false)
      setSki(true)
      setPro(false)
      setCon(false)
      setUpScroll(true)
    }
    else if((aboutRef.current.getBoundingClientRect().top<-1200) && (aboutRef.current.getBoundingClientRect().top>-1500)){
      setAbo(false)
      setSki(false)
      setPro(true)
      setCon(false)
      setUpScroll(true)
    }
    else if((aboutRef.current.getBoundingClientRect().top<-1600) && (aboutRef.current.getBoundingClientRect().top>-1900)){
      setAbo(false)
      setSki(false)
      setPro(false)
      setCon(true)
      setUpScroll(true)
    }
  }

  useEffect(()=>{window.addEventListener('scroll',handleScroll)},[])

  const handleMove = ()=>{
    setInnerMouse(true)
  }

  const handleOut = ()=>{
    setInnerMouse(false)
  }
  
  const skillsArr = [angularIcon, reactIcon, JSIcon, CSSIcon, HTMLIcon, PyIcon, DjangoIcon,  sql, Bootstrap]
  const toolsArr = [vsCode, py, dataOracle, figma, git, gitHub]

  return (
    <div className="App">
      <Header abo={abo} ski={ski} pro={pro} con={con} innerMouse={innerMouse} handleMove={handleMove} handleOut={handleOut}/>
      <HeroSection skillsArr = {skillsArr}/>
      <AboutSec aboutRef={aboutRef} handleMove={handleMove} handleOut={handleOut} />
      <SkillsSec skillsArr = {skillsArr} toolsArr = {toolsArr} />
      <ProjectSec handleMove={handleMove} handleOut={handleOut} />
      <ContactSec handleMove={handleMove} handleOut={handleOut} />
      <HomeComp upScroll={upScroll} handleMove={handleMove} handleOut={handleOut} />
    </div>
  );
}

export default App;