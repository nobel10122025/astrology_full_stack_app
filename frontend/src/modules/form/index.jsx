import React, { useState } from 'react';

import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { TimeField } from '@mui/x-date-pickers/TimeField';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import Typography from '@mui/material/Typography';
import { TextField, Box, Button } from '@mui/material';
import Checkbox from '@mui/material/Checkbox';
import Snackbar from '@mui/material/Snackbar';
import FormControlLabel from '@mui/material/FormControlLabel';

import { useStyles } from './style';
import { generate_horoscope } from '../apis/apis';
import { createPayload, payload_constants, chart_color_constants } from './utils';

import { PlanetTable } from '../planet-table';
import { KarmaTabs } from '../karma-tabs';

function FormPage() {
  const [data, setData] = useState(null)
  const [userValues, setUserValues] = useState({ date: '', long: '', lat: '', time: '', user_name: '' })
  const [loading, setLoading] = useState(false)
  const [toasterOpen, setToasterOpen] = useState(false)
  const [generateChart, setGenerateChart] = useState(false)
  const classes = useStyles()

  const handleClose = () => {
    setToasterOpen(false);
  };

  const generateHoroscope = () => {
    const formattedPayload = createPayload(userValues)
    const chart_constants = generateChart ? chart_color_constants : {}
    if (chart_constants && Object.keys(chart_constants).length > 0) chart_constants["chart_config"]["native_name"] = userValues["user_name"]
    setLoading(true)
    generate_horoscope({ ...formattedPayload, ...payload_constants, ...chart_constants, generate_chart: generateChart }).then((res) => res.json()).then((data) => {
      setData(data)
      setLoading(false)
    }).catch((err) => {
      console.log("err", err)
      setLoading(false)
      setToasterOpen(true)
    })
  }

  return (
    <>
      <Box className={classes.root}>
        <Box className={classes.formHolder}>
          <Typography variant='h6' align='center' color='success' fontWeight={700}>Generate your horoscope</Typography>
          <Box className={classes.fieldHolder} >
            <Typography className={classes.title}>Name</Typography>
            <TextField
              id="outlined-number"
              type="string"
              slotProps={{
                inputLabel: {
                  shrink: true,
                },
              }}
              variant="outlined"
              onChange={(event) => setUserValues({ ...userValues, user_name: event.target.value })}
            />
          </Box>
          <Box className={classes.fieldHolder} >
            <Typography className={classes.title}>Birth Date</Typography>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <DatePicker onChange={(value) => setUserValues({ ...userValues, date: value.format("DD-MM-YYYY") })} />
            </LocalizationProvider>
          </Box>
          <Box className={classes.fieldHolder} >
            <Typography className={classes.title}>Birth time</Typography>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <TimeField
                format="HH:mm:ss"
                onChange={(value) => setUserValues({ ...userValues, time: value.format("HH:mm:ss") })}
              />
            </LocalizationProvider>
          </Box>
          <Box className={classes.fieldHolder}>
            <Typography className={classes.title}>Lantitude</Typography>
            <TextField
              id="outlined-number"
              type="number"
              slotProps={{
                inputLabel: {
                  shrink: true,
                },
              }}
              variant="outlined"
              onChange={(event) => setUserValues({ ...userValues, lat: event.target.value })}
            />
          </Box>
          <Box className={classes.fieldHolder} >
            <Typography className={classes.title}>Longtitude</Typography>
            <TextField
              id="outlined-number"
              type="number"
              variant={"outlined"}
              slotProps={{
                inputLabel: {
                  shrink: true,
                },
              }}
              onChange={(event) => setUserValues({ ...userValues, long: event.target.value })}
            />
          </Box>
          <FormControlLabel control={
            <Checkbox
              color="secondary"
              onChange={(event) => setGenerateChart(event.target.checked)}
            />}
            label="Generate Chart"
          />
          <Box className={classes.btnContainer}>
            <Button
              variant='contained'
              color={'secondary'}
              onClick={() => generateHoroscope()}
              disabled={loading || Object.values(userValues).some(currentVal => currentVal == "")}
            >
              Generate horoscope
            </Button>
          </Box>
        </Box>
        {data && data.chart && <Box>
          <Typography variant='h6'>Your Birth Chart</Typography>
          <img src={data.chart} />
        </Box>}
      </Box>
      {data && <PlanetTable planets_data={data.planet_position} />}
      {data && <KarmaTabs karma_list={data.karma_list} />}
      <Snackbar
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        open={toasterOpen}
        onClose={handleClose}
        message={"Opps! Some error occured."}
      />
    </>
  )
}

export default FormPage