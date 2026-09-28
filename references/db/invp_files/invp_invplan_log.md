# 库存计划运算结果-invp_invplan_log

## 单据体-子表 t_invp_planlogentry

- **表名称：** 单据体-子表
- **表名：** t_invp_planlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsteptimespan | 运行时间(分钟) | varchar | 50 |  | √ | ' ' | 运行时间(分钟) |
| 3 | fdetailmsg_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 4 | fprocessdata | 处理数据量 | varchar | 50 |  | √ | ' ' | 处理数据量 |
| 5 | fstepresult | 运行结果 | bpchar | 1 |  | √ | ' ' | 运行结果,枚举: A :已完成 B :异常终止 C :手工终止 D :运行中 E :部分异常 |
| 6 | fdetailmsg | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 7 | fcalstepid | 步骤 | int8 | 64 |  | √ | 0 | [算法注册配置 invp_algoregister](../invp_files/invp_algoregister.md) |
| 8 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 9 | fstepname | 步骤名称 | varchar | 255 |  | √ | ' ' | 步骤名称 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_planlogentry |  | fentryid |
| 2 | idx_planlog_entry_fid |  | fid |

---

## 单据体-子表 t_invp_planresultentry

- **表名称：** 单据体-子表
- **表名：** t_invp_planresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | favbqty | 可用量 | numeric | 23 | 10 | √ | 0 | 可用量 |
| 3 | fplanorderdate | 计划建议日期 | timestamp | 0 |  |  | null | 计划建议日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | freplenishmentpolicy | 补货策略 | varchar | 50 |  | √ | ' ' | 补货策略,枚举: PURCHASE :采购 TRANS :调拨 |
| 7 | fsafeinvqty | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 8 | fplanoutlookdate | fplanoutlookdate | timestamp | 0 |  |  | null |  |
| 9 | fleadtime | 累计提前期(天) | int4 | 32 |  | √ | 0 | 累计提前期(天) |
| 10 | fmatchdetailid | 操作 | int8 | 64 |  | √ | 0 | 操作 |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fdemandorgid | 需求组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fplanavbdate | 计划可用日期 | timestamp | 0 |  |  | null | 计划可用日期 |
| 14 | freorderqty | 再订货点 | numeric | 23 | 10 | √ | 0 | 再订货点 |
| 15 | fplanadviceqty | 计划建议数量 | numeric | 23 | 10 | √ | 0 | 计划建议数量 |
| 16 | finvqty | finvqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fsupplyqty | 供应量 | numeric | 23 | 10 | √ | 0 | 供应量 |
| 18 | fmatchdate | 供需匹配日期 | timestamp | 0 |  |  | null | 供需匹配日期 |
| 19 | fbatchpolicy | 批量政策 | varchar | 50 |  | √ | ' ' | 批量政策,枚举: DIRECT :直接批量 ECO :经济批量 FIX :固定批量 |
| 20 | fmaxqty | 最大库存 | numeric | 23 | 10 | √ | 0 | 最大库存 |
| 21 | fdemandwarehouseid | 需求仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fdemandqty | 需求量 | numeric | 23 | 10 | √ | 0 | 需求量 |
| 23 | fecobatchqty | 经济批量 | numeric | 23 | 10 | √ | 0 | 经济批量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fminqty | 最小库存 | numeric | 23 | 10 | √ | 0 | 最小库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_planresultentry |  | fentryid |
| 2 | idx_invp_planresultentry_fk |  | fid |

---

## 库存计划运算结果-主表 t_invp_planlog

- **表名称：** 库存计划运算结果-主表
- **表名：** t_invp_planlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fschemeid | 计划方案编码 | int8 | 64 |  | √ | 0 | [库存计划方案 invp_scheme](../invp_files/invp_scheme.md) |
| 4 | fexecuteip | 运算机器ip | varchar | 50 |  | √ | ' ' | 运算机器ip |
| 5 | fcalcnum | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |
| 6 | fstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 7 | fprocessrate | 计算进度 | int8 | 64 |  | √ | 0 | 计算进度 |
| 8 | fplanoutlookday | 展望期 | int4 | 32 |  | √ | 0 | 展望期 |
| 9 | fstatus | 计划运算状态 | bpchar | 1 |  | √ | ' ' | 计划运算状态,枚举: A :运行中 B :运算成功 C :运算失败 D :手工终止 |
| 10 | fcreatedate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 11 | fcreatorid | 计划运算执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fplantype | 计划类型 | varchar | 50 |  | √ | ' ' | 计划类型,枚举: A :再订货点 B :最大最小 E :安全库存 |
| 13 | fcalcsource | 计划运算方式 | bpchar | 1 |  | √ | ' ' | 计划运算方式,枚举: 1 :手工运算 2 :调度运算 |
| 14 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | ftimespan | 计算总时长(分钟) | varchar | 50 |  | √ | ' ' | 计算总时长(分钟) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_planlog |  | fid |
| 2 | idx_planlog_fcalcnum |  | fcalcnum |
