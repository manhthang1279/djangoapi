import './header.scss';

import { Grading, Home, LocalLibraryOutlined, LoginOutlined, ScienceOutlined } from '@mui/icons-material';
import Mymenu from '../mymenu/Mymenu';


const Header = ({ title, items }) => {
    const cm = [
        'Thời khóa biểu',
        'Kế hoạch bài dạy',
        'Phân công dạy thay'
    ]
    const tv = [
        'Chủng loại',
        'Mượn trả'
    ]

    return (
        <div className="header">
            <div className="title">TRƯỜNG THCS HOÀNG TIẾN</div>
            <div className="right">
                <Home className='icon' />
                <div className="item">TRANG CHỦ </div>
                <Grading className='icon' />
                <div className="item">
                    <Mymenu title='CHUYÊN MÔN' items={cm} />
                </div>
                <LocalLibraryOutlined className='icon' />
                <div className="item">
                    <Mymenu title='THƯ VIỆN' items={tv} />
                </div>
                <ScienceOutlined className='icon' />
                <div className="item">THIẾT BỊ</div>
                <LoginOutlined className='icon' />
                <div className="item">
                    ĐĂNG NHẬP
                </div>

            </div>
        </div>
    );
}

export default Header;