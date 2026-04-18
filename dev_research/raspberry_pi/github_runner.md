# Starting the github runner

The raspberry pi is set up as a self-hosted runner and the [ci.yml](../../.github/workflows/ci.yml) 
picks this configuration up.

The self-hosted runner needs to be started in order to run the CI. To do this
you can simply run:

```bash
~/actions-runner/run.sh
```

This will start the github worker and start listening for jobs,
any new commits are then automatically deployed.