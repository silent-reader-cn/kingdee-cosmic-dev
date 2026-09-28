# 毛需求来源_数据-mrp_gdd_source_base

## 毛需求来源_数据-多语言表 t_mrp_grossdemand_source_l

- **表名称：** 毛需求来源_数据-多语言表
- **表名：** t_mrp_grossdemand_source_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_grossdemand_source_l |  | fid,flocaleid |
| 2 | pk_t_mrp_grossdemand_source_l |  | fpkid |

---

## 毛需求来源_数据-主表 t_mrp_grossdemand_source

- **表名称：** 毛需求来源_数据-主表
- **表名：** t_mrp_grossdemand_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialparentcode | 父项编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmaterialgroup | 编码分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpbom | PBOM | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | frequirementtype | 需求类型 | varchar | 50 |  | √ | ' ' | 需求类型 |
| 10 | fpauxproperty | 父项辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fcaculatelog | 计划运算号 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fproductmodel | 产品型号 | int8 | 64 |  | √ | 0 | [产品目录 bd_productsummary](../basedata_files/bd_productsummary.md) |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fqtys | 数量 | varchar | 50 |  | √ | ' ' | 数量 |
| 16 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fpconfiguredcode | 父项配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fmaterialcode | 编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_grossdemand_source |  | fnumber |
| 2 | pk_t_mrp_grossdemand_source |  | fid |
