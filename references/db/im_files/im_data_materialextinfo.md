# 指标数据_物料业务信息和单位转换-im_data_materialextinfo

## 指标数据_物料业务信息和单位转换-主表 t_im_data_materialextinfo

- **表名称：** 指标数据_物料业务信息和单位转换-主表
- **表名：** t_im_data_materialextinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftpl_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 2 | ftpl_pkid | ftpl_pkid | int8 | 64 |  | √ | 0 | id |
| 3 | fnumerator | 基本单位换算系数 | int4 | 32 |  | √ | 1 | 基本单位换算系数 |
| 4 | ftpl_type | 固化数据类型 | varchar | 50 |  | √ | ' ' | 固化数据类型,枚举: temp :临时数据 fix :固化数据 |
| 5 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | forg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftpl_sessionid | 物化标识ID | varchar | 100 |  | √ | ' ' | 物化标识ID |
| 8 | finvmaterial | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 9 | fdenominator | 源单位换算系数 | int4 | 32 |  | √ | 1 | 源单位换算系数 |
| 10 | ftpl_keycol | 维度唯一标识 | varchar | 510 |  | √ | ' ' | 维度唯一标识 |
| 11 | ftpl_datasourcetype | 自定义数据源类型 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 12 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | finvunit | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftpl_pkid | ftpl_pkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_data_matext_orgmat |  | forg,fmaterial |
| 2 | pk_im_data_materialextinfo |  | ftpl_pkid |
