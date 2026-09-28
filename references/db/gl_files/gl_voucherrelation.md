# 凭证关系-gl_voucherrelation

## 凭证关系-主表 t_gl_voucherrelation

- **表名称：** 凭证关系-主表
- **表名：** t_gl_voucherrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 1 :冲销 2 :自动转账 3 :结转损益 4 :期末调汇 5 :凭证摊销 |
| 3 | fsrcentityid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 4 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | ftargentityid | 目标凭证id | int8 | 64 |  | √ | 0 | 目标凭证id |
| 6 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 7 | fiseffective | 是否生效 | bpchar | 1 |  | √ | '1' | 是否生效 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_voucherralation_fsrcid |  | fsrcentityid |
| 2 | t_gl_voucherrelation_pkey |  | fid |
| 3 | idx_gl_voucherrelation |  | ftargentityid,fperiod |
