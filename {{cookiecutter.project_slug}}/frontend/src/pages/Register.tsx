import { FormEvent, useState } from "react";

import { Button } from "@material-ui/core";
import { useNotify } from "react-admin";
import Auth from "../components/Auth";
import { useHistory } from "react-router-dom";
import { authApi } from "../providers/env";
import {AxiosError} from "axios";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const notify = useNotify();
  const history = useHistory();

  const submit = async (e: FormEvent) => {
    e.preventDefault();
    const formData = { email, password };
    try {
      const response = await authApi.registerAuthRegisterPost({
        userCreate: formData,
      });
      if (response.data.id) {
        notify("Successfully registered, you can now log in");
        history.push("/login");
      }
    } catch (e) {
        const exp = (e as AxiosError);
        const errorMsg = exp.response?.data.detail[0].msg;
        if (errorMsg) {
            notify(errorMsg);
        } else {
            notify("Network error");
        }
    }
  };

  return (
    <Auth
      setEmail={setEmail}
      setPassword={setPassword}
      actionName="Register"
      submit={submit}
      extraActions={
        <Button color="secondary" onClick={() => history.push("/login")}>
          Sign in
        </Button>
      }
    />
  );
};

export default Register;
