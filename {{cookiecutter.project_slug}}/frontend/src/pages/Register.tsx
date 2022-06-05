import { FormEvent, useState } from "react";

import { useNotify } from "react-admin";
import Button from "@mui/material/Button";
import Auth from "../components/Auth";
import { useNavigate } from "react-router";
import { authApi } from "../providers/env";
import { AxiosError } from "axios";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const notify = useNotify();
  const navigate = useNavigate();

  const submit = async (e: FormEvent) => {
    e.preventDefault();
    const formData = { email, password };
    try {
      const response = await authApi.registerRegister({
        userCreate: formData,
      });
      if (response.data.id) {
        notify("Successfully registered, you can now log in", {
          type: "success",
        });
        navigate("/login");
      }
    } catch (e) {
      const exp = e as AxiosError;
      const errorMsg = exp.response?.data.detail[0].msg;
      if (errorMsg) {
        notify(errorMsg, { type: "error" });
      } else {
        notify("Network error", { type: "error" });
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
        <Button color="secondary" onClick={() => navigate("/login")}>
          Sign in
        </Button>
      }
    />
  );
};

export default Register;
