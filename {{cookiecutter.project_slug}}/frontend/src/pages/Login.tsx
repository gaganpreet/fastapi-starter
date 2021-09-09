import { FormEvent, useState } from "react";

import { useLogin, useNotify } from "react-admin";
import Auth from "../components/Auth";

import {
  Button,
} from "@material-ui/core";
import { useHistory } from "react-router";
const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const login = useLogin();
  const notify = useNotify();
  const history = useHistory();

  const submit = (e: FormEvent) => {
    e.preventDefault();
    login({ email, password }).catch((e) => {
        const msg = e.response?.data?.detail;
        if (msg) {
            notify(msg)
        } else {
            notify("Network error")
        }
    });
  };

  return (
    <Auth
      setEmail={setEmail}
      setPassword={setPassword}
      actionName="Sign in"
      submit={submit}
      extraActions={
        <Button color="secondary" onClick={() => history.push("/register")}>
          Register
        </Button>
      }
    />
  );
};

export default Login;
