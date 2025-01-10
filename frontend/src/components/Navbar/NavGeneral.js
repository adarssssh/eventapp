import React from 'react'
import styles from '../../styles/Home.module.css'
import file from '../../assests/logo/file.png'
import { useNavigate,Link } from 'react-router-dom';

function NavGeneral() {

    const navigate = useNavigate();

    const handleLogoClick = () => {
        navigate("/")
    }
    const handleUserClick = () => {

        if (localStorage.getItem('token')) {
            navigate("/profile")
        }
        else {
            navigate("/login")
        }
        
    }
  return (
    <div className={styles.header_background} >
      <header className={styles.nav} >
        <div className={styles.logo} onClick={handleLogoClick}>
          <img src={file} alt="Logo" className={styles.navbar_logo} />
        </div>

        <div className={styles.user_logo} onClick={handleUserClick}>

            <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12.6097 9.51178C14.1071 9.51178 15.3202 8.33063 15.3202 6.87364C15.3202 5.41747 14.1071 4.23633 12.6097 4.23633C11.1132 4.23633 9.89924 5.41747 9.89924 6.87364C9.89924 8.33063 11.1132 9.51178 12.6097 9.51178ZM6.63407 15.4005C7.41896 12.9149 9.79771 11.1071 12.6091 11.1071C15.422 11.1071 17.7998 12.9149 18.5842 15.4005C18.8042 16.0974 18.9142 16.4459 18.6422 16.8169C18.3702 17.188 17.9279 17.188 17.0434 17.188H8.17479C7.29023 17.188 6.84795 17.188 6.57597 16.8169C6.304 16.4458 6.41402 16.0974 6.63407 15.4005Z" fill="#43464A"></path>
            <path d="M32 16C32 24.8366 24.8366 32 16 32C7.16344 32 0 24.8366 0 16C0 7.16344 7.16344 0 16 0C24.8366 0 32 7.16344 32 16Z" fill="#43464A"></path>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M16.36 14.2184C18.4089 14.2184 20.0688 12.6022 20.0688 10.6086C20.0688 8.61615 18.4089 7 16.36 7C14.3123 7 12.6513 8.61615 12.6513 10.6086C12.6513 12.6022 14.3123 14.2184 16.36 14.2184ZM8.18351 22.2763C9.25748 18.8752 12.5123 16.4017 16.3591 16.4017C20.208 16.4017 23.4615 18.8752 24.5349 22.2762C24.8359 23.2298 24.9863 23.7066 24.6142 24.2143C24.242 24.722 23.6369 24.722 22.4265 24.722H10.2917C9.08134 24.722 8.47617 24.722 8.10403 24.2143C7.73188 23.7065 7.88242 23.2297 8.18351 22.2763Z" fill="white"></path>
            </svg>

            </div>
      </header>
    
        

            
        
    </div>
  )
}

export default NavGeneral