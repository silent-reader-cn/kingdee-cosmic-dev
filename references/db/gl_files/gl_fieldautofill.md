# 凭证字段自动携带设置-gl_fieldautofill

## 凭证字段自动携带设置-主表 t_gl_fieldautofill

- **表名称：** 凭证字段自动携带设置-主表
- **表名：** t_gl_fieldautofill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsettlettype | 结算方式 | bpchar | 1 |  | √ | '0' | 结算方式 |
| 3 | fmeasureunit | 计量单位 | bpchar | 1 |  | √ | '0' | 计量单位 |
| 4 | foriamount | 原币金额 | bpchar | 1 |  | √ | '0' | 原币金额 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fassgrp | 核算维度 | bpchar | 1 |  | √ | '1' | 核算维度 |
| 7 | fcurrency | 币种 | bpchar | 1 |  | √ | '0' | 币种 |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | faccount | 科目 | bpchar | 1 |  | √ | '0' | 科目 |
| 10 | fprice | 单价 | bpchar | 1 |  | √ | '0' | 单价 |
| 11 | fbusinessnum | 业务编号 | bpchar | 1 |  | √ | '0' | 业务编号 |
| 12 | fsettletnumber | 结算号 | bpchar | 1 |  | √ | '0' | 结算号 |
| 13 | fexpiredate | 到期日 | bpchar | 1 |  | √ | '0' | 到期日 |
| 14 | fdesc | 摘要 | bpchar | 1 |  | √ | '1' | 摘要 |
| 15 | fquantity | 数量 | bpchar | 1 |  | √ | '0' | 数量 |
| 16 | flocalrate | 汇率 | bpchar | 1 |  | √ | '0' | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_fieldautofill |  | forgid,fuserid |
| 2 | t_gl_fieldautofill_pkey |  | fid |
