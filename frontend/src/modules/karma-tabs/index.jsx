import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import { tab_names } from './utils';
import Typography from '@mui/material/Typography'
import { TextField } from '@mui/material';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import InputAdornment from '@mui/material/InputAdornment';

export const KarmaTabs = ({ karma_list, setUserValues, userValues, generateHoroscope }) => {
    const [value, setValue] = useState(1);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const getColorCode = (level) => {
        if ("very_strong" == level) return "#72BF78"
        if ("strong" == level) return "#A0D683"
        if ("medium" == level) return "#D3EE98"
        if ("low" == level) return "#FEFF9F"
        if ("very_low" == level) return "#F5F4B3"
        else return "#F3F3E0"
    }

    return (
        <>
            <Typography variant="h6" align="center">House's Karma</Typography>
            <Box display={'flex'} justifyContent={'center'} alignItems={'center'}>
                <Typography mr={2}>Shift the lagna</Typography>
                <TextField
                    id="outlined-number"
                    // label="Lagna"
                    type="number"
                    slotProps={{
                        inputLabel: {
                            shrink: true,
                        },
                    }}
                    onChange={(event) => setUserValues({...userValues, updated_house: event.target.value})}
                    value={userValues['updated_house']}
                    variant="standard"
                    endAdornment={<InputAdornment position="end">
                    </InputAdornment>}
                />
                <IconButton
                    edge="end"
                    onClick={() => generateHoroscope()}
                >
                    <SearchIcon />
                </IconButton>
            </Box>
            <Box sx={{ width: '70%', typography: 'body1', margin: '0px auto' }}>
                <TabContext value={value}>
                    <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                        <TabList onChange={handleChange} aria-label="lab API tabs example" variant="scrollable" orientation="horizontal" color="secondary">
                            {tab_names.map((current_tab, index) => {
                                return (<Tab label={current_tab} value={index + 1} />)
                            })}
                        </TabList>
                    </Box>
                    {karma_list && karma_list.map((current_house, index) => {
                        const valuesToRender = current_house[`${index + 1}`]
                        return valuesToRender && valuesToRender.map((current_planet) => {
                            const { level, name, reason, conjunction } = current_planet
                            return (
                                <TabPanel value={index + 1} style={{ backgroundColor: getColorCode(level) }}>
                                    <span >{name} Karma : </span> <span>{`${reason} ${conjunction ? "(" + conjunction + ")" : ''}`}</span>
                                </TabPanel>
                            )
                        })
                    })}
                </TabContext>
            </Box>
        </>
    );
}