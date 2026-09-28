# 采购付款匹配记录-pm_pomatch

## 采购付款匹配记录-主表 t_pm_pomatch

- **表名称：** 采购付款匹配记录-主表
- **表名：** t_pm_pomatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 匹配批号 | varchar | 80 |  | √ | ' ' | 匹配批号 |
| 3 | fcreatorid | 匹配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 匹配日期 | timestamp | 0 |  |  | null | 匹配日期 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fheadwfinfo | 匹配详情 | varchar | 512 |  |  | null | 匹配详情 |
| 8 | fwfnumber | 匹配编码 | varchar | 80 |  | √ | ' ' | 匹配编码 |
| 9 | fheadwfinfo_tag | 匹配详情_详情 | text | 0 |  |  | null | 匹配详情_详情 |
| 10 | fwriteofftypeid | 钩稽类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_pomatch_wfseq |  | fwfseq |
| 2 | pk_t_pm_pomatch |  | fid |

---

## 单据体-子表 t_pm_pomatchentry

- **表名称：** 单据体-子表
- **表名：** t_pm_pomatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fasssettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fassbillid | 付款单ID | int8 | 64 |  | √ | 0 | 付款单ID |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 订单应付金额 | numeric | 23 | 10 | √ | 0 | 订单应付金额 |
| 6 | fassbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fassamount | 付款单应付金额 | numeric | 23 | 10 | √ | 0 | 付款单应付金额 |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 10 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fassconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 12 | fassbillno | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单编号 |
| 13 | fasslicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 14 | fasscurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fassbilltype | 辅方单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fmainwfinfo_tag | 订单匹配详情_详情 | text | 0 |  |  | null | 订单匹配详情_详情 |
| 17 | fbillno | 采购订单编号 | varchar | 80 |  | √ | ' ' | 采购订单编号 |
| 18 | fqty | 订单本次匹配金额 | numeric | 23 | 10 | √ | 0 | 订单本次匹配金额 |
| 19 | fassbillentryid | 付款明细ID | int8 | 64 |  | √ | 0 | 付款明细ID |
| 20 | fmainwfinfo | 订单匹配详情 | varchar | 512 |  |  | null | 订单匹配详情 |
| 21 | fasswfinfo_tag | 付款单匹配详情_详情 | text | 0 |  |  | null | 付款单匹配详情_详情 |
| 22 | fassentryseq | fassentryseq | int8 | 64 |  | √ | 0 |  |
| 23 | fentryseq | 付款计划序号 | int8 | 64 |  | √ | 0 | 付款计划序号 |
| 24 | fassbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 25 | fbillentryid | 付款计划ID | int8 | 64 |  | √ | 0 | 付款计划ID |
| 26 | fbizdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 27 | fassqty | 付款单本次匹配金额 | numeric | 23 | 10 | √ | 0 | 付款单本次匹配金额 |
| 28 | fbillid | 采购订单ID | int8 | 64 |  | √ | 0 | 采购订单ID |
| 29 | fasswfinfo | 付款单匹配详情 | varchar | 512 |  |  | null | 付款单匹配详情 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fbilltype | 主方单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 33 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_pomatchentry |  | fentryid |
| 2 | idx_pm_pomatchentry_fbillno |  | fbillno |
| 3 | idx_pm_pomatchentry_fid |  | fid |
