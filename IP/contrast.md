# Paper1：Smartphones Based Crowdsourcing for Indoor Localization

RSS（Received Signal Strength）fingerprint 

localization :

1. Training: **calibration(校准)** engineers record the RSS fingerprints (e.g., WiFi signal strengths from multiple Access Points, APs) at every location of an interested area and accordingly build a fingerprint database (a.k.a. **radio map**) in which fingerprints are related with the locations where they are recorded.
2. Operating:  user sends a location query with his current RSS fingerprint, localization algorithms retrieve the fingerprint database and return the matched fingerprints as well as the corresponding locations.

Considering user movements in a building, originally separated RSS fingerprints are geographically connected by user moving paths of locations where they are recorded, and they consequently form a high dimension fingerprint space, in which the distances among fingerprints, measured by footsteps, are preserved.

## Locating in Fingerprint Space (LiFS)：

The key idea behind LiFS is that human motions can be applied to connect previously independent radio fingerprints under certain semantics. LiFS requires no prior knowledge of AP locations, which is often unavailable in commercial or office buildings where APs are installed by different organizations. In addition, LiFS’ users are in no need of explicit participation to label measured data with corresponding locations, even in the training stage. In all, LiFS transforms the localization problem from 2D floor plan to a high dimension fingerprint space and introduces new prospective techniques for automatic labeling.

## Result

The average localization error is 5.8 meters and can be reduced to be about 2 meters by incorporating trajectory matching, while the room-level localization error is about 11 percent.

## Section 2 Indoor localization technology and multi-dimensional scaling (MDS)

1. Fingerprinting-based 

The main idea is to fingerprint the surrounding signatures at every location in the areas of interests and then build a fingerprint database. The location is then estimated by mapping the measured fingerprints against the database. Researchers have striven to exploit different signatures of the existing devices or reduce the mapping effort.

2. Model-based.

These schemes calculate locations based on geometrical models rather than search for best-fit signatures from pre-labeled reference database. These approaches trade the measurement efforts at the cost of decreasing localization accuracy.

### 2.2 Simultaneous Localization and Mapping (SLAM)

LiFS exploits the geometry of fingerprint space to construct fingerprints databases. LiFS only measures walking steps and is free of using deadreckoning based on noisy inertial sensors of smartphones. 

### 2.3 Multidimensional Scaling(MDS)

MDS algorithm starts with a matrix of item-item dissimilarities, then assigns a location to each item in d-dimensional space, where d is specified a priori. For sufficiently small d (d = 2; 3), the resulting locations may be displayed in a 2D graph or a 3D structure.

Seeing inter-device distances as a metric of dissimilarity, many approaches of network localization adopt MDS as a tool for calculating the locations of wireless devices

MDS is used to assign a coordinate to each node such that the measured inter-node distances are as much preserved as possible. Some researchers propose MDS to figure out WiFi AP locations [14]. In their approach, AP-AP distances are determined by a radio attenuation model. Although being similar to our solution in terms of the usage of MDS, it is neither for user localization nor fingerprinting-based.

## 3 Framework

collect WiFi RSS characteristics (a.k.a. RSS fingerprints or signatures) at various locations along user movement paths, and the walking distances are also recorded. Walking distances are measured as footsteps from the readings of integrated accelerometers in mobile phones. Similarly, accelerometers also infer the starting and finishing moments of user paths.

LiFS harnesses the walking distance between two endpoints (denoted by corresponding fingerprints) along a user path to establish the geographical relationship among fingerprints.

### 3.1 Training phase

The core task of training phase is to build the fingerprint database. We divide this task into three steps:

**(1) transforming floor plan to stress-free floor plan;** 

we propose stress-free floor plan, which puts real locations in a floor plan into a high dimension space by multidimensional scaling [4], such that the geometrical distances between the points in the high dimension space reflect their real walking distances.Through stress-free floor plan, the walking distances collected by users can be accurately and carefully utilized.

