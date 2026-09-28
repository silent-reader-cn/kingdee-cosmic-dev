# 资产减值单-fa_asset_devalue

## 资产减值单-主表 t_fa_asset_devalue

- **表名称：** 资产减值单-主表
- **表名：** t_fa_asset_devalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fhasvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 7 | fdevalueperiod | 减值期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsumdecval | 本期减值总额 | numeric | 19 | 6 | √ | 0.000000 | 本期减值总额 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbusinessdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_adv_fbillno |  | fbillno |
| 2 | t_fa_asset_devalue_pkey |  | fid |
| 3 | idx_fa_devalue_org |  | forgid,fdepreuseid,fdevalueperiod |

---

## 减值明细分录-子表 t_fa_asset_devalue_info

- **表名称：** 减值明细分录-子表
- **表名：** t_fa_asset_devalue_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizdate | 折旧影响日期 | timestamp | 0 |  |  | null | 折旧影响日期 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcompfieldsv | 比较字段值 | varchar | 200 |  | √ | ' ' | 比较字段值 |
| 5 | fdecval | 本期减值 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减值 |
| 6 | frealcardmasterid | 卡片主数据ID | int8 | 64 |  | √ | 0 | 卡片主数据ID |
| 7 | ffincardid | 资产卡片财务信息 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dvl_info_fid |  | fid |
| 2 | t_fa_asset_devalue_info_pkey |  | fentryid |
