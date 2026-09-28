# 发票预警详情表-rim_inv_warning_detail

## 发票预警详情表-主表 t_rim_inv_warning_detail

- **表名称：** 发票预警详情表-主表
- **表名：** t_rim_inv_warning_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserial_no | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 3 | fdetail_period | 数据期限 | varchar | 10 |  | √ | ' ' | 数据期限,枚举: 0 :本月数据 1 :全部数据 |
| 4 | fwarning_type | 预警类别 | varchar | 10 |  | √ | ' ' | 预警类别,枚举: 1 :黑名单发票 2 :敏感词发票 3 :专票购方信息不完整 4 :节假日发票 5 :超期限报销发票 6 :超60天未入账 7 :超90天未入账 |
| 5 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_warning_detail |  | forg,fwarning_type |
| 2 | pk_rim_inv_warning_detail |  | fid |
