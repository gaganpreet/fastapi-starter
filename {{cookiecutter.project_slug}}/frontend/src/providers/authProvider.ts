import { authApi } from "./env";

type loginFormType = {
  email: string;
  password: string;
};

const authProvider = {
  login: ({ email, password }: loginFormType) => {
    const formData = { username: email, password };
    return authApi
      .loginAuthJwtLoginPost(formData)
      .then((response) => {
        return response.data;
      })
      .then((data) => {
        localStorage.setItem("token", data);
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
