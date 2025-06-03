// src/pages/Step3.jsx
import { useNavigate, useLocation } from "react-router-dom";
import { useState } from "react";
import ViewStep3 from "../views/viewStep3";

const eras = ["Classic", "Modern", "Contemporary"];
const densities = ["Entertaining", "Accessible", "Demanding"];

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export default function Step3() {
  const query = useQuery();
  const username = query.get("username");
  const genre = query.get("genre");

  const [era, setEra] = useState(null);
  const [density, setDensity] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = () => {
    if (!era || !density) return;
    navigate(
      `/result?username=${encodeURIComponent(username)}&genre=${encodeURIComponent(
        genre
      )}&era=${encodeURIComponent(era)}&density=${encodeURIComponent(density)}`
    );
  };

  return (
    <ViewStep3
      era={era}
      density={density}
      setEra={setEra}
      setDensity={setDensity}
      handleSubmit={handleSubmit}
      handleBack={() => navigate(-1)}
      eras={eras}
      densities={densities}
      genre={genre}
    />
  );
}
