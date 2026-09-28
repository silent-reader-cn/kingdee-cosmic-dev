# 关联项列表显示配置-plm_ipdsm_fc_field_cfg

## 关联项列表显示配置-主表 t_plm_ipdsm_fc_cfg

- **表名称：** 关联项列表显示配置-主表
- **表名：** t_plm_ipdsm_fc_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | des | des | varchar | 50 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_fc_cfg |  | fid |
| 2 | idx_plmipdsm_fc_field_cfg |  | des |

---

## 字段配置-多语言表 t_plm_ipdsm_fc_cfg_e_l

- **表名称：** 字段配置-多语言表
- **表名：** t_plm_ipdsm_fc_cfg_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnewname | 重命名 | varchar | 50 |  | √ | ' ' | 重命名 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdsm_fc_cfg_e_l |  | fpkid |
| 2 | idx_ipd_fc_field_cfg_e_l |  | fentryid,flocaleid |

---

## 字段配置-子表 t_plm_ipdsm_fc_cfg_e

- **表名称：** 字段配置-子表
- **表名：** t_plm_ipdsm_fc_cfg_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshow | 关联项列表字段 | bpchar | 1 |  | √ | '1' | 关联项列表字段 |
| 3 | ffieldname | 字段 | varchar | 50 |  | √ | ' ' | 字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnewname | 重命名 | varchar | 50 |  | √ | ' ' | 重命名 |
| 6 | fspecific | 特有属性 | varchar | 50 |  | √ | ' ' | 特有属性 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffieldkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipdsm_fc_cfg_e_fk |  | fid,ffieldname,ffieldkey,fnewname |
| 2 | pk_plm_ipdsm_fc_cfg_e |  | fentryid |
