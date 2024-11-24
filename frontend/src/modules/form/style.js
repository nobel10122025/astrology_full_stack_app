import { makeStyles } from '@mui/styles';

export const useStyles = makeStyles({
  root: {
    display: 'flex',
    justifyContent: 'space-evenly',
    alignItems: 'center',
    height: '95vh',
    width: '100%',
    backgroundBlendMode: 'lighten',
    backgroundColor: '#D2E0FB',
  },
  title: {
    color: '#C62E2E',
    fontWeight: `${600} !important`,
    marginRight: '14px !important',
    width: '30%'
  },
  fieldHolder: {
    display: 'flex',
    alignItems: 'center',
    margin: '8px 16px'
  },
  button: {
    marginTop: '16px'
  },
  formHolder: {
    width: '35%',
    background: "#FFFFFF",
    borderRadius: '10px',
    padding: "20px",
    display: 'flex',
    flexDirection: 'column',
    marginLeft: '30px',
    height: 'fit-content'

  },
  btnContainer: {
    display: 'flex',
    justifyContent: 'center',
    marginTop: "16px"
  }
});