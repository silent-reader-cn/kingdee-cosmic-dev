# 理财详情主表-aqap_financ_detail

## 理财详情主表-主表 t_aqap_financ_detail

- **表名称：** 理财详情主表-主表
- **表名：** t_aqap_financ_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fredeem_max | 赎回上限 | varchar | 50 |  | √ | ' ' | 赎回上限 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbank_version_id | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 7 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 8 | fbuy_price | 购买单价 | varchar | 50 |  | √ | ' ' | 购买单价 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fproduct_name | 理财名称 | varchar | 50 |  | √ | ' ' | 理财名称 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpublish_start_date | 发行开始日期 | timestamp | 0 |  |  | null | 发行开始日期 |
| 13 | freserved4 | 备用字段4 | varchar | 50 |  | √ | ' ' | 备用字段4 |
| 14 | fredeem_min | 赎回下限 | varchar | 50 |  | √ | ' ' | 赎回下限 |
| 15 | freserved5 | 备用字段5 | varchar | 50 |  | √ | ' ' | 备用字段5 |
| 16 | freserved2 | 备用字段2 | varchar | 50 |  | √ | ' ' | 备用字段2 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fpublish_end_date | 发行结束日期 | timestamp | 0 |  |  | null | 发行结束日期 |
| 19 | freserved3 | 备用字段3 | varchar | 50 |  | √ | ' ' | 备用字段3 |
| 20 | frisk_lev | 风险等级 | varchar | 50 |  | √ | ' ' | 风险等级 |
| 21 | freserved1 | 备用字段1 | varchar | 50 |  | √ | ' ' | 备用字段1 |
| 22 | fbillno | 理财编号 | varchar | 30 |  | √ | ' ' | 理财编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_financ_detail |  | fid |
| 2 | idx_financ_detail |  | fbillno |
