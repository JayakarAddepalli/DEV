import './Home.css'
import { useState, useEffect } from 'react';

function FeedBackComponent({onClose}){

    // function formSubmittion(event){
    //     event.preventDefault(); //which will remove the default behaviour of the form
    //     console.log(event.target.user.value);

    //     onClose()
    // }    

    const [csrfToken, setCsrfToken] = useState('');

    useEffect(() => {
        const fetchCsrfToken = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/csrf/');
                const data = await response.json();
                setCsrfToken(data.csrfToken);
            } catch (error) {
                console.error('Error fetching CSRF token:', error);
            }
        };

        fetchCsrfToken();
    }, []);


    const formSubmittion = async (e) =>{
        e.preventDefault()

        const formData = new FormData(e.target);
        const body = Object.fromEntries(formData.entries());

        try{
            const response = await fetch('http://127.0.0.1:8000/api/feedback/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken, // Add CSRF token to headers
                },
                body: JSON.stringify({
                    name: e.target.user.value,
                    feedback: e.target.feedback.value,
                }),
            });
        
            if (response.ok){
                console.log('Feedback submitted', body)
                onClose();
                alert('Thanks For Your Feedback')
            }
            else{
                const errorData = await response.json();
                console.log('error submitting feedback', errorData)
            }
        }
        catch(error){
            console.log(error);
        }
    };

    return(
        <>
            <div className="modal-overlay">
                <div className="modal-content">
                    <h4>Feedback</h4>
                    <p>Your feedback is very important for me to improve the website.</p>
                    <div>
                        <form onSubmit={formSubmittion}>
                            <div>
                                <label for='user'><b>Name:</b></label>
                                <input type='text' id='user' name='user' required maxLength={30}></input>
                            </div>
                            <div>
                                <label for='feedback'><b>Re-Marks:</b></label>
                                <textarea id='feedback' name='feedback' required></textarea>
                            </div>
                            <button className='submit-btn'>Submit</button>
                        </form>
                    </div>
                    <div>
                        <button onClick={onClose}>skip</button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default FeedBackComponent
