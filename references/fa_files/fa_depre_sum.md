# 资产折旧单-fa_depre_sum

## 资产折旧单-主表 t_fa_depre

- **表名称：** 资产折旧单-主表
- **表名：** t_fa_depre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotaldepr | 本期总折旧额 | numeric | 19 | 6 | √ | 0 | 本期总折旧额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 折旧期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fhasvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 9 | fdepreadjustid | 折旧调整单内码 | int8 | 64 |  | √ | 0 | 折旧调整单内码 |
| 10 | ftotaldepreamount | 本期总折旧额 | numeric | 19 | 6 | √ | 0.000000 | 本期总折旧额 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 13 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fversion_tag | 分摊版本_详情 | text | 0 |  |  | ' ' | 分摊版本_详情 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | ftotalshouldamount | ftotalshouldamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fversion | 分摊版本 | text | 0 |  |  | '-17433742583' | 分摊版本 |
| 23 | fdeprestatus | 折旧状态 | bpchar | 1 |  | √ | ' ' | 折旧状态,枚举: 1 :折旧中 2 :已提折旧 3 :折旧失败 |
| 24 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depre_org_1 |  | forgid,fperiodid,fdepreuseid |
| 2 | t_fa_depre_pkey |  | fid |
| 3 | idx_fa_depre_fbillno |  | fbillno |

---

## 折旧明细-子表 t_fa_depredetailentry

- **表名称：** 折旧明细-子表
- **表名：** t_fa_depredetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fxkexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fsplitamount | 分摊金额 | numeric | 19 | 6 | √ | 0.000000 | 分摊金额 |
| 4 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 5 | fxkcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fassetcatid | fassetcatid | int8 | 64 |  | √ | 0 |  |
| 8 | fmanualadjustment | 手工调整折旧额影响后续期间 | bpchar | 1 |  | √ | '0' | 手工调整折旧额影响后续期间 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fxkprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 11 | forgdutyid | 部门属性 | int8 | 64 |  | √ | 0 | 部门属性 bos_org_duty |
| 12 | frealcardid | 资产卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 13 | freversesplitdetailid | 反冲销id | int8 | 64 |  | √ | 0 | 反冲销id |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fxksupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 16 | fisreversesd | fisreversesd | bpchar | 1 |  | √ | '0' |  |
| 17 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 18 | fxkadminorgid | 使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fassinfo | 横表组合信息 | varchar | 4000 |  |  | null | 横表组合信息 |
| 21 | fdetailsid | fdetailsid | int8 | 64 |  | √ | 0 |  |
| 22 | fpercent | 分摊比例 | numeric | 19 | 6 | √ | 0.000000 | 分摊比例 |
| 23 | fdepreuseid | fdepreuseid | int8 | 64 |  | √ | 0 |  |

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

## 折旧明细分摊维度-子表 t_fa_depredetailsubentry

- **表名称：** 折旧明细分摊维度-子表
- **表名：** t_fa_depredetailsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fasstype | 维度 | varchar | 100 |  | √ | ' ' | 维度 |
| 3 | fcalculateid | 核算维度ID | int8 | 64 |  | √ | 0 | 核算维度ID |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fassid | 维度值 | int8 | 64 |  | √ | 0 | 维度值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depredetailsubentry_pkey |  | fdetailid |
| 2 | idx_fa_depredetailsubentry_fid |  | fentryid |

---

## 折旧汇总分摊维度-子表 t_fa_depresumass

- **表名称：** 折旧汇总分摊维度-子表
- **表名：** t_fa_depresumass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fasstype | 维度 | varchar | 50 |  | √ | ' ' | 维度 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fassid | 维度值 | int8 | 64 |  | √ | 0 | 维度值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresumass_pkey |  | fdetailid |
| 2 | idx_fa_depresumass |  | fentryid |

---

## 单据体-子表 t_fa_depresum_assentry

- **表名称：** 单据体-子表
- **表名：** t_fa_depresum_assentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fasstype | 维度 | varchar | 50 |  | √ | ' ' | 维度 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_depresum_assentry |  | fentryid |
| 2 | idx_fa_depresum_assentry_id |  | fid |

---

## 折旧汇总-子表 t_fa_depreentry_d_sum

- **表名称：** 折旧汇总-子表
- **表名：** t_fa_depreentry_d_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalsplitamount | 本期分摊折旧额 | numeric | 19 | 6 | √ | 0.000000 | 本期分摊折旧额 |
| 3 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 4 | ftotalsplitdeptid | 使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | forgdutyid | 部门属性 | int8 | 64 |  | √ | 0 | 部门属性 bos_org_duty |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_dprent_d_sum_fbillno |  | fseq |
| 2 | t_fa_depreentry_d_sum_pkey |  | fentryid |
