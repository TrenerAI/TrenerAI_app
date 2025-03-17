import { create } from "zustand";

const useUserStore = create((set) => ({
  bmi: 0,
  calories: 0,
  rpe: 0,
  rir: 0,
  setBMI: (bmi) => set({ bmi }),
  setCalories: (calories) => set({ calories }),
  setRPE: (rpe) => set({ rpe }),
  setRIR: (rir) => set({ rir }),
}));

export default useUserStore;
