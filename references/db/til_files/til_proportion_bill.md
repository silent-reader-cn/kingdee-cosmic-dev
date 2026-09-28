# 进项转出比例分摊-til_proportion_bill

## 进项转出比例分摊-主表 t_til_proportion_bill

- **表名称：** 进项转出比例分摊-主表
- **表名：** t_til_proportion_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fratio | 分摊比例 | numeric | 23 | 10 | √ | 0 | 分摊比例 |
| 9 | fcallbackinfo | 反写信息 | text | 0 |  |  | null | 反写信息 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | ftotalsales | 全部销售额 | numeric | 23 | 10 | √ | 0 | 全部销售额 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | funablededucttax | 无法划分的全部进项税额 | numeric | 23 | 10 | √ | 0 | 无法划分的全部进项税额 |
| 14 | ftransferoutdate | 转出税期 | timestamp | 0 |  |  | null | 转出税期 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmanualregiste | 手工登记 | bpchar | 1 |  | √ | '0' | 手工登记 |
| 17 | fmark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 18 | ftransferouttype | 进项转出类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |
| 19 | factualtaxamount | 实际转出税额 | numeric | 23 | 10 | √ | 0 | 实际转出税额 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fprojectsales | 项目销售额 | numeric | 23 | 10 | √ | 0 | 项目销售额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_tpb_bn |  | fbillno |
| 2 | pk_til_proportion_bill |  | fid |
| 3 | idx_proportion_bill_forgid |  | forgid,ftransferouttype,ftransferoutdate |
