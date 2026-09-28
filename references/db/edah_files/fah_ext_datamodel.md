# 异构数据对接模型-fah_ext_datamodel

## 异构数据对接模型-多语言表 t_ai_eventclass_l

- **表名称：** 异构数据对接模型-多语言表
- **表名：** t_ai_eventclass_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_eventclass_l |  | fpkid |
| 2 | idx_ai_eventclass_l |  | fid,flocaleid |

---

## 异构数据对接模型-主表 t_ai_eventclass

- **表名称：** 异构数据对接模型-主表
- **表名：** t_ai_eventclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 异构数据分类 | int8 | 64 |  | √ | 0 | 异构数据分类 fah_ext_datamodel_group |
| 3 | flatestversion | 是否为最新版本 | bpchar | 1 |  | √ | ' ' | 是否为最新版本 |
| 4 | fenabledtime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 C :发布 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 10 | fdisabledtime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisabledby | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fappversion | 是否新模型 | bpchar | 1 |  | √ | '0' | 是否新模型,枚举: 0 :否 1 :是 |
| 16 | frefdatacnt | 引用记录数 | int8 | 64 |  | √ | 0 | 引用记录数 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 19 | fenabledby | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 21 | ftemplateno | 单据模板 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fevtaction | fevtaction | varchar | 30 |  | √ | ' ' |  |
| 24 | fversionnum | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |
| 25 | fevtbill | fevtbill | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_eventclass |  | fid |
| 2 | idx_ai_eventclass |  | fnumber |
