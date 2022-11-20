import { yupResolver } from "@hookform/resolvers/yup";
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { schema } from "./schema";

export interface IPredictBasketComponentOnSubmitData {
  companyCategoryId: string;
}

export interface ICompany {
  name: string;
  id: number;
}

export interface IPredictBasketComponent {
  companies: ICompany[];
  currentCompanyId: number | null;
  setCurrentCompanyId: React.Dispatch<React.SetStateAction<number | null>>;
}

export const PredictBasketComponent: React.FC<IPredictBasketComponent> = (props) => {
  const { companies, currentCompanyId, setCurrentCompanyId } = props;

  const onChange = (e: any) => {
    setCurrentCompanyId(parseInt(e.target.value));
  };

  const selectedCompany = currentCompanyId ? companies.find((company) => company.id === currentCompanyId) : null;

  return (
    <div>
      {currentCompanyId ? <div>Hello, {selectedCompany?.name}!</div> : <div>Please log in :D</div>}

      <select onChange={onChange as any} placeholder="Company category">
        <option style={{ display: "none" }} defaultChecked value={undefined}>
          Please select an account
        </option>
        {companies.map((company) => (
          <option value={company.id}>{company.name}</option>
        ))}
      </select>
    </div>
  );
};
