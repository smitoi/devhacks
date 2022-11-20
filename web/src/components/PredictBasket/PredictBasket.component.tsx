import { yupResolver } from "@hookform/resolvers/yup";
import { useForm } from "react-hook-form";
import { schema } from "./schema";

export interface IPredictBasketComponentOnSubmitData {
  companyCategoryId: string;
}

export interface ICompanyCategory {
  name: string;
  id: number;
}

export interface IPredictBasketComponent {
  onSubmit: any;

  companyCategories: ICompanyCategory[];
}

export const PredictBasketComponent: React.FC<IPredictBasketComponent> = (props) => {
  const { onSubmit, companyCategories: categories } = props;

  const { handleSubmit, register, formState } = useForm<IPredictBasketComponentOnSubmitData>({
    resolver: yupResolver(schema),

    mode: "all",
  });

  console.log(formState);

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <select {...register("companyCategoryId")} placeholder="Company category">
          {categories.map((category) => (
            <option value={category.id}>{category.name}</option>
          ))}
        </select>
      </form>

      <button type="submit">Predict basket</button>
    </div>
  );
};
