# 销售收款匹配记录-sm_somatch

## 单据体-子表 t_sm_somatchentry

- **表名称：** 单据体-子表
- **表名：** t_sm_somatchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fasssettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fassbillid | 收款单ID | int8 | 64 |  | √ | 0 | 收款单ID |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 订单应收金额 | numeric | 23 | 10 | √ | 0 | 订单应收金额 |
| 6 | fassbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fassamount | 收款单应收金额 | numeric | 23 | 10 | √ | 0 | 收款单应收金额 |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 10 | fassconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 11 | fassbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 12 | fasslicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 13 | fasscurrencyid | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fassbilltype | 辅方单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fmainwfinfo_tag | 订单匹配详情_详情 | text | 0 |  |  | null | 订单匹配详情_详情 |
| 16 | fbillno | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 17 | fqty | 订单本次匹配金额 | numeric | 23 | 10 | √ | 0 | 订单本次匹配金额 |
| 18 | fassbillentryid | 收款明细ID | int8 | 64 |  | √ | 0 | 收款明细ID |
| 19 | fmainwfinfo | 订单匹配详情 | varchar | 512 |  |  | null | 订单匹配详情 |
| 20 | fasswfinfo_tag | 收款单匹配详情_详情 | text | 0 |  |  | null | 收款单匹配详情_详情 |
| 21 | fassentryseq | fassentryseq | int8 | 64 |  | √ | 0 |  |
| 22 | fentryseq | 收款计划序号 | int8 | 64 |  | √ | 0 | 收款计划序号 |
| 23 | fassbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 24 | fbillentryid | 收款计划ID | int8 | 64 |  | √ | 0 | 收款计划ID |
| 25 | fbizdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 26 | fassqty | 收款单本次匹配金额 | numeric | 23 | 10 | √ | 0 | 收款单本次匹配金额 |
| 27 | fbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 28 | fasswfinfo | 收款单匹配详情 | varchar | 512 |  |  | null | 收款单匹配详情 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fbilltype | 主方单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 32 | fcustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 33 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_somatchentry |  | fentryid |
| 2 | idx_sm_somatchentry_fid |  | fid |
| 3 | idx_sm_somatchentry_fbillno |  | fbillno |

---

## 销售收款匹配记录-主表 t_sm_somatch

- **表名称：** 销售收款匹配记录-主表
- **表名：** t_sm_somatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 匹配批号 | varchar | 80 |  | √ | ' ' | 匹配批号 |
| 3 | fcreatorid | 匹配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 匹配日期 | timestamp | 0 |  |  | null | 匹配日期 |
| 6 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 1 | pk_t_sm_somatch |  | fid |
| 2 | idx_sm_somatch_wfseq |  | fwfseq |
