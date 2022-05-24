import { UserIdentity } from "react-admin";
import { authApi, userApi } from "./env";

type loginFormType = {
  email: string;
  password: string;
};

const authProvider = {
  login: async ({ email, password }: loginFormType) => {
    const formData = { username: email, password };
    const resp = await authApi.authJwtLogin(formData);
    localStorage.setItem("token", resp.data.access_token);
    return Promise.resolve();
  },
  logout: () => {
    localStorage.removeItem("token");
    return Promise.resolve();
  },
  checkError: (error: { status: number }) => {
    const status = error.status;
    if (status === 401 || status === 403) {
      localStorage.removeItem("token");
      return Promise.reject();
    }
    return Promise.resolve();
  },
  checkAuth: (a: any) => {
    return localStorage.getItem("token") ? Promise.resolve() : Promise.reject();
  },
  getPermissions: () => {
    const role = JSON.parse(localStorage.getItem("permissions") || "{}");
    return role ? Promise.resolve(role) : Promise.reject();
  },
  getIdentity: async (): Promise<UserIdentity> => {
    const resp = await userApi.usersCurrentUser();
    localStorage.setItem("permissions", JSON.stringify(resp.data));
    return resp.data as UserIdentity;
  },
};

export default authProvider;
