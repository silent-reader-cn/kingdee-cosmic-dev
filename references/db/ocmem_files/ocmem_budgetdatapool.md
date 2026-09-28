# 预算数据源-ocmem_budgetdatapool

## 预算数据源-主表 t_ocmem_budgetdatapool

- **表名称：** 预算数据源-主表
- **表名：** t_ocmem_budgetdatapool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcomfirmuserid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未确认 B :已确认 C :数据异常 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 7 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ftotalbudgetamount | 参与预算金额合计 | numeric | 23 | 10 | √ | 0 | 参与预算金额合计 |
| 11 | fsourcebilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | frollbudgettime | 滚动预算时间 | timestamp | 0 |  |  | null | 滚动预算时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fisrolledbudget | 预算状态 | bpchar | 1 |  | √ | '0' | 预算状态,枚举: 0 :未计算 1 :已滚动计算 2 :已完成滚动预算 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | forderchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 18 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_budgetpool_billno |  | fbillno |
| 2 | pk_ocmem_budgetdatapool |  | fid |

---

## 预算数据源-关联追踪表 t_ocmem_budgetdatapool_tc

- **表名称：** 预算数据源-关联追踪表
- **表名：** t_ocmem_budgetdatapool_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_budgetdatapool_tc_tid |  | ftid |
| 2 | pk_ocmem_budgetdatapool_tc |  | fid |
| 3 | idx_ocmem_budgetdatapool_tc_tbill |  | ftbillid |

---

## 单据体-子表 t_ocmem_budgetpool_e

- **表名称：** 单据体-子表
- **表名：** t_ocmem_budgetpool_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 3 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | fapprovebaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fapproveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 13 | fsrcbillentryid | 来源单据分录id | int8 | 64 |  | √ | 0 | 来源单据分录id |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 15 | fisbudget | 计预算 | bpchar | 1 |  | √ | '0' | 计预算 |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 17 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_budgetpool_e |  | fentryid |
| 2 | idx_ocmem_budgetpool_e_fid |  | fid |

---

## 关联子实体-子表 t_ocmem_budgetpool_e_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocmem_budgetpool_e_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_budgetpool_e_lk_fk |  | fentryid |
| 2 | pk_ocmem_budgetpool_e_lk |  | fpkid |

---

## 预算数据源-反写记录表 t_ocmem_budgetdatapool_wb

- **表名称：** 预算数据源-反写记录表
- **表名：** t_ocmem_budgetdatapool_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_budgetdatapool_wb |  | fentryid |
| 2 | idx_ocmem_budgetdatapool_wb_fk |  | fid |
