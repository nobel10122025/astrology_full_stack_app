import { makeStyles } from "@mui/styles";

export const useStyles = makeStyles({
  root: {
    display: "flex",
    justifyContent: "space-evenly",
    alignItems: "center",
    width: "100%"
  },
  title: {
    color: "#C62E2E",
    fontWeight: `${600} !important`,
    marginRight: "14px !important",
    width: "30%",
  },
  fieldHolder: {
    display: "flex",
    alignItems: "center",
    margin: "8px 16px",
  },
  button: {
    marginTop: "16px",
  },
  formHolder: {
    width: "95%",
    background: "#FFFFFF",
    borderRadius: "10px",
    padding: "20px",
    display: "flex",
    flexDirection: "column",
    marginLeft: "30px",
    height: "fit-content",
  },
  btnContainer: {
    display: "flex",
    justifyContent: "center",
    marginTop: "16px",
  },
  modal: {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 400,
    backgroundColor: "#FFFFFF",
    border: "2px solid #D3D3D3",
    width: "50%",
    height: (props) =>  props && props.isSignUp ? "90vh" :"47vh",
    borderRadius: '10px'
  },
  link: {
    color: "#FA812F",
    fontWeight: 500,
    cursor: "pointer"
  }
});
