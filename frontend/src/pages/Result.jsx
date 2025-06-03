// src/pages/Result.jsx
import { useLocation, useNavigate } from "react-router-dom";
import ViewResult from "../views/viewResult";

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export default function Result() {
  const query = useQuery();
  const username = query.get("username");
  const genre = query.get("genre");
  const era = query.get("era");
  const density = query.get("density");

  const navigate = useNavigate();

  // Recomendación ficticia
  const recommendation = {
    title: "Possession (1981)",
    reason: `Based on your mood (“${genre}”), your preference for ${era.toLowerCase()} films, and your desire for something ${density.toLowerCase()}.`,
    poster: "https://upload.wikimedia.org/wikipedia/en/e/e4/Possession1981poster.jpg",
    link: "https://letterboxd.com/film/possession-1981/",
  };

  return (
    <ViewResult
      username={username}
      recommendation={recommendation}
      onRestart={() => navigate("/")}
    />
  );
}
