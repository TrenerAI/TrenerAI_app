import { createContext } from "react";

export interface UserData {
  age: number;
  weight: number;
  height: number;
  gender: string;
}

export const UserContext = createContext<UserData | null>(null);
