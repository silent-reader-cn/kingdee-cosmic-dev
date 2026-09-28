# 折旧明细-fa_depre_entity

## 折旧明细-主表 t_fa_depre

- **表名称：** 折旧明细-主表
- **表名：** t_fa_depre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotaldepr | ftotaldepr | numeric | 19 | 6 | √ | 0 |  |
| 3 | forgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fversion_tag | fversion_tag | text | 0 |  |  | ' ' |  |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 9 | fversion | fversion | text | 0 |  |  | '-17433742583' |  |
| 10 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fperiodid | 折旧期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fdepreadjustid | fdepreadjustid | int8 | 64 |  | √ | 0 |  |
| 16 | ftotaldepreamount | 本期总折旧额 | numeric | 19 | 6 | √ | 0.000000 | 本期总折旧额 |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fmigsrc | fmigsrc | int4 | 32 |  | √ | 0 |  |
| 19 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |
| 20 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 21 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 22 | ftotalshouldamount | ftotalshouldamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fdeprestatus | 折旧状态 | bpchar | 1 |  | √ | ' ' | 折旧状态,枚举: 1 :折旧中 2 :已提折旧 3 :折旧失败 |

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

## 折旧分摊汇总-子表 t_fa_depreentry_d_sum

- **表名称：** 折旧分摊汇总-子表
- **表名：** t_fa_depreentry_d_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalsplitamount | 本期分摊折旧额 | numeric | 19 | 6 | √ | 0.000000 | 本期分摊折旧额 |
| 3 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 4 | ftotalsplitdeptid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | forgdutyid | forgdutyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_dprent_d_sum_fbillno |  | fseq |
| 2 | t_fa_depreentry_d_sum_pkey |  | fentryid |
