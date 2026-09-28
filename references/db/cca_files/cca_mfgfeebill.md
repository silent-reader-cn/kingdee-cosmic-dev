# 费用归集-cca_mfgfeebill

## 费用归集-主表 t_cca_mfgfeecollc

- **表名称：** 费用归集-主表
- **表名：** t_cca_mfgfeecollc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcsysid | 来源系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fimpschid | 导入方案id | varchar | 2000 |  | √ | ' ' | 导入方案id |
| 4 | ftotalamount | 费用金额 | numeric | 23 | 10 | √ | 0 | 费用金额 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fvoucherentryid | 凭证分录id | varchar | 2000 |  | √ | ' ' | 凭证分录id |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: SYS :内部导入 IMP :外部导入 NEW :手工录入 |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 11 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 12 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 13 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fsrcbillid | 来源单据id | varchar | 2000 |  | √ | ' ' | 来源单据id |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型,枚举: VOUCHER :凭证 AP_BUS :暂估应付单 AP_FI :财务应付单 er_dailyreimbursebill :费用报销单 ar_finarbill :财务应收单 cal_costrecord_subentity :核算成本记录 ap_busbill :暂估应付单 ap_finapbill :财务应付单 gl_voucher :凭证 im_materialreqoutbill :领料出库单 fa_depresplitdetail :折旧分配明细 |
| 22 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | faccountid | 来源科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 24 | fsrcbillnum | 来源单据号 | varchar | 2000 |  | √ | ' ' | 来源单据号 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cca_mfgfeecollc |  | fid |
| 2 | idx_cca_mfgfeecollc_m0 |  | fbillno |

---

## 费用归集-多语言表 t_cca_mfgfeecollc_l

- **表名称：** 费用归集-多语言表
- **表名：** t_cca_mfgfeecollc_l

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
| 1 | pk_cca_mfgfeecollc_l |  | fpkid |
| 2 | idx_cca_mfgfeecollc_l_0 |  | fid,flocaleid |
