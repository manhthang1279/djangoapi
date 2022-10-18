import { useState } from "react";
import { Button, Divider, Menu, MenuItem } from "@mui/material";
import './mymenu.scss';


const Mymenu = ({ title, items }) => {

    const [anchorEl, setAnchorEl] = useState(null);
    const handleClick = (event) => {
        if (anchorEl !== event.currentTarget) {
            setAnchorEl(event.currentTarget);
        } else {
            setAnchorEl(null);
        }
    };
    const handleClose = () => {
        setAnchorEl(null)
    }


    return (
        <div>
            <Button
                aria-controls="menu"
                disableRipple
                onMouseOver={handleClick}
            // onClick={handleClick}
            // onMouseEnter={handleClick}
            >
                {title}
            </Button>
            <Menu
                style={{ marginTop: '5px' }}
                anchorEl={anchorEl}
                open={Boolean(anchorEl)}
                keepMounted
                onClose={handleClose}

            >
                <Divider className="divider" />
                {items.map((item) =>
                    <MenuItem className="menuitem" onClick={handleClose}>
                        {item}
                    </MenuItem>
                )}

            </Menu>
        </div>
    );
}

export default Mymenu;
