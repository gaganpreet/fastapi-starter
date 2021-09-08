import { FormEvent, useState } from "react";

import {
  Avatar,
  Button,
  Card,
  CardActions,
  CircularProgress,
} from "@material-ui/core";
import { createTheme, makeStyles } from "@material-ui/core/styles";
import { ThemeProvider } from "@material-ui/styles";
import LockIcon from "@material-ui/icons/Lock";
import {
  defaultTheme,
  Notification,
  useLogin,
  useNotify,
} from "react-admin";

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
  input: {
    marginTop: "1em",
  },
  field: {
    width: "100%",
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
    login({ email, password }).catch(() => notify("Invalid email or password"));
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
            <div className={classes.form}>
              <div className={classes.input}>
                <label htmlFor="email">Email</label>
                <div>
                  <input
                    name="email"
                    type="email"
                    value={email}
                    className={classes.field}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
              </div>
              <div className={classes.input}>
                <label htmlFor="password">Password</label>
                <div>
                  <input
                    name="password"
                    type="password"
                    value={password}
                    className={classes.field}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </div>
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
