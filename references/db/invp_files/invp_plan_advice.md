# 库存计划建议-invp_plan_advice

## 详细信息-子表 t_invp_plan_entry

- **表名称：** 详细信息-子表
- **表名：** t_invp_plan_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowbillstatus | 行关闭 | bpchar | 1 |  | √ | ' ' | 行关闭,枚举: A :正常 D :已关闭 |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconfirmqty | 确认基本数量 | numeric | 23 | 10 | √ | 0 | 确认基本数量 |
| 6 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | funpushqty | 未投放基本数量 | numeric | 23 | 10 | √ | 0 | 未投放基本数量 |
| 8 | fdemandbillentryid | 需求单据行id | int8 | 64 |  | √ | 0 | 需求单据行id |
| 9 | fdemandseq | 需求单据行号 | int4 | 32 |  | √ | 0 | 需求单据行号 |
| 10 | fdemandbillno | 需求单据编号 | varchar | 80 |  | √ | ' ' | 需求单据编号 |
| 11 | fplangroup | 计划组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 12 | fplandate | 计划建议日期 | timestamp | 0 |  |  | null | 计划建议日期 |
| 13 | fjoinqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 14 | fdate | 计划可用日期 | timestamp | 0 |  |  | null | 计划可用日期 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fdemandorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fqty | 建议基本数量 | numeric | 23 | 10 | √ | 0 | 建议基本数量 |
| 18 | fpushqty | 已投放基本数量 | numeric | 23 | 10 | √ | 0 | 已投放基本数量 |
| 19 | fplanuser | 计划员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 20 | fwarehouseid | 需求仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 21 | fentryremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | ffinishdate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 23 | frowterminatestatus | 行终止 | bpchar | 1 |  | √ | ' ' | 行终止,枚举: A :正常 B :已终止 |
| 24 | fstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 25 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fdemandbillid | 需求单据id | int8 | 64 |  | √ | 0 | 需求单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_pa_entry_fid |  | fid |
| 2 | pk_t_invp_plan_entry |  | fentryid |

---

## 详细信息-多语言表 t_invp_plan_entry_l

- **表名称：** 详细信息-多语言表
- **表名：** t_invp_plan_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fentryremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_plan_entry_l |  | fpkid |
| 2 | idx_pe_l_id_localeid |  | fentryid,flocaleid |

---

## 库存计划建议-多语言表 t_invp_planadvice_l

- **表名称：** 库存计划建议-多语言表
- **表名：** t_invp_planadvice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_l_fid_flocalid |  | fid,flocaleid |
| 2 | pk_t_invp_planadvice_l |  | fpkid |

---

## 库存计划建议-主表 t_invp_planadvice

- **表名称：** 库存计划建议-主表
- **表名：** t_invp_planadvice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fplanschemeid | 计划方案 | int8 | 64 |  | √ | 0 | 库存计划方案 invp_scheme |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fadvicetype | 建议类型 | varchar | 50 |  | √ | ' ' | 建议类型,枚举: A :采购 E :调拨 |
| 7 | forgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fhandcloseflag | 手工关闭 | bpchar | 1 |  | √ | ' ' | 手工关闭 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmainplantype | 计划类型 | bpchar | 1 |  | √ | ' ' | 计划类型,枚举: A :再订货点 B :最大最小 D :固定期间 E :安全库存 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 17 | fcalcsource | 计算来源 | bpchar | 1 |  | √ | ' ' | 计算来源,枚举: 1 :手工运算 2 :调度运算 |
| 18 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fplancalnum | 计划运算号 | varchar | 80 |  | √ | ' ' | 计划运算号 |
| 22 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_pa_fbillno |  | fbillno |
| 2 | pk_t_invp_planadvice |  | fid |
