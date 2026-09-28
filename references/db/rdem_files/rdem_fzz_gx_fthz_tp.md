# 高新分摊汇总结表(临时)-rdem_fzz_gx_fthz_tp

## 高新分摊汇总结表(临时)-主表 t_rdem_fzz_gx_fthz_tp

- **表名称：** 高新分摊汇总结表(临时)-主表
- **表名：** t_rdem_fzz_gx_fthz_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fftamount | 本币实际分摊金额 | numeric | 23 | 2 | √ | 0 | 本币实际分摊金额 |
| 5 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 6 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 7 | famount | 本币发生金额 | numeric | 23 | 2 | √ | 0 | 本币发生金额 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fcost | 费用类型 | int8 | 64 |  | √ | 0 | [高新费用类别 rdem_high_tech_costtype](../rdem_files/rdem_high_tech_costtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_fzz_gx_fthz_tp_m0 |  | fftamount |
| 2 | pk_rdem_fzz_gx_fthz_tp |  | fid |
