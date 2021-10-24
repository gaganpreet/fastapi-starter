import React from "react";
import { TestContext } from "ra-test";
import { render, screen } from "@testing-library/react";
import Register from "./Register";

test("renders register", () => {
  render(
    <TestContext>
      <Register />
    </TestContext>
  );
  const registerElements = screen.getAllByText(/Register/i);
  expect(registerElements).toHaveLength(2);

  const signInElement = screen.getByText(/Sign in/);
  expect(signInElement).toBeInTheDocument();
});
