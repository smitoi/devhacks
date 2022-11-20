import { PredictBasketContainer } from "@root/container/Login/PredictBasket/PredictBasket.container";
import type { NextPage } from "next";

const Home: NextPage = () => {
  return (
    <div>
      <div className="grid h-screen place-items-center">
        <PredictBasketContainer />
      </div>
    </div>
  );
};

export default Home;
