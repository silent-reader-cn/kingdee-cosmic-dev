# 运维中心统计被驳回单据-wf_devopsrejectbills

## 运维中心统计被驳回单据-多语言表 t_wf_devopsrejectbills_l

- **表名称：** 运维中心统计被驳回单据-多语言表
- **表名：** t_wf_devopsrejectbills_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 255 |  | √ | ' ' | 实体名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_devopsrejectbills_l |  | fpkid |
| 2 | idx_wf_devopsrejectbills_l |  | fid,flocaleid |

---

## 运维中心统计被驳回单据-主表 t_wf_devopsrejectbills

- **表名称：** 运维中心统计被驳回单据-主表
- **表名：** t_wf_devopsrejectbills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 实体名称 | varchar | 255 |  | √ | ' ' | 实体名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | frejecttimes | 被驳回次数 | int4 | 32 |  | √ | 0 | 被驳回次数 |
| 6 | fbusinesskey | 业务主键 | varchar | 50 |  | √ | ' ' | 业务主键 |
| 7 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 8 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_devopsrjtbill_entity |  | fentitynumber |
| 2 | pk_wf_devopsrejectbills |  | fid |
