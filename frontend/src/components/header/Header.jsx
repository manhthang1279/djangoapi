import './header.scss';

import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined';


const Header = () => {
    return (
        <div className="header">
            <div className="title">TRƯỜNG THCS HOÀNG TIẾN</div>
            <div className="right">
                <HomeOutlinedIcon className='homeicon' />
                <div className="item">CHUYÊN MÔN </div>
                <div className="item">THƯ VIỆN </div>
                <div className="item">THIẾT BỊ</div>
                <div className="item">ĐĂNG NHẬP</div>
            </div>
        </div>
    );
}

export default Header;