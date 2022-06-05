import { FormEvent, ReactElement } from "react";

import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardActions from "@mui/material/CardActions";
import TextField from "@mui/material/TextField";
import { Notification } from "react-admin";
import useStyles from "./authStyles";
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
  const classes = useStyles();

  return (
    <form noValidate onSubmit={submit}>
      <div className={classes.main}>
        <Card className={classes.card}>
          <div className={classes.avatar}>
            <Avatar className={classes.icon}>
              <LockIcon />
            </Avatar>
          </div>
          <CardHeader
            title={`{{ cookiecutter.project_name }} - ${actionName}`}
            className={classes.header}
          />
          <div className={classes.form}>
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
          <CardActions className={classes.actions}>
            <Button variant="contained" type="submit" color="primary" fullWidth>
              {actionName}
            </Button>
          </CardActions>
          <CardActions className={classes.actions}>{extraActions}</CardActions>
        </Card>
        <Notification />
      </div>
    </form>
  );
};

export default Auth;
