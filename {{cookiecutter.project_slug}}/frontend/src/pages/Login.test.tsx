import { render, screen } from "@testing-library/react";
import { AdminContext } from "react-admin";
import LoginPage from "./Login";

test("renders login", () => {
  render(
    <AdminContext>
      <LoginPage />
    </AdminContext>
  );
  const loginElements = screen.getAllByText(/Sign in/);
  expect(loginElements).toHaveLength(2);

  const registerElement = screen.getByText(/Register/);
  expect(registerElement).toBeInTheDocument();
});
