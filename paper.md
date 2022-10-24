# Awesome Object Pose Estimation

A curated list of challenges and papers pertaining to object pose estimation

## Challenges :space_invader:
* [ECCV 2022: Recovering Object Pose](http://cmp.felk.cvut.cz/sixd/workshop_2022/)
* [ECCV 2020: Recovering Object Pose](http://cmp.felk.cvut.cz/sixd/workshop_2020/)
* [ICCV 2019: Recovering Object Pose](http://cmp.felk.cvut.cz/sixd/workshop_2019/)
* [ECCV 2018: Recovering Object Pose](http://cmp.felk.cvut.cz/sixd/workshop_2018/)
* [ICCV 2017: Recovering Object Pose](http://cmp.felk.cvut.cz/sixd/workshop_2017/)
* [ECCV 2016: Recovering Object Pose](https://labicvl.github.io/R6D)
* [ICCV 2015: Recovering Object Pose](https://labicvl.github.io/3DPose-2015.html)
* [ICCV 2015: Occluded Object Challenge](https://hci.iwr.uni-heidelberg.de/vislearn/iccv2015-occlusion-challenge/)


## Papers :ghost:

### 2022 
There are so many papers in objects pose estimation in CVPR22 and ECCV22, so we order them in this order: \
generic without CAD -> generic with CAD -> category level -> tracking/refinement -> specific

* **Gen6D**: Yuan Liu, Yilin Wen, Sida Peng , Cheng Lin, Xiaoxiao Long, Taku Komura, Wenping Wang \
"Gen6D: Generalizable Model-Free 6-DoF Object Pose Estimation from RGB Images." ECCV (2022)\
[code](https://github.com/liuyuan-pal/Gen6D) | [pdf](https://arxiv.org/pdf/2204.10776.pdf)

* **OnePose**: Jiaming Sun, Zihao Wang, Siyu Zhang, Xingyi He, Hongcheng Zhao, Guofeng Zhang, Xiaowei Zhou \
"OnePose: One-Shot Object Pose Estimation without CAD Models." CVPR (2022)\
[code](https://github.com/zju3dv/OnePose) | [pdf](https://arxiv.org/pdf/2205.12257.pdf)

* **FS6D**: Yisheng He, Yao Wang, Haoqiang Fan, Jian Sun, Qifeng Chen\
"FS6D: Few-Shot 6D Pose Estimation of Novel Objects." CVPR (2022)\
[code](https://github.com/ethnhe/FS6D-PyTorch) | [pdf](https://arxiv.org/pdf/2203.14628.pdf)

* **Unseen object pose**: Zhao Chen, Yinlin Hu, Mathieu Salzmann\
"Fusing Local Similarities for Retrieval-based 3D Orientation Estimation of Unseen Objects." ECCV (2022)\
[code](https://github.com/sailor-z/Unseen_Object_Pose) | [pdf](https://arxiv.org/pdf/2203.08472.pdf)

* **Template-pose**: Van Nguyen Nguyen, Yinlin Hu, Yang Xiao, Mathieu Salzmann, Vincent Lepetit\
"Templates for 3D Object Pose Estimation Revisited: Generalization to New Objects and Robustness to Occlusions." CVPR (2022)\
[code](https://github.com/nv-nguyen/template-pose) | [pdf](https://arxiv.org/pdf/2203.17234)

* **OSOP**: Ivan Shugurov, Fu Li, Benjamin Busam, Slobodan Ilic\
"OSOP: A Multi-Stage One Shot Object Pose Estimation Framework." CVPR (2022)\
[pdf](https://arxiv.org/pdf/2203.15533v2.pdf)

* **OVE6D**: Dingding Cai, Janne Heikkilä, Esa Rahtu\
"OVE6D: Object Viewpoint Encoding for Depth-based 6D Object Pose Estimation ." CVPR (2022)\
[code](https://github.com/dingdingcai/OVE6D-pose) | [pdf](https://arxiv.org/pdf/2203.01072.pdf)

* **DISP6D**: Yilin Wen, Xiangyu Li, Hao Pan, Lei Yang, Zheng Wang, Taku Komura, Wenping Wang\
"DISP6D: Disentangled Implicit Shape and Pose Learning for Scalable 6D Pose Estimation." ECCV (2022)\
[code](https://github.com/fylwen/DISP-6D) | [pdf](https://arxiv.org/abs/2107.12549)

* **SHaPO**: Muhammad Zubair Irshad, Sergey Zakharov, Rares Ambrus, Thomas Kollar, Zsolt Kira, Adrien Gaidon\
"SHaPO: Implicit Representations for Multi Object Shape Appearance and Pose Optimization." ECCV (2022)\
[code](https://github.com/zubair-irshad/shapo) | [pdf](https://arxiv.org/pdf/2207.13691.pdf)

* **GPV-Pose**: Yan Di , Ruida Zhang, Zhiqiang Lou , Fabian Manhardt, Xiangyang Ji, Nassir Navab, Federico Tombari\
"GPV-Pose: Category-level Object Pose Estimation via Geometry-guided Point-wise Voting." CVPR (2022)\
[code](https://github.com/lolrudy/gpv_pose) | [pdf](https://arxiv.org/pdf/2203.07918.pdf)

* **SAR-Net**: Haitao Lin, Zichang Liu, Chilam Cheang, Yanwei Fu, Guodong Guo, Xiangyang Xue\
"SAR-Net: Shape Alignment and Recovery Network for Category-level 6D Object Pose and Size Estimation." CVPR (2022)\
[code](https://github.com/hetolin/SAR-Net) | [pdf](https://arxiv.org/pdf/2106.14193.pdf)

* **NeuralPose**: Lin Huang, Tomas Hodan, Lingni Ma, Linguang Zhang, Luan Tran, Christopher Twigg, Po-Chen Wu, Junsong Yuan, Cem Keskin, Robert Wang\
"Neural Correspondence Field for Object Pose Estimation." ECCV (2022)\
[code](https://github.com/LinHuang17/NCF-code) | [pdf](https://arxiv.org/abs/2208.00113)

* **Neural-Sim**: Yunhao Ge, Harkirat Behl, Jiashu Xu, Suriya Gunasekar, Neel Joshi, Yale Song, Xin Wang, Laurent Itti, Vibhav Vineet\
"Neural-Sim: Learning to Generate Training Data with NeRF." ECCV (2022)\
[code](https://github.com/gyhandy/Neural-Sim-NeRF) | [pdf](https://arxiv.org/abs/2207.11368)

* **Nerf-Supervision**: Lin Yen-Chen, Pete Florence, Jonathan T. Barron, Tsung-Yi Lin, Alberto Rodriguez, Phillip Isola\
"NeRF-Supervision: Learning Dense Object Descriptors from Neural Radiance Fields." ECCV (2022)\
[code](https://github.com/yenchenlin/nerf-supervision-public) | [pdf](https://arxiv.org/pdf/2203.01913.pdf)

* **ICG**: Manuel Stoiber, Martin Sundermeyer, Rudolph Triebel\
"ICG: Iterative Corresponding Geometry." CVPR (2022)\
[code](https://github.com/princeton-vl/coupled-iterative-refinement) | [pdf](https://arxiv.org/pdf/2203.12870.pdf)

* **FocalPose**: Georgy Ponimatkin, Yann Labbé, Bryan Russell, Mathieu Aubry, Josef Sivic\
"FocalPose: Focal Length and Object Pose Estimation via Render and Compare." CVPR (2022)\
[code](https://github.com/ponimatkin/focalpose) | [pdf](https://arxiv.org/pdf/2204.05145.pdf)

* **Coupled Iterative Refinement**: Lahav Lipson, Zachary Teed, Ankit Goyal and Jia Deng\
"Coupled Iterative Refinement for 6D Multi-Object Pose Estimation." CVPR (2022)\
[code](https://github.com/princeton-vl/coupled-iterative-refinement) | [pdf](https://arxiv.org/pdf/2203.12870.pdf)

* **RNNPose**: Yan Xu, Kwan-Yee Lin, Guofeng Zhang, Xiaogang Wang, Hongsheng Li\
"RNNPose: Recurrent 6-DoF Object Pose Refinement with Robust Correspondence Field Estimation and Pose Optimization ." CVPR (2022)\
[code](https://github.com/DecaYale/RNNPose) | [pdf](https://arxiv.org/pdf/2203.12870.pdf)

* **Uni6D**: Xiaoke Jiang, Donghai Li, Hao Chen, Ye Zheng, Rui Zhao, Liwei Wu\
"Uni6D: A Unified CNN Framework without Projection Breakdown for 6D Pose Estimation." CVPR (2022)\
[pdf](https://arxiv.org/pdf/2203.14531.pdf)

* **ES6D**: Lahav Lipson, Zachary Teed, Ankit Goyal and Jia Deng\
"A Computation Efficient and Symmetry-Aware 6D Pose Regression Framework." CVPR (2022)\
[code](https://github.com/GANWANSHUI/ES6D) | [pdf](https://arxiv.org/pdf/2204.01080.pdf)

* **DGECN**: Tuo Cao, Fei Luo, Yanping Fu, Wenxiao Zhang, Shengjie Zheng, Chunxia Xiao\
"DGECN: A Depth-Guided Edge Convolutional Network for End-to-End 6D Pose Estimation ." CVPR (2022)\
[code](https://github.com/maplect/DGECN_CVPR2022) | [pdf](https://arxiv.org/pdf/2204.09983.pdf)

* **UDA-COPE**: Taeyeop Lee, Byeong-Uk Lee, Inkyu Shin, Jaesung Choe, Ukcheol Shin, In So Kweon, Kuk-Jin Yoon\
"UDA-COPE: Unsupervised Domain Adaptation for Category-level Object Pose Estimation." CVPR (2022)\
[pdf](https://arxiv.org/pdf/2111.12580.pdf)

* **ZebraPose**: Yongzhi Su, Mahdi Saleh, Torben Fetzer, Jason Rambach, Nassir Navab, Benjamin Busam, Didier Stricker, Federico Tombari\
"ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation
." CVPR (2022)\
[code](https://github.com/suyz526/zebrapose) | [pdf](https://arxiv.org/pdf/2203.09418.pdf)

* **ES6D**: Lahav Lipson, Zachary Teed, Ankit Goyal and Jia Deng\
"A Computation Efficient and Symmetry-Aware 6D Pose Regression Framework." CVPR (2022)\
[code](https://github.com/GANWANSHUI/ES6D) | [pdf](https://arxiv.org/pdf/2204.01080.pdf)

* **SurfEmb**: Rasmus Laurvig Haugaard, Anders Glent Buch\
"SurfEmb: Dense and Continuous Correspondence Distributions for Object Pose Estimation with Learnt Surface Embeddings" CVPR (2022)\
[code](https://github.com/rasmushaugaard/surfemb) | [pdf](https://arxiv.org/pdf/2111.13489.pdf)

* **Polarimetric Pose Prediction**: Pengyuan Wang, HyunJun Jung, Yitong Li, Siyuan Shen, Rahul Parthasarathy Srikanth, Lorenzo Garattoni, Sven Meier, Nassir Navab, Benjamin Busam\
"Polarimetric Pose Prediction." CVPR (2022)\
[pdf](https://arxiv.org/pdf/2112.03810.pdf)

#
* **PIZZA**: Van Nguyen Nguyen*, Yuming Du*, Yang Xiao, Michaël Ramamonjisoa, Vincent Lepetit\
"PIZZA: A Powerful Image-only Zero-Shot Zero-CAD Approach to 6 DoF Tracking." 3DV (2022)\
[code](https://github.com/nv-nguyen/pizza) | [pdf](https://arxiv.org/pdf/2209.07589.pdf)

* **CenterSnap**: Muhammad Zubair Irshad, Thomas Kollar, Michael Laskey, Kevin Stone, Zsolt Kira\
"CenterSnap: Single-Shot Multi-Object 3D Shape Reconstruction and Categorical 6D Pose and Size Estimation." ICRA (2022)\
[code](https://github.com/zubair-irshad/CenterSnap) | [pdf](https://arxiv.org/pdf/2203.01929)

* **UnseenBenchmark**: Minghao Gou, Haolin Pan, Hao-Shu Fang, Ziyuan Liu, Cewu Lu, Ping Tan\
"Unseen Object 6D Pose Estimation: A Benchmark and Baselines." arXiv (2022)\
[code](https://graspnet.net/unseen6d) | [pdf](https://arxiv.org/pdf/2206.11808.pdf)


### 2021

* **CAPTRA**: Yijia Weng, He Wang, Qiang Zhou, Yuzhe Qin, Yueqi Duan, Qingnan Fan, Baoquan Chen, Hao Su, Leonidas J. Guibas.\
"CAPTRA: CAtegory-level Pose Tracking for Rigid and Articulated Objects from Point Clouds." ICCV (2021)\
[code](https://github.com/halfsummer11/CAPTRA) | [pdf](https://arxiv.org/abs/2104.03437)

* **RePOSE**: Shun Iwase, Xingyu Liu, Rawal Khirodkar, Rio Yokota, Kris M. Kitani.\
"RePOSE: Fast 6D Object Pose Refinement via Deep Texture Rendering." ICCV (2021)\
[code](https://github.com/sh8/repose) | [pdf](https://arxiv.org/abs/2104.00633)

* **DualPoseNet**: Jiehong Lin, Zewei Wei, Zhihao Li, Songcen Xu, Kui Jia, Yuanqing Li.\
"DualPoseNet: Category-level 6D Object Pose and Size Estimation Using Dual Pose Network with Refined Learning of Pose Consistency." ICCV (2021)\
[code](https://github.com/Gorilla-Lab-SCUT/DualPoseNet) | [pdf](https://arxiv.org/abs/2103.06526)

* **StereOBJ-1M**: Xingyu Liu, Shun Iwase, Kris M. Kitani.\
"StereOBJ-1M: Large-scale Stereo Image Dataset for 6D Object Pose Estimation." ICCV (2021)\
[pdf](https://arxiv.org/abs/2109.10115)

* **SO-Pose**: Yan Di, Fabian Manhardt, Gu Wang, Xiangyang Ji, Nassir Navab, Federico Tombari.\
"SO-Pose: Exploiting Self-Occlusion for Direct 6D Pose Estimation." ICCV (2021)\
[pdf](https://arxiv.org/abs/2108.08367)

* **PR-GCN**: Guangyuan Zhou, Huiqun Wang, Jiaxin Chen, Di Huang.\
"PR-GCN: A Deep Graph Convolutional Network with Point Refinement for 6D Pose Estimation." ICCV (2021)\
[pdf](https://arxiv.org/abs/2108.09916)

* **ELLIPSDF**: Mo Shan, Qiaojun Feng, You-Yi Jau, Nikolay Atanasov.\
"ELLIPSDF: Joint Object Pose and Shape Optimization with a Bi-level Ellipsoid and Signed Distance Function Description." ICCV (2021)\
[pdf](https://arxiv.org/abs/2108.00355)

* **ODAM**: Kejie Li, Daniel DeTone, Steven Chen, Minh Vo, Ian Reid, Hamid Rezatofighi, Chris Sweeney, Julian Straub, Richard Newcombe.\
"ODAM: Object Detection, Association, and Mapping using Posed RGB Video." ICCV (2021)\
[pdf](https://arxiv.org/abs/2108.10165)

#

* **FS-Net**: Wei Chen, Xi Jia, Hyung Jin Chang, Jinming Duan, Linlin Shen, Ales Leonardis.\
"FS-Net: Fast Shape-Based Network for Category-Level 6D Object Pose Estimation With Decoupled Rotation Mechanism." CVPR (2021)\
[code](https://github.com/DC1991/FS_Net) | [pdf](https://arxiv.org/abs/2103.07054)

* **RobotPose**: Yann Labbé, Justin Carpentier, Mathieu Aubry, Josef Sivic.\
"Single-view robot pose and joint angle estimation via render & compare." CVPR (2021)\
[code](https://github.com/ylabbe/robopose) | [pdf](https://arxiv.org/abs/2104.09359)

* **GDR-Net**: Gu Wang, Fabian Manhardt, Federico Tombari, Xiangyang Ji.\
"GDR-Net: Geometry-Guided Direct Regression Network for Monocular 6D Object Pose Estimation." CVPR (2021)\
[code](https://github.com/THU-DA-6D-Pose-Group/GDR-Net) | [pdf](https://arxiv.org/abs/2102.12145)

* **FFB6D**: Yisheng He, Haibin Huang, Haoqiang Fan, Qifeng Chen, Jian Sun.\
"FFB6D: A Full Flow Bidirectional Fusion Network for 6D Pose Estimation." CVPR (2021)\
[code](https://github.com/ethnhe/FFB6D) | [pdf](https://arxiv.org/abs/2103.02242)

* **StablePose**: Yifei Shi, Junwen Huang, Xin Xu, Yifan Zhang, Kai Xu.\
"StablePose: Learning 6D Object Poses from Geometrically Stable Patches." CVPR (2021)\
[pdf](https://arxiv.org/abs/2102.09334)

* **WideDepth**: Yinlin Hu, Sebastien Speierer, Wenzel Jakob, Pascal Fua, Mathieu Salzmann.\
"Wide-Depth-Range 6D Object Pose Estimation in Space." CVPR (2021)\
[pdf](https://arxiv.org/abs/2104.00337)

* **Keypoint-Graph**: Shaobo Zhang, Wanqing Zhao, Ziyu Guan, Xianlin Peng, Jinye Peng.\
"Keypoint-Graph-Driven Learning Framework for Object Pose Estimation." CVPR (2021).\
[pdf](https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_Keypoint-Graph-Driven_Learning_Framework_for_Object_Pose_Estimation_CVPR_2021_paper.html)

#

* **BundleTrack**: Bowen Wen, Kostas Bekris.\
"BundleTrack: 6D Pose Tracking for Novel Objects without Instance or Category-Level 3D Models." IROS (2021)\
[code](https://github.com/wenbowen123/BundleTrack) | [pdf](https://arxiv.org/abs/2108.00516)

* **CorNet**: Giorgia Pitteri, Slobodan Ilic, Vincent Lepetit\
"CorNet: Generic 3D Corners for 6D Pose Estimation of New Objects without Retraining " ICCVw (2021)\
[pdf](https://arxiv.org/pdf/1908.11457.pdf)

* **ZePHyR**: Brian Okorn, Qiao Gu, Martial Hebert, David Held\
"Zero-shot Pose Hypothesis Rating." ICRA (2021)\
[code](https://github.com/r-pad/zephyr) | [pdf](https://arxiv.org/pdf/2104.13526.pdf)

* **iNeRF**: Lin Yen-Chen, Pete Florence, Jonathan T. Barron, Alberto Rodriguez, Phillip Isola, Tsung-Yi Lin\
"iNeRF Inverting Neural Radiance Fields for Pose Estimation." IROS (2021)\
[code](https://github.com/yenchenlin/iNeRF-public) | [pdf](https://arxiv.org/pdf/2012.05877.pdf)



### 2020

* **CosyPose**: Yann Labbé, Justin Carpentier, Mathieu Aubry, Josef Sivic.\
"CosyPose: Consistent multi-view multi-object 6D pose estimation." ECCV (2020)\
[code](https://github.com/ylabbe/cosypose) | [pdf](https://arxiv.org/abs/2008.08465)

* **Few-Shot Viewpoint**: Yang Xiao, Renaud Marlet.\
"Few-Shot Object Detection and Viewpoint Estimation for Objects in the Wild." ECCV (2020)\
[code](https://github.com/YoungXIAO13/FewShotViewpoint) | [pdf](https://arxiv.org/abs/2007.12107)

* **Self6D**: Gu Wang, Fabian Manhardt, Jianzhun Shao, Xiangyang Ji, Nassir Navab, Federico Tombari.\
"Self6D: Self-Supervised Monocular 6D Object Pose Estimation." ECCV (2020)\
[code](https://github.com/THU-DA-6D-Pose-Group/Self6D-Diff-Renderer) | [pdf](https://arxiv.org/abs/2004.06468)

* **NOL**: Kiru Park, Timothy Patten, Markus Vincze.\
"Neural Object Learning for 6D Pose Estimation Using a Few Cluttered Images." ECCV (2020)\
[code](https://github.com/kirumang/NOL) | [pdf](https://arxiv.org/abs/2005.03717)

* **Shape Prior Deformation**: Meng Tian, Marcelo H Ang Jr, Gim Hee Lee.\
"Shape Prior Deformation for Categorical 6D Object Pose and Size Estimation." ECCV (2020)\
[code](https://github.com/mentian/object-deformnet) | [pdf](https://arxiv.org/abs/2007.08454)

* **Mask2CAD**: Weicheng Kuo, Anelia Angelova, Tsung-Yi Lin, Angela Dai.\
"Mask2CAD: 3D Shape Prediction by Learning to Segment and Retrieve." ECCV (2020)\
[pdf](https://arxiv.org/abs/2007.13034)

* **Neural Analysis-by-Synthesis**: Xu Chen, Zijian Dong, Jie Song, Andreas Geiger, Otmar Hilliges.\
"Category Level Object Pose Estimation via Neural Analysis-by-Synthesis." ECCV (2020)\
[pdf](https://arxiv.org/abs/2008.08145)

* **Geometric Correspondence Fields**: Alexander Grabner, Yaming Wang, Peizhao Zhang, Peihong Guo, Tong Xiao, Peter Vajda, Peter M. Roth, Vincent Lepetit.\
"Geometric Correspondence Fields: Learned Differentiable Rendering for 3D Pose Refinement in the Wild." ECCV (2020)\
[pdf](https://arxiv.org/abs/2007.08939)

#

* **EPOS**: Tomas Hodan, Daniel Barath, Jiri Matas.\
"EPOS: Estimating 6D Pose of Objects with Symmetries." CVPR (2020)\
[code](http://cmp.felk.cvut.cz/epos/) | [pdf](http://openaccess.thecvf.com/content_CVPR_2020/papers/Hodan_EPOS_Estimating_6D_Pose_of_Objects_With_Symmetries_CVPR_2020_paper.pdf)

* **LatentFusion**: Keunhong Park, Arsalan Mousavian, Yu Xiang, Dieter Fox.\
"LatentFusion: End-to-End Differentiable Reconstruction and Rendering for Unseen Object Pose Estimation." CVPR (2020)\
[code](https://github.com/NVlabs/latentfusion) | [pdf](https://arxiv.org/abs/1912.00416)

* **MoreFusion**: Kentaro Wada, Edgar Sucar, Stephen James, Daniel Lenton, Andrew J. Davison.\
"MoreFusion: Multi-object Reasoning for 6D Pose Estimation from Volumetric Fusion." CVPR (2020)\
[code](https://morefusion.wkentaro.com) | [pdf](https://arxiv.org/abs/2004.04336)

* **Multi-Path**: Martin Sundermeyer, Maximilian Durner, En Yen Puang, Zoltan-Csaba Marton, Narunas Vaskevicius, Kai O. Arras, Rudolph Triebel.\
"Multi-path Learning for Object Pose Estimation Across Domains." CVPR (2020)\
[code](https://github.com/DLR-RM/AugmentedAutoencoder/tree/multipath) | [pdf](https://arxiv.org/abs/1908.00151)

* **HybridPose**: Chen Song, Jiaru Song, Qixing Huang.\
"HybridPose: 6D Object Pose Estimation under Hybrid Representations." CVPR (2020)\
[code](https://github.com/chensong1995/HybridPose) | [pdf](https://arxiv.org/abs/2001.01869)

* **BPnP**: Bo Chen, Tat-Jun Chin, Alvaro Parra, Jiewei Cao, Nan Li.\
"End-to-End Learnable Geometric Vision by Backpropagating PnP Optimization." CVPR (2020)\
[code](https://github.com/BoChenYS/BPnP) | [pdf](https://arxiv.org/abs/1909.06043)

* **Single-Stage 6D Pose**: Yinlin Hu, Pascal Fua, Wei Wang, Mathieu Salzmann.\
"Single-Stage 6D Object Pose Estimation." CVPR (2020)\
[code](https://github.com/cvlab-epfl/single-stage-pose) | [pdf](https://arxiv.org/pdf/1911.08324.pdf)

* **PVN3D**: Yisheng He, Wei Sun, Haibin Huang, Jianran Liu, Haoqiang Fan, Jian Sun.\
"PVN3D: A Deep Point-wise 3D Keypoints Voting Network for 6DoF Pose Estimation." CVPR (2020)\
[code](https://github.com/ethnhe/PVN3D) | [pdf](https://arxiv.org/abs/1911.04231)

* **KeyPose**: Xingyu Liu, Rico Jonschkowski, Anelia Angelova, Kurt Konolige.\
"KeyPose: Multi-view 3D Labeling and Keypoint Estimation for Transparent Objects." CVPR (2020)\
[code](https://sites.google.com/view/keypose) | [pdf](https://arxiv.org/abs/1912.02805)

* **G2L-Net**: Wei Chen, Xi Jia, Hyung Jin Chang, Jinming Duan, Ales Leonardis.\
"G2L-Net: Global to Local Network for Real-time 6D Pose Estimation with Embedding Vector Features." CVPR (2020)\
[code](https://github.com/DC1991/G2L_Net) | [pdf](https://arxiv.org/abs/2003.11089)

* **ConsistentLandmarks**: Ming Cai, Ian Reid.\
"Reconstruct Locally, Localize Globally: A Model Free Method for Object Pose Estimation." CVPR (2020)\
[pdf](http://openaccess.thecvf.com/content_CVPR_2020/papers/Cai_Reconstruct_Locally_Localize_Globally_A_Model_Free_Method_for_Object_CVPR_2020_paper.pdf)

* **PFRL**: Jianzhun Shao, Yuhang Jiang, Gu Wang, Zhigang Li, Xiangyang Ji.\
"PFRL: Pose-Free Reinforcement Learning for 6D Pose Estimation." CVPR (2020) \
[pdf](http://openaccess.thecvf.com/content_CVPR_2020/papers/Shao_PFRL_Pose-Free_Reinforcement_Learning_for_6D_Pose_Estimation_CVPR_2020_paper.pdf)

* **Canonical Shape Space**: Dengsheng Chen, Jun Li, Zheng Wang, Kai Xu.\
"Learning Canonical Shape Space for Category-Level 6D Object Pose and Size Estimation." CVPR (2020)\
[pdf](https://arxiv.org/abs/2001.09322)

* **OK-POSE**: Wanqing Zhao, Shaobo Zhang, Ziyu Guan, Wei Zhao, Jinye Peng, Jianping Fan.\
"Learning deep network for detecting 3D object keypoints and 6D poses." CVPR (2020)\
[pdf](http://openaccess.thecvf.com/content_CVPR_2020/papers/Zhao_Learning_Deep_Network_for_Detecting_3D_Object_Keypoints_and_6D_CVPR_2020_paper.pdf)

* **SSV**: Siva Karthik Mustikovela, Varun Jampani, Shalini De Mello, Sifei Liu, Umar Iqbal, Carsten Rother, Jan Kautz.\
"Self-Supervised Viewpoint Learning From Image Collections." CVPR (2020)\
[code](https://github.com/NVlabs/SSV) | [pdf](https://arxiv.org/abs/2004.01793)

* **Cylindrical Convolution**: Sunghun Joung, Seungryong Kim, Hanjae Kim, Minsu Kim, Ig-Jae Kim, Junghyun Cho, Kwanghoon Sohn.\
"Cylindrical Convolutional Networks for Joint Object Detection and Viewpoint Estimation." CVPR (2020)\
[pdf](https://arxiv.org/abs/2003.11303)

* **Articulated Object Pose**: Xiaolong Li, He Wang, Li Yi, Leonidas Guibas, A. Lynn Abbott, Shuran Song.\
"Category-Level Articulated Object Pose Estimation." CVPR (2020)\
[pdf](https://arxiv.org/abs/1912.11913)

#

* **DPVL**: Xin Yu, Zheyu Zhuang, Piotr Koniusz, Hongdong Li.\
"6DoF Object Pose Estimation via Differentiable Proxy Voting Loss." BMVC (2020)\
[pdf](https://arxiv.org/abs/2002.03923)

* **Pose Proposal Critic**: Lucas Brynte, Fredrik Kahl.\
"Pose Proposal Critic: Robust Pose Refinement by Learning Reprojection Errors." BMVC (2020)\
[pdf](https://arxiv.org/abs/2005.06262)

* **Self-Supervised 6D**: Juil Sock, Guillermo Garcia-Hernando, Anil Armagan, Tae-Kyun Kim.\
"Introducing Pose Consistency and Warp-Alignment for Self-Supervised 6D Object Pose Estimation in Color Images." 3DV (2020)\
[pdf](https://arxiv.org/abs/2003.12344)

* **PointPoseNet**: Wei Chen, Jinming Duan, Hector Basevi, Hyung Jin Chang, Ales Leonardis.\
"PointPoseNet: Point Pose Network for Robust 6D Object Pose Estimation." WACV (2020)\
[pdf](http://openaccess.thecvf.com/content_WACV_2020/papers/Chen_PonitPoseNet_Point_Pose_Network_for_Robust_6D_Object_Pose_Estimation_WACV_2020_paper.pdf)

* **SymGAN**: Phil Ammirato, Jonathan Tremblay, Ming-Yu Liu, Alexander Berg, Dieter Fox.\
"SymGAN: Orientation Estimation without Annotation for Symmetric Objects." WACV (2020)\
[pdf](http://openaccess.thecvf.com/content_WACV_2020/papers/Ammirato_SymGAN_Orientation_Estimation_without_Annotation_for_Symmetric_Objects_WACV_2020_paper.pdf)

#

* **se(3)-TrackNet**: Bowen Wen, Chaitanya Mitash, Baozhang Ren and Kostas Bekris.\
"se(3)-TrackNet: Data-driven 6D Pose Tracking by Calibrating Image Residuals in Synthetic Domains." IROS (2020)\
[code](https://github.com/wenbowen123/iros20-6d-pose-tracking) | [pdf](https://arxiv.org/abs/2007.13866)

* **6-PACK**: Chen Wang, Roberto Martín-Martín, Danfei Xu, Jun Lv, Cewu Lu, Li Fei-Fei, Silvio Savarese, Yuke Zhu.\
"6-PACK: Category-level 6D Pose Tracker with Anchor-Based Keypoints." ICRA (2020)\
[code](https://github.com/j96w/6-PACK) | [pdf](https://arxiv.org/abs/1910.10750)

* **RotationAnchor**: Meng Tian, Liang Pan, Marcelo H Ang Jr, Gim Hee Lee.\
"Robust 6D Object Pose Estimation by Learning RGB-D Features." ICRA (2020)\
[code](https://github.com/mentian/object-posenet) | [pdf](https://arxiv.org/abs/2003.00188)

* **Self-Supervised 6D**: Xinke Deng, Yu Xiang, Arsalan Mousavian, Clemens Eppner, Timothy Bretl and Dieter Fox.\
"Self-supervised 6D Object Pose Estimation for Robot Manipulation." ICRA (2020)\
[pdf](https://arxiv.org/abs/1909.10159)

* **DirectShape**: Rui Wang, Nan Yang, Joerg Stueckler, Daniel Cremers.\
"DirectShape: Direct Photometric Alignment of Shape Priors for Visual Vehicle Pose and Shape Estimation." ICRA (2020)\
[pdf](https://arxiv.org/abs/1904.10097)

* **Local Surface Embedding**: Giorgia Pitteri, Aurelie Bugeau , Slobodan Ilic, Vincent Lepetit\
"3D Object Detection and Pose Estimation of Unseen Objects in Color Images with Local Surface Embeddings." ACCV (2020)\
[pdf](https://openaccess.thecvf.com/content/ACCV2020/papers/Pitteri_3D_Object_Detection_and_Pose_Estimation_of_Unseen_Objects_in_ACCV_2020_paper.pdf)


### 2019

* **Pix2Pose**: Kiru Park, Timothy Patten, Markus Vincze.\
"Pix2Pose: Pixel-Wise Coordinate Regression of Objects for 6D Pose Estimation." ICCV (2019)\
[code](https://github.com/kirumang/Pix2Pose) | [pdf](https://arxiv.org/abs/1908.07433)

* **CDPN**: Zhigang Li, Gu Wang, Xiangyang Ji.\
"CDPN: Coordinates-Based Disentangled Pose Network for Real-Time RGB-Based 6-DoF Object Pose Estimation." ICCV (2019)\
[code](https://github.com/LZGMatrix/BOP19_CDPN_2019ICCV) | [pdf](http://openaccess.thecvf.com/content_ICCV_2019/papers/Li_CDPN_Coordinates-Based_Disentangled_Pose_Network_for_Real-Time_RGB-Based_6-DoF_Object_ICCV_2019_paper.pdf)

* **DPOD**: Sergey Zakharov, Ivan Shugurov, Slobodan Ilic.\
"DPOD: 6D Pose Object Detector and Refiner." ICCV (2019)\
[pdf](https://arxiv.org/abs/1902.11020)

* **Pose Ambiguity**: Fabian Manhardt, Diego Martin Arroyo, Christian Rupprecht, Benjamin Busam, Tolga Birdal, Nassir Navab, Federico Tombari.\
"Explaining the Ambiguity of Object Detection and 6D Pose From Visual Data." ICCV (2019)\
[pdf](https://arxiv.org/abs/1812.00287)

* **CorNet**: Giorgia Pitteri, Slobodan Ilic, Vincent Lepetit.\
"CorNet: Generic 3D Corners for 6D Pose Estimation of New Objects without Retraining." ICCVW (2019)\
[pdf](https://arxiv.org/abs/1908.11457)

* **CullNet**: Kartik Gupta, Lars Petersson, Richard Hartley.\
"CullNet: Calibrated and Pose Aware Confidence Scores for Object Pose Estimation." ICCVW (2019)\
[pdf](https://arxiv.org/abs/1909.13476)

* **GP2C**: Alexander Grabner, Peter M. Roth and Vincent Lepetit.\
"GP2C: Geometric Projection Parameter Consensus for Joint 3D Pose and Focal Length Estimation in the Wild." ICCV (2019)\
[pdf](https://arxiv.org/abs/1908.02809)

* **RGB-CAD**: Georgios Georgakis, Srikrishna Karanam, Ziyan Wu, Jana Kosecka.\
"Learning Local RGB-to-CAD Correspondences for Object Pose Estimation." ICCV (2019)\
[pdf](https://arxiv.org/abs/1811.07249)

* **Wasserstein Training**: Xiaofeng Liu, Yang Zou, Tong Che, Peng Ding, Ping Jia, Jane You, B.V.K. Vijaya Kumar.\
"Conservative Wasserstein Training for Pose Estimation." ICCV (2019)\
[pdf](http://openaccess.thecvf.com/content_ICCV_2019/papers/Liu_Conservative_Wasserstein_Training_for_Pose_Estimation_ICCV_2019_paper.pdf)

#

* **PVNet**: Sida Peng, Yuan Liu, Qixing Huang, Xiaowei Zhou, Hujun Bao. \
"PVNet: Pixel-wise Voting Network for 6DoF Pose Estimation" CVPR (2019)\
[code](https://github.com/zju3dv/pvnet) | [pdf](https://arxiv.org/abs/1812.11788)

* **DesnseFusion**: Chen Wang, Danfei Xu, Yuke Zhu, Roberto Martín-Martín, Cewu Lu, Li Fei-Fei, Silvio Savarese. \
"DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion." CVPR (2019) \
[code](https://github.com/j96w/DenseFusion) | [pdf](https://arxiv.org/abs/1901.04780)

* **NOCS**: He Wang, Srinath Sridhar, Jingwei Huang, Julien Valentin, Shuran Song, Leonidas J. Guibas. \
"Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation." CVPR (2019)\
[code](https://github.com/hughw19/NOCS_CVPR2019) | [pdf](https://arxiv.org/abs/1901.02970)

* **SegDriven**: Yinlin Hu, Joachim Hugonot, Pascal Fua, Mathieu Salzmann. \
"Segmentation-driven 6D Object Pose Estimation." CVPR (2019)\
[code](https://github.com/cvlab-epfl/segmentation-driven-pose) | [pdf](https://arxiv.org/abs/1812.02541)

* **Spherical Regression**: Shuai Liao, Efstratios Gavves, Cees G. M. Snoek.\
"Spherical Regression: Learning Viewpoints, Surface Normals and 3D Rotations on n-Spheres." CVPR (2019)\
[code](https://github.com/leoshine/Spherical_Regression) | [pdf](https://arxiv.org/abs/1904.05404)

* **ROI-10D**: Fabian Manhardt, Wadim Kehl, Adrien Gaidon.\
"ROI-10D: Monocular Lifting of 2D Detection to 6D Pose and Metric Shape." CVPR (2019)\
[pdf](https://arxiv.org/abs/1812.02781)

#

* **PoseFromShape**: Yang Xiao, Xuchong Qiu, Pierre-Alain Langlois, Mathieu Aubry, Renaud Marlet.\
"Pose from Shape: Deep Pose Estimation for Arbitrary 3D Objects." BMVC (2019)\
[code](https://github.com/YoungXIAO13/PoseFromShape) | [pdf](https://arxiv.org/abs/1906.05105)

* **MetaView**: Hung-Yu Tseng, Shalini De Mello, Jonathan Tremblay, Sifei Liu, Stan Birchfield, Ming-Hsuan Yang, Jan Kautz.\
"Few-Shot Viewpoint Estimation." BMVC (2019)\
[pdf](https://arxiv.org/abs/1905.04957)

* **PoseRBPF**: Xinke Deng, Arsalan Mousavian, Yu Xiang, Fei Xia, Timothy Bretl and Dieter Fox.\
"PoseRBPF: A Rao-Blackwellized Particle Filter for 6D Object Pose Tracking." RSS (2019)\
[code](https://github.com/NVlabs/PoseRBPF) | [pdf](https://arxiv.org/abs/1905.09304)


### 2018

* **Implicit 3D Orientation**: Martin Sundermeyer, Zoltan-Csaba Marton, Maximilian Durner, Manuel Brucker, Rudolph Triebel.\
"Implicit 3D Orientation Learning for 6D Object Detection from RGB Images." ECCV (2018)\
[code](https://github.com/DLR-RM/AugmentedAutoencoder) | [pdf](https://arxiv.org/abs/1902.01275)

* **DeepIM**: Yi Li, Gu Wang, Xiangyang Ji, Yu Xiang and Dieter Fox.\
"DeepIM: Deep Iterative Matching for 6D Pose Estimation." ECCV (2018)\
[code](https://github.com/liyi14/mx-DeepIM) | [pdf](https://arxiv.org/abs/1804.00175)

* **StarMap**: Xingyi Zhou, Arjun Karpur, Linjie Luo, Qixing Huang.\
"StarMap for Category-Agnostic Keypoint and Viewpoint Estimation." ECCV (2018)\
[code](https://github.com/xingyizhou/StarMap) | [pdf](https://arxiv.org/abs/1803.09331)

* **Deep Directional Statistics**: Sergey Prokudin, Peter Gehler, Sebastian Nowozin.\
"Deep Directional Statistics: Pose Estimation with Uncertainty Quantification." ECCV (2018)\
[code](https://github.com/sergeyprokudin/deep_direct_stat) | [pdf](https://arxiv.org/abs/1805.03430)

* **Pose Refine**: Fabian Manhardt, Wadim Kehl, Nassir Navab, Federico Tombari.\
"Deep Model-Based 6D Pose Refinement in RGB." ECCV (2018)\
[code](https://github.com/fabi92/eccv18-rgb_pose_refinement) | [pdf](https://arxiv.org/abs/1810.03065)

* **Heatmap**: Markus Oberweger, Mahdi Rad, Vincent Lepetit.\
"Making Deep Heatmaps Robust to Partial Occlusions for 3D Object Pose Estimation." ECCV (2018)\
[pdf](https://arxiv.org/abs/1804.03959)

* **Insights & Models**: Gilad Divon, Ayellet Tal.\
"Viewpoint Estimation-Insights & Model." ECCV (2018) \
[pdf](https://arxiv.org/abs/1807.01312)

* **Multi-View Multi-Class**: Chi Li, Jin Bai, Gregory D. Hager.\
"A Unified Framework for Multi-View Multi-Class Object Pose Estimation." ECCV (2018)\
[pdf](https://arxiv.org/abs/1803.08103)

* **Fine-Grained**: Yaming Wang, Xiao Tan, Yi Yang, Xiao Liu, Errui Ding, Feng Zhou, Larry S. Davis.\
"3D Pose Estimation for Fine-Grained Object Categories." ECCV workshop (2018)\
[pdf](https://arxiv.org/abs/1806.04314)

#

* **YOLO-6D**: Bugra Tekin, Sudipta N. Sinha, Pascal Fua.\
"Real-Time Seamless Single Shot 6D Object Pose Prediction." CVPR (2018)\
[code](https://github.com/Microsoft/singleshotpose) | [pdf](https://arxiv.org/abs/1711.08848)

* **MultiView Consistency**:  Shubham Tulsiani, Alexei A. Efros, Jitendra Malik.\
"Multi-view Consistency as Supervisory Signal for Learning Shape and Pose Prediction." CVPR (2018) \
[code](https://github.com/shubhtuls/mvcSnP) | [pdf](https://arxiv.org/abs/1801.03910)

* **RotationNet**: Asako Kanezaki, Yasuyuki Matsushita, Yoshifumi Nishida.\
"RotationNet: Joint Object Categorization and Pose Estimation Using Multiviews from Unsupervised Viewpoints." CVPR (2018)\
[code](https://github.com/kanezaki/pytorch-rotationnet) | [pdf](https://arxiv.org/abs/1603.06208)

* **3D-RCNN**: Abhijit Kundu, Yin Li, James M. Rehg.\
"3D-RCNN: Instance-level 3D Object Reconstruction via Render-and-Compare." CVPR (2018)\
[pdf](http://abhijitkundu.info/Publications/3DRCNN_CVPR18.pdf)

* **Feature Mapping**: Mahdi Rad, Markus Oberweger, and Vincent Lepetit.\
"Feature Mapping for Learning Fast and Accurate 3D Pose Inference from Synthetic Images." CVPR (2018)\
[pdf](https://arxiv.org/abs/1712.03904)

* **3D Pose and 3D Model**: Alexander Grabner, Peter M. Roth, and Vincent Lepetit.\
"3D Pose Estimation and 3D Model Retrieval for Objects in the Wild." CVPR (2018)\
[pdf](https://arxiv.org/abs/1803.11493)

#

* **Classification-Regression**: Siddharth Mahendran, Haider Ali, Rene Vidal.\
"A Mixed Classification-Regression Framework for 3D Pose Estimation from 2D Images." BMVC (2018)\
[code](https://github.com/JHUVisionLab/multi-modal-regression) | [pdf](https://arxiv.org/abs/1805.03225)

* **Stochastic Congruent Sets**: Chaitanya Mitash, Abdeslam Boularias, Kostas Bekris.\
"Robust 6D Object Pose Estimation with Stochastic Congruent Sets." BMVC (2018)\
[code](https://github.com/cmitash/model_matching) | [pdf](https://arxiv.org/abs/1805.06324)

* **Multi-Task**: Juil Sock, Kwang In Kim, Caner Sahin, Tae-Kyun Kim.\
"Multi-Task Deep Networks for Depth-Based 6D Object Pose and Joint Registration in Crowd Scenarios". BMVC (2018)\
[pdf](https://arxiv.org/abs/1806.03891)

* **iPose**: Omid Hosseini Jafari, Siva Karthik Mustikovela, Karl Pertsch, Eric Brachmann, Carsten Rother.\
"iPose: Instance-Aware 6D Pose Estimation of Partly Occluded Objects." ACCV (2018)\
[pdf](https://arxiv.org/abs/1712.01924)

* **Domain Transfer**: Mahdi Rad, Markus Oberweger, Vincent Lepetit.\
"Domain Transfer for 3D Pose Estimation from Color Images without Manual Annotations." ACCV (2018)\
[pdf](https://arxiv.org/abs/1810.03707)

#

* **PoseCNN**: Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, Dieter Fox.\
"PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes." RSS (2018)\
[code](https://github.com/yuxng/PoseCNN) | [pdf](https://arxiv.org/abs/1711.00199)

* **DOPE**: Jonathan Tremblay, Thang To, Balakumar Sundaralingam, Yu Xiang, Dieter Fox, Stan Birchfield.\
"Deep Object Pose Estimation for Semantic Robotic Grasping of Household Objects."(CoRL 2018) \
[code](https://github.com/NVlabs/Deep_Object_Pose) | [pdf](https://arxiv.org/abs/1809.10790)

* **SilhoNet**: Gideon Billings, Matthew Johnson-Roberson.\
"SilhoNet: An RGB Method for 3D Object Pose Estimation and Grasp Planning." ICRA (2018)\
[code](https://github.com/gidobot/SilhoNet) | [pdf](https://arxiv.org/abs/1809.06893)

* **Rotational Symmetry**: Enric Corona, Kaustav Kundu, Sanja Fidler.\
"Pose Estimation for Objects with Rotational Symmetry." IROS (2018)\
[code](https://github.com/enriccorona/PoseSym) | [pdf](https://arxiv.org/abs/1810.05780)

* **Pose Interpreter**: Jimmy Wu, Bolei Zhou, Rebecca Russell, Vincent Kee, Syler Wagner, Mitchell Hebert, Antonio Torralba, David M.S. Johnson.\
"Real-Time Object Pose Estimation with Pose Interpreter Networks." IROS (2018)\
[code](https://github.com/jimmyyhwu/pose-interpreter-networks) | [pdf](https://arxiv.org/abs/1808.01099)


### 2017

* **SSD-6D**: Wadim Kehl, Fabian Manhardt, Federico Tombari, Slobodan Ilic, Nassir Navab.\
"SSD-6D: Making RGB-based 3D detection and 6D pose estimation great again." ICCV (2017)\
[code](https://github.com/wadimkehl/ssd-6d) | [pdf](https://arxiv.org/abs/1711.10006)

* **BB8**: Mahdi Rad, Vincent Lepetit.\
"BB8: A Scalable, Accurate, Robust to Partial Occlusion Method for Predicting the 3D Poses of Challenging Objects without Using Depth." ICCV (2017)\
[pdf](https://arxiv.org/abs/1703.10896)

* **Pose Guided RGBD Feature**: V. Balntas, A. Doumanoglou, C. Sahin, J. Sock, R. Kouskouridas, T-K. Kim.\
"Pose Guided RGBD Feature Learning for 3D Object Pose Estimation." ICCV (2017)\
[pdf](https://labicvl.github.io/docs/pubs/Vassilis_ICCV_2017.pdf)

* **MultiView and Camera Motion**: Juil Sock, S.Hamidreza Kasaei, Luis Seabra Lopes, Tae-Kyun Kim.\
"Multi-view 6D Object Pose Estimation and Camera Motion Planning using RGBD Images." ICCVW (2017)\
[pdf](https://labicvl.github.io/docs/pubs/Juil_ICCV_2017.pdf)

#

* **3D Bounding Box**: Arsalan Mousavian, Dragomir Anguelov, John Flynn, Jana Kosecka.\
"3D Bounding Box Estimation Using Deep Learning and Geometry." CVPR (2017)\
[code](https://github.com/smallcorgi/3D-Deepbox) | [pdf](https://arxiv.org/abs/1612.00496)

* **Global Hypothesis**: Frank Michel, Alexander Kirillov, Eric Brachmann, Alexander Krull, Stefan Gumhold, Bogdan Savchynskyy, Carsten Rother.\
"Global Hypothesis Generation for 6D Object Pose Estimation." CVPR (2017)\
[pdf](https://arxiv.org/abs/1612.02287)

* **3D Pose Regression**: Siddharth Mahendran, Haider Ali, Rene Vidal.\
"3D Pose Regression using Convolutional Neural Networks." CVPR workshop (2017) \
[pdf](https://arxiv.org/abs/1708.05628)

#

* **Amazon Picking Challenge**: Andy Zeng, Kuan-Ting Yu, Shuran Song, Daniel Suo, Ed Walker Jr., Alberto Rodriguez, Jianxiong Xiao.\
"Multi-view Self-supervised Deep Learning for 6D Pose Estimation in the Amazon Picking Challenge." ICRA (2017)\
[code](https://github.com/andyzeng/apc-vision-toolbox) | [pdf](https://arxiv.org/abs/1609.09475)


### 2016

* **Point Pair**: Stefan Hinterstoisser, Vincent Lepetit, Naresh Rajkumar, Kurt Konolige.\
"Going Further with Point Pair Features." ECCV (2016)\
[pdf](https://arxiv.org/abs/1711.04061)

* **Local RGB-D Patches**: Wadim Kehl, Fausto Milletari, Federico Tombari, Slobodan Ilic, Nassir Navab.\
"Deep Learning of Local RGB-D Patches for 3D Object Detection and 6D Pose Estimation." ECCV (2016)\
[pdf](https://arxiv.org/abs/1607.06038)

#

* **Uncertainty-Driven**: Eric Brachmann, Frank Michel, Alexander Krull, Michael Ying Yang, Stefan Gumhold, Carsten Rother.\
"Uncertainty-Driven 6D Pose Estimation of Objects and Scenes from a Single RGB Image." CVPR (2016)\
[pdf](https://openaccess.thecvf.com/content_cvpr_2016/html/Brachmann_Uncertainty-Driven_6D_Pose_CVPR_2016_paper.html)

* **Next-Best-View**: Andreas Doumanoglou, Rigas Kouskouridas, Sotiris Malassiotis, Tae-Kyun Kim.\
"Recovering 6D Object Pose and Predicting Next-Best-View in the Crowd." CVPR (2016)\
[pdf](https://arxiv.org/abs/1512.07506)

#

* **Crafting Multi-Task**: Francisco Massa, Renaud Marlet, Mathieu Aubry.\
"Crafting a multi-task CNN for viewpoint estimation." BMVC (2016)\
[code](http://imagine.enpc.fr/~suzano-f/bmvc2016-pose/) | [pdf](https://arxiv.org/abs/1609.03894)


### 2015

* **Render for CNN**: Hao Su, Charles R. Qi, Yangyan Li, Leonidas J. Guibas.\
"Render for CNN: Viewpoint Estimation in Images Using CNNs Trained with Rendered 3D Model Views." ICCV (2015)\
[code](https://github.com/ShapeNet/RenderForCNN) | [pdf](https://arxiv.org/abs/1505.05641)

* **Pose Induction**: Shubham Tulsiani, João Carreira, Jitendra Malik.\
"Pose Induction for Novel Object Categories." ICCV (2015)\
[code](https://github.com/shubhtuls/poseInduction) | [pdf](https://arxiv.org/abs/1505.00066)

* **Analysis-by-Synthesis**: Alexander Krull, Eric Brachmann, Frank Michel, Michael Ying Yang, Stefan Gumhold, Carsten Rother.\
"Learning Analysis-by-Synthesis for 6D Pose Estimation in RGB-D Images." ICCV (2015)\
[pdf](https://arxiv.org/abs/1508.04546)

* **Object Parts Representation**:
Alberto Crivellaro, Mahdi Rad, Yannick Verdie, Kwang Moo Yi, Pascal Fua, Vincent Lepetit.\
"A Novel Representation of Parts for Accurate 3D Object Detection and Tracking in Monocular Images." ICCV (2015)\
[pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Crivellaro_A_Novel_Representation_ICCV_2015_paper.pdf)

#

* **Viewpoints & Keypoints**: Shubham Tulsiani and Jitendra Malik.\
"Viewpoints and Keypoints." CVPR (2015)\
[code](https://github.com/shubhtuls/ViewpointsAndKeypoints) | [pdf](https://arxiv.org/abs/1411.6067)

* **Learning Descriptor**: Paul Wohlhart, Vincent Lepetit.\
"Learning Descriptors for Object Recognition and 3D Pose Estimation." CVPR (2015)\
[code](https://github.com/paroj/ObjRecPoseEst) | [pdf](https://arxiv.org/abs/1502.05908)

#

* **Hashmod**: Wadim Kehl, Federico Tombari, Nassir Navab, Slobodan Ilic, Vincent Lepetit.\
"Hashmod: A Hashing Method for Scalable 3D Object Detection." BMVC (2015)\
 [pdf](https://arxiv.org/abs/1607.06062)

* **Articulated Object Pose**: Frank Michel, Alexander Krull, Eric Brachmann, Michael Ying Yang, Stefan Gumhold and Carsten Rother.\
"Pose Estimation of Kinematic Chain Instances via Object Coordinate Regression." BMVC (2015)\
[pdf](http://wwwpub.zih.tu-dresden.de/~cvweb/publications/papers/2015/Pose_Estimation_of_Kinematic_Chain_Instances_via_Object_Coordinate_Regression-Michel-BMVC15.pdf)


### 2014

* **Latent-Class Hough Forests**: Alykhan Tejani, Danhang Tang, Rigas Kouskouridas, and Tae-Kyun Kim.\
"Latent-Class Hough Forests for 3D Object Detection and Pose Estimation." ECCV (2014)\
[pdf](https://labicvl.github.io/docs/pubs/Aly_ECCV_2014.pdf)

* **3D Object Coordinates**: Eric Brachmann, Alexander Krull, Frank Michel, Stefan Gumhold, Jamie Shotton, Carsten Rother.\
"Learning 6D Object Pose Estimation using 3D Object Coordinates" ECCV (2014)\
[pdf](http://wwwpub.zih.tu-dresden.de/~cvweb/publications/papers/2014/PoseEstimationECCV2014.pdf)


### 2012

* **LINEMOD**: Stefan Hinterstoisser, Vincent Lepetit, Slobodan Ilic, Stefan Holzer, Gary Bradski, Kurt Konolige, Nassir Navab.\
"Model Based Training, Detection and Pose Estimation of Texture-Less 3D Objects in Heavily Cluttered Scenes." ACCV (2012)\
[pdf](https://icwww.epfl.ch/~lepetit/papers/hinterstoisser_accv12.pdf)


### 2010
* **Point-Pair Feature**: Bertram Drost, Markus Ulrich, Nassir Navab, Slobodan Ilic.\
"Model Globally, Match Locally: Efficient and Robust 3D Object Recognition." CVPR (2010)\
[pdf](http://campar.in.tum.de/pub/drost2010CVPR/drost2010CVPR.pdf)


## Other resources

 * [Papers with code 6d-pose-estimation](https://paperswithcode.com/task/6d-pose-estimation)
 * [Papers with code viewpoint-estimation](https://paperswithcode.com/task/viewpoint-estimation)
 * [A Review on Object Pose Recovery](https://arxiv.org/abs/2001.10609)
 * [Instance- and Category-level 6D Object Pose Estimation](https://arxiv.org/abs/1903.04229)
 * [Vision-based Robotic Grasping from Object Localization, Pose Estimation, Grasp
Detection to Motion Planning: A Review](https://arxiv.org/pdf/1905.06658v1.pdf)
