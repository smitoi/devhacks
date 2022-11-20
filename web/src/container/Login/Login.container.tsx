import { ILoginOnSubmit, Login } from "@root/components/Login/Login.component";

export const LoginContainer = () => {
  const onSubmit = async (input: ILoginOnSubmit) => {
    console.log(input);
  };

  return (
    <Login
      {...{
        onSubmit,
      }}
    />
  );
};
