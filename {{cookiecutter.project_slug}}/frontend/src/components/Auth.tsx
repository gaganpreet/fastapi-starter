import { FormEvent, ReactElement } from "react";

import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardActions from "@mui/material/CardActions";
import TextField from "@mui/material/TextField";
import { Notification } from "react-admin";
import authStyles from "./authStyles";
import LockIcon from "@mui/icons-material/Lock";

interface AuthProps {
  submit(event: FormEvent): void;
  setEmail(value: string): void;
  setPassword?(value: string): void;
  actionName: string;
  extraActions?: ReactElement;
}

const Auth: React.FC<AuthProps> = ({
  submit,
  setEmail,
  setPassword,
  actionName,
  extraActions,
}) => {
  return (
    <form noValidate onSubmit={submit}>
      <div style={authStyles.main}>
        <Card sx={authStyles.card}>
          <div style={authStyles.avatar}>
            <Avatar>
              <LockIcon />
            </Avatar>
          </div>
          <CardHeader
            title={`{{ cookiecutter.project_name }} - ${actionName}`}
            sx={authStyles.header}
          />
          <div style={authStyles.form}>
            <div>
              <TextField
                id="email"
                label="Email"
                type="email"
                onChange={(e) => setEmail(e.target.value)}
                fullWidth
              />
            </div>

            {setPassword && (
              <div>
                <TextField
                  id="password"
                  label="Password"
                  type="password"
                  fullWidth
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            )}
          </div>
          <CardActions sx={authStyles.actions}>
            <Button variant="contained" type="submit" color="primary" fullWidth>
              {actionName}
            </Button>
          </CardActions>
          <CardActions sx={authStyles.actions}>{extraActions}</CardActions>
        </Card>
        <Notification />
      </div>
    </form>
  );
};

export default Auth;
