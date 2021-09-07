import { AuthApi, Configuration } from "../generated";

const basePath = process.env.API_BASE || "http://localhost:5000";

const apiConfig: Configuration = new Configuration({
  basePath,
});

export const authApi: AuthApi = new AuthApi(apiConfig);
