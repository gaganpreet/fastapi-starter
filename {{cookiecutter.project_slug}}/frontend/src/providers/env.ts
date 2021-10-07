import { AuthApi, Configuration, UsersApi } from "../generated";

export const basePath =
  process.env.API_BASE || "http://localhost:{{ cookiecutter.backend_port }}";

const readAccessToken = () => {
  return localStorage.getItem("token") || undefined;
};

const apiConfig: Configuration = new Configuration({
  basePath,
  accessToken: readAccessToken(),
});

export const authApi: AuthApi = new AuthApi(apiConfig);
export const userApi: UsersApi = new UsersApi(apiConfig);
