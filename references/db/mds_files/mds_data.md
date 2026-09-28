# 计划处理(后台)-mds_data

## 录入单据体-子表 t_mds_fcdataentry

- **表名称：** 录入单据体-子表
- **表名：** t_mds_fcdataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fcycletypee | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 0 :日 1 :周 2 :自定义周期 |
| 5 | frepeat | 是否重复 | bpchar | 1 |  | √ | '0' | 是否重复 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fprodorgg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | ffinishdate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fcycles | 期数 | int8 | 64 |  | √ | 0 | 期数 |
| 10 | fupdowndct | 上下级编码冲减控制 | bpchar | 1 |  | √ | '0' | 上下级编码冲减控制 |
| 11 | fplandate | 计划时间 | timestamp | 0 |  |  | null | 计划时间 |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fplangpp | fplangpp | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fcdataentry |  | fid,fseq |
| 2 | t_mds_fcdataentry_pkey |  | fentryid |

---

## 计划处理(后台)-主表 t_mds_fcdata

- **表名称：** 计划处理(后台)-主表
- **表名：** t_mds_fcdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprededucts | 向前冲减天数 | int8 | 64 |  | √ | 0 | 向前冲减天数 |
| 4 | fsuporg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fenablestatus | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: A :可用 B :禁用 |
| 6 | fbillstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: A :待确认 C :已确认 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | ffcvrnnum | 版本编码 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbkdeducts | 向后冲减天数 | int8 | 64 |  | √ | 0 | 向后冲减天数 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdeduct | 冲减 | bpchar | 1 |  | √ | '0' | 冲减 |
| 15 | finvaldate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mds_fcdata_pkey |  | fid |
| 2 | idx_mds_fcdata |  | fbillno,forgid |

---

## 明细单据体-子表 t_mds_fcdatadtlent

- **表名称：** 明细单据体-子表
- **表名：** t_mds_fcdatadtlent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fwriteoffnum | 冲减数量 | numeric | 23 | 10 | √ | 0.0000000000 | 冲减数量 |
| 4 | fcycletyped | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 0 :日 1 :周 2 :自定义 |
| 5 | fnowqty | 现有数量 | numeric | 23 | 10 | √ | 0.0000000000 | 现有数量 |
| 6 | fprodorg | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fplangp | 计划组 | int8 | 64 |  | √ | 0 | 计划业务组 mpdm_demandgroup |
| 8 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | ffcqty | 原始数量 | numeric | 23 | 10 | √ | 0.0000000000 | 原始数量 |
| 11 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdatenode | 时间点 | timestamp | 0 |  |  | null | 时间点 |
| 14 | fqtysrc | 来源 | varchar | 50 |  | √ | ' ' | 来源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fcdaent_material |  | fmaterialid |
| 2 | idx_mds_fcdatadtlent |  | fid,fseq |
| 3 | idx_mds_fcdatadtlent_fidmid |  | fid,fmaterialid |
| 4 | t_mds_fcdatadtlent_pkey |  | fentryid |
