# 自动抵扣勾选配置-rim_auto_deduction_task

## 适用组织-子表 t_rim_auto_deduct_userorg

- **表名称：** 适用组织-子表
- **表名：** t_rim_auto_deduct_userorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxpayer_name | 纳税人名称 | varchar | 120 |  | √ | ' ' | 纳税人名称 |
| 3 | ftaxpayer_tax_no | 纳税人税号 | varchar | 32 |  | √ | ' ' | 纳税人税号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftaxpayer_org | 核算组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_adeduct_org_taxno |  | ftaxpayer_tax_no |
| 2 | idx_rim_auto_deduct_userorg_fk |  | fid |
| 3 | pk_t_rim_auto_deduct_userorg |  | fentryid |

---

## 自动抵扣勾选配置-主表 t_rim_auto_deduction_task

- **表名称：** 自动抵扣勾选配置-主表
- **表名：** t_rim_auto_deduction_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceipttype | 按签收状态 | varchar | 50 |  | √ | ' ' | 按签收状态,枚举: -1 :不限 0 :未签收 1 :已签收 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | finput_out_amount | 进项转出 | numeric | 23 | 10 | √ | 0 | 进项转出 |
| 5 | faccountingorgid | 核算组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 6 | fexit_return_taxamount | 出口退税 | numeric | 23 | 10 | √ | 0 | 出口退税 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftaxname | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 10 | ftick | 按是否勾选 | varchar | 50 |  | √ | ' ' | 按是否勾选,枚举: -1 :不限 1 :是 0 :否 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | finvoiceresouce | 按来源方式 | varchar | 50 |  | √ | ' ' | 按来源方式,枚举: -1 :不限 12 :扫描仪采集 21 :拍照采集 22 :扫码采集 23 :邮箱收票 29 :短信收票 15 :税局同步 27 :微信卡包 25 :云票儿 24 :滴滴发票 |
| 15 | finvovicestatus | 按使用状态 | varchar | 50 |  | √ | ' ' | 按使用状态,枚举: -1 :不限 1 :未用 30 :在用 60 :已用 65 :已入账 |
| 16 | fdeductconfigtype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: 1 :按采集时间先进先抵 2 :按开票时间先进先抵 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | ftaxno | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 20 | fdeductconfig | 抵扣规则 | varchar | 50 |  | √ | ' ' | 抵扣规则,枚举: 1 :按固定税负率倒算进项税，进行抵扣 2 :按可抵扣票据全自动抵扣 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | finput_taxamount | 进项税额 | numeric | 23 | 10 | √ | 0 | 进项税额 |
| 24 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 25 | fdeduction_purpose | 抵扣用途按钮组 | varchar | 50 |  | √ | ' ' | 抵扣用途按钮组,枚举: 3 :退税勾选 1 :抵扣勾选 2 :不抵扣勾选 -1 :不限 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fpretick | 按预勾选 | varchar | 50 |  | √ | ' ' | 按预勾选,枚举: -1 :不限 0 :未勾选 4 :预勾选 |
| 28 | ftax_burden_rate | 税负率(%) | numeric | 23 | 2 | √ | 0 | 税负率(%) |
| 29 | fbegin_period_amount | 期初留抵进项税 | numeric | 23 | 10 | √ | 0 | 期初留抵进项税 |
| 30 | fcurrent_period_taxamount | 当期销项税额 | numeric | 23 | 10 | √ | 0 | 当期销项税额 |
| 31 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fcheck_status | 按查验状态 | varchar | 20 |  | √ | ' ' | 按查验状态,枚举: -1 :不限 1 :已验 4 :不查验 |
| 33 | finvoicetype | 按发票种类 | varchar | 50 |  | √ | ' ' | 按发票种类,枚举: -1 :不限 2 :电子专票 27 :全电专票 4 :纸质专票 12 :机动车 15 :通行费 21 :海关缴款书 00 :旅客运输 |
| 34 | faudit_result | 按预警结果 | varchar | 20 |  | √ | ' ' | 按预警结果,枚举: -1 :不限 0 :正常 2 :已处理 |
| 35 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 37 | fexcutetime | fexcutetime | varchar | 50 |  | √ | ' ' |  |
| 38 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 39 | fcurrent_period_amount | 当期应税销售收入 | numeric | 23 | 10 | √ | 0 | 当期应税销售收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rim_auto_deduction_task_createorg |  | fcreateorgid |
| 2 | idx_t_rim_auto_deduction_task_master |  | fmasterid |
| 3 | pk_t_rim_auto_deduction_task |  | fid |
| 4 | idx_rim_auto_de_task_masterid |  | fmasterid |
| 5 | idx_rim_auto_de_task_number |  | fnumber |

---

## 按业务单据-多选基础资料表 t_rim_auto_deduct_bills

- **表名称：** 按业务单据-多选基础资料表
- **表名：** t_rim_auto_deduct_bills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [手动添加单据类型 rim_expense_type](../rim_files/rim_expense_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_auto_deduct_bills |  | fpkid |
| 2 | idx_rim_auto_de_task_fid |  | fid |

---

## 自动抵扣勾选配置-使用范围表 t_rim_auto_deduction_task_u

- **表名称：** 自动抵扣勾选配置-使用范围表
- **表名：** t_rim_auto_deduction_task_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_auto_deduction_task_u |  | fdataid,fuseorgid |
| 2 | idx_t_rim_auto_deduction_task_u_uo |  | fuseorgid |

---

## 自动抵扣勾选配置-多语言表 t_rim_auto_deduction_task_l

- **表名称：** 自动抵扣勾选配置-多语言表
- **表名：** t_rim_auto_deduction_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_auto_deduction_task_l |  | fpkid |
| 2 | idx_auto_dedu_l_fid_flocal |  | flocaleid,fid |

---

## 自动抵扣勾选配置-使用范围位图表 t_rim_auto_deduction_task_m

- **表名称：** 自动抵扣勾选配置-使用范围位图表
- **表名：** t_rim_auto_deduction_task_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_auto_deduction_task_m |  | forgid |
