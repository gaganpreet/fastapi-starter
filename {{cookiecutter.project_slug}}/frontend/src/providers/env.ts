import { AuthApi, Configuration, UsersApi } from "../generated";

export const basePath = process.env.API_BASE || "http://localhost:5000";

const apiConfig: Configuration = new Configuration({
  basePath,
});

export const authApi: AuthApi = new AuthApi(apiConfig);
export const userApi: UsersApi = new UsersApi(apiConfig);
