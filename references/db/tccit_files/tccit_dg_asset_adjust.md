# 资产调整底稿单据-tccit_dg_asset_adjust

## 资产调整底稿单据-主表 t_tccit_dg_asset_adjust

- **表名称：** 资产调整底稿单据-主表
- **表名：** t_tccit_dg_asset_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :资产折旧摊销 2 :资产减值准备金 3 :资产损失扣除 4 :其他调整 5 :合计 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 8 | famount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dg_asset_adjust |  | fid |
| 2 | idx_tccit_dg_asset_adjust |  | forgid,fskssqq,fskssqz |
