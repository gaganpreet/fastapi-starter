import React from "react";
import { TestContext } from "ra-test";
import { render, screen } from "@testing-library/react";
import LoginPage from "./Login";

test("renders login", () => {
  render(
    <TestContext>
      <LoginPage />
    </TestContext>
  );
  const loginElements = screen.getAllByText(/Sign in/);
  expect(loginElements).toHaveLength(2);

  const registerElement = screen.getByText(/Register/);
  expect(registerElement).toBeInTheDocument();
});
