# 独立需求-psw_indepdemand

## 独立需求-主表 t_psw_indepdemand

- **表名称：** 独立需求-主表
- **表名：** t_psw_indepdemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fprodorg | 生产组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 8 | funitid | 基本单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 9 | freqbaseqty | 需求基本数量 | numeric | 23 | 10 |  | null | 需求基本数量 |
| 10 | fmastermaterielid | 主物料 | int8 | 64 |  |  | null | 物料 bd_material |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 13 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | 物料版本 bd_bomversion_new |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_indepdemand |  | fid |
| 2 | idx_t_psw_indepdemand |  | fbillno,fid |
