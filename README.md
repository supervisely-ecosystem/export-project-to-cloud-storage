<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/12828725/180172793-8ae42ac6-76bc-4b5c-bba2-e709dd7ec0c0.png"/>

# Export images project to cloud storage

<p align="center">
  <a href="#Overview">Overview</a> •
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

