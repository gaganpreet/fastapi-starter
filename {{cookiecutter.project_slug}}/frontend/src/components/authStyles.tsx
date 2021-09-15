import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  main: {
    display: "flex",
    flexDirection: "column",
    minHeight: "100vh",
    alignItems: "center",
    justifyContent: "flex-start",
    backgroundColor: "#fcf7e1",
  },
  card: {
    minWidth: 300,
    marginTop: "6em",
  },
  header: {
    textAlign: "center",
  },
  avatar: {
    margin: "1em",
    display: "flex",
    justifyContent: "center",
  },
  icon: {
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    padding: "0 1em 1em 1em",
  },
  actions: {
    padding: "0 1em 1em 1em",
  },
}));

export default useStyles;
