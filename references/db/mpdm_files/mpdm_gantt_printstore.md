# 甘特图打印存储-mpdm_gantt_printstore

## 甘特图打印存储-多语言表 t_mpdm_ganttprintstore_l

- **表名称：** 甘特图打印存储-多语言表
- **表名：** t_mpdm_ganttprintstore_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_gantrel_fid |  | fid,flocaleid |
| 2 | pk_mpdm_ganttprintstore_l |  | fpkid |
| 3 | idx_mpdm_gantrel_fname |  | fname |

---

## 甘特图打印存储-主表 t_mpdm_ganttprintstore

- **表名称：** 甘特图打印存储-主表
- **表名：** t_mpdm_ganttprintstore

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fentityobjectid | 实体对象ID | int8 | 64 |  | √ | 0 | 实体对象ID |
| 6 | fpicstore | 图片存储 | varchar | 255 |  | √ | ' ' | 图片存储 |
| 7 | fentityobjid | 实体对象 | varchar | 255 |  | √ | 0 | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fpageid | 页面ID | varchar | 200 |  | √ | ' ' | 页面ID |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fprintindex | 打印序号 | int4 | 32 |  | √ | 0 | 打印序号 |
| 16 | fbatchid | 批次ID | int8 | 64 |  | √ | 0 | 批次ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_ganttprintstore_fnum |  | fnumber |
| 2 | idx_mpdm_ganttprintstore_fct |  | fcreatetime |
| 3 | pk_mpdm_ganttprintstore |  | fid |
