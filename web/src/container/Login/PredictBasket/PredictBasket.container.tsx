import { ICompany, IPredictBasketComponentOnSubmitData } from "@root/components/PredictBasket/PredictBasket.component";
import { PredictBasketComponent } from "@root/components/PredictBasket/PredictBasket.component";
import env from "@root/env";
import { useEffect, useState } from "react";

import axios from "axios";

export const PredictBasketContainer = () => {
  const [currentCompanyId, setCurrentCompanyId] = useState<null | number>(null);

  const companies = [
    {
      id: 1,
      name: "Fast food restaurant",
    },
    {
      id: 2,
      name: "Fast food restaurant 2",
    },
    {
      id: 3,
      name: "Traditional Restaurant",
    },
    {
      id: 4,
      name: "Chinese Restaurant",
    },
    {
      id: 5,
      name: "Sweet Truck",
    },
    {
      id: 6,
      name: "Grand Hotel",
    },
    {
      id: 7,
      name: "Intercontinental Hotel",
    },
    {
      id: 8,
      name: "Car Moto Fixes",
    },
    {
      id: 9,
      name: "Motor Leads",
    },
    {
      id: 10,
      name: "Self Car Clean",
    },
  ] as ICompany[];

  const loadPredictions = async () => {
    try {
      const response = await axios.post(`${env.API_URL}/predict`, {
        company_id: currentCompanyId,
      });

      console.log(response);
    } catch (err) {
      console.log({ err });
    }
  };

  useEffect(() => {
    if (!currentCompanyId) return;

    loadPredictions();
  }, [currentCompanyId]);

  return <PredictBasketComponent {...{ companies, currentCompanyId, setCurrentCompanyId }} />;
};
