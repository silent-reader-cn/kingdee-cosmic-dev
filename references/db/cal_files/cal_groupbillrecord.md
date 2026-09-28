# 成组关系记录-cal_groupbillrecord

## 单据体-子表 t_cal_grouprecordentry

- **表名称：** 单据体-子表
- **表名：** t_cal_grouprecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fislastentry | 是否结转完成 | bpchar | 1 |  | √ | '0' | 是否结转完成 |
| 5 | foccupiedqty | 占用数量 | numeric | 23 | 10 | √ | 0.0000000000 | 占用数量 |
| 6 | fgroupno | 分组号 | int8 | 64 |  | √ | 0 | 分组号 |
| 7 | fownerid | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 9 | fweight | 权重 | numeric | 23 | 10 | √ | 0.0000000000 | 权重 |
| 10 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 0 :源单 1 :目标单 |
| 11 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 12 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 14 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fbaseqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_groupbillrecordentry |  | fid |
| 2 | idx_cal_grecord_entryid_id |  | fbillentryid,fid |
| 3 | t_cal_grouprecordentry_pkey |  | fentryid |
| 4 | idx_cal_grecordentry_bizbillid |  | fbizbillid |
| 5 | idx_cal_grecordentry_billid |  | fbillid |
| 6 | idx_cal_grouprecordentry_mat |  | fmaterialid |

---

## 成组关系记录-主表 t_cal_groupbillrecord

- **表名称：** 成组关系记录-主表
- **表名：** t_cal_groupbillrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostcolumn | 成组成本字段 | varchar | 255 |  | √ | ' ' | 成组成本字段,枚举: materialcost :材料成本 processcost :委外费用 fee :采购成本 manufacturecost :制造费用 resource :人工费用 |
| 3 | fgroupvalue | 成组值 | varchar | 255 |  | √ | ' ' | 成组值 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fgroupsettingid | 来源成组定义 | int8 | 64 |  | √ | 0 | 成组关系配置 cal_billgroupsetting |
| 6 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 7 | fiscompleted | 是否结转完成 | bpchar | 1 |  | √ | '0' | 是否结转完成 |
| 8 | fcostfields | 成组子要素ID集合 | varchar | 2000 |  | √ | ' ' | 成组子要素ID集合 |
| 9 | fgroupsettingtype | 来源成组配置类型 | varchar | 80 |  | √ | 'cal_billgroupsetting' | 来源成组配置类型,枚举: cal_billgroupsetting :关联关系 cal_writeoffgroupsetting :勾稽关系 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_groupre_setting |  | fgroupsettingid |
| 2 | idx_cal_groupre_updatetime |  | fupdatetime |
| 3 | idx_cal_groupre_gvalue |  | fgroupvalue |
| 4 | t_cal_groupbillrecord_pkey |  | fid |
