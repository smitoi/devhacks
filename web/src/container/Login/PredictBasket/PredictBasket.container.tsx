import { ICompanyCategory, IPredictBasketComponentOnSubmitData } from "@root/components/PredictBasket/PredictBasket.component";
import { PredictBasketComponent } from "@root/components/PredictBasket/PredictBasket.component";

export const PredictBasketContainer = () => {
  const onSubmit = async (input: IPredictBasketComponentOnSubmitData) => {
    console.log(input);
  };

  const companyCategories = [
    {
      id: 1,
      name: "Restaurant (all types)",
    },
    {
      id: 2,
      name: "Restaurant - Fast food",
    },
    {
      id: 3,
      name: "Restaurant - Traditional",
    },
    {
      id: 4,
      name: "Food trucks (all types)",
    },
    {
      id: 5,
      name: "Food trucks - Sweets",
    },
    {
      id: 6,
      name: "Hotels",
    },
    {
      id: 7,
      name: "Cars (all types)",
    },
    {
      id: 8,
      name: "Cars - Service",
    },
    {
      id: 9,
      name: "Cars - Washing",
    },
  ] as ICompanyCategory[];

  return <PredictBasketComponent {...{ onSubmit, companyCategories }} />;
};
