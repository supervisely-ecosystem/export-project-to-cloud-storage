<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/12828725/180172793-8ae42ac6-76bc-4b5c-bba2-e709dd7ec0c0.png"/>

# Export images project to cloud storage

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a> •
  <a href="#Example">Example</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/export-project-to-cloud-storage)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/export-project-to-cloud-storage)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/export-project-to-cloud-storage)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/export-project-to-cloud-storage)](https://supervise.ly)

</div>

# Overview

This apps allows to export images project with annotations (in [Supervisely format](https://developer.supervise.ly/api-references/supervisely-annotation-json-format)) to the most popular cloud storage providers from Supervisely Private instance.

List of providers:
- Amazon s3
- Google Cloud Storage (CS)
- Microsoft Azure
- and others with s3 compatible interfaces

✅ For developers: you can use the sources of this app as a starting point for your custom export to cloud. 

# How To Run

## Run from Ecosystem

1. Run app from the ecosystem

<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48913536/180185094-853935da-ae2e-4416-97a6-fbe164f9c3c4.png"/>
</div>

2. Select project, provider, enter the bucket name and press the **Run** button in the modal window

<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48913536/180185108-5ec87caa-0fa9-407b-84ee-80155ff6b909.png" width="650"/>
</div>

## Run from Images Project

**Step 1.** Run the application from the context menu of the Images Project

<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48913536/180185139-67c41ae9-360d-4dd9-950b-ee8baae7de24.png">  
</div>

**Step 2.** Select provider, enter the bucket name and press the **Run** button in the modal window

<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/48913536/180185153-d0b394a0-deea-4deb-a509-5519fc70fd4d.png" width="650">
</div>

# How To Use

0. Ask your instance administrator to add cloud credentials to instance settings. It can be done both in .env 
   configuration files or in Admin UI dashboard. Learn more in docs: [link1](https://docs.supervise.ly/enterprise-edition/installation/post-installation#configure-your-instance), 
   [link2](https://docs.supervise.ly/enterprise-edition/advanced-tuning/s3#links-plugin-cloud-providers-support). 
   In case of any questions or issues, please contact tech support.
2. Run app from the context menu of project you would like to export
3. In modal window choose desired cloud provider and define the bucket name (bucket has to be already created)
4. Press RUN button
5. The project will be exported to the following path: `/<bucker name>/<project name>`

# Example

Before import bucket is empty:

<img src="https://user-images.githubusercontent.com/12828725/180176958-4b14654b-ba9a-4882-b0e6-3dbfee224035.png"/>

After import the project data (images and annotations) is in bucket:

https://user-images.githubusercontent.com/12828725/180199053-5571ecf1-e26c-479e-836d-1d5ef0084873.mp4
