import React from "react";
import { Link } from "react-router-dom";
import SecondStepInfo from "./SecondStepInfo";

const SecondStep = () => {
  return (
    <main>
      <div className="container">
        <div className="step_choose first_step">
          <div className="choose_category">
            <p className="title">
              Совсем скоро ты сможешь задать вопрос, но сначала
            </p>
            <p className="choose_cat">Выбери район:</p>
            <ul className="list">
              {SecondStepInfo.map((item, index) => (
                <li key={item} className="button button_option blue">
                  {item}
                </li>
              ))}
            </ul>
            <div className="buttons_next_back">
              <Link to="/first_step" className="button button_next_back yellow">
                Назад
              </Link>
              <Link to="/third_step" className="button button_next_back yellow">
                Далее
              </Link>
            </div>
          </div>
          <div className="hint_block">
            <div className="hint">Подсказка</div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default SecondStep;
