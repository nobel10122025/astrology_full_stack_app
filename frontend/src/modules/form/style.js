import { makeStyles } from '@mui/styles';

export const useStyles = makeStyles({
  root: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '95vh',
    width: '100%',
    flexDirection: 'column',
    backgroundBlendMode: 'lighten',
    backgroundColor: '#CCCCFF'
  },
  title: {
    color: '#4B0082',
    fontWeight: `${600} !important`,
    marginRight: '14px !important'
  },
  fieldHolder: {
    display: 'flex',
    alignItems: 'center'
  },
  button: {
    marginTop: '16px'
  }
});