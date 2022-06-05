import { FormEvent, useState } from "react";

import { useLogin, useNotify } from "react-admin";
import Auth from "../components/Auth";

import Button from "@mui/material/Button";
import { Link } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const login = useLogin();
  const notify = useNotify();

  const submit = (e: FormEvent) => {
    e.preventDefault();
    login({ email, password }).catch((e) => {
      const msg = e.response?.data?.detail;
      if (msg) {
        notify(msg, { type: "error" });
      } else {
        notify("Network error", { type: "error" });
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
        <Button color="secondary" to={"/register"} component={Link}>
          Register
        </Button>
      }
    />
  );
};

export default Login;
