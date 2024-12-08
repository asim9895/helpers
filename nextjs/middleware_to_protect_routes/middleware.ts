// middleware.js
import { NextRequest, NextResponse } from "next/server";

// List of unprotected routes (public routes)
const PUBLIC_ROUTES = ["/login", "/signup"];

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;

  // Check if the current path is in the public routes
  const isPublicRoute = PUBLIC_ROUTES.some((route) =>
    pathname.startsWith(route)
  );

  // Assuming we use a cookie to check authentication
  const token = "fhbdfhdfh"; // Replace this with your own auth logic

  // If it's a public route, don't protect it, allow access
  if (isPublicRoute) {
    return NextResponse.next();
  }

  // If no token (user is not authenticated), redirect to login
  if (!token) {
    return NextResponse.redirect(new URL("/login", req.url));
  }

  // If authenticated, continue with the request
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api/public).*)"], // Apply middleware to all routes except public API endpoints
};
