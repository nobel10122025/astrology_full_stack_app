import React, { useState, useEffect } from 'react';

import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { Modal, Button } from '@mui/material';

import { get_auth_token, set_sign_up } from '../apis/apis';
import { useStyles } from './style';

import { LoginProps, SignUpProps } from './utils';
import cookie from '../../utils/cookie.js'

export default function LoginPage({ isModalOpen, setIsModalOpen, setIsLoggedIn, setToasterOpen }) {
  const [isSignUp, setIsSignUp] = useState(false)
  const [userValues, setUserValues] = useState({ username: "", password: "" })
  const [renderData, setRenderData] = useState(false)
  const [showError, setShowError] = useState(false)
  const classes = useStyles({ isSignUp })

  console.log("userValues userValues", userValues)

  useEffect(() => {
    if (isSignUp) setRenderData(SignUpProps)
    else setRenderData(LoginProps)
  }, [isSignUp])

  const logUserIn = () => {
    get_auth_token(userValues).then((res) => res.json()).then((data) => {
      if (data.access_token) {
        cookie.setCookie("authToken", data.access_token)
        setIsLoggedIn(true)
        setIsModalOpen(false)
      } else setToasterOpen({ open: true, msg: data.msg })
      setUserValues({})
    })
  }

  const getLoginDetails = () => {
    if (isSignUp) {
      set_sign_up(userValues).then(res => res.json()).then((data) => {
        if (data) logUserIn()
      })
    }
    else logUserIn()
  }

  const resetModal = () => {
    setIsSignUp(!isSignUp)
    setUserValues({})
  }

  return (
    <Modal open={isModalOpen} onClose={() => setIsModalOpen(false)}>
      <Box className={classes.modal}>
        <Box className={classes.root}>
          <Box className={classes.formHolder}>
            <Typography variant='h6' align='center' color='success' fontWeight={700}>{isSignUp ? "Sign Up" : "Sign in"}</Typography>
            {renderData && renderData.map((currentData) => {
              const { key, label, type, max_len, regex_exp, reason } = currentData
              return (
                <Box className={classes.fieldHolder}>
                  <Typography className={classes.title}>{label}</Typography>
                  <TextField
                    id="outlined-number"
                    type={type}
                    slotProps={{
                      inputLabel: {
                        shrink: true,
                      },
                    }}
                    variant="outlined"
                    onChange={(event) => setUserValues({ ...userValues, [key]: event.target.value })}
                    fullWidth={true}
                    helperText={userValues[key] ? regex_exp.test(userValues[key]) ? '' : reason : ''}
                    value={userValues[key]}
                  />
                </Box>
              )
            })}
            <Box className={classes.btnContainer}>
              <Button
                variant='contained'
                color={'secondary'}
                onClick={() => getLoginDetails()}
                disabled={false}
              >
                {isSignUp ? "Sign Up" : "Sign in"}
              </Button>
            </Box>
          </Box>
        </Box>
        {!isSignUp ? <Typography align='center' mb={2}>If you dont have a account? <span onClick={resetModal} className={classes.link}>Sign up</span></Typography> :
          <Typography align='center' mb={2}>Already have a account? <span onClick={resetModal} className={classes.link}>Sign In</span></Typography>}
      </Box>
    </Modal>
  )
}