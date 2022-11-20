import "../styles/globals.css";

import { createApp } from "@bluelibs/x-ui-next";
import { kernel } from "../startup/kernel";
import { LoaderCenter } from "@root/components/Loader/Loader";

export default createApp({
  kernel,
  loadingComponent: <LoaderCenter />,
});
