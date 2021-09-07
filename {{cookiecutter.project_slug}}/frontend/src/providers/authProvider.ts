import { authApi } from "./env";

type loginFormType = {
  username: string;
  password: string;
};

const authProvider = {
  login: ({ username, password }: loginFormType) => {
    const formData = { username, password };
    return authApi
      .loginAuthJwtLoginPost(formData)
      .then((response) => {
        return response.data;
      })
      .then((data) => {
        localStorage.setItem("token", data);
      })
      .catch((e) => {
        if (e.response.data?.detail === "LOGIN_BAD_CREDENTIALS") {
          throw new Error("Invalid credentials");
        }
        throw new Error("Network error");
      });
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
  checkAuth: () =>
    localStorage.getItem("token") ? Promise.resolve() : Promise.reject(),
  getPermissions: () => {
    const role = localStorage.getItem("permissions");
    return role ? Promise.resolve(role) : Promise.reject();
  },
};

export default authProvider;
