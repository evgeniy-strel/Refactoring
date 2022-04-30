import React from "react";
import { Link } from "react-router-dom";
import FirstStepInfo from "./FirstStepInfo";

const FirstStep = () => {
  const [activeItem, setActiveItem] = React.useState("");

  const getItemClass = (item) => {
    let itemClass = "button button_option blue";
    if (item === activeItem) itemClass += " button_option_active";
    return itemClass;
  };

  return (
    <main>
      <div className="container">
        <div className="step_choose first_step">
          <div className="choose_category">
            <p className="title">
              Совсем скоро ты сможешь задать вопрос, но сначала
            </p>
            <p className="choose_cat">Выбери категорию:</p>
            <ul className="list">
              {FirstStepInfo.map((item, index) => (
                <li
                  key={`${item}_${index}`}
                  className={getItemClass(item)}
                  onClick={() => {
                    setActiveItem(item);
                    console.log(item);
                  }}
                >
                  {item}
                </li>
              ))}
            </ul>
            <Link to="/second_step" className="button button_next_back yellow">
              Далее
            </Link>
          </div>
          <div className="hint_block">
            <div className="hint">Подсказка</div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default FirstStep;
