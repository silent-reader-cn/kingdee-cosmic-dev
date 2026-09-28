# 成本更新申请单-cal_costupdateapplybill

## 成本更新申请单-多语言表 t_cal_costupdateapplybill_l

- **表名称：** 成本更新申请单-多语言表
- **表名：** t_cal_costupdateapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costupdateapplybill_l_pkey |  | fpkid |
| 2 | idx_cal_costupdatebilll_local |  | fid,flocaleid |

---

## 成本更新申请单-主表 t_cal_costupdateapplybill

- **表名称：** 成本更新申请单-主表
- **表名：** t_cal_costupdateapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsrcsys | 来源系统 | bpchar | 1 |  | √ | 'A' | 来源系统,枚举: A :存货核算 B :成本系统 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fsrcbillentity | 来源单据对象 | varchar | 80 |  | √ | ' ' | 来源单据对象 |
| 18 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fsumtype | 汇总依据 | bpchar | 1 |  | √ | 'A' | 汇总依据,枚举: A :余额明细 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costupdateapplybill_pkey |  | fid |
| 2 | idx_cal_costupdatebill_billno |  | fbillno |

---

## 成本调整信息-子表 t_cal_costupdateentry

- **表名称：** 成本调整信息-子表
- **表名：** t_cal_costupdateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostdiff | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 11 | fwarehsouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 12 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fbaldetailid | 核算余额结转明细id | int8 | 64 |  | √ | 0 | 核算余额结转明细id |
| 15 | fnewunitcost | 更新后单价 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后单价 |
| 16 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 19 | funitcost | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 20 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 21 | fcostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 24 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 26 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fnewcost | 更新后金额 | numeric | 23 | 10 | √ | 0.0000000000 | 更新后金额 |
| 29 | fcost | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costupdateentry_pkey |  | fentryid |
| 2 | idx_cal_costupdateentry_id |  | fid |
