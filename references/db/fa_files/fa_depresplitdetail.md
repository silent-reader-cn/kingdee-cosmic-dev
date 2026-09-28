# 折旧分摊明细-fa_depresplitdetail

## 折旧分摊详情-子表 t_fa_depredetailentry

- **表名称：** 折旧分摊详情-子表
- **表名：** t_fa_depredetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 折旧汇总ID | int8 | 64 |  | √ | 0 | 折旧汇总ID |
| 2 | fxkexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fsplitamount | 分摊金额 | numeric | 19 | 6 | √ | 0.000000 | 分摊金额 |
| 4 | fperiodid | 期间（冗余） | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fxkcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 6 | forgid | 组织（冗余） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fassetcatid | 资产类别（冗余） | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 8 | fmanualadjustment | 手工调整折旧额影响后续期间 | bpchar | 1 |  | √ | '0' | 手工调整折旧额影响后续期间 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fxkprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 11 | forgdutyid | 部门属性 | int8 | 64 |  | √ | 0 | [部门属性 bos_org_duty](../base_files/bos_org_duty.md) |
| 12 | frealcardid | 卡片编号 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 13 | freversesplitdetailid | 反冲分摊明细ID | int8 | 64 |  | √ | 0 | 反冲分摊明细ID |
| 14 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fxksupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 16 | fisreversesd | 是反冲相关 | bpchar | 1 |  | √ | '0' | 是反冲相关 |
| 17 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 18 | fxkadminorgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fassinfo | 横表组合信息 | varchar | 4000 |  |  | null | 横表组合信息 |
| 21 | fdetailsid | fdetailsid | int8 | 64 |  | √ | 0 |  |
| 22 | fpercent | 分摊比例 | numeric | 19 | 6 | √ | 0.000000 | 分摊比例 |
| 23 | fdepreuseid | 折旧用途（冗余） | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depredetailentry_fid |  | fid |
| 2 | idx_fa_depredetailentryrcard |  | frealcardid |
| 3 | idx_fa_depreentry_details_ffid |  | fdetailsid,ffincardid |
| 4 | t_fa_depredetailentry_pkey |  | fentryid |
| 5 | idx_fa_depreentry_cardfin |  | ffincardid |
| 6 | idx_fa_detailentry_org_dpc |  | forgid,fdepreuseid,fperiodid,fassetcatid |

---

## 折旧分摊维度-子表 t_fa_depredetailsubentry

- **表名称：** 折旧分摊维度-子表
- **表名：** t_fa_depredetailsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fasstype | 基础资料类型 | varchar | 100 |  | √ | ' ' | 基础资料类型 |
| 3 | fcalculateid | 核算维度ID | int8 | 64 |  | √ | 0 | 核算维度ID |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fassid | 基础资料id | int8 | 64 |  | √ | 0 | 基础资料id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depredetailsubentry_fid |  | fentryid |
| 2 | t_fa_depredetailsubentry_pkey |  | fdetailid |

---

## 折旧分摊明细-主表 t_fa_depresplitdetail

- **表名称：** 折旧分摊明细-主表
- **表名：** t_fa_depresplitdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 折旧期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | frealcardid | 卡片编号 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 13 | fsplitdeptid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 15 | freversesplitdetailid | 反冲分摊明细ID | int8 | 64 |  | √ | 0 | 反冲分摊明细ID |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 18 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 19 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 20 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 24 | fdetailsid | fdetailsid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailsid | fdetailsid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depresplitdetail |  | forgid,fdepreuseid,fperiodid |
| 2 | pk_t_fa_depresplitdetail |  | fdetailsid |
| 3 | idx_fa_depresplitdetailfcard |  | ffincardid |
| 4 | idx_fa_depresplitdetailrcard |  | frealcardid |
