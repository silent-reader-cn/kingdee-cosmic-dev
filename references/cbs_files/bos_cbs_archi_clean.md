# 单据清除规则-bos_cbs_archi_clean

## 单据清除规则-多语言表 t_cbs_archi_config_l

- **表名称：** 单据清除规则-多语言表
- **表名：** t_cbs_archi_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_config_l |  | fid,flocaleid |
| 2 | pk_cbs_archi_config_l |  | fpkid |

---

## 单据清除规则-主表 t_cbs_archi_config

- **表名称：** 单据清除规则-主表
- **表名：** t_cbs_archi_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | ffiltertype | 条件类型 | varchar | 50 |  | √ | ' ' | 条件类型,枚举: bill :单据 es :ElasticSearch custom :自定义 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fentitynumber | 清除单据（编码） | varchar | 36 |  | √ | ' ' | 清除单据（编码） |
| 8 | ftarget_type | ftarget_type | varchar | 50 |  | √ | ' ' |  |
| 9 | fmovingtype | 转储或清除 | bpchar | 1 |  | √ | ' ' | 转储或清除,枚举: 0 :转储 1 :清除 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | farchiveplugin | farchiveplugin | varchar | 2000 |  | √ | ' ' |  |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbillsetid | 清除单据 | int8 | 64 |  | √ | 0 | 可归档单据范围 bos_cbs_archi_billset |
| 14 | fconditiondesc | 清除条件 | varchar | 2000 |  | √ | ' ' | 清除条件 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fconditiontype | fconditiontype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fpreset | fpreset | bpchar | 1 |  | √ | '0' |  |
| 19 | fsyncbasedata | fsyncbasedata | bpchar | 1 |  | √ | ' ' |  |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 21 | fcondition | 清除条件序列值 | text | 0 |  |  | null | 清除条件序列值 |
| 22 | fregion | fregion | varchar | 50 |  | √ | ' ' |  |
| 23 | fnumber | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_config |  | fid |
| 2 | idx_cbs_archi_config |  | fnumber |
