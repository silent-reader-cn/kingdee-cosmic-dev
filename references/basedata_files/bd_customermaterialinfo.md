# 客户物料对应表明细信息-bd_customermaterialinfo

## 客户物料对应表明细信息-主表 t_bd_customermaterialinfo

- **表名称：** 客户物料对应表明细信息-主表
- **表名：** t_bd_customermaterialinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 客户物料分组内码 | int8 | 64 |  | √ | 0 | 客户物料分组内码 |
| 2 | fcusmatmod | 客户物料规格型号 | varchar | 255 |  | √ | ' ' | 客户物料规格型号 |
| 3 | fcusmatgroupnumber | 客户物料分组编码 | varchar | 50 |  | √ | ' ' | 客户物料分组编码 |
| 4 | fismatch | 默认携带 | bpchar | 1 |  | √ | '0' | 默认携带 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fcusmatname | 客户物料名称 | varchar | 255 |  | √ | ' ' | 客户物料名称 |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fcusmatgroupname | 客户物料分组名称 | varchar | 500 |  | √ | ' ' | 客户物料分组名称 |
| 10 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 11 | fentrycomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 12 | fcusmatid | 客户物料编码 | varchar | 255 |  | √ | ' ' | 客户物料编码 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_customermaterialinfo |  | fentryid |
| 2 | idx_bd_customermaterialinfo_fk |  | fid |

---

## 客户物料对应表明细信息-多语言表 t_bd_customermaterialinfo_l

- **表名称：** 客户物料对应表明细信息-多语言表
- **表名：** t_bd_customermaterialinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcusmatmod | 客户物料规格型号 | varchar | 255 |  | √ | ' ' | 客户物料规格型号 |
| 2 | fcusmatname | 客户物料名称 | varchar | 255 |  | √ | ' ' | 客户物料名称 |
| 3 | fentrycomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fcusmatgroupname | 客户物料分组名称 | varchar | 500 |  | √ | ' ' | 客户物料分组名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_customermaterialinfo_l |  | fentryid,flocaleid |
| 2 | pk_t_bd_customermaterialinfo_l |  | fpkid |
