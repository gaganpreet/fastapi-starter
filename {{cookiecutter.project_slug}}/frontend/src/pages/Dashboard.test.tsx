import React from "react";
import { TestContext } from "ra-test";
import { render, screen } from "@testing-library/react";
import Dashboard from "./Dashboard";

test("renders dashboard", () => {
  render(
    <TestContext>
      <Dashboard />
    </TestContext>
  );
  const linkElement = screen.getByText(/Welcome to admin/i);
  expect(linkElement).toBeInTheDocument();
});