**(2) creating fingerprint space;** 

 According to the inter-fingerprint distances, MDS is used to create a high dimension space, in which fingerprints are represented by points, and their mutual distances are preserved. In traditional approaches, fingerprints are geographically unrelated, losing the possibility of building fingerprint space. 

**(3) mapping fingerprints to real locations.**

In fingerprint database, fingerprints are associated with their collecting locations (i.e., fingerprints are labeled with locations). Such associations are achieved by mapping fingerprint space (fingerprints) to stress-free floor plan (locations)

### 3.2 Operating phase

When a location query comes, usually an RSS fingerprint sent by a user, LiFS takes it as a keyword and searches the fingerprint database. The best matched item is viewed as the location estimation and sent back to users.

In this design, we adopt a simple one, the nearest neighbor algorithm. More specifically, we assume that a fingerprint f is collected at the same location as f0 , if f0 is the most similar to f in the fingerprint database. Besides the classical nearest neighbor algorithm, we also propose a continuous trajectory matching scheme to reduce the localization error caused by the fingerprint ambiguity for mobile users. In this scheme, a user’s location is estimated based on his/her moving trajectory, instead of one single RSS report, by measuring successive RSSs and the accompanying mobility information when a user is moving.

## 4 Strss-free Floor Plan

In our experiment, we set l=2 m. By calculating the distances between all pairs of sample locations, we have the distance matrix D [dij]  , where dij is the walking distance between two sample locations pi and pj in the floor plan. Using D as an input, MDS maps all pis into a d-dimension euclidean space. In a stressfree floor plan, the euclidean distance between a pair of points reflects the walking distance of their corresponding locations in a real floor plan. 

## 5 fingerprint space

### 5.1 fingerprint collection

the RSS fingerprint at this location can be denoted as a vector f = (s1; s2; ... ; sm), where s_i is the RSS of the i-th AP and s_i = 0 if the signal of the i-th AP cannot be detected

Suppose at somewhere a mobile phone records fi; Along with walking users, it moves to another position and records fj. In this case, dij is the number of footsteps during the movement.

### 5.2 pre-processing

RSS difference (dissimilarity) betwenn f<sub>i</sub> and f<sub>j</sub>

<img src="/Users/yuanfangxu/Library/Application Support/typora-user-images/image-20210929204654760.png" alt="image-20210929204654760" style="zoom: 50%;" />

if their dissimilarity \delta<sub>ij</sub> is smaller than a predefined threshold , then they are merged as a same point in the fingerprint space to be generated. Otherwise, if dij >  e, fi and fj are treated as two different points.



Employed a local variance threshold method [13] to detect the number of steps. The method is based on filtering the magnitude of acceleration followed by applying a threshold on the variance of acceleration over a sliding window. 





As for stride length, the variation of stride length can be efficiently alleviated through the fact that non-metric MDS can tolerate measurement errors gracefully, due to its over-determined nature



### 6.1 corridor Recognition

 fingerprints collected at corridors reside in core positions in fingerprint space. In terms of graph centrality, these fingerprints have a relatively large centrality values.  In our context, we adopt the betweenness centrality to identify corridor fingerprints.

Conceptually, vertices that have a high probability to occur on a randomly chosen shortest path between two randomly chosen nodes have a high betweenness. 

According to the distances among fingerprints, we build the Minimum Spanning Tree (MST) T that connects all fingerprints in F. In addition, we compute the vertex betweenness for all vertices (fifingerprints) in T and then distinguish fifingerprints from corridors and other areas based on a betweenness watershed. 

The betweenness watershed value is determined by two parameters: 

1) the area ratio r<sub>c</sub> of corridors to entire floor plan (i.e., r<sub>c</sub>=size(corridor)/size(all)), which is available when generating the stress-free floor plan; 
2) the largest gap of betweenness values of fingerprints. 

The area ratio r<sub>c</sub> is used to cut a feasible inter val of the betweenness distribution and then the watershed is fifinally determined by fifinding the largest gap of betweenness values in the feasible interval.

### 6.2 Room Recognition

To gather the fifingerprints that are suffificiently close to each other, the k-means algorithm 