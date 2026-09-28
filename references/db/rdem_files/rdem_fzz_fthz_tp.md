# 分摊结果汇总表（临时）-rdem_fzz_fthz_tp

## 分摊结果汇总表（临时）-主表 t_rdem_fzz_fthz_tp

- **表名称：** 分摊结果汇总表（临时）-主表
- **表名：** t_rdem_fzz_fthz_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprecost | 上一级费用类型 | int8 | 64 |  | √ | 0 | [研发费用类型 rdem_cost_type](../rdem_files/rdem_cost_type.md) |
| 3 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fftamount | 本币实际分摊金额 | numeric | 23 | 2 | √ | 0 | 本币实际分摊金额 |
| 6 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 7 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 8 | famount | 本币发生金额 | numeric | 23 | 2 | √ | 0 | 本币发生金额 |
| 9 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: capital :资本化 cost :费用化 |
| 10 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | fcost | 费用类型 | int8 | 64 |  | √ | 0 | [研发费用类型 rdem_cost_type](../rdem_files/rdem_cost_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_fzz_fthz_tp |  | fid |
| 2 | idx_rdem_fzz_fthz_tp_m0 |  | fftamount |
