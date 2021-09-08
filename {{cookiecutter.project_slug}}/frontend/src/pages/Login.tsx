import { FormEvent, useState } from "react";

import {
  Avatar,
  Button,
  Card,
  CardHeader,
  CardActions,
  TextField,
} from "@material-ui/core";
import { createTheme, makeStyles } from "@material-ui/core/styles";
import { ThemeProvider } from "@material-ui/styles";
import LockIcon from "@material-ui/icons/Lock";
import { defaultTheme, Notification, useLogin, useNotify } from "react-admin";

const theme = createTheme(defaultTheme);

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

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const login = useLogin();
  const classes = useStyles();
  const notify = useNotify();

  const submit = (e: FormEvent) => {
    e.preventDefault();
    login({ email, password }).catch((e) => {
      if (e.response?.data?.detail === "LOGIN_BAD_CREDENTIALS") {
        notify("Invalid credentials");
      }
      notify("Network error");
    });
  };

  return (
    <ThemeProvider theme={createTheme(theme)}>
      <form noValidate onSubmit={submit}>
        <div className={classes.main}>
          <Card className={classes.card}>
            <div className={classes.avatar}>
              <Avatar className={classes.icon}>
                <LockIcon />
              </Avatar>
            </div>
            <CardHeader title="Login" className={classes.header}/>
            <div className={classes.form}>
              <div>
                <TextField
                  id="email"
                  label="Email"
                  onChange={(e) => setEmail(e.target.value)}
                  fullWidth
                />
              </div>
              <div>
                <TextField
                  id="password"
                  label="Password"
                  type="password"
                  fullWidth
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            </div>
            <CardActions className={classes.actions}>
              <Button
                variant="contained"
                type="submit"
                color="primary"
                fullWidth
              >
                Sign in
              </Button>
            </CardActions>
          </Card>
          <Notification />
        </div>
      </form>
    </ThemeProvider>
  );
};

export default Login;
