import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import { tab_names } from './utils';
import Typography from '@mui/material/Typography'

export const KarmaTabs = ({ karma_list }) => {
    const [value, setValue] = useState(1);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const getColorCode = (level) => {
        if ("very_strong" == level) return "#72BF78"
        if ("strong" == level) return "#A0D683"
        if ("medium" == level) return "#D3EE98"
        if ("low" == level) return "#FEFF9F"
        else return "#F5F4B3"
    }

    return (
        <>
            <Typography variant="h6" align="center">House's Karma</Typography>
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
                            const { level, name, reason } = current_planet
                            return (
                                <TabPanel value={index + 1} style={{ backgroundColor: getColorCode(level) }}>
                                    <span >{name} Karma : </span> <span>{reason}</span>
                                </TabPanel>
                            )
                        })
                    })}
                </TabContext>
            </Box>
        </>
    );
}