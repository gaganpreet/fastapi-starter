import { AdminContext } from "react-admin";
import { render, screen } from "@testing-library/react";
import Register from "./Register";

test("renders register", () => {
  render(
    <AdminContext>
      <Register />
    </AdminContext>
  );
  const registerElements = screen.getAllByText(/Register/i);
  expect(registerElements).toHaveLength(2);

  const signInElement = screen.getByText(/Sign in/);
  expect(signInElement).toBeInTheDocument();
});
