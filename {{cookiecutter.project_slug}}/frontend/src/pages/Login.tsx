import { FormEvent, useState } from "react";

import { useLogin, useNotify } from "react-admin";
import Auth from "../components/Auth";

import { Button } from "@material-ui/core";
import { useNavigate } from "react-router";
const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const login = useLogin();
  const notify = useNotify();
  const navigate = useNavigate();

  const submit = (e: FormEvent) => {
    e.preventDefault();
    login({ email, password }).catch((e) => {
      const msg = e.response?.data?.detail;
      if (msg) {
        notify(msg, "error");
      } else {
        notify("Network error", "error");
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
        <Button color="secondary" onClick={() => navigate("/register")}>
          Register
        </Button>
      }
    />
  );
};

export default Login;
