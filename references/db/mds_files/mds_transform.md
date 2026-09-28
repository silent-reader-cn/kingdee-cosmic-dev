# 物料编码转换-mds_transform

## 物料编码转换-主表 t_mds_transform

- **表名称：** 物料编码转换-主表
- **表名：** t_mds_transform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funitafter | 转换后计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbeforenum | 转换前数量比 | numeric | 23 | 10 | √ | 0 | 转换前数量比 |
| 7 | funitbefore | 转换前计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fnumerator | fnumerator | int8 | 64 |  | √ | 0 |  |
| 9 | feffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fdenominator | fdenominator | int8 | 64 |  | √ | 0 |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fafternum | 转换后数量比 | numeric | 23 | 10 | √ | 0 | 转换后数量比 |
| 16 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fmaterielbefore | 转换前物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fmaterielafter | 转换后物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_transform |  | fid |
| 2 | idx_mds_transform_no |  | fnumber |

---

## 物料编码转换-多语言表 t_mds_transform_l

- **表名称：** 物料编码转换-多语言表
- **表名：** t_mds_transform_l

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
| 1 | pk_mds_transform_l |  | fpkid |
| 2 | idx_mds_transform_l_id |  | fid,flocaleid |
