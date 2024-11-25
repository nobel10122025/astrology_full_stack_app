import React, { useEffect, useState } from 'react';
import dayjs from 'dayjs';

import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { TimeField } from '@mui/x-date-pickers/TimeField';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import Typography from '@mui/material/Typography';
import { TextField, Box, Button, Autocomplete } from '@mui/material';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';

import { useStyles } from './style';
import { generate_horoscope, get_cities_list } from '../apis/apis';
import { createPayload, payload_constants, chart_color_constants } from './utils';


import { PlanetTable } from '../planet-table';
import { KarmaTabs } from '../karma-tabs';
let timeout = null;

function FormPage({ setToasterOpen }) {
  const [data, setData] = useState(null)
  const [userValues, setUserValues] = useState({ date: '', long: '', lat: '', time: '', user_name: '', updated_house: null })
  const [loading, setLoading] = useState(false)
  const [generateChart, setGenerateChart] = useState(false)
  const [city, setCity] = useState('')
  const [cityList, setCityList] = useState([])
  const [completeCities, setCompleteCities] = useState([])
  const classes = useStyles()
  const currentYear = dayjs();

  console.log("userValues userValues", userValues)

  useEffect(() => {
    if (timeout) clearTimeout(timeout)
    timeout = setTimeout(() => get_cities_list({ "name": city }).then((res) => res.json()).then((data) => {
      setCompleteCities(data)
      const citiesName = data.reduce((acc, currentCity) => {
        acc.push(currentCity.name)
        return acc
      }, [])
      setCityList(citiesName)
    }), 1500)
  }, [city])

  const generateHoroscope = (reset=false) => {
    const formattedPayload = createPayload(userValues)
    const chart_constants = generateChart ? chart_color_constants : {}
    if (chart_constants && Object.keys(chart_constants).length > 0) chart_constants["chart_config"]["native_name"] = userValues["user_name"]
    setLoading(true)
    generate_horoscope({ ...formattedPayload, ...payload_constants, ...chart_constants, generate_chart: generateChart, updated_house: userValues["updated_house"] == 0 || reset ? null : userValues["updated_house"] }).then((res) => res.json()).then((data) => {
      setData(data)
      setLoading(false)
    }).catch((err) => {
      console.log("err", err)
      setLoading(false)
      setToasterOpen({ msg: 'Some error occured', open: true })
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
              fullWidth={true}
            />
          </Box>
          <Box className={classes.fieldHolder} >
            <Typography className={classes.title}>Birth Date</Typography>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <DatePicker
                onChange={(value) => setUserValues({ ...userValues, date: value.format("DD-MM-YYYY") })}
                fullWidth={true}
                sx={{ width: '100%' }}
                views={['year', 'month', 'day']}
              />
            </LocalizationProvider>
          </Box>
          <Box className={classes.fieldHolder} >
            <Typography className={classes.title}>Birth time</Typography>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <TimeField
                format="HH:mm:ss"
                onChange={(value) => setUserValues({ ...userValues, time: value.format("HH:mm:ss") })}
                fullWidth={true}
              />
            </LocalizationProvider>
          </Box>
          <Box className={classes.fieldHolder}>
            <Typography className={classes.title}>City</Typography>
            <Autocomplete
              disablePortal
              options={cityList}
              value={city}
              fullWidth={true}
              onChange={(event, value) => {
                const cityDetails = completeCities.length > 0 ? completeCities.find((currentCity) => currentCity.name == value) : null
                if (cityDetails) {
                  setUserValues({ ...userValues, "lat": cityDetails.lat, "long": cityDetails.long })
                  setCity(value)
                }
              }}
              renderInput={(params) => <TextField
                {...params}
                type='search'
                slotProps={{
                  inputLabel: {
                    shrink: true,
                  },
                }}
                onChange={(event) => setCity(event.target.value)}
                value={city}
              />}
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
      {data && <KarmaTabs karma_list={data.karma_list} setUserValues={setUserValues} userValues={userValues} generateHoroscope={generateHoroscope} />}
      <Backdrop
        sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
        open={loading}
      >
        <CircularProgress color="inherit" />
      </Backdrop>
    </>
  )
}

export default FormPage