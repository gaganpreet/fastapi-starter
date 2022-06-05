import { render, screen } from "@testing-library/react";
import Dashboard from "./Dashboard";
import { AdminContext } from "react-admin";

test("renders dashboard", () => {
  render(
    <AdminContext>
      <Dashboard />
    </AdminContext>
  );
  const linkElement = screen.getByText(/Welcome to admin/i);
  expect(linkElement).toBeInTheDocument();
});
