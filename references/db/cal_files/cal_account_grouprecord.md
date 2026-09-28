# 成本主体级成组关系记录-cal_account_grouprecord

## 单据体-子表 t_cal_atgrouprecord_entry

- **表名称：** 单据体-子表
- **表名：** t_cal_atgrouprecord_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostrecordentryid | 核算成本记录分录ID | int8 | 64 |  | √ | 0 | 核算成本记录分录ID |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fcalbillid | 核算单ID | int8 | 64 |  | √ | 0 | 核算单ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fislastentry | 是否调拨完成 | bpchar | 1 |  | √ | '0' | 是否调拨完成 |
| 8 | foccupiedqty | 占用数量 | numeric | 23 | 10 | √ | 0.0000000000 | 占用数量 |
| 9 | fgroupno | 分组号 | int8 | 64 |  | √ | 0 | 分组号 |
| 10 | fcalentryid | 核算单分录ID | int8 | 64 |  | √ | 0 | 核算单分录ID |
| 11 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 12 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fweight | 权重 | numeric | 23 | 10 | √ | 0.0000000000 | 权重 |
| 14 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :源单 1 :目标单 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fisbeforeperiod | 是否往期单据 | bpchar | 1 |  | √ | '0' | 是否往期单据 |
| 17 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fbaseqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_agrecordentry_mat |  | fmaterialid |
| 2 | idx_cal_agrecordentry_fid |  | fid |
| 3 | idx_cal_atgrouprecorde_billno |  | fbillno |
| 4 | idx_cal_agrecordentry_ca |  | fcostaccountid,fmaterialid,fperiodid |
| 5 | t_cal_atgrouprecord_entry_pkey |  | fentryid |
| 6 | idx_cal_atgrecordentry_calentryid |  | fcalentryid,fid |
| 7 | idx_atgrouprecord_entry_calbillid |  | fcalbillid,fid |

---

## 成本主体级成组关系记录-主表 t_cal_accountgrouprecord

- **表名称：** 成本主体级成组关系记录-主表
- **表名：** t_cal_accountgrouprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostaccounttypeid | 主体类别 | int8 | 64 |  | √ | 0 | 成本主体类别 cal_bd_costaccounttype |
| 3 | fcostcolumn | 成组成本字段 | varchar | 255 |  | √ | ' ' | 成组成本字段,枚举: materialcost :材料成本 processcost :委外费用 fee :采购成本 manufacturecost :制造费用 resource :人工费用 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fiscompleted | 是否结转完成 | bpchar | 1 |  | √ | '0' | 是否结转完成 |
| 6 | fdestbookdate | 目标单记账日期 | timestamp | 0 |  |  | null | 目标单记账日期 |
| 7 | fbizgrouprecordid | 业务成组关系记录id | int8 | 64 |  | √ | 0 | 业务成组关系记录id |
| 8 | fisresidualcaled | 是否有残值退料计算 | bpchar | 1 |  | √ | '0' | 是否有残值退料计算 |
| 9 | fgroupsettingtype | 来源成组配置类型 | varchar | 80 |  | √ | 'cal_billgroupsetting' | 来源成组配置类型,枚举: cal_billgroupsetting :关联关系 |
| 10 | fgroupvalue | 成组值 | varchar | 255 |  | √ | ' ' | 成组值 |
| 11 | fgroupsettingid | 来源成组定义 | int8 | 64 |  | √ | 0 | 成组关系配置 cal_billgroupsetting |
| 12 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 13 | fcostfields | 成组子要素ID集合 | varchar | 2000 |  | √ | ' ' | 成组子要素ID集合 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_accountgrouprecord_pkey |  | fid |
| 2 | idx_cal_agrecord_updatetime |  | fupdatetime |
| 3 | idx_cal_accountgrouprecord_groupvalue |  | fgroupvalue |
| 4 | idx_cal_agrecord_bizrecordid |  | fbizgrouprecordid |
