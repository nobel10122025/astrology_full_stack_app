import React from 'react'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Box, Typography } from '@mui/material';
import { header_list } from './utils';
import { useStyles } from './style';


export const PlanetTable = ({ planets_data }) => {
    const classes = useStyles()
    return (
        <>
            <Typography variant='h6' align='center'>Planet's Information</Typography>
            <Box className={classes.tableContainer}>
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                {header_list.map((currentTitle) => {
                                    return (<TableCell align='center'>{currentTitle}</TableCell>)
                                })}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {planets_data && planets_data.length > 0 && planets_data.map((currentPlanet) => {
                                const { name, rasi, star, normDegree, isRetro, star_lord, status } = currentPlanet
                                return (
                                    <TableRow
                                        key={name}
                                    >
                                        <TableCell align='center'>
                                            {name}
                                        </TableCell>
                                        <TableCell align="center">{star}</TableCell>
                                        <TableCell align="center">{rasi}</TableCell>
                                        <TableCell align="center">{normDegree}</TableCell>
                                        <TableCell align="center">{star_lord}</TableCell>
                                        <TableCell align="center">{status}</TableCell>
                                        <TableCell align="center">{isRetro}</TableCell>
                                    </TableRow>
                                )
                            })}
                        </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        </>
    )
}
