// src/components/SelectableCard.jsx
export default function SelectableCard({ label, emoji, selected, onClick }) {
  return (
    <div
      onClick={onClick}
      className={`selectable-card ${selected ? "selectable-card-selected" : ""}`}
    >
      <div className="selectable-emoji">{emoji}</div>
      <div className="selectable-label">{label}</div>
    </div>
  );
}
