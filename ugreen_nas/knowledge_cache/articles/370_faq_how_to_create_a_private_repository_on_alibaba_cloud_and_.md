# [FAQ] How to Create a Private Repository on Alibaba Cloud and Upload Images

> **Article ID**: `370`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [FAQ] How to Create a Private Repository on Alibaba Cloud and Upload Images`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/370  

---

Using Alibaba Cloud Container Registry (ACR), you can easily manage and distribute Docker images. The following steps explain how to create a private repository on Alibaba Cloud and upload a local Docker image to it.

## Create a Private Repository on Alibaba Cloud

### Log in to the [Alibaba Cloud Console](https://www.aliyun.com/)

Open your browser and go to [the Alibaba Cloud Console](https://www.aliyun.com/) , then log in.

### Enable Container Registry

● Navigate to [Container Registry]. On the console homepage, go to [Product] > [Container], and select "Container Registry".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/f8af3e3d770344e998b1c6266ddecf8b.webp)

● In [Container Registry ACR], click "Get it free". The trial version supports up to 100 image repositories.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/8aa3c513a8aa4b49a88f8d4c9f059e85.webp)

### Create a Namespace

In the left-hand navigation panel, select [Namespace], then click the "Create Namespace" button. Enter the namespace name and set the [Default Repository Type] to "Private".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/c6d825a457864d2f9149d447e6536fc0.webp)

### Create a Repository

In the left-hand navigation panel, select [Repositories], then click the "Create Repository" button. Choose the namespace you just created, enter the repository name, set the “Repository Type” to "Private", and the content for the summary can be customized. Click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/0a4b5489e44b4088a55916928d3ade5d.webp)

1. Select the code source you want to use and configure it according to the build requirements of that source.

2. After confirming the settings are correct, click "Create Repository".

## Prepare the Docker Image

### Method 1: Upload a TAR Image Package Downloaded from the Web to a Private Repository

If your computer cannot directly access Docker Hub, you can use the following method to work with and upload images: First, download the `.tar` format image package from a web source to your local machine. Then, upload this image package to your Alibaba Cloud private repository to enable image distribution and usage.

**Steps**:

1. **Download Docker Desktop on Windows.**

![](https://file-us.ugreennas.com/admin/article/2025-09-04/08b9aef6a66b4b30892e263033c68b2c.webp)

2. **Download the Image Package:**

● Download a `.tar` format Docker image package to your local computer from a link provided by others or other sources.

3. **Load the Image into the Local Docker Environment:**

● Use a Docker command to load the `.tar` file into your local Docker environment. Replace `/path/to/your/image.tar` with the actual path to your `.tar` image file.

```
docker load -i /path/to/your/image.tar
```

### Method 2: Download an Image Package from Docker Desktop

If your computer can connect to docker.hub, you can download images directly in Docker Desktop. For example, you can download the Ubuntu image as shown in the illustration.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/33d0e4b5fa18463295bf0fd944392435.webp)

After the download is complete, open the command line by pressing **Win + R**, typing `cmd`, and hitting Enter. Then enter the command `docker images` to view the downloaded image. (Of course, if you downloaded the image through other means, you can also use the `docker import` command to import the image into Docker Desktop.)

![](https://file-us.ugreennas.com/admin/article/2025-09-04/404c79e9771c48a8a51237482e2bddc8.webp)

## Upload the Image to Alibaba Cloud Private Repository

1. The next step is to upload the image to your Alibaba Cloud private image repository. Below is a sample command provided by Alibaba Cloud, which you can find in the image repository page.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/4da4ccd8f2d94fb6b4e0a1e0c18745f9.webp)

2. Log in to Alibaba Cloud Container Registry. Press **Win + R** to open the Run dialog, type `CMD` to open the Command Prompt, then enter the following command in the prompt:

```
docker login --username=<your-username> registry.cn-hangzhou.aliyuncs.com
```

● `<your-username>`is your Alibaba Cloud account. You will need to enter your Alibaba Cloud account password when logging in.

3. Tag the local image with the Alibaba Cloud repository tag.

```
docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/<namespace>/<repository>:[Image Version Number]
```

● `ImageId`：Local image name.

● `namespace`：Name of the namespace.

● `<repository>`：Name of the repository.

● `<tag>`：Image tag (e.g., `latest`).

Example:

```
docker tag 37bb9c63c8b2 registry-vpc.cn-hangzhou.aliyuncs.com/acs/agent:0.7-dfb6816
```

4. For example, if my username is `ugreen_docker`, replace the placeholder and execute the command.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/3d557773e36149b7ac578683a05a4bd0.webp)

After logging in successfully, push the image:

docker tag ubuntu:24.04 registry.cn-hangzhou.aliyuncs.com/ugreen\_docker/ubuntu:24.04

docker push registry.cn-hangzhou.aliyuncs.com/ugreen\_docker/ubuntu:24.04

5. Push the image to the Alibaba Cloud repository.

```
docker push registry.cn-hangzhou.aliyuncs.com/<namespace>/<repository>:[Image Version Number]
```

Example:

```
docker push registry-vpc.cn-hangzhou.aliyuncs.com/acs/agent:0.7-dfb6816
```

6. Verify the upload by logging into the Alibaba Cloud console.

Go to the Container Registry service, locate the repository you just created, and confirm that the image has been successfully uploaded.
