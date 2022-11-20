export const Loader: React.FC = () => {
  return (
    <div className="flex items-center justify-center ">
      <div className="w-16 h-16 border-b-2 border-gray-900 rounded-full animate-spin"></div>
    </div>
  );
};

export const LoaderCenter: React.FC = () => {
  return (
    <div className="grid h-screen place-items-center">
      <Loader />
    </div>
  );
};
