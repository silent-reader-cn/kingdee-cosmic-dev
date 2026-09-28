# 制造费用归集-cad_mfgfeebill

## 制造费用归集-多语言表 t_cad_mfgfeecollc_l

- **表名称：** 制造费用归集-多语言表
- **表名：** t_cad_mfgfeecollc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_mfgfeecollc_l |  | fpkid |
| 2 | idx_t_cad_mfgfeecollc_l |  | fid,flocaleid |

---

## 来源系统-多选基础资料表 t_cad_mfgfeecollc_srcsys

- **表名称：** 来源系统-多选基础资料表
- **表名：** t_cad_mfgfeecollc_srcsys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_mfgfeecollc_srcsys |  | fid |
| 2 | pk_t_cad_mfgfeecollc_srcsys |  | fpkid |

---

## 制造费用归集-主表 t_cad_mfgfeecollc

- **表名称：** 制造费用归集-主表
- **表名：** t_cad_mfgfeecollc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrcsysid | 来源系统 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 4 | fimpschid | 引入方案id | varchar | 2000 |  | √ | ' ' | 引入方案id |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 费用金额 | numeric | 23 | 10 | √ | 0 | 费用金额 |
| 7 | fallocmold | 分配类型 | varchar | 50 |  | √ | ' ' | 分配类型,枚举: A :非生产分配 B :辅助生产分配 C :基本生产分配 E :委外生产分配 |
| 8 | fproductgroup | 产品组 | int8 | 64 |  | √ | 0 | [产品组 cad_productintogroup](../aca_files/cad_productintogroup.md) |
| 9 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 10 | fsource | 来源(根据需求暂不显示) | varchar | 50 |  | √ | ' ' | 来源(根据需求暂不显示),枚举: MANUAL :手工新增 SYS :从业务系统引入 API :API引入 EXCEL :模板引入 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | freferidentity | 引用标识（成本计算-合法性检查使用） | bpchar | 1 |  | √ | '0' | 引用标识（成本计算-合法性检查使用） |
| 13 | fvoucherentryid | 凭证分录id | varchar | 2000 |  | √ | ' ' | 凭证分录id |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: SYS :内部引入 IMP :外部导入 NEW :手工录入 |
| 16 | fprocesscode | 工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 18 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 19 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 23 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fsrcbillid | 来源单据id | varchar | 2000 |  | √ | ' ' | 来源单据id |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | foutsourcetype | 委外成本类型 | varchar | 50 |  | √ | ' ' | 委外成本类型,枚举: A :委外加工费 B :委外费用 C :制造费用 |
| 30 | ffcostobjectid | ffcostobjectid | int8 | 64 |  | √ | 0 |  |
| 31 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 32 | fcostobjectid | 成本核算对象编码 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 33 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型,枚举: VOUCHER :凭证 AP_BUS :暂估应付单 AP_FI :财务应付单 er_dailyreimbursebill :费用报销单 ar_finarbill :财务应收单 cal_costrecord_subentity :核算成本记录 ap_busbill :暂估应付单 ap_finapbill :财务应付单 gl_voucher :凭证 im_materialreqoutbill :领料出库单 fa_depresplitdetail :折旧分摊明细 |
| 34 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fsrcbillnum | 来源单据号 | varchar | 2000 |  | √ | ' ' | 来源单据号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_mfgfeecollc |  | forgid,fcostcenterid,fcostaccountid,fmanuorgid |
| 2 | pk_t_cad_mfgfeecollc |  | fid |
