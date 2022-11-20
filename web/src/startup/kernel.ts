import { Kernel } from "@bluelibs/core";
import { XUINextBundle } from "@bluelibs/x-ui-next";
import { LoaderCenter } from "@root/components/Loader/Loader";
import { UIAppBundle } from "../bundles/UIAppBundle/UIAppBundle";
import env from "../env";

export const kernel = new Kernel({
  bundles: [
    new XUINextBundle({
      apollo: {
        client: {
          uri: env.API_URL,
        },
      },

      react: {
        initialisingComponent: LoaderCenter,
      },

      guardian: {
        loadingComponent: LoaderCenter,
      },
    }),
    new UIAppBundle(),
  ],
});

export const container = kernel.container;
