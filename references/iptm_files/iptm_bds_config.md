# 业务数据统计配置表-iptm_bds_config

## 单据体-子表 t_iptm_bds_configentry

- **表名称：** 单据体-子表
- **表名：** t_iptm_bds_configentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldvalue | 过滤字段值 | varchar | 200 |  | √ | ' ' | 过滤字段值 |
| 3 | fqcp | 比较符 | varchar | 30 |  | √ | ' ' | 比较符,枚举: = :等于 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffieldkey | 过滤字段标识 | varchar | 50 |  | √ | ' ' | 过滤字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_bds_configentry_id |  | fid |
| 2 | idx_iptm_bds_configentry_key |  | ffieldkey |
| 3 | pk_t_iptm_bds_configentry |  | fentryid |

---

## 业务数据统计配置表-多语言表 t_iptm_bds_config_l

- **表名称：** 业务数据统计配置表-多语言表
- **表名：** t_iptm_bds_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fformname | 业务对象名称 | varchar | 200 |  | √ | ' ' | 业务对象名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_bds_config_l |  | fid,flocaleid |
| 2 | pk_t_iptm_bds_config_l |  | fpkid |

---

## 业务数据统计配置表-主表 t_iptm_bds_config

- **表名称：** 业务数据统计配置表-主表
- **表名：** t_iptm_bds_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forgfield | 单据组织字段 | varchar | 50 |  | √ | ' ' | 单据组织字段 |
| 5 | fappnumber | 应用标识 | varchar | 50 |  | √ | ' ' | 应用标识 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisinitial | 是否初始化 | bpchar | 1 |  | √ | ' ' | 是否初始化 |
| 8 | fcloudnumber | 云标识 | varchar | 50 |  | √ | ' ' | 云标识 |
| 9 | fcreatedatefield | 单据创建日期字段 | varchar | 50 |  | √ | ' ' | 单据创建日期字段 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 20 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fformid | 业务对象标识 | varchar | 50 |  | √ | ' ' | 业务对象标识 |
| 17 | fformname | 业务对象名称 | varchar | 200 |  | √ | ' ' | 业务对象名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_bds_config |  | fid |
| 2 | idx_iptm_bos_config_cloudapp |  | fcloudnumber,fappnumber |
| 3 | idx_iptm_bds_config_fnumber |  | fnumber |
