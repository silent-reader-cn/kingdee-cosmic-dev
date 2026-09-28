# 流程流转关系-wf_circulaterelation

## 流程流转关系-主表 t_wf_circulaterelation

- **表名称：** 流程流转关系-主表
- **表名：** t_wf_circulaterelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 3 | fparentprocinstid | 父流程实例 | int8 | 64 |  | √ | 0 | 父流程实例 |
| 4 | factinstid | 活动实例ID | int8 | 64 |  | √ | 0 | 活动实例ID |
| 5 | fsourceid | 源单ID | varchar | 36 |  | √ | ' ' | 源单ID |
| 6 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 7 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 8 | fprocidentifier | 流程标识 | varchar | 255 |  | √ | ' ' | 流程标识 |
| 9 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 10 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 11 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: underway :进行中 complete :已完成 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | ftype | 类型(业务流或其他) | varchar | 30 |  | √ | ' ' | 类型(业务流或其他),枚举: bizflow :业务流 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 15 | factid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fbusinesskey | 单据ID | varchar | 36 |  | √ | ' ' | 单据ID |
| 18 | fbizeventid | 业务事件ID | int8 | 64 |  | √ | 0 | 业务事件ID |
| 19 | facttype | 节点类型 | varchar | 50 |  | √ | ' ' | 节点类型 |
| 20 | fbiztracedesc | 业务跟踪描述 | varchar | 500 |  | √ | ' ' | 业务跟踪描述 |
| 21 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 22 | fbizidentifier | 业务标识 | varchar | 255 |  | √ | ' ' | 业务标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_cirelation_tracesrcid |  | fbiztraceno,fsourceid |
| 2 | idx_wf_cirelation_busentity |  | fbusinesskey,fentitynumber |
| 3 | pk_t_wf_circulaterelation |  | fid |
| 4 | idx_wf_circulaterelation |  | fsourceid,fprocinstid |
| 5 | idx_wf_cirelation_procinst |  | fprocinstid |

---

## 流程流转关系-多语言表 t_wf_circulaterelation_l

- **表名称：** 流程流转关系-多语言表
- **表名：** t_wf_circulaterelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fbiztracedesc | 业务跟踪描述 | varchar | 500 |  | √ | ' ' | 业务跟踪描述 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_circulaterelation_l |  | fpkid |
| 2 | idx_wf_circulaterelation_l |  | fid,flocaleid |
