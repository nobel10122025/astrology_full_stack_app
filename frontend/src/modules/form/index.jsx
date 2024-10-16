import React, { useState } from 'react';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import Typography from '@mui/material/Typography';
import { TextField, Box, Button } from '@mui/material';
import { useStyles } from './style';
import bgImage from "../../assets/images.jpeg"
import { generate_horoscope } from '../apis/apis';
import { createPayload, payload_constants } from './utils';

function FormPage() {
  const [data, setData] = useState([])
  const [userValues, setUserValues] = useState({date: '', long: '', lat: ''})
  const classes = useStyles()
  console.log("userValues", userValues)
  console.log("data data", data)

  const generateHoroscope = () => {
    const formattedPayload =  createPayload(userValues)
    generate_horoscope({...formattedPayload, ...payload_constants}).then((res) => res.json()).then((data) => setData(data))
    .catch((err) => console.log("err", err))
  }

  return (
    <Box className={classes.root} style={{ backgroundImage: `url(${bgImage})` }}>
      <Box className={classes.fieldHolder} >
        <Typography className={classes.title}>Date of birth</Typography>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DateTimePicker
            onChange={(value) => setUserValues({...userValues,date:value.format("DD-MM-YYYY HH:mm:ss")})}
            timeSteps={{ hours: 1, minutes: 1, seconds: 1 }}
            views={['year', 'month', 'day', 'hours', 'minutes', 'seconds']}
          />
        </LocalizationProvider>
      </Box>
      <Box className={classes.fieldHolder} >
        <Typography className={classes.title}>Lantitude</Typography>
        <TextField
          id="outlined-number"
          type="number"
          slotProps={{
            inputLabel: {
              shrink: true,
            },
          }}
          variant="standard"
          onChange={(event) => setUserValues({...userValues, lat: event.target.value})}
        />
      </Box>
      <Box className={classes.fieldHolder} >
        <Typography className={classes.title}>Longtitude</Typography>
        <TextField
          id="outlined-number"
          type="number"
          variant="standard"
          slotProps={{
            inputLabel: {
              shrink: true,
            },
          }}
          onChange={(event) => setUserValues({...userValues, long: event.target.value})}
        />
      </Box>
      <Box mt={2}>
      <Button
        variant='contained'
        color={'secondary'}
        onClick={() => generateHoroscope()}
      >
        Generate horoscope
      </Button>
      </Box>
    </Box>
  )
}

export default FormPage