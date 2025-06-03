// src/pages/Step2.jsx
import { useNavigate, useLocation } from "react-router-dom";
import { useState } from "react";
import ViewStep2 from "../views/viewStep2";
/**
 * Genre choice 
 */

const genres = [
  "Laugh", "Just for fun", "Get mad", "Cry",
  "A bit of history", "Something unsettling"
];

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export default function Step2() {
  const query = useQuery();
  const username = query.get("username");
  const navigate = useNavigate();
  const [selected, setSelected] = useState(null);

  const handleSelect = (genre) => {
    setSelected(genre);
    setTimeout(() => {
      navigate(`/step3?username=${username}&genre=${encodeURIComponent(genre)}`);
    }, 500);
  };

  return (
    <ViewStep2
      genres={genres}
      selectedGenre={selected}
      onSelectGenre={handleSelect}
      genre={selected}
    />
  );
}