import * as yup from "yup";

export const schema = yup.object({
  companyCategoryId: yup.string().required(),
});
